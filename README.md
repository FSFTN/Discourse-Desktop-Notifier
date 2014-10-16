## Desktop Notification system for Discourse Powered Site

This small program when run in the background, will check for new notifications on the user profile on discourse powered discussion site and notifies the user on the desktop.

The Notification will remain on the screen until the user manually closes it. However, this setting can be overridden.

-----------------------

## Running the program

Clone this repository.

    git clone https://github.com/FSFTN/discourse-desktop-notifier.git

    cd discourse-desktop-notifier

    python configure.py


`configure.py` will check for pre-requisites to run the program. If everything was fine and if you see the message `Done Setting Up.`,then try running

    python notification.py


Read the below section and come back here, if configuration failed.


----------------------

## Environment Variables

The program will look for `DISCOURSE_APIKEY` & `DISCOURSE_USERNAME` variables in order to run. If not found, the application cannot be run.

**Setting variables**
* `DISCOURSE_APIKEY` is the API_KEY generated for your account on the discourse site. To find your key or to generate a new key, go to the discourse powered site, login into your account and hit the endpoint `http://yoursite.com/admin/users/YOUR_USERNAME`.

* You can find API Key section where you can generate a key. Copy the key value.

* In your terminal, run the following


    export DISCOURSE_APIKEY='PASTE_THE_KEY_VALUE_COPIED'
    export DISCOURSE_USERNAME='YOUR_USERNAME'

Note: You can update the ~/.profile file so that the environment variables will be preserved and you need to repeat this process of setting the variables everytime before you run the program.

**Run `python configure.py` again to make sure things are in place**

-----------------------

## PyDiscourse

[PyDiscourse](https://github.com/tindie/pydiscourse/) is an Python API for working with Discourse. We are using this python API to communicate with discourse powered site. Since pydiscourse also depends on `requests` library, we need to install that too.

**Installing PyDiscourse**

    git clone https://github.com/tindie/pydiscourse.git
    
    cd pydiscourse

    sudo python setup.py install

    sudo pip install -U requests


On successfull installation, run the `python configure.py` again to make sure things are in place.

------------------------

## Check Notification

`python notification.py` will produce system notification if there are any new notifications for you.

Use crontab to check notification after n number of minutes.

**Example**

`crontab -r` (**caution**: This will remove any existing cron jobs if you already have.)

* Open the `cronfile` in your text editor present in the same directory and set the values for `DISCOURSE_APIKEY` & `DISCOURSE_USERNAME`. Also do replace the `/path/to` to point to the path where this directory is located.

`crontab cronfile` (We are supplying `cronfile` as input to the crontab)


Save the file and the above cron job will run the program for every 10 minutes to check for notification
