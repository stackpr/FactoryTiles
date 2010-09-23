SHELL = /bin/sh

all:
	cd ./floor/ && make && cd ..
	markdown README.md > README.html
