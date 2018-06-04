# url-shortener-flask-tinymongo

URL Shortener with Python Flask and TinyDB

## Run Server:

Define your domain and run the server:

```bash
$ python app.py
```

## Create a Shortlink:

Create a shortlink by using the /create endpoint:

```bash
curl http://localhost:5000/create/https://ip.ruanbekker.com
Your TinyURL is: <a href="http://localhost:5000/u/znJDoXQTxqfXIqv">http://localhost:5000/u/znJDoXQTxqfXIqv</a>
```

## Check a Shortlink's Full URL:

Check the Full URL by passing the shortlinks address:

```bash
$ curl http://localhost:5000/check/http://localhost:5000/u/znJDoXQTxqfXIqv
Your Full URL is: https://ip.ruanbekker.com
```

## Hit the Shortlink URL:

Make a GET request to the shortlink url, and it should redirect you to the target address:

```bash
$ curl -iLv http://localhost:5000/u/znJDoXQTxqfXIqv
* Connected to localhost (127.0.0.1) port 5000 (#0)
> GET /u/znJDoXQTxqfXIqv HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.54.0
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 302 FOUND
HTTP/1.0 302 FOUND
< Content-Type: text/html; charset=utf-8
Content-Type: text/html; charset=utf-8
< Content-Length: 257
Content-Length: 257
< Location: https://ip.ruanbekker.com
Location: https://ip.ruanbekker.com
< Server: Werkzeug/0.14.1 Python/3.6.5
Server: Werkzeug/0.14.1 Python/3.6.5
< Date: Mon, 04 Jun 2018 23:11:27 GMT
Date: Mon, 04 Jun 2018 23:11:27 GMT

<
* Closing connection 0
* Issue another request to this URL: 'https://ip.ruanbekker.com'
* Rebuilt URL to: https://ip.ruanbekker.com/
```
