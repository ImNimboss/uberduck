"""
Copyright 2022-present ImNimboss

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from typing import List

class Membership:
    """
    This is a model class Membership that represents the membership attribute of a voice.
    
    Attributes:
        `name (str)`: The name of the membership.
        `id (int)`: The ID of the membership.

    Magic methods:
        `__str__`: Returns a string representation of the Membership object in the format `Membership: Name - {name}, ID - {id}`.
        `__repr__`: Returns a string representation of the Membership object in the format `<Membership name='{name}' id={id}>`.

    This class is read-only.
    """
    def __init__(self, name: str = None, id: int = None):
        self.name = name
        self.id = id

    def __str__(self):
        return f'Membership: Name - {self.name}, ID - {self.id}'

    def __repr__(self):
        return f'<Membership name=\'{self.name}>\' id={self.id}>'

class Voice:
    """
    This is a model class Voice that represents a voice.

    Attributes:
        `architecture (str)`: The architecture of the voice i.e. the engine that was used to make the voice.
        `category (str)`: The category of the voice i.e. where it's from (WWE, SpongeBob etc).
        `contributors (list)`: The contributors' names of the voice.
        `controls (bool)`: Whether the voice has controls.
        `display_name (str)`: The display name of the voice i.e. a better formatted name to show to general users.
        `is_active (bool)`: Whether the voice is active.
        `model_id (str)`: The model ID of the voice. This is not a unique identification, the name is.
        `memberships (list)`: The memberships of the voice.
        `is_private (bool)`: Whether the voice is private.
        `name (str)`: The name of the voice i.e. the name you pass to the API in order for it to recognize which voice you want.
        `symbol_set (str)`: The symbol set of the voice.
        `voicemodel_uuid (str)`: The voice model's UUID.

    Magic methods:
        `__str__`: Returns a string representation of the Voice object in the format `Voice: Architecture - {architecture}, Category - {category}, Controls - {controls}, Display Name - {display_name}, Name - {name}, Model ID - {model_id}, Memberships - {memberships}, Is Private - {is_private}, Contributors - {contributors}`.
        `__repr__`: Returns a string representation of the Voice object in the format `<Voice architecture='{architecture}' category='{category}' controls='{controls}' display_name='{display_name}' name='{name}' model_id='{model_id}' memberships='{memberships}' is_private='{is_private}' contributors='{contributors}'>`.
    
    This class is read-only.
    """
    def __init__(
        self,
        architecture: str,
        category: str,
        contributors: List[str],
        controls: bool,
        display_name: str,
        is_active: bool,
        model_id: str,
        memberships: list,
        is_private: bool,
        name: str,
        symbol_set: str,
        voicemodel_uuid: str
    ) -> None:
        self.architecture = architecture
        self.category = category
        self.contributors = contributors
        self.controls = controls
        self.display_name = display_name
        self.is_active = is_active
        self.model_id = model_id
        self.memberships = memberships
        if self.memberships:
            self.memberships: List[Membership] = [Membership(*memberships)]
        self.is_private = is_private
        self.name = name
        self.symbol_set = symbol_set
        self.voicemodel_uuid = voicemodel_uuid

    def __str__(self):
        return f'Voice: Architecture - {self.architecture}, Category - {self.category}, Contributors - {self.contributors}, Controls - {self.controls}, Display Name - {self.display_name}, Is Active - {self.is_active},  Model ID - {self.model_id}, Memberships - {self.memberships}, Is Private - {self.is_private}, Name - {self.name}, Symbol Set - {self.symbol_set}, Voice model UUID - {self.voicemodel_uuid}'

    def __repr__(self):
        return f'<Voice architecture=\'{self.architecture}\' category=\'{self.category}\' contributors=\'{self.contributors}\' controls=\'{self.controls}\' display_name=\'{self.display_name}\' is_active=\'{self.is_active}\' model_id=\'{self.model_id}\' memberships=\'{self.memberships}\' is_private=\'{self.is_private}\' name=\'{self.name}\' symbol_set=\'{self.symbol_set}\' voicemodel_uuid=\'{self.voicemodel_uuid}\'>'

class UberduckException(Exception):
    """
    Base class for all exceptions raised by Uberduck. This exception could be used to catch any exceptions thrown by this library.
    """
    pass

class InvalidVoice(UberduckException):
    """
    Raised when an invalid voice is specified. See all the voices from `uberduck.get_voices()`, `uberduck.get_voices_async()` or [uberduck.ai/quack-help](https://uberduck.ai/quack-help).
    """
    def __init__(self, voice: str) -> None:
        self.voice = voice
        super().__init__(f'Invalid voice: {voice}.')

class Unauthorized(UberduckException):
    """
    Exception raised when your API key is invalid or your API secret is invalid. Get an API key and secret from [uberduck.ai/account/manage](https://uberduck.ai/account/manage).
    """
    def __init__(self) -> None:
        super().__init__('Invalid API credentials. Please check your api key and/or api secret.')

class Ratelimited(UberduckException):
    """
    Exception raised when you are being ratelimited from the API.
    """
    def __init__(self) -> None:
        super().__init__('You are being ratelimited from the API. Please try again later.')

class HTTPException(UberduckException):
    """
    Exception raised when the HTTP request fails due to an unknown cause.
    """
    def __init__(self, status_code: int, detail) -> None:
        self.status_code = status_code
        self.detail = detail
        super().__init__(f'Unexpected HTTP response with status code {status_code} and detail {detail}.')