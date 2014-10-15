#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author = Prasanna Venkadesh
Free Software (GPL V3)

--------------------------

This will check for pre-requisites for the application to run properly.
Starting with simple directory check, this file might grow gradually
depending on the addition of new features.
--------------------------
'''

import os
import sys

def check_libraries():
    try:
        import pydiscourse
        print "SUCCESS: PyDiscourse Library Found."
    except:
        print "FAILURE: pydiscourse not found. Please install from https://github.com/tindie/pydiscourse"
        print "-" * 20
        sys.exit()



if __name__ == '__main__':
    directory = os.environ.get('HOME') + '/.discourse'

    print "-" * 20

    if not os.path.exists(directory):
        print "Target Directory doesn't exist. Creating one"
        os.makedirs(directory)
        print "SUCCESS: Target Directory created."
    else:
        print "Target Directory found."

    if os.environ.get('DISCOURSE_APIKEY', None) == None:
        print "FAILURE: DISCOURSE_APIKEY environment variable not found."
        print "-" * 20
        sys.exit()
    else:
        print "SUCCESS: DISCOURSE_APIKEY environment variable found."

    if os.environ.get('DISCOURSE_USERNAME', None) == None:
        print "FAILURE: DISCOURSE_USERNAME environment variable not found. ERROR"
        print "-" * 20
        sys.exit()
    else:
        print "SUCCESS: DISCOURSE_USERNAME environment variable found."

    check_libraries()

    print "Done setting up."

    print "-" * 20
