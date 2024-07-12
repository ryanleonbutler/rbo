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
[mise](https://mise.jdx.dev/).

```bash
> mise use -g go@latest
```

The above will install latest version of Go and set it as the default global version to use.

Now we can confirm if we have the latest verson Go available.

```bash
> go version                                                                   │
go version go1.22.3 darwin/arm64
```

# Starting a new Go project

I am creating the [learn_go](https://github.com/ryanleonbutler/learn_go) repository, which is also on my Github page.

```bash
mkdir learn_go && cd learn_go && git init && touch README.md
```

Next let's start with a classic, the old `"Hello, world!"`

```bash
> mkdir hello_world

> go mod init hello_world/main
go: creating new go.mod: module hello_world/main

go mod tidy

cd hello_world && touch main.go && nvim main.go
```

# Hello world code

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

# Formatting code with go fmt

```bash
> go fmt
main.go
```

# Running code

```bash
> go run main.go
Hello, World!
```

# Last words

Wow! I like how easy it is to started with Go and the built-in dev tools. I look forward to the next step and learning more about Go. 

# Post History
- Updated: 2024-07-12
- Posted: 2023-10-06
