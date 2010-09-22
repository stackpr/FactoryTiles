SHELL = /bin/sh

all:
	cd ./floor/ && make && cd ..
	#cd ./property/ && make && cd ..
	markdown README.md > README.html
