# Address book application

## Server (Docker, Flask, postgreSQL): Run from `/server` directory

1. [Need to have Docker installed](https://docs.docker.com/install/)
2. Create new `.env` file within `/server` directory and copy contents of `example.env` into there
    * Note: by leaving FLASK_DEBUG=1 the server will hot reload (because of the volumes setup in the docker-compose server service)
    * Turn off by setting FLASK_DEBUG=0
3. In `.env`, set USPS_USER_ID equal to your USPS username. 
4. If you have PostgreSQL running locally make sure to stop that to free up port:
    * Ex: `brew services stop postgres`
    * Ex: `pg_ctl -D /usr/local/var/postgres stop`
5. From `/server` run `docker-compose build`
6. From `/server` run `docker-compose up`
7. Check status of server with GET to `http://localhost:5000/api/v1/ping` --> status 200

## Client (Vue.js): Run from `/client` directory

### Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Run your unit tests
```
npm run test:unit
```

### Run your end-to-end tests
```
npm run test:e2e
```

