<p align="center">
    <img src="https://raw.githubusercontent.com/ImNimboss/uberduck/main/.github/assets/uberduck-logo.png" alt="Uberduck Logo">
</p>

# Uberduck

<a href="https://pypi.org/project/uberduck" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/pypi/v/uberduck.svg?color=9cf&logo=pypi" alt="PyPI Uberduck version number">
    <img src="https://img.shields.io/pypi/dm/uberduck?color=9cf&logo=pypi" alt="PyPI downloads per month">
    <img src="https://img.shields.io/pypi/pyversions/uberduck.svg?color=9cf&logo=pypi" alt="PyPI supported Python versions">
</a>
<a href="https://github.com/ImNimboss/uberduck/issues" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/github/issues/ImNimboss/uberduck?color=9cf&logo=github" alt="Number of open GitHub issues">
</a>
<a href="https://github.com/ImNimboss/uberduck/contributors" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/github/contributors/ImNimboss/uberduck?color=9cf&logo=github" alt="Number of contributors">
</a>
<a href="https://discord.gg/FcxqdJ7AQq" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/discord/930791886522810399?color=9cf&logo=discord&label=discord" alt="Discord server">
</a>

## Description

A synchronous and asynchronous API wrapper for the [UberDuck](https://uberduck.ai) text-to-speech service with 100% coverage and top-notch utilities.

## Main features

- [x] - Synchronous support
- [x] - Asynchronous support
- [x] - Object-oriented
- [x] - Easy to use
- [x] - Utilities like file-saving, audio-playing etc. packed all in one
- [x] - Very adjustable/configurable
- [x] - Regularly maintained
- [x] - Makes the hard tasks of polling and asynchronous operations easy

## Links

* [Documentation](https://github.com/ImNimboss/uberduck/tree/main/Documentation)
* [PyPI](https://pypi.org/project/uberduck)
* [Issue Tracking](https://github.com/ImNimboss/uberduck/issues)
* [Discord server](https://discord.gg/FcxqdJ7AQq)
* [Uberduck main site](https://uberduck.ai)


## Installation and upgrades

```
pip install uberduck
```
for the stable version (recommended).

```
pip install -U uberduck
```
to update your stable version.

```
pip install git+https://github.com/ImNimboss/uberduck
```
to install it straight off of GitHub (you need git installed for this).

```
pip install -U git+https://github.com/ImNimboss/uberduck
```
to upgrade your version that you got from GitHub.

## How to use

Check [Documentation/Basics.md](https://github.com/ImNimboss/uberduck/blob/master/Documentation/Basics.md).

## Examples

Check [Documentation/Examples.md](https://github.com/ImNimboss/uberduck/blob/master/Documentation/Examples.md).

## Some credits

The idea to implement logging in this library came from [discord.py](https://github.com/Rapptz/discord.py).

The idea to use the `polling` library came from [CupOfGeo/UberDuckAPI](https://github.com/CupOfGeo/UberDuckAPI), another uberduck.ai API wrapper.

## Changelog

* `v0.0.1` - Initial release.
* `v0.0.2` - Fixed `get_voices()` and `get_voices_async()` by updating the `Voice` class to be compatible with the new voice data available from the API.
* `v0.0.3` - Moved `README.md` from `.github` to root folder due to compatibility issues with other software
* `v0.0.4` - Added attributes `added_at`, `is_primary`, `hifi_gan_vocoder`, `ml_model_id`, `speaker_id`, `language` to `Voice` class