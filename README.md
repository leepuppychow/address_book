# ADDRESS BOOK APPLICATION

## Server (Docker, Flask, postgreSQL)

### Setup (instructions are for MacOS)

1. [Need to have Docker installed](https://docs.docker.com/install/)
2. Create new `.env` file within `/server` directory and copy contents of `example.env` into there
    * Note: by leaving FLASK_DEBUG=1 the server will hot reload (because of the volumes setup in the docker-compose server service)
    * Turn off by setting FLASK_DEBUG=0
3. In `.env`, set USPS_USER_ID equal to your USPS username. 
4. In `.env`, set JWT_SECRET to whatever you would like.
5. If you have PostgreSQL running locally make sure to stop that to free up port:
    * Ex: `brew services stop postgres`
    * Ex: `pg_ctl -D /usr/local/var/postgres stop`
6. If you happen to have existing Docker containers named `server_server_1` and/or `server_postgres_1` remove those first:
    * From `/server` directory run: `docker-compose down`
7. Be in directory `/server`, and then run `docker-compose build`
8. Be in directory `/server`, and then run `docker-compose up`
9. Check status of server with GET to `http://localhost:5000/api/v1/ping` --> status 200

### Notes

* All routes except `/ping`, `/login`, and `/register` are protected with JWT
* Pass in token with header (ex: `"Authorization": "Bearer yourtokenblahblahblah..."`)
* To get a token, POST to `/api/v1/login` with body:

    ```
        {
            "email": "test@test.com",
            "password": "password"
        }
    ```

### Routes

* GET /api/v1/ping
* POST /api/v1/login
* POST /api/v1/register
* GET /api/v1/addresses
* GET /api/v1/addresses/:id
* POST /api/v1/addresses
* PUT /api/v1/addresses/:id
* DELETE /api/v1/addresses/:id
* POST /api/v1/zipcode-lookup

## Client (Vue.js)

### Project setup (have server running first)

```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

* You can login with a test user:

```
    EMAIL = test@test.com
    PASSWORD = password
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

### Run your end-to-end tests (this uses [Cypress](https://www.cypress.io/))
```
npm run test:e2e
```

