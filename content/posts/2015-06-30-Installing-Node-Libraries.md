Title:  Installing Node Libraries
Date:   2015-06-30 14:21:00
Author: Ashley Anderson

One of the nicest features of GPI is how easy it is to add a library and begin
using new nodes. Whether the library contains nodes and networks you created,
or code from a collaborator or colleague, installation is the same simple
process.

Here we cover installing an updated version of the Core library. This will
serve as a general demonstration of how to install additional node libraries.
<h2>The .gpirc File</h2>
GPI searches for libraries (by default) in a <code>~/gpi/</code> directory
within your home directory. On Mac OS X, the full path of this folder is
<code>/Users/&lt;username&gt;/gpi/</code>, and on Ubuntu (and most flavors of
Linux) it is <code>/home/&lt;username&gt;/gpi/</code>. Thus, to install a new
library, simply move its root directory into this folder. New libraries are
imported automatically any time GPI is started.

The <code>~/.gpirc</code> file contains per-user configuration options for GPI.
Since the file is hidden (begins with a <code>.</code>), you will not see it in
a normal directory listing; use <code>ls -a</code> to see it. If this file does
not exist on your system, you can generate a basic version from the GPI
"Config" menu.

![fitw75]({filename}/images/Screenshot-2015-02-05-11.21.10-300x80.png)

Select "Generate Config File" to create a basic .gpirc file.

The default GPI library path (<code>~/gpi/</code>) is stored in the
<code>LIB_DIRS</code> variable within the `.gpirc` file. You can amend the
<code>LIB_DIRS</code> in your <code>.gpirc</code> file to tell GPI to look for
libraries in some other directories, if you prefer. Append (or prepend)
directories to `LIB_DIRS` separated by colons.

![fitwidth]({filename}/images/Screenshot-2015-06-30-14.09.30.png)

My .gpirc file with modified LIB_DIRS to include additional node libraries.

<h2>Installing the Updated Core Library</h2>
The GPI package includes a snapshot of the Core node library, but new versions
of the Core nodes are maintained on <a title="GitHub"
href="https://github.com/gpilab/core-nodes"
target="_blank">GitHub</a>. Installing the updated Core library will *not*
override the default installation of the Core library, so you need to remove
its path (<code>/opt/gpi/node/core/</code>) from the `LIB_DIRS` variable in
your `.gpirc` file. A current snapshot of the Core library can be downloaded as
a zip archive from main GitHub page. To install this snapshot, simply unzip the
archive into <code>~/gpi/core/</code> as described above.

To stay up-to-date with the latest changes, it is recommended to link your
local Core library with the remote repository by cloning it using <a
title="Git" href="http://git-scm.com" target="_blank">Git</a>. Git is a popular
version control system, available on all platforms. Using Git makes it easy to
update your local copy of the source code, and to contribute back your own
enhancements and bug fixes.

To install the Core library using Git, open a terminal session and execute the
following commands (after installing Git if necessary):

<pre>% cd ~/gpi
% git clone https://github.com/gpilab/core-nodes.git core
</pre><br>

This will create a copy of the remote <code>core-nodes</code> repository to
your computer, inside your default GPI library directory.

<h3>Compiling the Core Library</h3>
GPI includes a Python/C++ interface called PyFI. The Core library uses PyFI to
implement algorithms in a combination of C++ and Python code. GPI includes a
script (<code>gpi_make</code>) to help compile C++ files associated with a GPI
library.

Compiled binary objects are not included in the Git repository, so it's
necessary to build the library after installation. Once you have downloaded or
cloned the repository into <code>~/gpi/core/</code>, run the following commands
to compile the C++ code:
<pre>% cd ~/gpi/core
% gpi_make --all
</pre>
<br>

<h3>Updating the Core Library</h3>
As mentioned, Git makes it easy to update the Core library with any new changes
from the developers. If you cloned the repository using Git, you can update
your copy of the Core library using the following commands:

<pre>% cd ~/gpi/core
% git pull
% gpi_make --all</pre><br>

Running <code>git pull</code> fetches any new changes from the core-nodes
repository on GitHub, and merges them into your local copy. To finish updating,
it's also good idea to re-compile the C++ code in case any changes were
made. Note you may get some warnings or errors if you attempt to "pull" changes
after modifying the code yourself. If you have changes you'd like to keep (or
contribute back!) please fork the project on GitHub, or just get in touch!

<h4>Branches in the <code>core-nodes</code> Repository</h4>
Development in the <code>core-nodes</code> repository follows the <a
title="gitflow"
href="http://nvie.com/posts/a-successful-git-branching-model/">gitflow</a> branching
model. There are two main branches in this model: <em>master</em>, which
contains stable releases; and <em>develop</em>, which contains newer,
untested changes. Most likely you will want to keep your local copy on
the <em>master</em> branch, unless you are planning to make changes to the
library and contribute them back to the community.

Use <code>git branch</code> to see which branch you are on, and <code>git
checkout &lt;branch name&gt;</code> to switch to a different branch. You will
again want to recompile (`gpi_make --all`) any time you change branches.

--------

Hopefully this will help you collaborate and stay up-to-date with the latest
changes in your GPI node libraries. Check out the
[documentation](http://docs.gpilab.com) for more information, and please [get
in touch](/community) if you have questions or if you're
interested in contributing to the project.
<h2></h2>
