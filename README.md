# IUCN Redlist importer

## Installation

Clone the project:

    git clone https://github.com/cottagelabs/redlist-indexer.git

get all the submodules

    cd myapp
    git submodule init
    git submodule update

This will initialise and clone the esprit and magnificent octopus libraries

Then get the submodules for Magnificent Octopus

    cd myapp/magnificent-octopus
    git submodule init
    git submodule update

Create your virtualenv and activate it

    virtualenv /path/to/venv
    source /path/tovenv/bin/activate

Install esprit and magnificent octopus (in that order)

    cd myapp/esprit
    pip install -e .
    
    cd myapp/magnificent-octopus
    pip install -e .
    
Create your local config

    cd myapp
    touch local.cfg

Then you can override any config values that you need to

To start the application, you'll also need to install it into the virtualenv just this first time

    cd myapp
    pip install -e .

## To index the data    
___Note:___   
___1. Make sure elastic search is running___   
___2. Download the IUCN redlist data of interest from the [IUCN website](http://www.iucnredlist.org/search/) in csv format___. Downloading these data now requires a login and a brief (at least minutes) waiting period.
  
  ```
  from service.importer import import_species
  import_species('path_to_csv_file')
  ```
