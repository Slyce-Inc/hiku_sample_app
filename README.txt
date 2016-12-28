----------------------
Getting started
----------------------

This sample app is for showing how easy it is to integrate hiku data anywhere using webhooks.

The sample is built on heroku using python flask, but the concepts of receiving webhook data and taking action on it
can be applied to any environment. To learn more about simple python flask apps in heroku, see http://virantha
.com/2013/11/14/starting-a-simple-flask-app-with-heroku/. It is a helpful tutorial for setting up your local
environment and deploying to heroku.

To get started, clone the repository at https://github.com/rkatcher/hiku_sample_app.git, and then push it to a newly
created heroku app that you own.

In order to see the demo work live, you will need to add Pusher to your heroku app. The app can run for free on
heroku, no paid add-ons or upgrades are required. Add your Pusher credentials as environment varaibles in heroku as
follows. You can set these up in your local environment by creating a .env file.
PUSHER_APP_ID=
PUSHER_KEY=
PUSHER_SECRET=

Then email support@hiku.us with the url of your newly deployed endpoint, https://yourHerokuAppName.heroku.com/beep,
and the hiku team will setup your webhook.

Point a browser to https://yourHerokuAppName.heroku.com/showBeep. Then scan or speak into hiku. When deployed
properly, the scan/speak item will display an alert window in the open browser.

----------------------
Build something really cool!
----------------------
This app is purely a demonstration. Please take the code and modify it to do more interesting things with hiku, e.g.
add items to shopping basket, another list app, send an SMS, control the temperature of a Nest thermostat,
etc!

If you would like API credentials to do more than use webhooks, please email support@hiku.us.

