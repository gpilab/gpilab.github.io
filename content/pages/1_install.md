Title: Install GPI
Date: 2016-04-03 19:25
Modified: 2022-02-10 09:30
Category: downloads
Tags: downloads
Slug: downloads
Authors: Nicholas Zwart, Daniel Borup, Abdulrahman Alfayad
Header_Cover: /images/downloads_banner.jpg
Summary:

> This software is made available for download via this website
> subject to the [license terms and conditions](/license), available also on
> this website. You will be required to view and accept these [license terms and
> conditions](/license) upon installation of the software. If you do not
> accept or agree to these [license terms](/license), you are not permitted
> to download, install or otherwise use the software in any way. By continuing
> with this download, you are agreeing to the applicable [license terms and
> conditions](/license).

## <a name="min-hardware"></a> Minimum Hardware

It is recommended to use at least a dual processor system with 4GB of system memory for GPI.

## <a name="installation"></a> Installation

GPI is built and distributed on [PyPI](https://pypi.org), the official third-party software repository for Python packages distributed using the package manager **pip**. GPI also uses conda to create it's development enviromet. Conda allows you to create and maintain many separate "environments", each containing different software (such as different versions of Python). You can also save snapshots of an environment to help others verify or reproduce your work using exactly the same software versions.

### <a id="install-command"></a> Installing from the command line

1. If you already have a conda distribution installed, skip ahead to step 2. If not, download and install Anaconda [here](https://www.anaconda.com/distribution/#download-section), or Miniconda (a lighter version about 90% smaller than Anaconda) [here](https://docs.conda.io/en/latest/miniconda.html).
  
    **Note** If you do not want terminal windows to open with the "base" conda environment active by default, you can disable this behavior with the following:
    
    ```
    conda config --set auto_activate_base false
    ``` 

2. Launch a new terminal instance. Windows users with Anaconda can launch "Anaconda Prompt" from the Start Menu, or any other terminal (cmd.exe, PowerShell, or MinGW) for which conda has been configured. Next, choose a name for the environment that will hold GPI. We will use `gpi_env` for this tutorial. Finally, run the following commands to set up and configure the new environment:

    ```
    conda create -n gpi_env fftw eigen
    ```
    
    ```
    conda activate gpi_env
    ```
    
  
  
3. Install GPI and the core nodes. In the same terminal as above (making sure `gpi_env` is still the active environment), run the following command:
  
    ```
    pip install gpilab
    ```
  
    Python 3.9 currently provides the "smoothest" running GPI, but you can also install with Python 3.7 or 3.8.

4. **Running GPI** - GPI is now installed and ready to use. Run it with the command `gpi`. When starting from a new terminal, remember that you will first need to activate the environment `gpi_env` using `conda activate gpi_env`.

-----------

## Updating GPI

You can update GPI like any other pip package, using the command line.

   ```
   pip install gpilab --upgrade
   ```

-----------

### Other Notes

* If you are having issues with node libraries not being visible, make sure to
  check your `~/.gpirc` file for the correct library path. By default, the packaged `gpi_core` library and any library under `~/gpi` is searched.
