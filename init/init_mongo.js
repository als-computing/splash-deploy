use admin
db.createUser(
  {
    user: "wave_admin",
    pwd: "" , 
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
  }
)


use splash
db.createUser(
  {
    user: "wave_app",
    pwd:  "", 
    roles: [ { role: "readWrite", db: "splash" } ]
  }
)