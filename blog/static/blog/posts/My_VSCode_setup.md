<img align="center" src="/static/markdownx/2021/01/12/myvscode.png_bd9705fa-2da5-41bd-ba17-15a4df26bf0f.png" alt="myvscode" width="1920"/>

In my [previous post](https://ryanbutler.online/my-terminal-setup-mac-os) we reviewed setting up your terminal on MacOS. Today we look at the most important tool in a developer's tool belt, the code editor/IDE.

Visual Studio Code (VSCode) is currently one of the most popular code editors. I myself use VSCode daily for multiple tasks, including taking notes, writing markdown for posts, writing other documentation and off course writing code.

Follow along below where I will guide you on how to install and customize your VSCode to replicate my setup. Thank you once again for your time and support and please reach out to me on the [contact page](https://ryanbutler.online/contact/) if you have any questions or just want to chat about anything related to Python.

# Table of Contents
1. [Install VSCode](#install_vscode)
2. [Customize VSCode](#custom_vscode)
3. [Install Extensions](#install_ext)


<div id='install_vscode' markdown='1'></div>

## 1. Install VSCode

Download and install VSCode from the official website [here](https://code.visualstudio.com/).


<div id='custom_vscode' markdown='1'></div>

## 2. Customize VSCode
Once you have installed VSCode we are going to change some of the settings. This can be done via the Graphical User Interface (GUI) or you can edit the settings JSON files. There are two types of settings files, one for the USER and one for the WORKSPACE. The USER settings are the default settings which will be used for new workspaces you create. You can customize each workspace, which will override the USER settings, should you have workspace specific requirements.


On MacOS, press F1 to open the Command Palette, type "Preferences: Open User Settings" and press enter in order to edit settings via the GUI.


-OR-


Press F1 to open the Command Palette, type "Preferences: Open Settings (JSON)" to edit the local settings file, which contains all the same settings, just represented in JSON.


**Steps for GUI:**

* Change Font and Font Size
    * First we going to change the font type and font size. We are going to set this to the same as our terminal setup in my [previous post](https://ryanbutler.online/my-terminal-setup-mac-os). Search for "Font" in the top search bar, then set the Editor: Font family to "[Fira Code](https://github.com/tonsky/FiraCode)". Also change the Editor: Font size to "15".

* Disable Minimap
    * Search for "Minimap" and disable the Minimap. I personally don't like the minimap as it uses valuable screen real estate. If you need a minimap to navigate long code bases in single files you need to consider breaking up the code into smaller pieces for improved readability and maintainability (where possible of course).

* Change Integrated Terminal 
    * Search for "Terminal" and change the to iTerm.app. We configured our default terminal as iTerm in the [previous post](https://ryanbutler.online/my-terminal-setup-mac-os).
    * Change the integrated terminal shell to "Zsh" ("/bin/zsh"), change the font family to "Fira Code" and the font size to "15".

* Change Auto Save 
    * Find "Auto Save" and change to "After delay". I find the default of 1000ms to be sufficient.

* Python Specific Settings 
    * Select a default Python interpreter
        * In the command palette, type "Python: Select Interpreter", press Enter. Choose the relevant interpreter or browse/enter path. *(Note: I use a combination of [pyenv](https://github.com/pyenv/pyenv) and [venv](https://docs.python.org/3/library/venv.html) to manage my Python versions and virtual environments. I use pyenv to install and manage different Python versions only and then venv to create and manage the virtual environments themselves. I will go into more detail about this in a future post)*

    * Change the linter to [flake8](https://github.com/pycqa/flake8)
        * In the command palette, type "Python: Select Linter", press Enter. Choose flake8. *(Note: flake8 needs to be [installed](https://pypi.org/project/flake8/) as a Python package and I recommend using [pipx](https://pypi.org/project/pipx/) to install as a global isolated package which can be used for multiple Python projects and you do not need to re-install across multiple Python environments)*

    * Change the formatter to [black](https://github.com/psf/black).
        * In the command palette, type "Preferences: Open User Settings", press Enter. Search for "python formatting". Now change Python > Formatting: Provider to "black" and update Python > Formatting: Black Path to the relevant path for your black installation. *(Note: black needs to be [installed](https://pypi.org/project/black/) as Python package and I recommend using [pipx](https://pypi.org/project/pipx/) to install as a global isolated package which can be used for multiple Python projects and you do not need to re-install across multiple Python environments.)*

Refer to the below steps for the editing the JSON file method. In the JSON file method I included additional settings which is not covered in the GUI method. These are file watchers, searches and explorers. These are just some common directories in my development workflow, which I do not want VSCode to crawl, index or include in the file explorer. Excluding these keeps your workspace neat and clean and can increase editor performance.

**Steps for JSON:**

* Copy the below and edit your local JSON accordingly:

```
{
    "editor.fontFamily": "Fira Code",
    "editor.fontSize": 15,
    "editor.minimap.renderCharacters": false,
    "editor.minimap.enabled": false
    "editor.renderWhitespace": "all",
    "editor.suggestSelection": "first",
    "terminal.external.osxExec": "iTerm.app",
    "terminal.integrated.shell.osx": "/bin/zsh",
    "terminal.integrated.fontFamily": "Fira Code"
    "terminal.integrated.fontSize": 15,
    "files.autoSave": "afterDelay",
    "python.formatting.provider": "black",
    "python.linting.flake8Path": "flake8",
    "files.watcherExclude": {
        "**/build": true,
        "**/.pytest_cache": true,
        "**/.vscode": true,
        "**/build-tools": true,
        "**/env": true,
        "**/logs": true,
        "**/venv": true,
        "**/__pycache__": true
    },
    "files.exclude": {
        "**/.pytest_cache": true,
        "**/.vscode": true,
        "**/build": true,
        "**/build-tools": true,
        "**/env": true,
        "**/logs": true,
        "**/venv": true,
        "**/__pycache__": true
    },
    "search.exclude": {
        "**/build": true,
        "**/.pytest_cache": true,
        "**/.vscode": true,
        "**/build-tools": true,
        "**/env": true,
        "**/logs": true,
        "**/venv": true,
        "**/__pycache__": true
    },
}
```

That's all that needs changing with regards to the VSCode specific settings. In the next section we will cover installing extensions.

<div id='install_ext' markdown='1'></div>

## 3. Install Extensions
This is arguably VSCode's best feature, the ability to install extensions and customize your code editing experience to suite your needs. There are thousands of extensions out there, therefore it can be hard to manage them and to ensure you not bloating your code editor with unnecessary or overlapping extensions. The below list is my current trusted and curated list of extensions I use daily.

### Python Extensions

* Python
    * Linting, Debugging (multi-threaded, remote), Intellisense, Jupyter Notebooks, code formatting, refactoring, unit tests, snippets, and more.
    * [Marketplace Link](https://marketplace.visualstudio.com/items?itemName=ms-python.python) 

* Pylance
    * A performant, feature-rich language server for Python in VS Code.
    * [Marketplace Link]( https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)

* Python Docstring Generator
    * Automatically generates detailed docstrings for python functions.
    * [Marketplace Link](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) 

* indent-rainbow
    * Makes indentation easier to read.
    * [Marketplace Link](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow) 

* Bracket Pair Colorizer 2
    * A customizable extension for colorizing matching brackets.
    * [Marketplace Link](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2)


### Productivity Extensions

* GitLens — Git supercharged
    * Supercharge the Git capabilities built into Visual Studio Code — Visualize code authorship at a glance via Git blame annotations and code lens, seamlessly navigate and explore Git repositories, gain valuable insights via powerful comparison commands, and so much more.
    * [Marketplace Link](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)

* Project Manager
    * Easily switch between projects.
    * [Marketplace Link](https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager)

* Bookmarks
    * Mark lines and jump to them.
    * [Marketplace Link](https://marketplace.visualstudio.com/items?itemName=alefragnani.Bookmarks)

* Live Server
    * Launch a development local Server with live reload feature for static & dynamic pages.
    * [Marketplace Link](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

* Path Intellisense
    * Visual Studio Code plugin that autocompletes filenames.
    * [Marketplace Link](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense)

* Remote - SSH
    * Open any folder on a remote machine using SSH and take advantage of VS Code's full feature set.
    * [Marketplace Link](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)

* Settings Sync
    * Synchronize Settings, Snippets, Themes, File Icons, Launch, Keybindings, Workspaces and Extensions Across Multiple Machines Using GitHub Gist.
    * [Marketplace Link](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync)

* Todo Tree
    * Show TODO, FIXME, etc. comment tags in a tree view.
    * [Marketplace Link](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree)

* WakaTime
    * Metrics, insights, and time tracking automatically generated from your programming activity.
    * [Marketplace Link](https://marketplace.visualstudio.com/items?itemName=WakaTime.vscode-wakatime)

### Theme and icons
* Dracula Official
    * Official Dracula Theme. A dark theme for many editors, shells, and more.
    * [Marketplace Link](https://marketplace.visualstudio.com/items?itemName=dracula-theme.theme-dracula)

* vscode-icons
    * Icons for Visual Studio Code.
    * [Marketplace Link](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons)

## Last words
There are still so many changes you can make and extensions you can install for your VSCode editor we just scratched the surface on this post. The above implementation is what I deemed as the essentials to improve your editing experience at the time of writing.

That is all for now and I trust you found the above information useful.

*Best Regards*

*Ryan*