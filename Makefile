SHELL = /bin/sh
MAKE = /usr/bin/make

firstlevel := robot floor module property
secondlevel := $(foreach dir,$(firstlevel),$(wildcard $(dir)/*))
scalables := $(foreach file,$(secondlevel),$(wildcard $(file)/scalable/*.svg))

all: readme .64

.16:
	for file in $(scalables); do cd "`dirname $$file`"; mkdir -p ../16/; inkscape -z -w 16 -e "../16/`basename $$file .svg`".png  "`basename $$file`"; cd ../../../; done
.24:
	for file in $(scalables); do cd "`dirname $$file`"; mkdir -p ../24/; inkscape -z -w 24 -e "../24/`basename $$file .svg`".png  "`basename $$file`"; cd ../../../; done
.32:
	for file in $(scalables); do cd "`dirname $$file`"; mkdir -p ../32/; inkscape -z -w 32 -e "../32/`basename $$file .svg`".png  "`basename $$file`"; cd ../../../; done
.48:
	for file in $(scalables); do cd "`dirname $$file`"; mkdir -p ../48/; inkscape -z -w 48 -e "../48/`basename $$file .svg`".png  "`basename $$file`"; cd ../../../; done
.64:
	for file in $(scalables); do cd "`dirname $$file`"; mkdir -p ../64/; inkscape -z -w 64 -e "../64/`basename $$file .svg`".png  "`basename $$file`"; cd ../../../; done
.96:
	for file in $(scalables); do cd "`dirname $$file`"; mkdir -p ../96/; inkscape -z -w 96 -e "../96/`basename $$file .svg`".png  "`basename $$file`"; cd ../../../; done
.128:
	for file in $(scalables); do cd "`dirname $$file`"; mkdir -p ../128/; inkscape -z -w 128 -e "../128/`basename $$file .svg`".png  "`basename $$file`"; cd ../../../; done
.160:
	for file in $(scalables); do cd "`dirname $$file`"; mkdir -p ../160/; inkscape -z -w 160 -e "../160/`basename $$file .svg`".png  "`basename $$file`"; cd ../../../; done
.256:
	for file in $(scalables); do cd "`dirname $$file`"; mkdir -p ../256/; inkscape -z -w 256 -e "../256/`basename $$file .svg`".png  "`basename $$file`"; cd ../../../; done
.384:
	for file in $(scalables); do cd "`dirname $$file`"; mkdir -p ../384/; inkscape -z -w 384 -e "../384/`basename $$file .svg`".png  "`basename $$file`"; cd ../../../; done
.512:
	for file in $(scalables); do cd "`dirname $$file`"; mkdir -p ../512/; inkscape -z -w 512 -e "../512/`basename $$file .svg`".png  "`basename $$file`"; cd ../../../; done
.768:
	for file in $(scalables); do cd "`dirname $$file`"; mkdir -p ../768/; inkscape -z -w 768 -e "../768/`basename $$file .svg`".png  "`basename $$file`"; cd ../../../; done
.1024:
	for file in $(scalables); do cd "`dirname $$file`"; mkdir -p ../1024/; inkscape -z -w 1024 -e "../1024/`basename $$file .svg`".png  "`basename $$file`"; cd ../../../; done

readme:
	markdown README.md > README.html
	echo $|;
