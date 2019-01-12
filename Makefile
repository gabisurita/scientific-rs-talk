# https://pandoc.org/MANUAL.html#producing-slide-shows-with-pandoc

SLIDE_OPTIONS=-t revealjs --css=./custom.css -s

all: scientific-rust.html

scientific-rust.html: scientific-rust.md reveal.js/css/reveal.css
	pandoc $(SLIDE_OPTIONS) $< -o $@

watch: scientific-rust.md reveal.js/css/reveal.css scientific-rust.html
	fswatch -o --event Updated $< | xargs -n1 -I{} sh -c "echo Rebuilding...; pandoc $(SLIDE_OPTIONS) $< -o scientific-rust.html"

full: scientific-rust.md reveal.js/css/reveal.css
	pandoc  $(SLIDE_OPTIONS) --self-contained $< -o scientific-rust.html

reveal_version=3.6.0

reveal.js/css/reveal.css:
	wget -O /tmp/$(reveal_version).tar.gz https://github.com/hakimel/reveal.js/archive/$(reveal_version).tar.gz
	tar xvzf /tmp/$(reveal_version).tar.gz
	rm /tmp/$(reveal_version).tar.gz
	mv reveal.js-$(reveal_version) reveal.js
	touch $@
