Title: Downloads
Date: 2016-04-03 19:25
Modified: 2016-04-03 19:25
Category: downloads
Tags: downloads
Slug: downloads
Authors: Nicholas Zwart
Header_Cover: /images/downloads_banner.jpg
Summary:

> Dignity Health makes this software available for download via this website
subject to the [license terms and conditions](/license), available also on
this website. You will be required to view and accept these [license terms and
conditions](/license) upon installation of the software. If you do not
accept or agree to these [license terms](/license), you are not permitted
to download, install or otherwise use the software in any way. By continuing
with this download, you are agreeing to the applicable [license terms and
conditions](/license).

## GPI v1.0
The latest release can be downloaded below.  This is the current development
release used by the MR Technology Design Group.

<div class="container">
<div class="row">

<div class="col-md-3 col-sm-3">
<a href="https://github.com/gpilab/framework/releases/download/v1.0.0-rc1/GPI_1.0.0-rc.dmg">
<div class="text-center">
<img src="/images/osx_dl.jpg" width="100%" />
<h3>Mac OS 10.7+</h3>
</a>
GPI_1.0.0-rc.dmg <br> 364MB <br>
<i>Provides an OSX app that can be launched from your dock.</i>
</div>
</div>

<div class="col-md-3 col-sm-3">
<a href="https://raw.githubusercontent.com/gpilab/conda-distro/master/GPI_Install_Latest.sh">
<div class="text-center">
<img src="/images/script_dl.jpg" width="100%" />
<h3>Ubuntu 12.04+ <br> & <br> Mac OS  10.9+</h3>
</a>
GPI_Install_Latest.sh <br> 4.5KB <br>
<i>Install GPI (to be launched from a command line) using conda. This script should also work in Ubuntu (WSL) on Windows 10 (unsupported).</i>
</div>

</div>

<div class="col-md-3 col-sm-3">
<a href="https://github.com/gpilab/framework/releases/download/v1.0.2/GPI_Stack_1.0.2.vmwarevm.zip">
<div class="text-center">
<img src="/images/vm_dl.jpg" width="100%" />
<h3>VMware VM <br> (Ubuntu 15.10) </h3>
</a>
GPI_VM_1.0.2.zip <br> 1.2GB <br>
<i>A complete Linux virtual machine containing GPI.</i>
</div>
</div>

<br>

</div> <!-- row -->

<a href="https://github.com/gpilab/framework/releases">Release Archive</a>

</div> <!-- container -->

## <a name="Installation"></a> Installation

The following sections cover the installation for OSX and Linux.  If you are
upgrading to a newer version of GPI from GPI v0.5 or older, move (or remove)
the existing installation by executing the following command in a terminal
window as root.

```
$ sudo mv /opt/gpi /opt/gpi.old
```

-----------

## <a name="MinHardware"></a> Minimum Hardware

For native installs it is recommended to use at least a dual processor system
with 4GB of system memory. The virtual machine uses VMware hardware <a
title="Virtual Hardware Compatibility "
href="http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=1003746"
target="_blank">version 8</a>.

-----------
## <a name="MacPorts"></a> MacPorts Installation
Our thanks to [Eric Borisch](https://github.com/eborisch) for enabling GPI installation via MacPorts. To install via MacPorts. Use the following commands to install the latest GPI framework and core nodes.

```
$ sudo port install py-gpilab-framework
$ sudo port install py-gpilab-core
```

-----------
## OSX App
To install the OSX app, download and open the `.dmg` file, then drag the
`GPI.app` to the `/Applications` folder (which is linked in the `.dmg` image).
In order to add the `gpi_make` command and the anaconda python suite to your
environment, add the following to your `~/.bashrc`.

```
PATH="/Applications/GPI.app/Contents/Resources/miniconda/bin:$PATH"
```

-----------

### Installation Notes
* If you are having issues with node libraries not being visible, make sure to
check your `~/.gpirc` file for the correct library paths.
* By default, the packaged `core` library and any library under `~/gpi` is
searched.
* The OSX gatekeeper in 10.11 *El Capitan* appears to take more time to
validate packages.  This may require you to wait a few minutes before allowing
the package to be opened in the *Security & Privacy* preferances pane.

-----------

#### OSX Gatekeeper

After downloading and opening the GPI `.dmg` bundle, depending on the security
settings, the Gatekeeper may require an extra acknowledgement before allowing
installation. This can be granted in the

`System Preferences → Security & Privacy → Allow apps...`

preferences menu. Then continue on to the guided installation.

To compile C++ extension modules, install <a
href="https://itunes.apple.com/us/app/xcode/id497799835?mt=12&amp;uo=4"
target="_blank">xcode</a> and the <a
href="https://developer.apple.com/library/mac/technotes/tn2339/_index.html"
target="_blank">xcode commandline</a> tools.  The `gpi` and `gpi_make` commands
can be added to your path by adding the following line to your shell config
file (i.e. `~/.bashrc`).

```
PATH="/Applications/GPI.app/Contents/Resources/miniconda/bin:$PATH"
```

-----------

## Install Script
To use the install script `GPI_Install_Latest-rc.sh`, first make sure the
script is executable by entering the following command in a terminal:

```
$ chmod a+x GPI_Install_Latest-rc.sh
```

Then run the script with a path to the desired install location:

```
$ GPI_Install_Latest-rc.sh ~/gpi_stack
```

This script will install GPI from [Anaconda Cloud](https://anaconda.org) using the `conda` package manager. If you already use `conda`, you can install `gpi` with from the `gpi` channel, with dependencies from the `conda-forge` channel (this is how the installation script works).

```
$ conda install gpi -c conda-forge -c gpi -c defaults
```

-----------

## Virtual Machine

Download and unzip the GPI Stack `.zip` file.  This will create a directory
with the virtual machine contents.  Open the contained `.vmx` file with a
VMware compatible player.

To compile C++ extension modules in Ubuntu linux, install g++ with the
following command:

```
$ sudo apt-get install build-essential
```

The password for the default user is `gpilab`.
