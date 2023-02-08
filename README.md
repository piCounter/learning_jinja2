# Learning Jinja2 using a containerized flask webapp
*Although this app was written using podman, it should run the same with docker. Just replace podman with docker in the commands*

## Run website
1. `podman volume create jinja`
2. `podman run --rm -it -v jinja:/mnt -p 8000:5000 --name=jinja_web fedora`


### While container is running...
#### From *outside* container
1. `podman cp <location_of_cloned_repo>/mnt jinja_web:/`
	
#### From *within* container
1. `cd /mnt`
1. `sh install.sh`
1. `python app.py`

#### From *outside* container
>navigate to http://localhost:8000 to view website

When finished with app...
- Enter CTRL+C to quit flask (the web server).
- Enter `exit` to exit the container.
- Enter `podman volume rm jinja` to remove the container volume.
