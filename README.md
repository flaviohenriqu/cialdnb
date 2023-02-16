# cialdnb challenge

## Directory structure

```
cialdnb-challenge
|____ main.py
|____ tasks.py
|____ requirements.txt
|____ Dockerfile
|____ websites.txt
|____ .gitignore
```

## Build an image

```
$ docker build --tag cialdnb-challenge .

[+] Building 2.7s (10/10) FINISHED
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 203B
 => [internal] load .dockerignore
 => => transferring context: 2B
 => [internal] load metadata for docker.io/library/python:3.10-slim-buster
 => [1/6] FROM docker.io/library/python:3.10-slim-buster
 => [internal] load build context
 => => transferring context: 953B
 => CACHED [2/6] WORKDIR /app
 => [3/6] COPY requirements.txt requirements.txt
 => [4/6] RUN pip install -r requirements.txt
 => [5/6] COPY . .
 => [6/6] CMD [ "python", "-m", "main"]
 => exporting to image
 => => exporting layers
 => => writing image sha256:8cae92a8fbd6d091ce687b71b31252056944b09760438905b726625831564c4c
 => => naming to docker.io/library/python-docker
```

## Run your image

```
$ cat websites.txt | docker run -i cialdnb-challenge

DEBUG:httpx._client:HTTP Request: GET https://www.cialdnb.com/contact/ "HTTP/1.1 200 OK"
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): www.cialdnb.com:443
DEBUG:urllib3.connectionpool:https://www.cialdnb.com:443 "HEAD /data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20326%2060'%3E%3C/svg%3E HTTP/1.1" 403 0
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): www.cialdnb.com:443
DEBUG:urllib3.connectionpool:https://www.cialdnb.com:443 "HEAD /wp-content/uploads/2020/01/logo-cialdnb-color.png HTTP/1.1" 200 0
DEBUG:httpx._client:HTTP Request: GET https://chemondis.com/contact-us.html "HTTP/1.1 200 OK"
DEBUG:httpx._client:HTTP Request: GET https://www.cmsenergy.com/contact-us/default.aspx "HTTP/1.1 200 OK"
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): chemondis.com:443
DEBUG:urllib3.connectionpool:https://chemondis.com:443 "HEAD /images/Logo_White.svg?h=1bc3bbdcbb2bb10528d87991c053f71d HTTP/1.1" 200 0
INFO:tasks:website's logo not found
DEBUG:httpx._client:HTTP Request: GET https://pt.aptoide.com/company/about-us "HTTP/1.1 200 OK"
INFO:tasks:website's logo not found
DEBUG:httpx._client:HTTP Request: GET https://www.illion.com.au "HTTP/1.1 200 OK"
DEBUG:httpx._client:HTTP Request: GET https://www.illion.com.au/contact-us "HTTP/1.1 200 OK"
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): www.illion.com.au:443
DEBUG:urllib3.connectionpool:https://www.illion.com.au:443 "HEAD /data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20109%2032'%3E%3C/svg%3E HTTP/1.1" 301 0
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): www.illion.com.au:443
DEBUG:urllib3.connectionpool:https://www.illion.com.au:443 "HEAD /wp-content/uploads/2019/03/ION-RGB-Gradient-64.png HTTP/1.1" 200 0
DEBUG:httpx._client:HTTP Request: GET https://www.phosagro.com/contacts/ "HTTP/1.1 200 OK"
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): www.phosagro.com:443
DEBUG:urllib3.connectionpool:https://www.phosagro.com:443 "HEAD /local/templates/.default/img/fosagro-logo-en--coloured.svg HTTP/1.1" 200 0
[{'logo': 'https://www.illion.com.au/wp-content/uploads/2019/03/ION-RGB-Gradient-64.png',
  'phones': [],
  'website': 'https://www.illion.com.au'},
 {'logo': 'https://www.cialdnb.com/wp-content/uploads/2020/01/logo-cialdnb-color.png',
  'phones': [],
  'website': 'https://www.cialdnb.com/contact/'},
 {'logo': 'https://www.illion.com.au/wp-content/uploads/2019/03/ION-RGB-Gradient-64.png',
  'phones': ['13 23 33',
             '+61398283200',
             '13 23 33',
             '+61871229452',
             '+64800836268',
             '1800233533'],
  'website': 'https://www.illion.com.au/contact-us'},
 {'logo': None,
  'phones': [],
  'website': 'https://www.cmsenergy.com/contact-us/default.aspx'},
 {'logo': 'https://www.phosagro.com/local/templates/.default/img/fosagro-logo-en--coloured.svg',
  'phones': ['+74952329689',
             '+74959561902',
             '+74952313115',
             '+749523296892712',
             '+79296004642',
             '+79255862405',
             '+78202593232',
             '+74952329689',
             '+74952313115',
             '+79255862405'],
  'website': 'https://www.phosagro.com/contacts/'},
 {'logo': 'https://chemondis.com/images/Logo_White.svg?h=1bc3bbdcbb2bb10528d87991c053f71d',
  'phones': [],
  'website': 'https://chemondis.com/contact-us.html'},
 {'logo': None,
  'phones': [],
  'website': 'https://pt.aptoide.com/company/about-us'}]
```