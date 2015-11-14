all: talk.slides.html


talk.slides.html: talk.ipynb
	ipython nbconvert talk.ipynb --to slides  --reveal-prefix 'reveal.js'
	patch talk.slides.html -i patch_width.patch

serve: talk.slides.html
	python -m http.server 8080
