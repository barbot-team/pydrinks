# pydrinks

PyDrinks Python Library for making drinks using barbot

## Requires

- Python 2.7
- [pyserial](http://pyserial.sourceforge.net/)
- [pyyaml](http://pyyaml.org/wiki/PyYAML)

## Installation

First install [pyserial](http://pyserial.sourceforge.net/), which is
required to open up the serial connection. [pyyaml](http://pyyaml.org/wiki/PyYAML) is also required in order to read drinks yaml files. Then download
the pydrinks repo. You can use the following git command or download the
[.zip file](https://github.com/barbot-team/pydrinks):

    git clone https://github.com/barbot-team/pydrinks.git

Then `cd` into the pydrinks directory and run the setup.py script to install:

    $ python setup.py install

## Setting up your configuration

Rather than inputing the recipes into barbot by hand in python you can write,
YAML files which will represent the recipes. An example recipes file is found below:

    # Example Recipes File
	# Chris W.
	- name: Manhattan
	  description: A nice drink to have.
	  ingredients:
	    - Whiskey:  3 # parts
	    - Vermouth: 1 # parts
	- name: Perfect Manhattan
	  description: An altered version of a Manhattan.
	  ingredients:
	    - Whiskey: 2 # parts
	    - Vermouth: 2 # parts