# What is this?
This is a project that contains git submodules. It is a convenience for getting all components in one step. See [Splash Docs](https://github.com/als-computing/splash-doc/tree/60a7584c4790c65ef7c920b1c9fd8424d0a594fd) for more info.

# Developers
Clone or fork this repo along with splach-server and splash-client. The docker-compose.override.yml file brings up a fully functional development-mode installation. 

Running
```
docker-compose up
```

Will bring up all components (elastic, mongo, flask, vue, monstache). flask and vue are brought up in developer mode:
* make changes to splash-server python code and it auto-reloads in the server
* Save vue files in splash-client, and it auto-reloads.

In this case, the url to access the splash page is localhost:8080

# Production
Delete the docker-compose.override.yml file. This removes developer mode. The flask code is run in a multi-process uwsgi container instead. In this case, the url to acces the splash page is localhost:80.

