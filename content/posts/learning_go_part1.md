---
title: 'Learning Golang (Part 1)'
image: '/images/posts/aisvri-l1LFITfODPE-unsplash.webp'
date: 2023-10-06
description: 'In this multi part series we start from the beginning and learn this great general purpose language!'
tags: ['Golang', 'Software Development']
type: post
weight: 20
showTableOfContents: true
---

![](/images/posts/aisvri-l1LFITfODPE-unsplash.webp)

I have been thinking about learning a new language for a while. But which one 🤷

There is a lot of hype around Rust of late, and I have considered it for a while, but there is just something about Go
that keeps pulling me back to it. That brings us here, where I will be learning Go, also known as Golang, and sharing
my journey here.

Hold on tight, Go is fast, really fast!

# Installing Go

Seems to be a few ways to go about this. My preference, like I have been doing with Python and Node, is using
[asdf](https://asdf-vm.com). You would need to install the [asdf-go](https://github.com/asdf-community/asdf-golang)
plugin as well. Once you have that out the way we can install golang v1.21.1.

```bash
asdf install golang 1.21.1
```

Once installed you can set it to the local or global shim using asdf to add the new installed version to your path

```bash
asdf global golang 1.21.1
```

Now we can confirm if we have the installed version available.

```bash
go version                                                                   │
go version go1.21.1 darwin/arm64                                                                                 │
```

# Starting a new Go project

I am creating the [learn_go](https://github.com/ryanleonbutler/learn_go) repository, which is also on my Github page.

```bash
mkdir learn_go && cd learn_go && git init && touch README.md
```

Next let's start with a classic, the old `"Hello, world!"`

```bash
mkdir example && cd example

go mod init example/hello
go: creating new go.mod: module example/hello

go mod tidy

touch hello.go
```

# Hello world code

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

# Running code
```bash
go run hello.go

Hello, World!
```
