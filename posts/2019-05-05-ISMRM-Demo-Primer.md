Title: ISMRM Demo Primer
Date: 2019-05-05 12:29:00
Author: Nicholas Zwart
Header_Cover: /images/ismrm2019_commsw.jpg

GPI is going to be presented at the [ISMRM 2019 Open-Source Software Tools for
MR Pulse Design, Simulation & Reconstruction Weekend Course](https://www.ismrm.org/19/program_files/WE21.htm).
The format of this session will be to allow developers to pitch their designs
and then provide a break-out tutorial session to give participants a chance to
interact with the software directly.  To that end, this post is about
installing the latest demo examples via virtual machine or via a free-tier
Amazon-EC2 instance.

This guide is split into two sections:

* Using Amazon-EC2 via AMI
* Using a Virtual Machine Locally

If you are not familiar with either of these technologies, it would behoove you
to take some time before the meeting to get one of these setups working.

---------

# Using Amazon-EC2 via AMI
Lets start by introducing some terms:

* EC2: Elastic Compute Cloud (the '2' is meant to save space by doubling the abbreviated 'C')
    * The "elastic compute" generally referes to a computer in the cloud that you can use by secure shelling (ssh) into and starting services like an jupyter notebook or web-server, etc...
* AMI: Amazon Machine Image (if you say "Amazon-AMI", you could then shorten it by saying A2MI)
    * The "machine image" is a freeze dried, pre-installed system that can be run on an EC2 instance. -Giving you the ability to choose the EC2 hardware that you'd like to run the "machine image" on.

The idea is that the GPI demo can be pre-installed on an AMI and the interested
ISMRM participant can simply start their own private EC2 instance to test-drive
the software.  This mechanism for software demos is a new initiative setup by
the organizing committee (see the [Call for Community Software
page](https://www.ismrm.org/19m/call-for-community-software-tools-demos/) for
details).

There is still some setup, you'll have to get an Amazon Web Services (AWS)
account, find the GPI-AMI, start an instance, setup an ssh tunnel to interact
with the cloud system.  Since GPI is a graphical desktop application, we've
chosen to use [VNC](https://en.m.wikipedia.org/wiki/Virtual_Network_Computing)
as a remote desktop client.

I'm going to include instructions for MacOS, Ubuntu Linux and Windows. -Take
the Windows steps with a grain of salt, I'm listing some instructional links
but this isn't the method I'm personally familiar with.

## 1. Install an SSH Client
To connect to the EC2 instance (of an AMI) you'll need a secure shell client
application. This is already part of MacOS and Linux, so you're set.  If you're
using Windows then you'll need a client like
[Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).

## 2. Install VNC
Each OS has various VNC capabilities. MacOS has it by default, it can be
accessed by pressing the key sequence `Command-k` with the `Finder.app` in
focus.

### Ubuntu Linux
I prefer [tightVNC](https://www.tightvnc.com/) since it has nice compression
features and has been available nearly for ever.

```
   $ sudo apt-get update
   $ sudo apt-get install xtightvncviewer
```

### Windows
Find and install a VNC client.  It appears that
[RealVNC](https://www.realvnc.com) has a free trial version.

## 3. Sign up for a Free Amazon Web Service Account
Point your browser to [console.aws.amazon.com](https://console.aws.amazon.com)
and sign up.  You'll have to enter a credit card, but if you only select 'free
tier' services (which are labelled at every step), then you won't incur any
charges... probably.

## 4. Run the GPI-AMI on EC2
There are few menus to navigate through to get to the AMI instance that we've
setup for the demo:

* Click the Region button in the upper right hand corner of the page.
    * Mine says "Ohio", but you can choose either "Ohio" or "Oregon", this will allow you to find the AMI
* Click the link "Launch a virtual machine"
    * this brings you to a page that has various pre-configure images
* Click the "Community AMIs" tab on the left hand side of the page.
    * use the search bar to find either of the following AMIs:
        * Name: GPILAB, AMI-Name: GPILAB-DEMO, AMI ID: ami-02203acf16dd4a983 Region: (US East, Ohio)
        * Name: GPILAB, AMI-Name: GPILAB-DEMO, AMI ID: ami-0080216529b04243b Region: (US West, Oregon)
* Click the checkbox next to the list AMI and then click the "Launch" button above the list
    * Choose the "General purpose" (t2.micro) machine config
    * Press "Review and Launch"
    * Then Press "Launch"

At this point you'll see a dialog box that is asking you to generate a
"key-pair".  This is for secure shelling into your instance, and its the only
way to do so. So choose "create a new key pair" and download the `PEM` file to
your home directory (remember what you named it, and where you put it). Hit the
final "Launch" button and then hit the "View Instance" button.

## 5. Connect to Your EC2 Instance
Almost connected!  Within the "EC2 Instance" view right click on your newly
running instance to get a popup-dialog, from there hit connect for another
popup that shows the following information:

```
To access your instance:

1. Open an SSH client. (find out how to connect using PuTTY)
2. Locate your private key file (GPILAB_Demo.pem). The wizard automatically detects the key you used to launch the instance.
3. Your key must not be publicly viewable for SSH to work. Use this command if needed:

    chmod 400 GPILAB_DEMO.pem

4. Connect to your instance using its Public DNS:

    ec2-3-17-23-92.us-east-2.compute.amazonaws.com

Example:

    ssh -i "GPILAB_DEMO.pem" root@ec2-3-17-23-92.us-east-2.compute.amazonaws.com

Please note that in most cases the username above will be correct, however please ensure that you read your AMI usage instructions to ensure that the AMI owner has not changed the default AMI username.
```

You'll need to take that information to parameterize your ssh client (with your
instances domain and the user 'ubuntu').

### MacOS and Linux
In a terminal enter the following command (after you replace the relevant parts
with your instance information):

```
    $ ssh -i "GPILAB_DEMO.pem" -L 5900:localhost:5900 ubuntu@ec2-3-17-23-92.us-east-2.compute.amazonaws.com
```

The `-L 5900:localhost:5900` is used to forward the VNC port over the ssh
connection.

### Windows
Take note of the `PEM` file location, the port forwarding command, the username
and domain; these will be entered into Putty to perform the ssh link and VNC
tunnel.

Follow [this guide](https://crl.ucsd.edu/handbook/vnc/index.php) to ensuring
that Putty and VNC are setup correctly.

## 6. Start the VNC Client
With the ssh connection established (and the VNC port forwarded to `localhost`).
You can fire up your VNC client and enter the following information:

### MacOS
Focus the `Finder.app` and hit `Command-k`.  In the dialog box labelled 'server address' type:

```
    vnc://localhost:5900
```

Then press connect.

### Linux
In a terminal enter:

```
    $ xtightvncviewer localhost:5900
```

### Windows
Follow [this guide](https://crl.ucsd.edu/handbook/vnc/index.php) to ensuring
that Putty and VNC are setup correctly.

#### The VNC Password is `gpilab`
Assuming the ISMRM conference wifi has enough bandwidth to tunnel a VNC
connection, you should be good to go ;).

## Start GPI
There is a script on the desktop called `startGPI`, just double click to get
started.

If you'd like more information on the process of setting up an AMI, the ISMRM
organizers have a nice guide (with pictures) used in a past [DL
tutorial](https://github.com/peterchang77/dl_tutorial).

---------

# Using A Virtual Machine Locally
If your not convinced you'll be able to connect to an Amazon EC3 instance or
perhaps you're more used to using a virtual machine locally, we've got an open
virtual appliance that's ready to go.  You'll need to download and install
either VirtualBox or VMware:

* [VirtualBox (MacOS, Linux, Windows)](https://www.virtualbox.org/wiki/Downloads)
* [VMware Fusion (MacOS)](https://www.vmware.com/products/fusion/fusion-evaluation.html)
* [VMware Workstation Player (Linux, Windows)](https://www.vmware.com/products/workstation-player/workstation-player-evaluation.html)

Then you'll have to download our pre-installed GPI virtual machine from the
release page or directly:

* [GPI Release Page](https://github.com/gpilab/framework/releases/tag/v1.0.4)
* [gpilab_v104_2019may05.ova (1.28GB)](https://github.com/gpilab/framework/releases/download/v1.0.4/gpilab_v104_2019may05.ova)

Open your chosen virtual machine client and import the downloaded `OVA` file.
After a few dialog boxes you should be able to start your VM directly.

## Start GPI
There is a script on the desktop called `startGPI`, just double click to get
started.
