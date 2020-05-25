#!/bin/sh

/usr/bin/python /webvirtmgr/manage.py collectstatic --noinput
/usr/bin/python /webvirtmgr/manage.py syncdb --noinput

