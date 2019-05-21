
.. image:: https://travis-ci.org/SFB-ELAINE/ckanext-disablepwreset.svg?branch=master
    :target: https://travis-ci.org/SFB-ELAINE/ckanext-disablepwreset

.. image:: https://coveralls.io/repos/SFB-ELAINE/ckanext-disablepwreset/badge.svg
  :target: https://coveralls.io/r/SFB-ELAINE/ckanext-disablepwreset

=============
ckanext-disablepwreset
=============

This extension enables or disables passwort reset requests depending on the configuration option::

    # If not present or set to "False" passwort reset is disabled
    ckanext.disablepwreset.permit_reset = False

------------
Requirements
------------

This extension was tested with CKAN v2.8.2


------------
Installation
------------

In order to install the extension execute the following::

    git clone https://github.com/SFB-ELAINE/ckanext-disablepwreset.git
    cd ckanext-disablepwreset
    python setup.py develop
    pip install -r dev-requirements.txt


-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.disablepwreset --cover-inclusive --cover-erase --cover-tests
