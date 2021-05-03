<div align="center" id="top"> 
  <img src="../../../misc/logo.jpg" alt="Common Utils" />

  &#xa0;

  <!-- <a href="https://github.com/multiscale-cosim/common-utils">Demo</a> -->
</div>

<h1 align="center">Common Utils</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/multiscale-cosim/common-utils?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/multiscale-cosim/common-utils?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/multiscale-cosim/common-utils?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/multiscale-cosim/common-utils?color=56BEB8">

  <img alt="Github issues" src="https://img.shields.io/github/issues/multiscale-cosim/common-utils?color=56BEB8" />

  <img alt="Github forks" src="https://img.shields.io/github/forks/multiscale-cosim/common-utils?color=56BEB8" />

  <img alt="Github stars" src="https://img.shields.io/github/stars/multiscale-cosim/common-utils?color=56BEB8" />
</p>

## Status

<h4 align="center"> 
	🚧  Common Utils 🚀 Under construction...  🚧
</h4> 

<hr>

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/multiscale-cosim" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

A collection of modules facilitating the general functionalities and thus can be adpated to address many common functional requiremnents. It contains the following modules:

* <a href="/python/configuration_manager"> Configurations Manager </a>
## :sparkles: Features ##

:heavy_check_mark: A Module for centralized management of configuration settings, setting up directories and setting a uniform format for the logging. More details are provided <a href="/python/configuration_manager"> here</a>.


## :rocket: Technologies ##

The following tools were used in this project:

- [Python](https://www.python.org/)
- [CMake](https://cmake.org/)
- [C++](https://isocpp.org/)
- [Makefile](https://www.gnu.org/software/make/manual/make.html)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Python](https://www.python.org/) and [CMake](https://cmake.org/) installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone git@github.com:multiscale-cosim/common-utils.git

# Access
$ cd common-utils

# set enviornment variable
$ export PYTHONPATH=/path/to/common-utils

# Install for CMake older than 3.15
$ cmake --build . --target install


# Install for CMake 3.15 and newer
$ cmake --install <dir> [<options>]

# Run the project
To be done

```

## TODO

Out of source build is currently broken
 - test runner files are missing
 - The including / building of the Table.h file goes wrong

## :memo: License ##

This project is under license from Apache License, Version 2.0. For more details, see the [LICENSE](LICENSE) file.


Made by <a href="https://github.com/multiscale-cosim" target="_blank">Multiscale Co-simulation team.</a>

&#xa0;

<a href="#top">Back to top</a>