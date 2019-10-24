<img src="https://i.imgur.com/24ebrZ1.png" />

# Using the app:

## Make sure you have docker installed.

## Change working directory to app:

- ```cd app```

## Build a docker image (we will tag it as "sajans/exoselfie" for this example), run:

Note: it will take a minute or two to install all dependencies (final image is around 1.5 GB in size).

- ```docker build . -t sajans/exoselfie```

Final output should look like this:
<img src="https://i.imgur.com/NcXupMP.png"  width="400" height="180" />

## Run docker image:

Note: in order for the app to work, port forwarding has to be done in the exact same way as in the example:

Run in the background:
- ```docker run -d -p 8000:8000 -p 5000:5000 sajans/exoselfie```

Run in attached mode:
- ```docker run -p 8000:8000 -p 5000:5000 sajans/exoselfie```

## You are ready to access your app on http://127.0.0.1:5000/ :

<img src="https://i.imgur.com/Z9wAToG.jpg"  />

## Upload your photo and have fun!

<img src="https://i.imgur.com/wKXaBLE.jpg"  />

