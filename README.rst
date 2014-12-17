Planlos App using flask
=======================

Rewrite of the current django-based planlos-app with Flask+MongoDB.


Dependencies / How to setup
------------

* 	install python
		sudo apt-get install python
*	install pip module manager
		sudo apt-get install pip
*	install flask and external flask modules
		sudo pip install flask-login flask-mail flask-mongokit flask-script flask-testing flask-wtf flask-sijax
*	install other python modules
		sudo pip install mongokit pymongo nose coverage python-dateutil
*	install mongoDB database
		sudo apt-get install mongodb



Development
-----------

For your convenience use virtualenv+pip, then

Run the development server::
     python manage.py runserver

Run the tests + coverage::
     python manage.py test


There are some management commands to fill your database with events from the current planlos. Or to add users, etc.
see ``manage.py``.
