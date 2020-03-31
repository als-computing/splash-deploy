# What is this?
This is a project that sets up docker containers to ease in deployment of the Splash system for both developers and for production use.

Previously, this project was a super module of splash-client and splash-server. The submodules have been undone, and this project should now sit as a siblish to the two. An example might look like, where splash-client, splash-deploy and splash-server are clones of github repositories.

```
splash
├── splash-client
├── splash-deploy
└── splash-server
```



# Developers
Fork this repo along with splash-server and splash-client. The docker-compose.override.yml file brings up a fully functional development-mode installation. 

Run:
```
docker-compose up
```

Developer mode differs from production mode in several important ways.

Production mode depends on the vue.js app being built manually and installed into slash-client/dist. This is then picked up by the nginx server via configuration in splash-deploy/web/nginx.conf. For development, this has been removed, and developers are responsible for launching vue themselves. Install npm for your operating system, then:

```
cd splash-client
npm run serve
```

This will start vue server 

This will bring up all components except vue (elastic, mongo, flask, monstache). flask and vue are brought up in developer mode:
* make changes to splash-server python code and it auto-reloads in the server
* Save vue files in splash-client, and it auto-reloads.

In this case, the url to access the splash page is localhost:8080.

Another important aspect to this configuration is that development-quality web server that npm starts will redirect ```/api``` requests to localhost:5000 (which is the flask exposed by the development containers). Additionally, ```/search``` requests will be forwarded to the elastic service.

Finally, in development mode, the flask code in splash-server is started up in developer mode as well. This starts up as a single process and autoreloads python code when is saved in the splash-server project.

# Production
Production mode differs from development mode in several important ways. The production service exposes fewer ports, depends on splash-client vue code being built ahead of time, and does not autoload code in vue or python. The flask service is launche the more robust uwsgi service.

To run production mode:
1. Copy the prebuilt vue app into splash-cleint/dist.
2. Launch docker without the docker-compose.override.yml file:
  
   ```docker-compose -f docker-compose.yml```

