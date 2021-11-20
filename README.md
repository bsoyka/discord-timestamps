# discord-timestamps

**discord-timestamps** generates properly-formatted dynamic timestamps for
Discord messages, with support for Arrow objects.

```py
>>> format_timestamp(datetime(2021, 11, 20, 12, 0, 0))
'<t:1637409600>'

>>> format_timestamp(datetime(...), TimestampType.RELATIVE)
'<t:1637409600:R>'
```

[![Downloads](https://pepy.tech/badge/discord-timestamps)](https://pepy.tech/project/discord-timestamps)
[![Supported Versions](https://img.shields.io/pypi/pyversions/discord-timestamps.svg)](https://pypi.org/project/discord-timestamps)
[![Testing](https://img.shields.io/github/workflow/status/bsoyka/discord-timestamps/Test%20with%20pytest?label=tests)](https://github.com/bsoyka/discord-timestamps/actions?query=workflow%3A%22Test+with+pytest%22)
[![License](https://img.shields.io/pypi/l/discord-timestamps)](https://github.com/bsoyka/discord-timestamps/blob/master/LICENSE)
[![Version](https://img.shields.io/pypi/v/discord-timestamps?label=latest)](https://pypi.org/project/discord-timestamps)

## Installation

discord-timestamps is available on PyPI:

```console
$ pip install discord-timestamps
```

discord-timestamps officially supports Python 3.6+.

## API Reference

See [Read the Docs](https://averager.readthedocs.io) for Averager's documentation.
