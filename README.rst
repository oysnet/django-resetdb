-----
About
-----

Allow to drop tables before syncdb

------------
Installation
------------

To install the latest stable version::

	pip install -e git+https://github.com/oxys-net/django-resetdb#egg=django-resetdb


You will need to include ``resetdb`` in your ``INSTALLED_APPS``::

	INSTALLED_APPS = (
	    ...
	    'resetdb',            
	)


-----
Usage
-----

	./manage.py help resetdb 
	