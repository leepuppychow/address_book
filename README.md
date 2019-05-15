# Address book application

## Server (Docker, Flask, postgreSQL): Run from `/server` directory

1. Need to have Docker installed
2. If you have PostgreSQL running locally make sure to stop that to free up port:
    * Ex: `brew services stop postgres`
    * Ex: `pg_ctl -D /usr/local/var/postgres stop`
3. From `/server` run `docker-compose build`
4. From `/server` run `docker-compose up`
5. Check status of server with GET to `http://localhost:5000/api/v1/ping` --> status 200

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

