# Dash-based dashboards


## local development using a conda environment

There are three lockfiles corresponding to windows, mac or linux.  Use the appropriate lockfile
for your operating system, e.g. for macs:

    conda create --name db1 --file conda-osx-64.lock
    conda activate db1
    pip install -r requirements.txt
    python -m counter.do_count

This will start dash on localhost:8050 in dev mode.  The actual dashboard code is located at:
[do_count.py](https://github.com/phaustin/eoscdbd-counter/blob/main/counter/do_count.py)

### To modify your environment

If you want to add a package to the environment, update a version, etc.,  edit
the conda [environment.yml](https://github.com/phaustin/eoscdbd-counter/blob/main/environment.yml)
and/or [requirements.txt](https://github.com/phaustin/eoscdbd-counter/blob/main/requirements.txt)

and rebuild the lock files with:

    conda-lock -f environment.yml -p win-64
    conda-lock -f environment.yml -p osx-64

Update your [version number](https://github.com/phaustin/eoscdbd-counter/blob/main/counter/__version__.py) and
then:

Kill the dash server, create a new environment, and restart:

    conda create --name db2 --file conda-osx-64.lock
    conda activate db2
    pip install -r requirements.txt
    python -m counter.do_count

and delete your old environment if you no longer need it:

    conda env remove -n db1

## Building docker containers

### To build and run the production container:

     docker-compose up --build prod_count

This will build a docker container using [this Dockerfile](https://github.com/phaustin/eoscdbd-counter/blob/main/counter_image/Dockerfile) using a version of the
[Pangeo base image](https://github.com/phaustin/pangeo-docker-images/blob/dashboard/base-image/Dockerfile)

The production dashboard will be running on locahost:8000

### To build and run the dev container:

    docker-compose up --build dev_count

This will bring the server up in dev mode on localhost:8050.  The image is the same as for the `dev_prod` service but the local counter code is [bind mounted](https://github.com/phaustin/eoscdbd-counter/blob/main/docker-compose.yml#L22) in the
container, so that local edits [do_count.py](https://github.com/phaustin/eoscdbd-counter/blob/main/counter/do_count.py)
will show up when you stop and restart the service.

## To do:

### Setting up a github action to build the container

- See the [pangeo example](https://github.com/pangeo-data/pangeo-docker-images/tree/master/.github/workflows)

- Setting up the [dockerhub webhook](https://docs.docker.com/docker-hub/webhooks/)
