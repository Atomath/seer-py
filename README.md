Python SDK for SEER API [![Build Status](https://travis-ci.org/seer-project/seer-py.svg)](https://travis-ci.org/seer-project/seer-py)
=======================

Requirements
------------

requests==2.9.1


Installation
------------

Justing run this in your terminal:

```
$ pip install requests==2.8.1
$ cd seer-py && python setup.py install

# or
$ cd seer-py && pip install seer
```


Quickstart
----------

[SEER's Documentation](http://seer-py.readthedocs.org/en/latest/)

```
# Examples

import seer
from pprint import pprint

Your_API_Token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# Hosts Search
client = seer.Hosts(Your_API_Token)
pprint client.ip('8.8.8.8')
pprint client.port(8000)

# DNS Search
client = seer.DNS(Your_API_Token)
pprint client.domain('google.com')

# etc.
```
