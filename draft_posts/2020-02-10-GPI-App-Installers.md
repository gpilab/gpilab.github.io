Title: Two Ways to Install GPI
Date: 2020-02-10
Author: Daniel Borup <borup.daniel@mayo.edu>

### Interested in trying GPI? It's easier than ever to get started!

We've been making some major behind-the-scenes upgrades to GPI in recent months! We've added the ability to run GPI natively on Windows, squashed a few bugs, and even restored GPI's ability to keep itself up to date. All of this means a smoother experience for new and existing users alike.

GPI can be used by anyone from a new Python coder to an experienced MRI reconstruction developer —- and we want everyone to be able to install and run GPI without hassle. To facilitate this, we'll be supporting two methods of GPI installation going forward:

### Installing GPI

#### 1. (Recommended) Install using Anaconda
Anaconda is widely used in the open-source scientific computing community. As a package manager, it allows you to maintain many separate "environments", each containing different packages (including different versions of Python, R, etc.).

1. Install Anaconda. If you already have it (or another distribution, like Miniconda), you can skip ahead to step 2. If not, download the latest Anaconda [here](https://www.anaconda.com/distribution/#download-section) (choose the "Python 3.7" version). New users can find documentation and instructions for using Anaconda at [this link](https://docs.anaconda.com/anaconda/). 
 
2. Create a new environment with Python 3.6, 3.7 (recommended), or 3.8. You can use any name — we'll assume you chose `gpi` for the rest of these instructions. This can be done in the Anaconda navigator GUI or from a terminal with:
    ```
    conda create -n gpi python=3.7
    ```
3. Configure the new environment for GPI installation. To do this, create a file called `<path-to-your-Anaconda>/envs/gpi/.condarc` containing the following four lines:
    ```
    channels:
      - conda-forge
      - defaults
    channel-priority: strict
    ```
4. Install `pyqt` 5.6, 5.9 (recommended), or 5.12 (required for Python 3.8) and `gpi_core`, which will also install GPI. This can be done in the Anaconda navigator GUI or from a terminal with:
    ```
    conda install -n gpi pyqt=5.9 gpi_core
    ```
    
5. You should now be able to activate the new environment and launch GPI, either using Anaconda navigator or with the commands:    
```
conda activate gpi
gpi
```

#### 2. Install as a standalone program
For those less experienced with programming, GPI can also be installed as a more traditional application. Using this method is simple: just download the appropriate installation script for your operating system from the [Downloads page](http://gpilab.com/downloads/), then run the script by double-clicking (Mac/Windows) or calling it from the a terminal window (Linux).

This installation will provide a desktop shortcut to GPI for Windows and Linux users, and a shortcut in the Applications folder for Mac users. We are still working to ensure that all of GPI's features work from within the application itself (i.e., without requiring a command line), but there are likely still a few bugs and missing features present — please feel free to submit anything you find on our [GitHub page](https://www.github.com/gpilab/framework/issues)!

**Note to users with an existing Anaconda installation**: this script will create a separate installation of Miniconda on your machine. No modifications will be made to your system's `PATH` variable or shell configuration, meaning that your existing Anaconda, system Python, etc. should remain unaffected. However, we still recommend method 1 above for these users as we can't guarantee perfect compatibility in all cases. Please feel free to examine the installation script and post at https://www.github.com/gpilab/conda-distro/issues with any feedback!

### Updating GPI
Once you've installed GPI and the core nodes, you'll want to keep them up to date as updates are released frequently.

Anaconda users (install method 1 above) should search for and install updates to GPI and the core nodes (`gpi_core`) like any other package.

App-style users (install method 2) can install updates using the built-in GPI updater, found under:
- `GPI > Search For Updates` (Mac)
- `Help > Search For Updates` (Windows/Linux)

### Contributing to GPI
We value community contributions highly and hope you'll consider helping us make GPI even better! All of our development work is carried out at www.github.com/gpilab -- please drop by, feel free to start a fork of any repository, and communicate with us via Issues with any bugs, feature requests, or general thoughts on GPI!