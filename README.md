"Rust for Scientists with deadlines" talk at Rust SP
====================================================


Deps:

* [pandoc](https://pandoc.org/MANUAL.html#producing-slide-shows-with-pandoc)
* [reveal.js](https://revealjs.com/)


Generating HTML:

```
pandoc -t revealjs --css=./custom.css -s scientific-rust.md -o scientific-rust.html
```
