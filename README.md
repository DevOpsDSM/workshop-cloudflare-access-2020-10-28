# workshop-cloudflare-access-2020-10-28

This codebase was used to demo Cloudflare Access.

_NOTE_: we assume you have a cloudflare account and at least one zone setup already.

## Server Setup

Login to cloudflared

```bash
$ cloudflared login
```

Copy your cloudflare cert.pem to a local folder (not great, but meh)

```bash
$ mkdir -p cloudflared
$ cp ~/.cloudflared/cert.pem ./cloudflared/
```

For testing, we have included a docker-compose that will set up everything on the server side. 

This emulates an internal web application and database.

```bash
$ docker-compose up -d
$ docker-compose run web python manage.py migrate
$ docker-compose logs -f web-tunnel db-tunnel
```

To shut the docker containers down:

```bash
$ docker-compose stop
```

## Client Setup

Connecting to the web ui just navigate to `django.spencerherzberg.com`

To connect to the database remotely:

```bash
$ cloudflared access tcp --hostname https://django-postgres.spencerherzberg.com --url localhost:5432
```

This will open a browser window to approve the request. After you click approve, any postgres client can now connect to `localhost:5432`.

## Hit authenticated URLS different ways

https://developers.cloudflare.com/access/cli/connecting-from-cli