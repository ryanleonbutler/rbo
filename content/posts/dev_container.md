---
title: 'Building My Own Custom Dev Container'
image: '/images/posts/ian-taylor-jOqJbvo1P9g-unsplash.webp'
date: 2024-07-12
description: 'In this post I explain how I built my own custom Dev container for my side projects'
tags: ['Docker', 'Software Development']
type: post
weight: 20
showTableOfContents: true
---

![](/images/posts/ian-taylor-jOqJbvo1P9g-unsplash.webp)

There was always this need for me to build my own dev container with all of my dev tools. For a very long time I have been managing my dotfiles
using source control and creating little shell scripts that can easily setup my machine, but the ultimate portable environment has to be a 
dev Docker container.

In this post I will be creating my own Docker file with all my dev tools.

Lets see if this goes and hopefully it will be pretty good.

# Installing Docker

First things first, we need [Docker](https://docs.docker.com/guides/getting-started/get-docker-desktop/).

After following the relevant install guide and we can confirm the installation in complete, lets verify it is up and running.

```bash
> docker --version
Docker version 25.0.3, build 4debf41

> docker run -d -p 8889:80 docker/welcome-to-docker
Unable to find image 'docker/welcome-to-docker:latest' locally
latest: Pulling from docker/welcome-to-docker
579b34f0a95b: Pull complete
d11a451e6399: Pull complete
54b19e12c655: Pull complete
1c2214f9937c: Pull complete
1fb28e078240: Pull complete
94be7e780731: Pull complete
b42a2f288f4d: Pull complete
89578ce72c35: Pull complete
Digest: sha256:eedaff45e3c78538087bdd9dc7afafac7e110061bbdd836af4104b10f10ab693
Status: Downloaded newer image for docker/welcome-to-docker:latest
8d5e291b3ee211e427c2d5e6449f14c41e74d7c46b1af378ce291b852a03ae37

> curl -I http://localhost:8080
HTTP/1.1 200 OK
Server: nginx/1.25.3
Date: Fri, 12 Jul 2024 13:05:41 GMT
Content-Type: text/html
Content-Length: 651
Last-Modified: Tue, 07 Nov 2023 16:50:23 GMT
Connection: keep-alive
ETag: "654a6acf-28b"
Accept-Ranges: bytes
```

# Starting with our custom Dockerfile

I am creating the [dev_machine](https://github.com/ryanleonbutler/dev_machine) repository for this project.

Next create the Dockerfile. This is a manifest which has all the details of what OS and software will be in our container.
```bash
mkdir dev_machine && cd dev_machine && git init && touch README.md && touch Dockerfile && vim Dockerfile
```

I will be using the Alpine image, which is a minimal linux environment with some basic tools and features. Alpine is all about keeping the images
compact and with no clutter.

```yaml
# Dockerfile
FROM alpine:latest

WORKDIR /root

RUN apk update;
```

# Post History
- Posted: 2024-07-12
