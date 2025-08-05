#!/bin/bash
# sudo apt install  imagemagic inkscape librsvg2-bin


## convert SVG files (passed as arguments) to PNG
if [[ $# -lt 1 ]]; then
	echo "Usage: $0 file1.svg [file2.svg ...]"
	exit 1
fi

for file in "$@"; do
	if [[ -f "$file" && "$file" == *.svg ]]; then
		inkscape --export-type=png "$file"
	else
		echo "Skipping $file (not an SVG file)"
	fi
done

## process PNG images in 'images' folder
annotated_dir="images/annotated"
mkdir -p "$annotated_dir"

for file in images/*.png; do
	out_file="$annotated_dir/$(basename "$file")"
	convert "$file" \
		-font Arial -pointsize 18 -fill black -stroke none \
		-gravity NorthEast -annotate +10+10 "${file##*/}" \
		"$out_file"
done
