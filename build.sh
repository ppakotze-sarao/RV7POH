#!/bin/sh

# Build twice to resolve cross references for electronic document
pdflatex --output-directory=temp zuwab.tex 
pdflatex --output-directory=temp zuwab.tex 
mv temp/zuwab.pdf .

# Build printable book
pdflatex --output-directory=temp zuwab-book.tex
mv temp/zuwab-book.pdf .

# Cleanup
rm temp/*

