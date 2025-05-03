#!/bin/bash

# Declare an associative array
declare -A fruits

# Add elements to the associative array
fruits[apple]="red"
fruits[banana]="yellow"
fruits[grape]="purple"
fruits[orange]="orange"

# Access elements of the associative array
echo "The color of apple is ${fruits[apple]}"
echo "The color of banana is ${fruits[banana]}"

# Iterate over keys and values
echo "All fruits and their colors:"
for fruit in "${!fruits[@]}"; do
    echo "$fruit: ${fruits[$fruit]}"
done

# Get the number of elements in the array
echo "Total number of fruits: ${#fruits[@]}"