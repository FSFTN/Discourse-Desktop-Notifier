#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Prasanna Venkadesh (prasanna@fsftn.org)
Free Software (GPL V3)
'''

try:
    import sys
    from pydiscourse.client import DiscourseClient
    from os import system, environ, path

    file_path = environ.get('HOME') + '/.discourse/notification_count'
except BaseException, be:
    print be.message
    print "Please run configure.py"
    sys.exit()

discourse_powered_site = 'http://discuss.fsftn.org'


def main():
    client = DiscourseClient(discourse_powered_site,
                             api_username=API_USERNAME,
                             api_key=API_KEY)

    user = client.user(API_USERNAME)
    notification_count = int(user.get('notification_count'))
    print notification_count

    if path.isfile(file_path):
        # open the existing file and update the value if it has changed
        with open(file_path, 'r+') as notification_file:
            previous_count = int(notification_file.read().strip())
            print "Previous count: %d" % previous_count

            if notification_count > previous_count:
                notification_file.seek(0)
                notification_file.write(str(notification_count))
                notification_file.truncate()

                new_notification = notification_count - previous_count

                # send system notification
                system("notify-send -t 0 'FSFTN Discussion' 'You have new notification(s)'")

    else:
        # create the file for the first time
        with open(file_path, 'w') as notification_file:
            notification_file.write(str(notification_count))


if __name__ == '__main__':

    API_KEY = environ.get('DISCOURSE_APIKEY', None)
    API_USERNAME = environ.get('DISCOURSE_USERNAME', None)

    if API_KEY is None or API_USERNAME is None:
        print("DISCOURSE_APIKEY / DISCOURSE_USERNAME environment \
              variable not set.\nRun the configure.py before running \
              this program.")
        sys.exit()

    main()
