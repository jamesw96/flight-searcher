# flight-searcher
Simplistic way of flight searching using Amadeus API

Features
--------

* Testing concurrently with pytest, using one of the three modes
    - Multiprocess (--concmode=mproc)
    - Multithread (--concmode=mthread)
    - Asynchronous Network with gevent (--concmode=asyncnet)
* The ability to designate the amount of work to be used for testing
* The ability to put your tests into separate groups

Requirements
------------

* Python3 version [3.3 +]


Installation
------------

Not required


Usage
-----
* Go on https://sandbox.amadeus.com/ and register for an API key
* Clone this repo
* Replace the <API KEY> with your API key

You can run this script by running::

    $ python FlightSearcher.py

Contributing
------------
Contributions are very welcome.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-concurrent" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.
