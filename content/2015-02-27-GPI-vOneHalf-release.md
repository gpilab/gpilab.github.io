Title:  GPI v½ Release
Date:   2015-02-27 15:39:00
Author: Nicholas Zwart
Header_Cover: /images/banner_v05.jpg

GPI v0.5 is now available for download in its first public release!

<div style="display: block; margin-left: auto; margin-right: auto; position: relative; width: 100%; height: 100px;">
<div id="image1_ban" style="position: relative; top: 0px; left: 0px; padding: 10px;"><img class="noborder aligncenter size-medium wp-image-5" src="http://gpilab.com/wp-content/uploads/2014/09/logo-300x113.png" alt="logo" width="300" height="113" /></div>
<div id="image2_conf" style="background: none repeat scroll 0% 0% transparent; outline: medium none; text-align: center; vertical-align: middle; position: relative; top: -200px; left: -200px; z-index: 2; padding: 10px;"><img class="noborder aligncenter size-medium wp-image-324" src="{filename}/images/confetti.gif" alt="confetti" width="300" /></div>
</div>
&nbsp;

The GPI project has been able to develop into a robust first release thanks to
the efforts of the <a
href="https://github.com/gpilab/core-nodes/blob/develop/AUTHORS"
target="_blank">Keller Center for Imaging Innovation</a> group in Phoenix,
sponsorship from Philips Healthcare and the collaboration with Phoenix
Children's Hospital, Vanderbilt University, University of Texas Southwestern,
Tsinghua University and Cincinnati Children's Hospital as well as those who
have participated in GPI training.

GPI now has native packages for OSX, Linux, and a pre-installed Linux virtual
machine to run GPI on your PC. The GPI project and node code is also now being
hosted on GitHub.  Visit <a href="http://github.com/gpilab"
target="_blank">github.com/gpilab</a> to get the latest updates and node
library releases. There is now a <a
href="http://gpilab.com/mailman/listinfo/gpi-users_gpilab.com"
target="_blank">GPI users</a> mailing list for users who wish to participate in
community support.

## What's New in Version 0.5

### Features

<ul>
    <li>Added Support for OSX 10.7</li>
    <li>Upgraded to Anaconda 2.1</li>
    <li>Improved HDF5 reader node</li>
    <li>Added a new Matlab file reader (for old and new HDF5 formats)</li>
    <li><strong>Left-mouse-button port-edge-connect!</strong></li>
    <li>Right-click downstream ports to delete an edge <br><a href="http://gpilab.com/wp-content/uploads/2015/02/rightclickdelete.gif"><img class=" size-full wp-image-184 aligncenter" src="http://gpilab.com/wp-content/uploads/2015/02/rightclickdelete.gif" alt="rightclickdelete" width="244" height="202" /></a><br></li>
</ul>
<ul>
    <li>Node reload; just select a node (or multiple nodes), press Ctrl+R and the node will update and reconnect to up and downstream nodes<br><img class="alignnone size-full wp-image-182 aligncenter" src="http://gpilab.com/wp-content/uploads/2015/02/node_reload.gif" alt="node_reload" width="262" height="212" /><br></li>
    <li>Auto generate the user library (via the main menu)</li>
    <li><code>gpi_make</code> now does a force recompile on all node .py files</li>
    <li><code>LIB_DIRS</code>, in the <code>.gpirc</code>, will now search the parent directory for libraries, so now you can easily setup your custom library directory and new libraries will be loaded as they are added
<ul>
    <li>By default, the <code>~/gpi</code> directory is searched</li>
</ul>
</li>
</ul>

### Bugfixes

<ul>
    <li>Fixed node updating via drag'n drop, copy/paste, or reload by force recompiling all node .py files</li>
    <li>Fixed file association bug for capitalized extensions</li>
    <li>Updated numpy to qimage conversions with the qimage2ndarray library</li>
    <li>Removed zlib string compression on StringBox widgets to prevent nodes from segfaulting when using the StringBox in Linux</li>
</ul>
<p style="text-align: center;"></p>
