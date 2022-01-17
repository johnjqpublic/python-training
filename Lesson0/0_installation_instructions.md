# How to Install Python

Author: John Q
Date: 22 December 2022

<br>

**NOTE:** This is a markdown file

----
<br>

## Step 1

* Go to https://www.python.org/
* Click "Downloads"
* Download a version of Python for your operating system
    - I recommend learning Python 3 instead of Python 2
    - Personally, I tend to be one minor release behind the latest minor version
    - We have Python 3.5 at work so anything newer is an upgrade
* Run the Python installer
* Reboot if necessary

----
<br>

## Step 2

### Windows
* Run `cmd.exe`
* Type "`python`" (w/out quotes)
This opens an interactive session of the Python interpreter
    - You can type Python commands in this session
    - For example, try typing "`pi=3.14159; print(pi)`" (w/out quotes) and then press **Enter**
    - You can also type "`help()`" (w/out quotes) to enter the Python help utility  
    The very fist line printed by the interpreter shows the version
    - This should match the version you just installed
* Type "`exit()`" (w/out quotes) to exit the interpreter
* Close the command window

### macOS (formerly OS X)
* Launch the terminal
* Type "`python3`" (w/out quotes)
    - Apple includes an installation of Python 2 by default, DO NOT try to uninstall it!
    - You can run multiple versions of Python side-by-side as long as you're clear about which version of Python you're telling the system to use (hence why we use the "`python3`" command)
* This opens an interactive session of the Python interpreter
    - You can type Python commands in this session
    - For example, try typing "`pi=3.14159; print(pi)`" (w/out quotes) and then press **return**
    - You can also type "`help()`" (w/out quotes) to enter the Python help utility  
    The very fist line printed by the interpreter shows the version
    - This should match the version you just installed
* Type "`exit()`" (w/out quotes) to exit the interpreter
* Close the terminal

----
<br>

## Step 3 (optional)

> Installing SciPi provides access to useful packages such as **pandas** and **Matplotlib**

* Go to https://www.scipy.org/
* Click "Install"
* Use the pip installation instructions to install SciPy
    - Note for macOS users: Be sure to use "python3" instead of "python" in the command so that SciPy is installed for the desired version of Python
* Reboot if necessary

----
<br>

## Step 4
Run the sample code by following the instructions below

### Windows
* Run cmd.exe
* Navigate to the directory of this lesson
* Type "`python sample.py`" (w/out quotes) and then press **Enter**
* The program *should* run...
* Close the command window

### macOS (formerly OS X)
* Launch the terminal
* Navigate to the directory of this lesson
* Type "`python3 sample.py`" (w/out quotes) and then press **return**
* The program *should* run...
* Close the terminal

----
<br>

## Final Notes

* Installing Python will install IDLE as the default Interactive Development Environment (IDE) for Python
    - IDLE is functional, but ugly
* [PyCharm](https://www.jetbrains.com/pycharm/) is a popular (and free) IDE for Python
    - PyCharm is a bit complicated for my taste
* For a bare bones approach, you can use a text editor and the command line for Python development
    - [Notepad++](https://notepad-plus-plus.org/) is a free and more powerful alternative to Notepad for Windows
    - [TextMate](https://macromates.com/) is a free and more powerful alternative to TextEdit for macOS
* My personal favorite editor is [VS Code](https://code.visualstudio.com/)  
(free, open source, and multi-platform)

I recommend trying a few out and picking what you like best.
