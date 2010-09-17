sources := left forward right \
	leftForward leftForwardRight forwardRight

all: native

production: native
	for f in $(sources); do mkdir -p ./16/; inkscape -z -e ./16/$$f.png -w 16 scalable/$$f.svg &> /dev/null; done
	for f in $(sources); do mkdir -p ./24/; inkscape -z -e ./24/$$f.png -w 22 scalable/$$f.svg &> /dev/null; done
	for f in $(sources); do mkdir -p ./32/; inkscape -z -e ./32/$$f.png -w 32 scalable/$$f.svg &> /dev/null; done
	for f in $(sources); do mkdir -p ./48/; inkscape -z -e ./48/$$f.png -w 48 scalable/$$f.svg &> /dev/null; done

native:
	for f in $(sources); do mkdir -p ./64/; inkscape -z -e ./64/$$f.png -w 64 scalable/$$f.svg &> /dev/null; done

oversize: production
	for f in $(sources); do mkdir -p ./96/; inkscape -z -e ./96/$$f.png -w 96 scalable/$$f.svg &> /dev/null; done
	for f in $(sources); do mkdir -p ./128/; inkscape -z -e ./128/$$f.png -w 128 scalable/$$f.svg &> /dev/null; done
	for f in $(sources); do mkdir -p ./192/; inkscape -z -e ./192/$$f.png -w 192 scalable/$$f.svg &> /dev/null; done
	for f in $(sources); do mkdir -p ./256/; inkscape -z -e ./256/$$f.png -w 256 scalable/$$f.svg &> /dev/null; done
	for f in $(sources); do mkdir -p ./384/; inkscape -z -e ./384/$$f.png -w 384 scalable/$$f.svg &> /dev/null; done
	for f in $(sources); do mkdir -p ./512/; inkscape -z -e ./512/$$f.png -w 512 scalable/$$f.svg &> /dev/null; done

huge: oversize
	for f in $(sources); do mkdir -p ./768/; inkscape -z -e ./768/$$f.png -w 768 scalable/$$f.svg &> /dev/null; done
	for f in $(sources); do mkdir -p ./1024/; inkscape -z -e ./1024/$$f.png -w 1024 scalable/$$f.svg &> /dev/null; done
	for f in $(sources); do mkdir -p ./1536/; inkscape -z -e ./1536/$$f.png -w 1536 scalable/$$f.svg &> /dev/null; done
	for f in $(sources); do mkdir -p ./2048/; inkscape -z -e ./2048/$$f.png -w 2048 scalable/$$f.svg &> /dev/null; done
