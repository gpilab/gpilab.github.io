Title: GPI on Windows
Date: 2016-09-27 15:28:00
Author: Akshay Bakhru
Header_Cover: /images/win_banner.jpeg

This is a quick step by step guide for getting GPI installed for native use on
Windows!  This capability is made possible through the new "Windows
Subsystem for Linux".  The guide starts with the installation and verification
of Ubuntu Linux and then provides steps for installing GPI.  This is an
exciting step forward for GPI users and developers.

# Installing the Linux Bash Shell on Windows

## Ensure you are running the right Windows 10 version
1. You have to have the 64-bit build of Windows 10
2. You should have the Windows 10 anniversary update or higher. To check the
   version type “About your PC” in the start menu and press “Enter”. Version
   should be 1607 or higher (shown in the about window below)

![fitw75]({filename}/images/win_1_settings.jpg)

## Enable developer mode
1. Open the Settings app and head to Update & Security > For Developers
2. Enable Developer Mode

![fitw75]({filename}/images/win_2_devmode.jpg)

## Enable the “Windows Subsystem for Linux (Beta)”
1. Open the Control Panel, click “Programs,” and click “Turn Windows Features
   On or Off”
2. Enable the “Windows Subsystem for Linux (Beta)” option in the list here and
   click “OK.”
3. After you do, you’ll be prompted to reboot your computer. Click “Restart
   Now” to reboot your computer and Windows 10 will install the new feature.

![fitw75]({filename}/images/win_3_subsys.jpg)

## Install
1. After your computer restarts, click the Start button (or press the Windows
   key), type “bash”, and press “Enter.”
2. The first time you run the bash.exe file, you’ll be prompted to accept the
   terms of service.
3. The command will then download the “Bash on Ubuntu on Windows” application
   from the Windows Store.
4. You’ll be asked to create a user account and password for use in the Bash
   environment.

![fitw75]({filename}/images/win_5_useradd.jpg)

## Run the bash shell
1. Now you have a full command-line bash shell based on Ubuntu.
2. To open the Bash shell, just open your Start menu and search for “bash” or
   “Ubuntu.”

![fitw75]({filename}/images/win_6_bash.jpg)

## Some tips (Installing packages and accessing windows dirs.)
1. You can use Ubuntu’s apt-get command to install software from Ubuntu’s
   repositories.
2. Install an Application Package: sudo apt-get install packagename (Replace
   “packagename” with the package’s name.)
3. Windows drives will be available in the “mnt” folder

![fitw75]({filename}/images/win_7_mnt.jpg)

---------

# Enable GUI app support for Linux Shell
Microsoft still does not support graphical applications in Bash on Windows.
However, Microsoft built an entire “Windows Subsystem for Linux” that allows
Windows 10 to natively run Linux applications, even graphical ones. The only
missing piece is an X server that allows those graphical applications to appear
on your Windows desktop. This is basically the same technique people would use
to run graphical Linux desktop applications over a network. Please note: Not
all Linux GUI applications might work with this, but it works for most, and it
works great with GPI.

## Download and install “Xming X server” for windows
1. The installer is available here: https://sourceforge.net/projects/xming/
2. Download and install it on your Windows 10 PC
3. Just use the default settings and it’ll work fine
4. Launch Xming and it will appear in your system tray, running in the
   background and waiting for you to launch a graphical Linux program.

![fitw75]({filename}/images/win_8_xming.jpg)

## Try a graphical application
1. Install Firefox using below command

    ```
    sudo apt-get install firefox
    ```

2. After installation launch Firefox using the below commands

    `export DISPLAY=:0` <br>
    `firefox`

![fitw75]({filename}/images/win_9_firefox.jpg)

## Install Anaconda
1. In Firefox launched above, download the Linux installer from here

    [https://www.continuum.io/downloads#linux](https://www.continuum.io/downloads#linux)

2. Run below command
    
    ```
    bash ~/Downloads/Anaconda3-4.1.1-Linux-x86_64.sh
    ```

3. Select a location to install
4. Accept the option to add the Anaconda directory to your bash shell `PATH`
   environment variable

## Verify the Install
1. Navigate to the Anaconda folder
2. Check that python 3.x is installed in the packages
3. Check if conda is also available

![fitw75]({filename}/images/win_10_conda.jpg)

## Install GPI via Conda
1. Run the below command

    ```
    conda install -c https://conda.anaconda.org/GPI gpi
    ```

2. If you get the below errors, follow the sub steps

    ![fitw75]({filename}/images/win_11_error.jpg)

    * This error is also shown if higher versions of numpy and python are
      installed
    * Remove the bottleneck package using below command conda remove bottleneck
    * Repeat step a to install GPI

3. Also install any other packages like core nodes

    ```
    conda install -c https://conda.anaconda.org/GPI gpi-core-nodes
    ```

4. Check GPI config as shown here:
   [http://docs.gpilab.com/en/develop/config.html](http://docs.gpilab.com/en/develop/config.html)

![fitw75]({filename}/images/win_12_gpiconf.jpg)

## Launch the GPI GUI

`export DISPLAY=:0 gpi`

![fitw75]({filename}/images/win_13_gpi.jpg)
![fitw75]({filename}/images/win_14_gpi.jpg)


