----------------------
Getting started
----------------------

This sample app is for showing how easy it is to integrate hiku data anywhere using webhooks.

The sample is built on heroku using python flask, but the concepts of receiving webhook data and taking action on it
can be applied to any environment. To learn more about simple python flask apps in heroku, see http://virantha
.com/2013/11/14/starting-a-simple-flask-app-with-heroku/. It is a helpful tutorial for setting up your local
environment and deploying to heroku.

To get started, clone the repository at https://github.com/hikuinc/hiku_sample_app.git, and then push it to a newly
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

The sample app is currently deployed to https://hiku-sample-app.herokuapp.com/.

----------------------
A note on security
----------------------
This is a sample app and is not built with security in mind. The Pusher key and channel is exposed in the javascript of
showBeep.htm, so anyone can listen to it with those credentials. No one will be able to send messages over that
Pusher channel though. However, the /beep endpoint does not do any security checks which we would expect, e.g.
validate the token sent via the webhook. So anyone can POST to that endpoint and mimic the payload (well documented in
our API's). In other words, if you plan to build a commercial application, please include additional security.

----------------------
Good for demos
----------------------
You can customize how data is displayed by modifying docs/showBeep.htm. By 'branding' that page and applying your own
fonts, color schemes, styles, etc it will demonstrate how easy it is for our partners to integrate hiku data into
their own digital systems. We have found that a demo is very convincing with other stakeholders when hiku scan/speaks
immediately show up in their own digital ecosystem.

----------------------
Build something really cool!
----------------------
This app is purely a demonstration. Please take the code and modify it to do more interesting things with hiku than
simply display the last scan/speak, e.g. add items to shopping basket, another list app, send an SMS, control the
temperature of a Nest thermostat, etc!

You can learn more about hiku webhooks (e.g. payload specifications, types of events supported, etc) and the full
hiku API/SDK suite at https://github.com/hikuinc/hiku_shared. If you would like API credentials to do more than use
webhooks, please email devrel@hiku.us.

