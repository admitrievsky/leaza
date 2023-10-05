This repository has been archived by the owner. It is now read-only.
====

Leaza
=====

Leaza is a social media Django website engine. It focuses on user-created content.
Any post may contain rich text, images dropped to the editor (no upload of files needed), embedded youtube videos.
There is an tree-like commenting system where comment is an ordinal post, so it also may contain rich media.
 
Requirements
============

* Python 3.4 or higher
* Tested with Django 1.8
* SQL Database you like
* apt-get install coffee
* apt-get install node-less


Installation
============
* (Optional) Create an virtual environment
* Install requirements ```pip install -r requirements.txt```
* Copy leaza/settings_local_example.py to leaza/settings_local.py and review it
* Migrate ```./manage.py migrate```
* Install gunicorn, run the webserver you like

Licence
=======

This code is under BSD license. There may be third-party code that is under their license.
