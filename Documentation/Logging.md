# Logging

## Intro

Uberduck uses python's `logging` module to log messages, errors and info. You can setup logging to see this information in the stdout or in a file.

## Setting up logging

You can use this snippet to configure logging to your stdout. This will setup logging for every process to your stdout.

```python
import logging

logging.basicConfig(level = logging.DEBUG)
```

You can use this snippet to configure logging to a file named "uberduck.log". This is recommended for more verbose logging since a lot of logging can clog up your stdout.

```python
import logging

logger = logging.getLogger('uberduck')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='uberduck.log', encoding='utf-8')
handler.setFormatter(logging.Formatter('%(name)s: %(level)s @ %(asctime)s: %(message)s'))
logger.addHandler(handler)
```

## Logging credits

This library's logging and logging docs was inspired by [discord.py's logging](https://discordpy.readthedocs.io/en/master/logging.html)