MapIt
=====

MapIt is an open source project to help people run a web service that maps
geographical points to administrative areas. It is useful for anyone who has
the co-ordinates of a point on Earth, and who needs to find out what country,
region, city, constituency, or state it lies within. It’s also great for
looking up the shapes of all those boundaries.

It was created in 2003 by `mySociety <https://www.mysociety.org/>`__, a UK
charity, for use by their various tools needing admin area lookup.

Installation
------------

MapIt can be installed as a Django app, or as a standalone server. For full
details, please see our site at http://code.mapit.mysociety.org/ for help
and documentation.

Mapit Africa
-------------
Mapit Africa (mapit.hurumap.org) uses the django app 
`project <https://github.com/CodeForAfrica/mapit/tree/geo-files/project>`_ to host administrative 
areas geographical boundaries and maps geographical points for more than 10 African countries.

Development
```````````
We use docker-based environment for development and deployment. Refer to the 
`docker-compose.yml <https://github.com/TakwimuAfrica/Dashboard/blob/master/docker-compose.yml>`_ file.

To get started, clone this repository and spin up docker-containers as shown below. 


- git clone git@github.com:CodeforAfrica/mapit.git
- cd mapit
- docker-compose up

Once containers are up, visit `<http:localhost:8000>`_

Countries' geofiles are available in the folder `geo`.
The file `import.md <https://github.com/CodeForAfrica/mapit/tree/geo-files/geo/import.md>`_ has
steps on how to import MapIt data. Make sure you're on the web container bash to run import commands.

Use MAPIT API documentation displayed on landing page to understand the web services.

Examples
--------

`mySociety <https://www.mysociety.org>`__ runs public installations of MapIt that
you might be able to use:

    * `MapIt Global <http://global.mapit.mysociety.org/>`_ - global boundaries
      from the `OpenStreetMap <http://www.openstreetmap.org/>`_ project.
    * `MapIt UK <https://mapit.mysociety.org/>`_ - UK boundaries from various
      sources.

The above are free for non-commercial, low-volume use. For details of
what constitutes "low-volume", and for commercial licensing arrangements,
please consult `MapIt pricing <https://mapit.mysociety.org/pricing/>`_ .

Rate limiting
-------------

Usage is rate limited by default; clients may be rate limited by IP address
or by a User Token passed in the User-Agent: header. Clients may be excluded
from the effects of rate limiting via the RATE_LIMIT option in the
configuration file.

