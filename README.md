# Learning Jinja2 using a containerized flask webapp

## Run website
	podman volume create jinja
	podman run --rm -it -v jinja:/mnt -p 8000:5000 --name=jinja_web fedora


### While container is running...
#### From *outside* container...
	podman cp <location_of_cloned_repo>/mnt jinja_web:/
	
#### From *within* conatiner
	cd /mnt
	sh install.sh
	python app.py

### From outside container...
>navigate to http://localhost:8000 to view website
