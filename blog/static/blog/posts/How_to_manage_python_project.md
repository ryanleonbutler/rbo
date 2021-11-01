<div id='header-img'
<img src="/static/markdownx/2021/02/20/coding-monitor-laptop.jpg_9d384059-5af7-4a4a-b7e3-3c80c5f67fc2.jpg" alt="" />
</div>

Have you ever struggled to manage your Python projects? From installing different Python versions, creating virtual environments, installing different libraries and dependencies and creating configuration files for your project. I have been through this journey a few times, tried multiple approaches and tools, none which really worked or which I liked. About a year or so ago, I was listening to a podcast about Python where the hosts were talking about a tool called [Poetry](https://python-poetry.org/). Some of you might have heard about Poetry before or even use it already, regardless I will share with you my experience using Poetry in managing Python projects and how it has made my life so much simpler. I will also share other tools in this post, which compliment Poetry. I will also share an example of my workflow when starting a new Python project. Please follow me on [Twitter](https://twitter.com/ryanleonbutler) and [LinkedIn](https://www.linkedin.com/in/ryanleonbutler/) if you like the content I am creating or just any Python related questions or questions regarding this post. Thank you for the support!

# Contents
1. [What is Poetry?](#intro)
2. [Installation](#instal)
3. [Basic Usage](#use)
4. [My workflow](#workflow)

<div id='intro' markdown='1'></div>

## 1. What is Poetry?
Poetry's main goal is dependency management and packaging in Python. The tool allows you to declare the libraries your project uses and will manage them for you, either by installing or updating them. It also has a bunch of other features, which include creating a "pyproject.toml", creating virtual environments and publishing a Python application or module to [PyPI](https://pypi.org/). 

<div id='install' markdown='1'></div>

## 2. Installation?
Just like any other Python package, Poetry can be installed using pip.
```bash
$  pip install poetry
```
I recommend using [pipx](https://github.com/pypa/pipx) in this case. It is great for installing system wide Python applications in isolation. This avoids installing Poetry to a specific Python installation or virtual environment. It also adds the command line application to your system path allowing you to execute the tool even if other Python virtual environments are active. 


```bash
# Install pipx and add it to the system path
$ brew install pipx
$ pipx ensure path
```

Just a tip on using pipx, if you wan to use a specific Python version in your pipx environments, I recommend setting an environment variable in your shell start-up script (e.g. in "~/.zshrc") to change the version to use pyenv's path. This important when using Poetry, since Poetry will inherit the Python version from pipx to create its virtual own environments.
```bash
# ~/.zshrc
export PIPX_DEFAULT_PYTHON=/Users/$USER/.pyenv/shims/python
```

Now we can install Poetry using pipx.
``````bash
$ pipx install poetry
```

<div id='use' markdown='1'></div>

## 3. Basic Usage?
In order to create a new directory with predefined files and project structure you can simply run:
```bash
$ poetry new my_project
```
You will be presented with a few prompts regarding your project and once completed a new directory will be created with the below contents:
```bash
my_project
├── pyproject.toml
├── README.rst
├── my_project
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_my_project.py
```

If you have an existing Python project and directory structure you can navigate to the project directory and then run:
```
$ poetry init
```
Enter the details in the prompts and at the end you will notice a new file called "pyproject.toml" is created in the root of your new project, if there if not one present already.

To manage dependencies you can simply use the 'add', 'remove', 'install' and 'update' commands.
```
$ poetry add pprint  # Adds pprint to you depedencies
$ poetry add -D black  # Adds black to your developer dependencies
$ poetry remove -D black  # Removes black
$ poetry update  # Updates all depedencies
$ poetry install # Installs all depedencies in the virtual environment
```

Poetry also has some bonus features like exporting your dependencies to a requirements file.
```
poetry export >> requirements.txt  # Exports all depedencies to requirements file
```

There are many more commands, which is very well documented on their beautifully crafted website [here]().

<div id='workflow' markdown='1'></div>

## 4. My Workflow
Moving to my workflow when starting a new project, I use a combination of Poetry and [pyenv](https://github.com/pyenv/pyenv) to setup my project. Typically I have a "workspace" or "development" folder in my home directory on my local machine. Within this directory I have all my projects.
```bash
$ cd ~/development

$ ls -l
drwxr-xr-x  20 butryan  staff   640B Oct 18 21:30 dotfiles/
drwxr-xr-x   4 butryan  staff   128B Aug 25 20:01 scratches/
drwxr-xr-x   5 butryan  staff   160B Jul 23 10:36 scripts/
drwxr-xr-x  14 butryan  staff   448B Sep 20 13:52 tests/
```

First let's check which Python versions we have installed using pyenv.
```bash
$ pyenv versions
  system
* 3.9.7 (set by /Users/butryan/.pyenv/version)
```

As you can see from the above I have two Python versions installed, "system" which will be the version which is managed by my OS and the OS package manager, for example HomeBrew on MacOS and one that I previously installed with pyenv, namely 3.9.7. In the case I want to use 3.9.7 and in order to ensure I am using this Python version, I can set it as the global default on my system as well as check the version and location of the binary.
```bash
$ pyenv global 3.9.7

$ python -V                            
Python 3.9.7

$ which python
/Users/butryan/.pyenv/shims/python
```

Now that we can see my I am using Python 3.9.7 as my default Python runtime we can create our project using Poetry.
```bash
$ poetry new my_project  
```

Now we have our basic skeleton, let's change a few things.
```bash
$ cd my_project && git init  # change directory into your new project and initialse it as a git repository to start source control
$ rm README.rst && touch README.md  # I prefer markdown to restructered text for the README file
$ echo '# my_project' >> README.md  # add heading to new README
$ touch my_project/main.py  # create some source files and modules for your project
$ echo 'import pprint as print\nprint("Poetry is great!")' >> my_project/main.py  # adding some code to my sample source file
```

See basic example of a "pyproject.toml" file for a Python project on my GitHub profile in the "python_project"" repository [here](https://github.com/ryanleonbutler/python_project/blob/main/pyproject.toml).

You will notice there are a lot of other developer tools listed in the dev-dependencies section of the above "pyproject.toml" example, these are just some additional tools, which I added over time into my workflow. I might cover them in a future post, but for your ease of reference see the links to the respective home pages for more information:

- [Tox](https://tox.wiki/en/latest/)
- [Pre-commit](https://pre-commit.com/)
- [Black](https://github.com/psf/black)
- [Flake8](https://flake8.pycqa.org/en/latest/)
- [iSort](https://github.com/PyCQA/isort)
- [pytest](https://docs.pytest.org/en/6.2.x/)
- [coverage](https://coverage.readthedocs.io/en/6.0.2/)
- [Sphinx](https://www.sphinx-doc.org/en/master/)

Now, if I want to run my Python project there are two ways you can achieve this.
```bash
# 1. Using the Poetry 'run' command to run the Python version which Poetry is managing for you
$ poetry run python my_project/main.py

Poetry is great!

# 2. Drop into a new shell with the Poetry Python version as the activated virtual environment
$ poetry shell
(.venv) $ python my_project/main.py

Poetry is great!
```

## Last words

Easy as that, I really like how Poetry has abstracted a lot of the repetative tasks. I trust the above information has provided you with some new insights into managing your Python projects using Poetry and other tools. Please follow me on [Twitter](https://twitter.com/ryanleonbutler) and [LinkedIn](https://www.linkedin.com/in/ryanleonbutler/) if you like the content I am creating and keep an eye out for my future posts. 

*Take care fellow Pythonistas,*
*Ryan*
