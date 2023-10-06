---
title: 'My terminal setup 2.0'
image: '/images/posts/joshua-j-cotten-uyKB8ZZApU0-unsplash.webp'
date: 2023-09-03
description: 'Update from previous terminal setup'
tags: ['Tools', 'Terminal']
type: post
weight: 20
showTableOfContents: true
---

![](/images/posts/joshua-j-cotten-uyKB8ZZApU0-unsplash.webp)

Previous post: [My terminal setup](/posts/my_terminal_setup)

This is an update on my previous post showcasing my terminal setup and the tools I use. Since then I moved to
Alacritty, still using fish shell with the Starship prompt. See below some basic steps to get started with each and
links to my configuration files on GitHub.

# [Alacritty](https://alacritty.org)

Alacritty is actually a very basic terminal. No tabs and no menus. And that's what makes it great. It does not try and
do too much, keeping things simple, but fast. Yet offering you some flexibility if you wish to go down the
configuration rabbit hole.

## Install Alacritty

Alacritty is supported on Linux, MacOS and Windows. You can find the installation instructions
[here](https://alacritty.org/#Installation).

## Customize Alacritty

This is where Alacritty also shines. It uses YAML as a configuration language and it is really easy to customize with a
lot of online resources and examples. I also like the live reload feature. When you save your terminal settings the
changes are immediately applied without the need to restart the terminal. Magic!

Once installation is complete you can create the following configuration file or edit the existing one:

```bash
vim ~/.config/alacritty/alacritty.yml
```

The main things you would want to change first is:

-   Font family and size - JetBrains has some great tools, but I'd argue their best creation is their font 👏

```yaml
font:
    normal:
        family: JetBrainsMono Nerd Font Mono
        style: Regular

    bold:
        family: JetBrainsMono Nerd Font Mono
        style: Bold

    italic:
        family: JetBrainsMono Nerd Font Mono
        style: Italic

    bold_italic:
        family: JetBrainsMono Nerd Font Mono
        style: Bold Italic

    size: 16.0
```

-   Live config reload

```yaml
live_config_reload: true
```

-   Theme - I am actually just using the default, but you can change it to something like catppuccin. I recommend
    importing and keeping the theme config in another file.
    [Here](https://github.com/ryanleonbutler/dotfiles/blob/main/alacritty/themes/catppuccin.yaml) is the link to the
    below config file.

```yaml
import:
    - ~/.config/alacritty/themes/catppuccin.yaml
```

# [Fish shell](https://fishshell.com)

For details on fish shell see everything you need in a previous post:
[Moving to fish shell](/posts/moving_to_fish_shell)

# Starship

Yes, Starship prompt. Beautiful. Fast.

## Install Starship

A simple bash one liner does the trick, but you can visit their
[installation page](https://starship.rs/guide/#%F0%9F%9A%80-installation) for more methods.

```bash
curl -sS https://starship.rs/install.sh | sh
```

## Customize Starship

You can customize almost every little detail of your prompt using Starship, and again, it pretty easy since it also
uses a YAML configuration file. The creators also have excellent [documentation](https://starship.rs/config/#prompt)
which makes it a pleasure to configure.

Here is a link to my configuration:
[~/.config/starship/starship.toml](https://github.com/ryanleonbutler/dotfiles/blob/main/starship/starship.toml)

# Summary

With these latest additions to my tool belt I feel really good about my workflow and the tools I am using. Does not
hurt that it looks great as well 😄
