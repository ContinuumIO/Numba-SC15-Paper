numba_sc15.pdf: numba_sc15.ps
	ps2pdf numba_sc15.ps

numba_sc15.ps: numba_sc15.dvi
		dvips numba_sc15.dvi

numba_sc15.dvi: numba_sc15.tex
		latex numba_sc15.tex

clean:
	rm -f numba_sc15.pdf numba_sc15.ps numba_sc15.dvi
