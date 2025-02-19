#!/bin/bash

for dir in */; do

  for subdir in "$dir"*/; do

    # Check if optimized.py exists and rename it
    if [[ -f "$subdir/optimized.py" ]]; then
      number=$(basename "$subdir" | awk '{print $1}')
      mv "$subdir/optimized.py" "$subdir/${number}-optimized.py"
      echo "Renamed optimized.py to ${number}-optimized.py in $subdir"
    fi

    # Check if caveman.py exists and rename it
    if [[ -f "$subdir/caveman.py" ]]; then
      number=$(basename "$subdir" | awk '{print $1}')
      mv "$subdir/caveman.py" "$subdir/${number}.py"
      echo "Renamed caveman.py to ${number}.py in $subdir"
    fi

  done
done

