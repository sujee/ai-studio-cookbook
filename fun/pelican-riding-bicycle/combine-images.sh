#!/bin/bash
# Usage: ./combine-images.sh input1.png input2.png ... -o output.png

if [[ $# -lt 3 ]]; then
    echo "Usage: $0 -o output.png input1.png input2.png ..."
    exit 1
fi

# Parse arguments
inputs=()
output=""
while [[ $# -gt 0 ]]; do
    case "$1" in
        -o)
            shift
            output="$1"
            ;;
        *)
            inputs+=("$1")
            ;;
    esac
    shift
done

if [[ -z "$output" ]]; then
    echo "Error: Output file must be specified with -o flag."
    exit 1
fi

rm -f "$output"  # Remove existing output file if it exists

# Remove any input PNG files that don't exist
valid_inputs=()
for img in "${inputs[@]}"; do
    if [[ -f "$img" ]]; then
        valid_inputs+=("$img")
    #else
        # echo "Warning: $img does not exist and will be skipped."
    fi
done

if [[ ${#valid_inputs[@]} -eq 0 ]]; then
    echo "Error: No valid input PNG files to combine."
    exit 1
fi

# Combine all valid input PNGs vertically
convert "${valid_inputs[@]}" -append "$output"