Title: How to manage Python projects 
Date: 2022-01-10 
Tags: Python, Tools
Category: Productivity 
Summary: Have you ever struggled to manage your Python
projects? Let's see how Poetry can help manage your Python projects.

<img src="{static}/images/joshua-j-cotten-uyKB8ZZApU0-unsplash.webp"
alt="screenshot" style="width:100%;" />

From installing different Python versions, creating virtual environments,
installing different libraries and dependencies and creating configuration
files for your project. I have been through this journey a few times, tried
multiple approaches and tools, none which really worked or which I liked. About
a year or so ago, I was listening to a podcast about Python where the hosts
were talking about a tool called [Poetry](https://python-poetry.org/). Some of
you might have heard about Poetry before or even use it already, regardless I
will share with you my experience using Poetry in managing Python projects and
how it has made my life so much simpler. I will also share other tools in this
post, which compliment Poetry. I will also share an example of my workflow when
starting a new Python project. Please follow me on
[Twitter](https://twitter.com/ryanleonbutler) and
[LinkedIn](https://www.linkedin.com/in/ryanleonbutler/) if you like the content
I am creating or just any Python related questions or questions regarding this
post. Thank you for the support!

# 1. What is Poetry?
Poetry's main goal is dependency management and packaging in Python. The tool
allows you to declare the libraries your project uses and will manage them for
you, either by installing or updating them. It also has a bunch of other
features, which include creating a 'pyproject.toml', creating virtual
environments and publishing a Python application or module to
[PyPI](https://pypi.org/).

# 2. Installation 
Just like any other Python package, Poetry can be installed using pip.

    :::bash
    // Install poetry 
    ❯ pip install poetry

I recommend using [pipx](https://github.com/pypa/pipx) in this case. It is
great for installing system wide Python applications in isolation. This avoids
installing Poetry to a specific Python installation or virtual environment. It
also adds the command line application to your system path allowing you to
execute the tool even if other Python virtual environments are active.

    :::bash
    // Install pipx and add it to the system path 
    ❯ brew install pipx 
    ❯ pipx ensure path

Just a tip on using pipx, if you wish to use a specific Python version in your
pipx environments, I recommend setting an environment variable in your shell
start-up script (e.g. in 'config.fish') to change the version to use
[asdf](https://asdf-vm.com/)'s path. This is important when using Poetry, since
Poetry will inherit the Python version from pipx in order to create its own
virtual environments.

    :::bash
    // ~/.config/fish/config.fish 
    ❯ set -g PIPX_DEFAULT_PYTHON ~/.asdf/shims/python

Now we can install Poetry using pipx.

    :::bash
    // using pipx to install poetry globally 
    ❯ pipx install poetry 

# 3. Basic Usage In order to create a new directory with predefined files and
project structure you can simply run:

    :::bash
    // creates new project 
    ❯ poetry new my_project

You will be presented with a few prompts regarding your project and once
completed a new directory will be created with the below contents:

    :::bash
    // example project structure 
    my_project 
    ├── pyproject.toml 
    ├── README.rst
    ├── my_project 
    │   └── __init__.py 
    └── tests 
        ├── __init__.py 
        └─ test_my_project.py 

If you have an existing Python project and directory structure you can navigate
to the project directory and then run:

    :::bash
    // creates poetry project in existing project 
    ❯ poetry init 

Enter the details in the prompts and at the end you will notice a new file
called 'pyproject.toml' is created in the root of your new project, if there if
not one present already.

To manage dependencies you can simply use the 'add', 'remove', 'install' and
'update' commands.

    :::bash
    // example poetry commands for managing depedencies 
    ❯ poetry add pprint  // Adds pprint to depedencies 
    ❯ poetry add -D black  // Adds black to your developer dependencies 
    ❯ poetry remove -D black  // Removes black 
    ❯ poetry update  // Updates all depedencies 
    ❯ poetry install // Installs all depedencies in the virtual environment

Poetry also has some bonus features like exporting your dependencies to a
requirements file.

    :::bash
    // Exports all depedencies to requirements file 
    ❯ poetry export --without-hashes -o requirements.txt 

## 4. My Workflow 
Moving to my workflow when starting a new project, I use a combination of
Poetry and asdf to setup my project. Typically I have a 'workspace' or
'development' folder in my home directory on my local machine. Within this
directory I save store all my projects.

    :::bash
    // contents of development folder 
    ❯ cd ~/development

    ❯ ls -l 
    drwxr-xr-x  20 user  staff   640B Oct 18 21:30 dotfiles/ 
    drwxr-xr-x   4 user  staff   128B Aug 25 20:01 scratches/ 
    drwxr-xr-x   5 user  staff   160B Jul 23 10:36 scripts/ 
    drwxr-xr-x  14 user  staff   448B Sep 20 13:52 tests/

First let's check which Python versions we have installed using asdf.

    :::bash
    // check available versions 
    ❯ asdf list python
      3.11.0
     *3.11.1

As you can see from the above I have two Python versions installed, "system"
which will be the version which is managed by my OS and the OS package manager,
for example HomeBrew on MacOS and one that I previously installed with pyenv,
namely 3.9.7. In this project I want to use 3.9.7 and in order to ensure I am 
using this Python version, I can set it as the global default on my system  as 
well as check the version and location of the binary.

    :::bash
    // set python version 
    ❯ pyenv global 3.9.7

    ❯ python -V 
    Python 3.9.7

    ❯ which python 
    /Users/user/.pyenv/shims/python-poetry

Now that we have confirmed Python 3.9.7 is set as the default Python binary we
can create our project using Poetry.

    :::bash
    # creates new project 
    ❯ poetry new my_project

We now have our basic skeleton, let's change a few things.

    :::bash
    // additional project setup 
    ❯ cd my_project && git init 
    ❯ rm README.rst && touch README.md  // I prefer markdown 
    ❯ echo '# my_project' >> README.md 
    ❯ touch my_project/main.py 
    ❯ echo 'import pprint as print\nprint("Poetry is great!")' >> my_project/main.py 

See basic a example of a 'pyproject.toml' file for a Python project on my GitHub
profile in the 'python_project' repository
[here](https://github.com/ryanleonbutler/python_project/blob/main/pyproject.toml).

You will notice there are a lot of other developer tools listed in the
dev-dependencies section of the above 'pyproject.toml' example. These are just
some additional tools which I added over time into my workflow. I will cover
them in a future post, but for your ease of reference see the links to the
respective home pages for more information:

- [Tox](https://tox.wiki/en/latest/)
- [Pre-commit](https://pre-commit.com/)
- [Black](https://github.com/psf/black)
- [flake8](https://flake8.pycqa.org/en/latest/)
- [isort](https://github.com/PyCQA/isort)
- [pytest](https://docs.pytest.org/en/6.2.x/)
- [coverage](https://coverage.readthedocs.io/en/6.0.2/)
- [Sphinx](https://www.sphinx-doc.org/en/master/)

We are now ready to run the Python project. There are two ways you can achieve
this.

    :::bash
    // 1. using the Poetry 'run' command will run the Python version which
    Poetry is managing for you 
    ❯ poetry run python my_project/main.py 

    Poetry is great!

    // 2. drop into a new shell with the Poetry Python version as the activated
    virtual environment 
    ❯ poetry shell (.venv) ❯ python my_project/main.py

    Poetry is great!

Note, regarding option 2. above, if you prefer that Poetry creates a virtual
environment in the root if your project, you can set the following
configuration.

    :::bash
    // example venv path configuration 
    ❯ poetry config --list

    ... virtualenvs.in-project = false ...

    ❯ poetry config virtualenvs.in-project true
    ❯ poetry config --list

    ... virtualenvs.in-project = true ... 

It is as simple as that to get started with Poetry. I like how it has abstracted
the repetitive tasks and additional overhead added to the developer in managing
depedencies and virtual environments.
