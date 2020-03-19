docker-compose up -d

docker exec -it splash_db_1 /bin/bash


echo mongo --host db:27017 

echo above will get you logged into the mongo command line, but
echo you need to manually type after:



var cfg = {  
  "_id": "rs0",
  "version": 1,
  "members" : [
   {"_id": 1, "host": "db:27017"}
  ],settings: {chainingAllowed: true}
 }

 rs.initiate(cfg, { force: true });
