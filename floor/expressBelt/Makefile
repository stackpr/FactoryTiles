sources := left.svg forward.svg right.svg leftRight.svg \
	leftForward.svg leftForwardRight.svg forwardRight.svg

all: .64

.16:
	for f in $(sources); do mkdir -p ./16/; inkscape -z -e ./16/$$f.png -w 16 scalable/$$f.svg &> /dev/null; done
.24:
	for f in $(sources); do mkdir -p ./24/; inkscape -z -e ./24/$$f.png -w 22 scalable/$$f.svg &> /dev/null; done
.32:
	for f in $(sources); do mkdir -p ./32/; inkscape -z -e ./32/$$f.png -w 32 scalable/$$f.svg &> /dev/null; done
.48:
	for f in $(sources); do mkdir -p ./48/; inkscape -z -e ./48/$$f.png -w 48 scalable/$$f.svg &> /dev/null; done

.64:
	mkdir -p ./64/;
	for f in $(sources); \
	do \
		CURRENT_FILE = basename $$f svg; \
		echo $$CURRENT_FILE; \
		set currentSVG = $$CURRENT_FILE .svg; \
		set currentPNG = $$CURRENT_FILE .png; \
		#inkscape -z -e .png -w 64 scalable/$$f.svg \ # &> /dev/null; \
	done

.96:
	for f in $(sources); do mkdir -p ./96/; inkscape -z -e ./96/$$f.png -w 96 scalable/$$f.svg &> /dev/null; done
.128:
	for f in $(sources); do mkdir -p ./128/; inkscape -z -e ./128/$$f.png -w 128 scalable/$$f.svg &> /dev/null; done
.192:
	for f in $(sources); do mkdir -p ./192/; inkscape -z -e ./192/$$f.png -w 192 scalable/$$f.svg &> /dev/null; done
.256:
	for f in $(sources); do mkdir -p ./256/; inkscape -z -e ./256/$$f.png -w 256 scalable/$$f.svg &> /dev/null; done
.384:
	for f in $(sources); do mkdir -p ./384/; inkscape -z -e ./384/$$f.png -w 384 scalable/$$f.svg &> /dev/null; done
.512:
	for f in $(sources); do mkdir -p ./512/; inkscape -z -e ./512/$$f.png -w 512 scalable/$$f.svg &> /dev/null; done

.768:
	for f in $(sources); do mkdir -p ./768/; inkscape -z -e ./768/$$f.png -w 768 scalable/$$f.svg &> /dev/null; done
.1024:
	for f in $(sources); do mkdir -p ./1024/; inkscape -z -e ./1024/$$f.png -w 1024 scalable/$$f.svg &> /dev/null; done
.1536:
	for f in $(sources); do mkdir -p ./1536/; inkscape -z -e ./1536/$$f.png -w 1536 scalable/$$f.svg &> /dev/null; done
.2048:
	for f in $(sources); do mkdir -p ./2048/; inkscape -z -e ./2048/$$f.png -w 2048 scalable/$$f.svg &> /dev/null; done
