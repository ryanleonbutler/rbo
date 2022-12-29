![](/static/markdownx/paco-joss-4GL53Okjaic-unsplash.jpg)

## Moving to Fish Shell
Fish (short for Friendly Interactive Shell) is a Unix shell that aims to be more interactive and user-friendly than other shells such as the Bourne Shell (sh) or the Bourne Again Shell (bash).

# Contents
1. [Features](#feature)
2. [Installation](#install)
3. [Basic Usage](#use)
4. [My workflow](#workflow)

<div id='feature' markdown='1'></div>

## 1. Features
Some of the features that make Fish more user-friendly include:

- Syntax highlighting: Fish automatically highlights different parts of the command line to make it easier to read and understand.
- Autosuggestions: As you type a command, Fish will suggest possible completions based on your history and the contents of your directories.
- Web-based configuration: Fish provides a web-based interface for configuring and customizing the shell, which can be accessed by running the fish_config command.
- Consistency: Fish has a consistent syntax and naming conventions for its commands, which can make it easier to learn and use.
- Fish also includes a number of other features that can be useful for users, such as tab completion, history search, and support for plugins and themes. It is available for most Unix-like operating systems, including Linux, macOS, and BSD.

<div id='install' markdown='1'></div>

## 2. Installation
To install on macOS or Linux using Homebrew(Linuxbrew):

<pre><code class="language-bash">
$  brew install fish
</code></pre>

<pre><code class="language-bash">
$ fish
Welcome to fish, the friendly interactive shell
Type help for instructions on how to use fish
you@hostname ~>
</code></pre>

Just a tip on using pipx, if you wish to use a specific Python version in your pipx environments, I recommend setting an environment variable in your shell start-up script (e.g. in '~/.zshrc') to change the version to use pyenv's path. This is important when using Poetry, since Poetry will inherit the Python version from pipx in order to create its own virtual environments.

<pre><code class="language-bash">
# ~/.zshrc
export PIPX_DEFAULT_PYTHON=/Users/user/.pyenv/shims/python
</code></pre>

Now we can install Poetry using pipx.

<pre><code class="language-bash">
# using pipx to install poetry globally
$ pipx install poetry
</code></pre>

<div id='use' markdown='1'></div>

## 3. Basic Usage
In order to create a new directory with predefined files and project structure you can simply run:

<pre><code class="language-bash">
# creates new project
$ poetry new my_project
</code></pre>

You will be presented with a few prompts regarding your project and once completed a new directory will be created with the below contents:

<pre><code class="language-bash">
# example project structure
my_project
├── pyproject.toml
├── README.rst
├── my_project
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_my_project.py
</code></pre>

If you have an existing Python project and directory structure you can navigate to the project directory and then run:

<pre><code class="language-bash">
# creates poetry project in existing project
$ poetry init
</code></pre>

Enter the details in the prompts and at the end you will notice a new file called 'pyproject.toml' is created in the root of your new project, if there if not one present already.

To manage dependencies you can simply use the 'add', 'remove', 'install' and 'update' commands.

<pre><code class="language-bash">
# example poetry commands for managing depedencies
$ poetry add pprint  # Adds pprint to depedencies
$ poetry add -D black  # Adds black to your developer dependencies
$ poetry remove -D black  # Removes black
$ poetry update  # Updates all depedencies
$ poetry install # Installs all depedencies in the virtual environment
</code></pre>

Poetry also has some bonus features like exporting your dependencies to a requirements file.

<pre><code class="language-bash">
# Exports all depedencies to requirements file
poetry export --without-hashes -o requirements.txt
</code></pre>

There are many more commands, which is very well documented on their beautifully crafted website [here]().

<div id='workflow' markdown='1'></div>

## 4. My Workflow
Moving to my workflow when starting a new project, I use a combination of Poetry and [pyenv](https://github.com/pyenv/pyenv) to setup my project. Typically I have a 'workspace' or 'development' folder in my home directory on my local machine. Within this directory I save store all my projects.

<pre><code class="language-bash">
# contents of development folder
$ cd ~/development

$ ls -l
drwxr-xr-x  20 user  staff   640B Oct 18 21:30 dotfiles/
drwxr-xr-x   4 user  staff   128B Aug 25 20:01 scratches/
drwxr-xr-x   5 user  staff   160B Jul 23 10:36 scripts/
drwxr-xr-x  14 user  staff   448B Sep 20 13:52 tests/
</code></pre>

First let's check which Python versions we have installed using pyenv.

<pre><code class="language-bash">
# check available versions
$ pyenv versions
  system
* 3.9.7 (set by /Users/user/.pyenv/version)
</code></pre>

As you can see from the above I have two Python versions installed, "system" which will be the version which is managed by my OS and the OS package manager, for example HomeBrew on MacOS and one that I previously installed with pyenv, namely 3.9.7. In this project I want to use 3.9.7 and in order to ensure I am using this Python version, I can set it as the global default on my system as well as check the version and location of the binary.

<pre><code class="language-bash">
# set python version
$ pyenv global 3.9.7

$ python -V
Python 3.9.7

$ which python
/Users/user/.pyenv/shims/python
</code></pre>

Now that we have confirmed Python 3.9.7 is set as the default Python binary we can create our project using Poetry.

<pre><code class="language-bash">
# creates new project
$ poetry new my_project
</code></pre>

We now have our basic skeleton, let's change a few things.

<pre><code class="language-bash">
# additional project setup
$ cd my_project && git init
$ rm README.rst && touch README.md  # I prefer markdown
$ echo '# my_project' >> README.md
$ touch my_project/main.py
$ echo 'import pprint as print\nprint("Poetry is great!")' >> my_project/main.py
</code></pre>

See basic a example of a 'pyproject.toml' file for a Python project on my GitHub profile in the 'python_project' repository [here](https://github.com/ryanleonbutler/python_project/blob/main/pyproject.toml).

You will notice there are a lot of other developer tools listed in the dev-dependencies section of the above 'pyproject.toml' example. These are just some additional tools which I added over time into my workflow. I will cover them in a future post, but for your ease of reference see the links to the respective home pages for more information:

- [Tox](https://tox.wiki/en/latest/)
- [Pre-commit](https://pre-commit.com/)
- [Black](https://github.com/psf/black)
- [flake8](https://flake8.pycqa.org/en/latest/)
- [isort](https://github.com/PyCQA/isort)
- [pytest](https://docs.pytest.org/en/6.2.x/)
- [coverage](https://coverage.readthedocs.io/en/6.0.2/)
- [Sphinx](https://www.sphinx-doc.org/en/master/)

We are now ready to run the Python project. There are two ways you can achieve this.

<pre><code class="language-bash">
# 1. using the Poetry 'run' command will run the Python version which Poetry is managing for you
$ poetry run python my_project/main.py
Poetry is great!

# 2. drop into a new shell with the Poetry Python version as the activated virtual environment
$ poetry shell
(.venv) $ python my_project/main.py

Poetry is great!
</code></pre>

Note, regarding option 2. above, if you prefer that Poetry creates a virtual environment in the root if your project, you can set the following configuration.

<pre><code class="language-bash">
# example venv path configuration
$ poetry config --list

...
virtualenvs.in-project = false
...

$ poetry config virtualenvs.in-project true
$ poetry config --list

...
virtualenvs.in-project = true
...
</code></pre>

It is as simple as that to get started with Poetry. I like how it has abstracted the repetitive tasks and additional overhead added to the developer in managing depedencies and virtual environments.
