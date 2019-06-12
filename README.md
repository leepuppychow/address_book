# ADDRESS BOOK APPLICATION

### Dashboard Screenshot

![Screenshot](./Addr-Screenshot.png)

## Server (Docker, Flask, postgreSQL)

### Setup (instructions are for MacOS)

1. [Need to have Docker installed](https://docs.docker.com/install/)
2. Create new `.env` file within `/server` directory and copy contents of `example.env` into there
    * Note: by leaving FLASK_DEBUG=1 the server will hot reload (because of the volumes setup in the docker-compose server service)
    * Turn off by setting FLASK_DEBUG=0
3. In `.env`, set the following environment variables:
    * USPS_USER_ID equal to your USPS username. 
    * JWT_SECRET to whatever you would like.
    * SENDGRID_API_KEY
    * TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER
4. If you have PostgreSQL running locally make sure to stop that to free up port:
    * Ex: `brew services stop postgres`
    * Ex: `pg_ctl -D /usr/local/var/postgres stop`
5. If you happen to have existing Docker containers named `server_server_1` and/or `server_postgres_1` remove those first:
    * From `/server` directory run: `docker-compose down`
6. Be in directory `/server`, and then run `docker-compose build`
7. Be in directory `/server`, and then run `docker-compose up`
    * NOTE: For more workers (for sending emails or text messages) run: `docker-compose up --scale worker=5`
8. Check status of server with GET to `http://localhost:5000/api/v1/ping` --> status 200
9. You can monitor the status of the Celery workers via the Flower monitoring service at `http://localhost:5555`

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
* POST /api/v1/email
* POST /api/v1/send-text

## Client (Vue.js)

* NOTE: if there is an issue running the client-side code locally, you can view the most recent app with the link below. You still need the server running locally (I did not want to deploy the server and database at this time):

    [Deployed via Netlify](https://stoic-wing-d9a1c2.netlify.com/#/)

* Use: _Node.js version: 8.9.4_
* From the `/client` directory:

### Project setup

```
npm install
```

### Compiles and hot-reloads for development

* Make sure that server is running.

```
npm start
```

* You can login with test users:

```
    EMAIL = test@test.com
    PASSWORD = password
```

```
    EMAIL = test2@test.com
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

#### Contributors:
* Lee Chow
* [Heather Hartley](https://github.com/hlhartley) - Frontend UI & Design 

