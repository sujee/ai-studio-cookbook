# Pelican Riding a Bicycle - A fun vibe benchmark

This is inpired by [Simon Willison](https://simonwillison.net/)'s experiment called [pelican riding a bicycle](https://simonwillison.net/tags/pelican-riding-a-bicycle/).  It has become a cool vibe benchmark to evaluate LLMs.  
Original github repo: [simonw/pelican-bicycle](https://github.com/simonw/pelican-bicycle)

## How to run it

It is very simple.  Issue the the following prompt on playground of any model (text to text model)

> Generate an SVG of a pelican riding a bicycle

It will generate a SVG code snippet.  Copy it and save it as an svg file (e.g. `image.svg`)

See the screenshots below.

<img src="studio-1.png" width="45%">
<img src="studio-2.png" width="45%">


You can view SVG file using any browser and modern graphic programs.

## Generated Images

You can find [generated images here](images/).

Annotated images (with model names) can found in in [images/annotated](images/annotated/)

**Qwen3-235B-A22B-Instruct-2507.SVG**  ([png](images/Qwen3-235B-A22B-Instruct-2507-1.png))

![](images/Qwen3-235B-A22B-Instruct-2507-1.svg)

**DeepSeek-R1-0528-1.svg**  ([png](images/DeepSeek-R1-0528-1.png))

![](images/DeepSeek-R1-0528-1.svg)


### Handy Scripts

You can also convert SVG into other image formats like PNG.  Here is how to do it in command line 

```bash
## using Image Magic's convert
convert input.svg output.png

## Using inkscape
inkscape --export-type=png --export-filename=output.png input.svg
```

- [convert2png.sh](convert2png.sh) : script to convert svgs to png 
- [combine-images.sh](combine-images.sh): script to combine multiple PNGs into a single one.



## References

- github: [simonw/pelican-bicycle](https://github.com/simonw/pelican-bicycle)