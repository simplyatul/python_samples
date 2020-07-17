This is a simple dockerize ReST Server

Build image
$ docker build --rm -t rest_server:1.0 .

Run image
$ docker run -d -p 5000:5000 --name restsrv1.0 rest_server:1.0


Credits: 
https://www.docker.com/blog/containerized-python-development-part-1/

