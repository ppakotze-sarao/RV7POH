# ZU-WAB POH source

Here is everything you need to know about flying ZU-WAB. The document is written in TeX so it does need to be
built. The recommended configuration is to use [TeX Live](https://www.tug.org/texlive/) with the provided 
build script. The script will create an electronic version of the document (`zuwab.pdf`) as well as a printable
version (`zuwab-book.pdf`) which can be directly printed on two-sided A4 paper and bound. Simply run the buider 
script as follows:
```bash
./build.sh
```
Note that if you manually build the documents, you must first build the electronic version: 
```bash
pdflatex --output-directory=temp zuwab.tex # Repeat if you need to build the table of contents etc. again
```
The resulting pdf will be in `temp/zuwab.pdf`. The printable version is simply a rework of the electronic 
version. It expects to find the base electronic version's pdf in `zuwab.pdf` so you must copy it from the
`temp` directory first. Build the printable version like this:
```bash
pdflatex --output-directory=temp zuwab-book.tex 
```
Again, the artefact will be in `temp/zuwab-book.pdf`.

