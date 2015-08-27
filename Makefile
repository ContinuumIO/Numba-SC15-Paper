numba_sc15.pdf: numba_sc15.ps
	ps2pdf numba_sc15.ps

numba_sc15.ps: numba_sc15.dvi
	dvips numba_sc15.dvi

numba_sc15.dvi: numba_sc15.tex cite.bib
	latex numba_sc15
	bibtex numba_sc15
	latex numba_sc15
	latex numba_sc15

clean:
	rm -f numba_sc15.pdf numba_sc15.ps numba_sc15.dvi
