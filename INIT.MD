How to initialize the docker containers:

Make sure to create all of the folders that will be used by the volumes first. If you don't it creates weird permissions issues. Also create a file called `monstache.config.toml` in the monstache volume directory. It may be necessary to set `elasticsearch-healthcheck-timeout` and `elasticsearch-healthcheck-timeout-startup` to larger values in this config file depending on how slow your computer is.

On Linux hosts run  `sysctl -w vm.max_map_count=262144`  and then `sysctl --system`

See: https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-prod-cluster-composefile

Change your working directory to the top level directory

These commands initialize the replica set for mongo:

`docker-compose start db`

`docker exec -i splash_db_1 /bin/bash < ./init/init_mongo.sh`

`docker-compose stop db`


Run `docker-compose up`

Wait until you see 

monstache        | INFO 2020/05/16 00:16:52 Successfully connected to Elasticsearch version 7.5.0

monstache        | INFO 2020/05/16 00:16:52 Listening for events

monstache        | INFO 2020/05/16 00:16:52 Watching changes on the deployment

Open another terminal and change your working directory to `./init/python`

Run:

`python3 -m venv env`

`source ./env/bin/activate`

`pip install -r requirements.txt`

Additionally if in development run: `pip install -r requirements-dev.txt`

`python3 setup.py`
