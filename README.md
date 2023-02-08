# Learning Jinja2 using a flask webapp

## Run website
	```bash
		podman volume create jinja
		podman run --rm -it -v jinja:/mnt -p 8000:5000 --name=jinja_web fedora
	```


# After container is running...
	## From outside container...
		```bash
			podman cp ${location_of_cloned_repo}/mnt jinja_web:/
		```
	
	## From within conatiner
		```bash
			cd /mnt
			sh install.sh
			python app.py
		```

	## From outside container...
	navigate to http://localhost:8000 to view website
