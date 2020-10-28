# workshop-cloudflare-access-2020-10-28

This codebase was used to demo Cloudflare Access

## Setup

Login to cloudflared

```bash
$ cloudflared login
```

Copy your cloudflare cert.pem to a local folder (not great, but meh)

```bash
$ mkdir -p cloudflared
$ cp ~/.cloudflared/cert.pem ./cloudflared/
```

## Hit authenticated URLS:

https://developers.cloudflare.com/access/cli/connecting-from-cli