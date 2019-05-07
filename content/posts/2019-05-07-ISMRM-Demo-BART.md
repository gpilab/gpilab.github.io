Title: ISMRM Demo: CS with BART in GPI
Date: 2019-05-07 08:59
Author: Ashley Anderson III <aganders3@gmail.com>
Header_Cover: /images/ismrm2019_bart.png

As part of our GPI demo at at the [ISMRM 2019 Open-Source Software Tools for MR
Pulse Design, Simulation & Reconstruction Weekend
Course](https://www.ismrm.org/19/program_files/WE21.htm), we've revived an
example of BART working inside GPI. This example is intended to demonstrate the
flexibility and capabilities of GPI to integrate other packages. This demo also
highlights the use of GPI as a teaching tool; the example is based on [this
example from Professor
Lustig](http://people.eecs.berkeley.edu/~mlustig/CS.html).

Before getting started here, please see Nick's post on [setting up GPI for the
ISMRM 2019 demo]({filename}/posts/2019-05-05-ISMRM-Demo-Primer.md).

---------

# Download and Compile BART for GPI

[BART for GPI](https://github.com/nckz/bart) is a fork of the [BART
project](https://github.com/mrirecon/bart). We concede this fork is out of
date, but it should suffice for a demonstation. Updating to a newer version
would be fairly trivial for someone familiar with both BART and GPI. Check
out Nick's _other_ post on [how BART was wrapped for use in
GPI]({filename}/posts/2016-02-16-GPI-and-the-BART.md) if you're interested in
making this work.

First, prepare your virtual machine for BART compilation:

    > sudo apt-get install git gcc make libfftw3-dev liblapack-dev libpng-dev

If you're using the GPI ISMRM 2019 demo VM or AMI on EC2, the password for the
`ubuntu` user is `gpilab`.

Next clone the BART for GPI fork into your `gpi` library folder:

    > git clone https://github.com/nckz/bart.git /home/${USER}/gpi/bart

Finally, build and test BART:

    > cd ~/gpi/bart
    > make
    > ./bart bench

If you're not working in the GPI VM, instead follow the instructions in the
BART for GPI README.

# Launch GPI and Open the Example

Open GPI using the startup script or from a terminal. Right click anywhere on
the canvas and you should see a new Library in the menu called `bart`. GPI
Libraries can contain both nodes and networks. Most BART functions should have
corresponding nodes here, but for now go ahead and select the `brain_cs_example
(net)` near the bottom of the menu.

<img src="{filename}/images/ismrm2019_bart/network_select.png" width="75%" class="center-block img-responsive"/>

The demo network will be loaded on the canvas, and the `DownloadFile` node
should begin downloading the example data. This data (about 5 MB) will be
stored in a temporary file.

<img src="{filename}/images/ismrm2019_bart/network_overview.png" width="75%" class="center-block img-responsive"/>

# Configure and Run the Network

Note the three `ReadMatlab` nodes. Each is reading data from the same file (the
one downloaded by the `DownloadFile` node) which contains several arrays.
Right-click on each of these nodes to open their node menus. In the menu you
will be able to select which array is output. From left to right we need to
select the sampling mask, the image, and the sampling pdf.

<img src="{filename}/images/ismrm2019_bart/ReadMatlab_select.png" class="center-block img-responsive"/>

Right-click on a few of the `ImageDisplay` nodes to probe the algorithm at
various points. The `ImageDisplay` node labeled `CS Image` is the
compressed-sensing reconstruction (though at this point it is only the inital
condition based on zero-filling).

Open the `Iter` node and click the "Start/Stop" button to begin the iterative
reconstruction. The `CS Image` will be updated with each iteration, and you can
watch as the undersampling artifacts are removed by the wavelet-based
soft-thresholding constraint.

<img src="{filename}/images/ismrm2019_bart/cs_example_animated.gif" class="center-block img-responsive"/>

There you have it! Explore the rest of the BART tools in GPI and let us know if
you come up with any cool examples.

