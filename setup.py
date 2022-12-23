from setuptools import setup

with open('README.md') as file:
    long_description = file.read()

with open('uberduck/__init__.py') as file:
    lines = file.readlines()

for line in lines:
    if line.startswith('__version__: str = '):
        version = line[20:-2]
        break

setup(
    name = 'uberduck',
    version = version,
    description = 'A synchronous and asynchronous API wrapper for the UberDuck text-to-speech service (https://uberduck.ai) with 100% coverage and top-notch utilities.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = 'ImNimboss',
    author_email = 'nim@nimboss.me',
    url = 'https://github.com/ImNimboss/uberduck',
    license = 'MIT',
    packages = ['uberduck'],
    keywords = [
        'uberduck', 'wrapper', 'api', 'text-to-speech', 'async', 'famous',
        'tts', 'texttospeech', 'AI', 'api-wrapper', 'api-key', 'api-secret'
    ],
    install_requires = ['requests', 'aiohttp', 'polling', 'pydub'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Artistic Software',
        'Topic :: Games/Entertainment',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Players',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ], # https://pypi.org/classifiers/
    python_requires = '>=3.6.0',
    project_urls = {
        'Documentation': 'https://github.com/ImNimboss/uberduck/tree/main/Documentation',
        'Issue Tracker': 'https://github.com/ImNimboss/uberduck/issues',
        'Source': 'https://github.com/ImNimboss/uberduck',
        'Funding': 'https://patreon.com/nimboss',
        'API Credits': 'https://uberduck.ai',
        'Creator': 'https://nimboss.me',
        'Discord': 'https://discord.gg/FcxqdJ7AQq',
        'Repository': 'https://github.com/ImNimboss/uberduck'
    }
)