Title: GPI version 1.1 has arrived!
Date: 2019-08-14
Author: Daniel Borup <borup.daniel@mayo.edu>

### A new release is here!

GPI version 1.1 is now available, along with version 2.0 of the GPI core nodes. For the most part, the look and feel of GPI should remain unchanged to the end user. But we’ve made some significant improvements under the hood that we hope will make GPI easier for users, developers, and maintainers going forward. Below you'll find a description of the major changes, upgrade process, and a list of changes to the core nodes.

As of this version, the recommended installation method is to use the installation script. All changes listed below will be accounted for by default when installing with the script, so if you're a new user you can just sit back, relax, and enjoy GPI.

## Major changes

Two main changes come as part of this release.

### Qt5

We've added support for Qt5 thanks to a contribution from community member Gregory Lee. Support is now provided using the QtPy wrapper, which is technically compatible with Qt4 — however, because Qt4 has been end-of-life for some time now, we're no longer supporting it in GPI.

For most users, this change will show up as nothing more than a slightly different look to menus. However, if you were developing your own nodes and making use of Qt libraries imported from GPI, you may need to update your import statements to reference the new "QtWidgets" module -- for an example, see the changes made to the core nodes library as part of this update (https://github.com/gpilab/core-nodes/pull/10).

### Conda-forge packaging

GPI, and the core nodes, are now packaged on conda-forge! This is another "under the hood" change for most users, but one that we're very excited about as it will make our development, testing, and release process much more streamlined and reliable. Since GPI already relied on numerous packages from conda-forge, it made sense to add our work to this community ecosystem, too.

If you're a new user or otherwise installing GPI from scratch, this change should be completely invisible. 

If you want to upgrade an existing GPI installation, there are a few minor differences. First, the core nodes are now packaged and distributed under the name `gpi_core`. At the surface level, this means these nodes will appear under the heading `gpi_core` in the node selection menu. More critically, if you've written nodes that import or include modules from the core library, you'll need to change those import/include statements to reference `gpi_core` instead of `core` after upgrading.

## Upgrading

To upgrade an existing GPI installation, you can take the following simple steps.

1) Remove the `gpi` channel from your conda configuration, as it's no longer necessary. You can do this directly by modifying `~/.condarc`. While various configurations may work, the `.condarc` provided with a fresh GPI install is the following:

```
channels:
  - conda-forge
  - defaults
channel_priority: strict
```

This sets `conda-forge` and `defaults` as the two channels to search (in that order) and sets "strict channel priority" as currently recommended for in the conda-forge ecosystem.

2) Make a backup copy of any node libraries you may use outside of the GPI core nodes, as you may need to modify your nodes slightly to work with v1.1.

3) Run `conda update -n base conda` to get the latest version of the package manager itself.

4) Install GPI and the core nodes. If you use conda exclusively for GPI, you can upgrade inside your existing gpi environment with:

```
conda activate gpi
conda install gpi gpi_core
```

Or, if you prefer a more conservative approach, make a new environment for GPI 1.1 and install there:

```
conda create -n <new-env-name>
conda activate <new-env-name>
conda install gpi gpi_core
```

5) Make any necessary changes to other node libraries as described above.

6) Get started with GPI 1.1 -- and consider helping us make it even better!

## Core Node Library Changes

Minor changes to the core nodes themselves include two new nodes:

- `Int_Math`, which works just like `Float_Math` for integer values.
- `Switch`, which allows you to toggle between a left and right input without re-drawing connections.

And some modifications to existing nodes:

- In the `Collapse` node, you can now use the "non-zero" option for collapsing in a single dimension, not just with "collapse all" selected
- The `shapes` node now allows for the generation of complex-valued noise, as well as repeatable noise using a user-specified seed.
- `Calc_101` now allows for more granular control over the scheme used for derivatives and integrals.
- Many trigonometric functions now have a "cycles" option in addition to degrees and radians.
- Nodes with multiple functions will provide more information on the canvas about which function is active.

Development of both the GPI framework and core nodes library is ongoing, and we welcome community contributions of any kind!
