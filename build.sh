#!/bin/sh

# Build twice to resolve cross references
pdflatex --output-directory=build zuwab.tex 
pdflatex --output-directory=build zuwab.tex 

# Cleanup
rm build/*.aux build/*.log build/*.mtc* build/*.toc build/*.maf

