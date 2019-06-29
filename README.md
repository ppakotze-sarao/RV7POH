# ZU-WAB POH source

Here is everything you need to know about flying ZU-WAB. The document is written in TeX so it does need to be
built. The recommended configuration is to use [TeX Live](https://www.tug.org/texlive/) with the provided 
build script. Simply run the buider script as follows:
```bash
./build.sh
```
The completed document will be in `build/zuwab.pdf`. If you want to build it manually, use 
`pdflatex --output-directory=build zuwab.tex` from the root directory.