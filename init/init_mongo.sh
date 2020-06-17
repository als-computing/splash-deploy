


mongo --eval 'var cfg = {
  "_id": "rs0",
  "version": 1,
  "members" : [
   {"_id": 1, "host": "db:27017"}
  ],settings: {chainingAllowed: true}
 }
 rs.initiate(cfg, { force: true });'
