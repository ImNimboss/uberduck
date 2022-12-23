"""
A synchronous and asynchronous API wrapper for the [UberDuck](https://uberduck.ai) text-to-speech service with 100% coverage and top-notch utilities.

Copyright 2022-present ImNimboss

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from uberduck.main import UberDuck, get_voices, get_voices_async
from uberduck.classes import *
import logging as _logging

__author__: str = 'ImNimboss'
__license__: str = 'MIT'
__version__: str = '0.0.3'
GITHUB: str = 'https://github.com/ImNimboss/uberduck'
ISSUE_TRACKER: str = 'https://github.com/ImNimboss/uberduck/issues'
DOCUMENTATION: str = 'https://github.com/ImNimboss/uberduck/tree/main/Documentation'
SPONSOR: str = 'https://patreon.com/ImNimboss'
API_CREDITS: str = 'https://uberduck.ai'

_logging.getLogger(__name__).addHandler(_logging.NullHandler())