"""
Copyright 2022-present ImNimboss

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from requests import post, get
from aiohttp import request, BasicAuth
from asyncio import get_event_loop, AbstractEventLoop
from typing import Union, Literal, Optional, List
from uberduck.classes import *
from polling import poll
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO
from logging import getLogger

log = getLogger(__name__)

def _handle_exceptions(
    status_code: int,
    data: dict,
    voice: str = None
):
    """
    A private function to handle all HTTP exceptions received by the API, if any.
    """
    if 299 >= status_code >= 200:
        log.debug(f'Checked for HTTP exceptions, none found (status code {status_code}).')
        return
    detail = data.get('detail')
    if detail == 'That voice does not exist':
        log.error(f'The voice "{voice}" does not exist. Status code {status_code}, detail {data}.')
        raise InvalidVoice(voice)
    elif status_code == 401 and detail == 'Could not validate credentials':
        log.error(f'The API key and/or secret is invalid. Status code {status_code}, detail {data}.')
        raise Unauthorized()
    elif status_code == 429:
        log.error(f'The API key has been rate-limited. Status code {status_code}, detail {data}.')
        raise Ratelimited()
    else:
        log.error(f'An error has occurred. Status code {status_code}, detail {data}.')
        raise HTTPException(status_code, data)

def _write_to_file(file_path: str, bytes_to_write: bytes):
    """
    A private function to assist in saving files.
    """
    with open(file_path, 'wb') as file:
        file.write(bytes_to_write)

def _get_audio(uuid: str) -> Union[str, Literal[False]]:
    """
    A private function to recieve audio from the API using a UUID. This function is polled until the desired audio is available.
    """
    response = get(
        url = f'https://api.uberduck.ai/speak-status?uuid={uuid}'
    )
    json: dict = response.json()
    log.debug(f'Polling for audio with UUID {uuid} - received status code {response.status_code}, got audio: {bool(json.get("path"))}.')
    _handle_exceptions(response.status_code, json)
    return json if json.get('path') else False

def get_voices(*, return_only_names: bool = False) -> Union[List[Voice], List[str]]:
    """
    A synchronous function that returns every possible voice that can be used by the API for text-to-speech.

    Parameters:
        `return_only_names (bool)` - If True, the function will return a list of string names instead of `uberduck.Voice` objects containing the full details of voices. Defaults to False.

    Returns:
        Either a list of strings or a list of `uberduck.Voice` objects depending on the `return_only_names` parameter.
    """
    response = get('https://api.uberduck.ai/voices?mode=tts-basic')
    json: list = response.json()
    log.debug(f'Got voice data - status code {response.status_code}.')
    _handle_exceptions(response.status_code, json)
    if return_only_names:
        return [voice['name'] for voice in json]
    return [Voice(**voice) for voice in json]

async def get_voices_async(*, return_only_names: bool = False) -> Union[List[Voice], List[str]]:
    """
    An asynchronous function that returns every possible voice that can be used by the API for text-to-speech.

    Parameters:
        `return_only_names (bool)` - If True, the function will return a list of string names instead of `uberduck.Voice` objects containing the full details of voices. Defaults to False.

    Returns:
        Either a list of strings or a list of `uberduck.Voice` objects depending on the `return_only_names` parameter.
    """
    async with request('GET', 'https://api.uberduck.ai/voices?mode=tts-basic') as response:
        json: list = await response.json()
        log.debug(f'Got voice data asynchronously - status code {response.status}.')
        _handle_exceptions(response.status, json)
    if return_only_names:
        return [voice['name'] for voice in json]
    return [Voice(**voice) for voice in json]

class UberDuck:
    """
    The class used to interact with the UberDuck text-to-speech API.

    Initialization parameters:
        `api_key (str)` - The API key used to authenticate with the API.`
        
        `api_secret (str)` - The API secret used to authenticate with the API.
    
    Attributes:
        `api_key` - The API key used to authenticate with the API. Using this attribute, you can change it later on.
        
        `api_secret` - The API secret used to authenticate with the API. Using this attribute, you can change it later on.

    Functions:
        `speak(speech: str, voice: str | uberduck.Voice, *, return_bytes: bool = True, check_every: int = 1, file_path: str = None, play_sound: bool = False)` - This function is synchronous and returns the bytes/string of the audio that is generated by the API (depending on the `return_bytes` argument).
        
        `speak_async(speech: str, voice: str | uberduck.Voice, *, return_bytes: bool = True, check_every: int = 1, file_path: str = None, play_sound: bool = False, asyncio_loop: AbstractEventLoop = None)` - This function is asynchronous and returns the bytes/string of the audio that is generated by the API (depending on the `return_bytes` argument).

        Read more about the functions in the [documentation](https://github.com/ImNimboss/uberduck/tree/main/Documentation/Basics.md).
    """
    def __init__(self, api_key: str, api_secret: str) -> None:
        self.api_key = api_key
        self.api_secret = api_secret

    def speak(
        self,
        speech: str,
        voice: Union[str, Voice],
        *,
        return_bytes: bool = True,
        check_every: Union[int, float] = 1,
        file_path: Optional[str] = None,
        play_sound: bool = False
    ) -> Union[bytes, str]:
        """
        Parameters:
            `speech (str)` - The text that will be spoken.

            `voice (str | uberduck.Voice)` - The voice that will be used to speak the text.

            `return_bytes (bool)` - If True, the function will return the bytes of the audio that is generated by the API. If False, the function will return the URL of the audio that is generated by the API. Defaults to True.

            `check_every (int | float)` - The number of seconds that the function will wait between checking if the audio is available. Defaults to 1.

            `file_path (str)` - The path of the file that the audio will be saved to. If not specified, the function will not save the audio.

            `play_sound (bool)` - If True, the function will play the audio that is generated by the API. Defaults to False.

        Returns:
            Either the bytes of the audio that is generated by the API or the URL of the audio that is generated by the API depending on the `return_bytes` argument.

        Raises:
            `uberduck.InvalidVoice` - If the voice is not valid.
            `uberduck.Unauthorized` - If the API key or secret is invalid.
            `uberduck.Ratelimited` - If you got ratelimited by the API.
            `uberduck.HTTPException` - If the HTTP request failed from an unknown cause.
        """
        if isinstance(voice, Voice):
            voice = voice.name
        response = post(
            url = 'https://api.uberduck.ai/speak',
            auth = (self.api_key, self.api_secret),
            json = {'speech': speech, 'voice': voice.lower()}
        )
        json = response.json()
        log.debug(f'UUID request sent - status code {response.status_code}, data {json}.')
        _handle_exceptions(response.status_code, json, voice)
        
        result: dict = poll(
            lambda: _get_audio(json['uuid']),
            step = check_every,
            poll_forever = True
        )
        
        bytes_ = None
        if file_path is not None:
            bytes_ = get(result['path']).content
            _write_to_file(file_path, bytes_)
            log.debug(f'Wrote audio to file {file_path}.')
        if play_sound:
            bytes_ = bytes_ or get(result['path']).content
            log.debug(f'Playing sound "{speech}" by voice "{voice}" with UUID "{json["uuid"]}" and URL "{result["path"]}".')
            play(AudioSegment.from_file(BytesIO(bytes_), format = 'wav'))
        if return_bytes:
            return bytes_ or get(result['path']).content
        return result['path']

    async def speak_async(
        self,
        speech: str,
        voice: Union[str, Voice],
        *,
        return_bytes: bool = True,
        check_every: int = 1,
        file_path: Optional[str] = None,
        play_sound: bool = False,
        asyncio_loop: AbstractEventLoop = None
    ) -> Union[bytes, str]:
        """
        Parameters:
            `speech (str)` - The text that will be spoken.

            `voice (str | uberduck.Voice)` - The voice that will be used to speak the text.

            `return_bytes (bool)` - If True, the function will return the bytes of the audio that is generated by the API. If False, the function will return the URL of the audio that is generated by the API. Defaults to True.

            `check_every (int | float)` - The number of seconds that the function will wait between checking if the audio is available. Defaults to 1.

            `file_path (str)` - The path of the file that the audio will be saved to. If not specified, the function will not save the audio.

            `play_sound (bool)` - If True, the function will play the audio that is generated by the API. Defaults to False.

            `asyncio_loop (AbstractEventLoop)` - The event loop that the function will use. Defaults to the creation of a new event loop.

        Returns:
            Either the bytes of the audio that is generated by the API or the URL of the audio that is generated by the API depending on the `return_bytes` argument.

        Raises:
            `uberduck.InvalidVoice` - If the voice is not valid.
            `uberduck.Unauthorized` - If the API key or secret is invalid.
            `uberduck.Ratelimited` - If you got ratelimited by the API.
            `uberduck.HTTPException` - If the HTTP request failed from an unknown cause.
        """
        if isinstance(voice, Voice):
            voice = voice.name
        async with request(
            'POST',
            url = 'https://api.uberduck.ai/speak',
            json = {'speech': speech, 'voice': voice.lower()},
            auth = BasicAuth(self.api_key, self.api_secret)
        ) as response:
            json = await response.json()
            log.debug(f'Asynchronous UUID request sent - status code {response.status}, data {json}.')
            _handle_exceptions(response.status, json, voice)

        asyncio_loop = asyncio_loop or get_event_loop()
        result = await asyncio_loop.run_in_executor(
            None,
            lambda: poll(
                lambda: _get_audio(json['uuid']),
                step = check_every,
                poll_forever = True
            )
        )
        
        bytes_ = None
        if file_path is not None:
            async with request('GET', result['path']) as response:
                bytes_ = await response.read()
            await asyncio_loop.run_in_executor(
                None,
                lambda: _write_to_file(file_path, bytes_)
            )
            log.debug(f'Wrote audio to file {file_path}.')
        if play_sound:
            if not bytes_:
                async with request('GET', result['path']) as response:
                    bytes_ = await response.read()
            log.debug(f'Playing sound "{speech}" by voice "{voice}" with UUID "{json["uuid"]}" and URL "{result["path"]}" asynchronously.')
            await asyncio_loop.run_in_executor(
                None,
                lambda: play(AudioSegment.from_file(BytesIO(bytes_), format = 'wav'))
            )
        if return_bytes:
            if not bytes_:
                async with request('GET', result['path']) as response:
                    return await response.read()
            return bytes_
        return result['path']