Title: Install GPI
Date: 2016-04-03 19:25
Modified: 2020-02-10 09:30
Category: downloads
Tags: downloads
Slug: downloads
Authors: Nicholas Zwart, Daniel Borup
Header_Cover: /images/downloads_banner.jpg
Summary:

> This software is made available for download via this website
subject to the [license terms and conditions](/license), available also on
this website. You will be required to view and accept these [license terms and
conditions](/license) upon installation of the software. If you do not
accept or agree to these [license terms](/license), you are not permitted
to download, install or otherwise use the software in any way. By continuing
with this download, you are agreeing to the applicable [license terms and
conditions](/license).

## <a name="min-hardware"></a> Minimum Hardware

It is recommended to use at least a dual processor system with 4GB of system memory for GPI.

## <a name="installation"></a> Installation

### Read This First
GPI is built and distributed on [Conda-Forge](https://conda-forge.org/#about), a community for open-source software distributed using the package manager **conda**. Conda allows you to create and maintain many separate "environments", each containing different software (such as different versions of Python). You can also save snapshots of an environment to help others verify or reproduce your work using exactly the same software versions.

The most common conda distribution is Anaconda, which contains the package manager, a number of commonly used packages, and a graphical interface that may be easier for new GPI users. If you'd like to install GPI using Anaconda and the GUI (Anaconda Navigator), follow the guide for [installing with Anaconda Navigator](#install-navigator).

GPI can also be installed, configured, and launched directly from the command line. This install method will be more appropriate for advanced users or those who are already using conda from the command line. If you prefer this method, skip ahead to the instructions for [installing from the command line](#install-command).

### <a id="install-navigator"></a> Installing with Anaconda Navigator

1. If you already have Anaconda installed, go ahead to step 2. If not, download and run the latest Anaconda installer [here](https://www.anaconda.com/distribution/#download-section) (choose the "Python 3.7" version). *When prompted, make sure to respond "yes" to the question about initializing Anaconda3 with conda init.*
    <details>
    <summary><b>Advanced notes (click to expand)</b></summary>  
    The installer will typically modify `~/.bashrc` or `~/.bash_profile` (or `~/.zshrc`, on OSX 10.15) so that new terminal windows open with the `base` conda environment active. If you'd prefer terminal windows to open outside of any conda environment, run the command:
    
    ```
    conda config --set auto_activate_base false
    ```
    
    The installer may also ask if it should add conda to your `PATH`. We recommend responding "no" (the default) to avoid breaking programs that rely on the system Python. For more information on Anaconda installation options, see the [Anaconda FAQ](https://docs.anaconda.com/anaconda/user-guide/faq/).
    </details>

2. If Anaconda Navigator is not already open, launch it as follows:
    * **Mac** - Choose the icon in your Applications folder.
    * **Windows** - Search for "Anaconda Navigator" in the Start Menu.
    * **Linux** - Open a terminal window and enter the command `anaconda-navigator` (note that if you set `auto_activate_base` to `false` in step 1, you'll have to enter `conda activate base` first - and you may find it more straightforward to use the command line installation method below).

3. In Navigator, select `Environments` at left, then click `Create` at the bottom of the screen. Enter a name for this new environment (we'll call it `gpi_env` for the rest of these instructions). Make sure the box next to Python is checked, and select version 3.7. Click `Create`. The window should disappear, and after a few seconds you should see `gpi_env` show up in the environment list.

4. There should be a triangle to the right of `gpi_env` indicating that it is the active environment. If this isn't the case, first double-click on `gpi_env` to activate it. Then click the triangle and choose `Open Terminal` to bring up a command prompt.

5. A terminal window should open (on Linux, it may appear silently as a new tab in the terminal from step 2). Enter the following commands:

    ```
    conda config --env --add channels conda-forge
    ```
    
    ```
    conda config --env --set channel_priority strict
    ```

    This prepares your new environment to install the correct packages for GPI, without modifying any other environments.

6. Close the terminal window/tab launched in step 4. In the right side of the Anaconda Navigator, you should see the list of packages installed in `gpi_env`. Above that list, click `Update Index` to refresh the list of available packages.

7. Once this has finished running, change `Installed` to `Not Installed` in the drop-down menu, then type `gpi` into the search box at right. You should see a list of packages including `gpi` and `gpi_core`. You may also see other public GPI node libraries, which will have names starting with `gpi_`. Select `gpi` and `gpi_core` (and others, if you want to install them), then click `Apply`.

8. A pop-up window will open and display a list of packages that will be added to `gpi_env`. You can take a look through this list, if you're interested in what software GPI depends on behind the scenes. When you're ready, click `Apply` again. The installation may take several minutes.

9. **Run GPI:** Once installation is complete, you should see GPI listed under the `Home` tab, with a `Launch` button available. You can run GPI using this button (in our experience, the first launch may be a bit slow). Each time you close and re-open Anaconda Navigator, you'll need to select `gpi_env` from the drop-down menu or Environments tab for GPI to appear.
    <details>
    <summary><b>Advanced notes (click to expand)</b></summary>
    You may also wish to launch GPI by opening the `gpi_env` terminal (as in step 4) and entering the command `gpi`. This will allow you to see GPI warnings and error messages, which are currently not visible when launching from the `Home` tab (we're working on a fix!). Launching a `gpi_env` terminal also allows you to use the `gpi_make` command for building [C++ extensions with PyFI](http://docs.gpilab.com/en/develop/NodeDev/devguide.html#pyfi-extending-gpi-nodes-with-c).
    </details>


### <a id="install-command"></a> Installing from the command line

1. If you already have a conda distribution installed, skip ahead to step 2. If not, download and install Anaconda [here](https://www.anaconda.com/distribution/#download-section), or Miniconda (a lighter version about 90% smaller than Anaconda) [here](https://docs.conda.io/en/latest/miniconda.html). When prompted during installation, answer "yes" to the question about initializing conda using `conda init`. We recommend the default response of "no" when asked if you want to add conda to your system `PATH`, as this may break other things that depend on your system's installation of Python. For more information, please see the [Anaconda FAQ](https://docs.anaconda.com/anaconda/user-guide/faq/).
  
    **Note** If you do not want terminal windows to open with the "base" conda environment active by default, you can disable this behavior with the following:
    
    ```
    conda config --set auto_activate_base false
    ``` 

2. Launch a new terminal instance. Windows users with Anaconda can launch "Anaconda Prompt" from the Start Menu, or any other terminal (cmd.exe, PowerShell, or MinGW) for which conda has been configured. Next, choose a name for the environment that will hold GPI. We will use `gpi_env` for this tutorial. Finally, run the following commands to set up and configure the new environment:

    ```
    conda create -n gpi_env
    ```
    
    ```
    conda activate gpi_env
    ```
    
    ```
    conda config --env --add channels conda-forge
    ```
    
    ```
    conda config --env --set channel_priority strict
    ```

    <details>
    <summary><b>Advanced notes (click to expand)</b></summary>
    These commands assume you are starting from a clean installation of conda. If you have made config changes to conda prior to this installation, you may need to pay attention to those settings. The end goal is to have a new environment with at least two channels, **conda-forge** (first) and **defaults** (second), and with the **channel_priority** attribute set to "strict". You can omit the `--env` flag in the above commands if you want these configuration changes to apply to *all* of your conda environments. See [here](https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html) for a full description of conda configuration options.
    </details>
  
  
3. Install GPI and the core nodes. In the same terminal as above (making sure `gpi_env` is still the active environment), run the following command:
  
    ```
    conda install gpi_core python=3.7 pyqt=5.9
    ```
  
    Python 3.7 and Qt 5.9 currently provide the "smoothest" running GPI, but you can also install with Python 3.6 or 3.8, and Qt 5.6 or 5.12 (the latter is required for Python 3.8). If you omit the python and pyqt pinnings from the above command, conda will use the newest possible version from conda-forge for both packages.

4. **Running GPI** - GPI is now installed and ready to use. Run it with the command `gpi`. When starting from a new terminal, remember that you will first need to activate the environment `gpi_env` using `conda activate gpi_env`.

-----------
## Updating GPI
You can update GPI like any other conda package, either from within Anaconda Navigator or using the command line. In addition, GPI contains a built-in updater, which is found under:
- `GPI > Search For Updates` (Mac)
- `Help > Search For Updates` (Windows/Linux)

##### Additional Notes
If you are upgrading from a very early version of GPI, v0.5 or older, first move (or remove) the existing installation, which will most likely be located at `/opt/gpi`.

If you are a Mac user upgrading from the previous App-packaged version, simply delete the older GPI in your Applications folder prior to installing the new one. You may also need to modify the file `~/.bashrc` or `~/.bash_profile` to remove links to the App-style GPI package (which included a hidden installation of Miniconda).

-----------
## <a name="macports"></a> MacPorts Installation
Our thanks to [Eric Borisch](https://github.com/eborisch) for enabling GPI installation via MacPorts. To install via MacPorts, use the following commands:

```
$ sudo port install py-gpilab-framework
$ sudo port install py-gpilab-core
```

-----------

### Other Notes
* If you are having issues with node libraries not being visible, make sure to
check your `~/.gpirc` file for the correct library path. By default, the packaged `gpi_core` library and any library under `~/gpi` is searched.
