# Exceptions this library can throw

## `uberduck.UberduckException`

Base class for all exceptions raised by Uberduck. This exception could be used to catch any exceptions thrown by this library.

## `uberduck.InvalidVoice`

Raised when an invalid voice is specified. See all the voices from `uberduck.get_voices()`, `uberduck.get_voices_async()` or [uberduck.ai/quack-help](https://uberduck.ai/quack-help).

## `uberduck.Unauthorized`

Exception raised when your API key is invalid or your API secret is invalid. Get an API key and secret from [uberduck.ai/account/manage](https://uberduck.ai/account/manage).

## `uberduck.Ratelimited`

Exception raised when you are being ratelimited from the API.

## `uberduck.HTTPException`

Exception raised when the HTTP request fails due to an unknown cause.