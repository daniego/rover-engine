
# Run container
docker run -it -p 8089:8089 --privileged daniego/rover-engine

# Run container with local code
docker run -it -p 8089:8089 -v ${PWD}:/srv/rover-engine --privileged daniego/rover-engine

# Run and login
docker run -it -p 8089:8089 --privileged --entrypoint='bash' daniego/rover-engine

# Run and login with local code
docker run -it -p 8089:8089 -v ${PWD}:/srv/rover-engine --privileged --entrypoint='bash' daniego/rover-engine
