# Basics

## Creating a class instance of `UberDuck`

First, you have to get an uberduck API key and API secret from [uberduck.ai/account/manage](https://uberduck.ai/account/manage).

Make sure to store these credentials securely, these are private and should not be given to anyone else.

Then you need to make an instance of class `UberDuck` using `your_instance = UberDuck("Your API Key", "Your API Secret")`.

You can change your API key and API secret anywhere in the code by simply reinitializing the attributes, like -
```python
your_instance.api_key = "Your API Key"
your_instance.api_secret = "Your API Secret"
```

**NOTE:** This is not the ideal way to store your API key and secret. See [Store-your-credentials-securely.md](https://github.com/ImNimboss/uberduck/blob/main/Documentation/Store-your-credentials-securely.md) for more information.

## Using it synchronously

Now that you have created an instance with an example name `your_instance`, you can use a method from it named `speak`.

It takes 5 parameters:

* `speech`: The text you want to speak of type `str`. This parameter is mandatory.

* `voice`: The voice you want to use of type `str`. You can get a list of voices using functions in the library (read the "Getting voices" section of the documentation below). You can also go to [uberduck.ai/quack-help](https://uberduck.ai/quack-help). This parameter is mandatory.

* `return_bytes`: This parameter is a `bool` type. Setting this to `True` means it will return the audio in the form of bytes. Setting this to `False` means it will simply return the URL of the audio. This parameter is optional, a keyword-only argument, and defaults to `True`.

* `check_every`: This parameter is a `float` or `int` type. It is the time in seconds between checking if the audio is ready. This parameter is optional, a keyword-only argument, and defaults to `1`.

* `file_path`: This parameter is a `str` type. It is the path to the file you want to save the audio to. This parameter is optional, a keyword-only argument, and defaults to `None` which means that the file will not be saved.
  
* `play_sound`: This parameter is a `bool` type. Setting this to `True` means it will play the audio using [pydub](http://pydub.com/). Setting this to `False` means it will not play the audio. This parameter is optional, a keyword-only argument, and defaults to `False`.

See examples in [Examples.md](https://github.com/ImNimboss/uberduck/blob/main/Documentation/Examples.md).

## Using it asynchronously

An instance of `UberDuck` also has another method - `speak_async`.

This is an asynchronous method. It takes the same parameters as the synchronous method and 1 more:

* `asyncio_loop`: This parameter is a `asyncio.AbstractEventLoop` type. It is the event loop you want to use for functions inside the method. This parameter is optional, a keyword-only argument, and defaults to `None` which means that a new event loop will be created.

See examples in [Examples.md](https://github.com/ImNimboss/uberduck/blob/main/Documentation/Examples.md).

## Handling returned bytes and saving files

*When you get returned bytes from any of the functions and intend to package them to a file/file-like object OR save your output to a file, it is recommended that you write it to a `.wav` file.*

The original output from the API is also in a `.wav` file and while you can write the bytes to another audio file format like `.mp3` and `.flac`, it may sound different or may just be unsupported.

## Getting voices

The main module `uberduck` has 2 functions - `get_voices` and `get_voices_async`. Both do the same thing and have the same parameters except `get_voices` is not async.

They have 1 parameter:

* `return_only_names`: This parameter is a `bool` type. Setting this to `True` means it will return only the names of the voices in a list. Setting this to `False` means it will return the full details of the voices in a list of `uberduck.Voice` objects. This parameter is optional, a keyword-only argument, and defaults to `False`.

See more info about `uberduck.Voice` in [Models.md](https://github.com/ImNimboss/uberduck/blob/main/Documentation/Models.md).

See examples in [Examples.md](https://github.com/ImNimboss/uberduck/blob/main/Documentation/Examples.md).

**NOTE:** `get_voices` and `get_voices_async` do not need you to have an API key and/or secret and are NOT methods of the `UberDuck` class. They are functions of the `uberduck` module.