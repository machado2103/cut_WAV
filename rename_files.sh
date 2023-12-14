#!/bin/bash

# Specify the folder path
folder_path="/home/pedro/Desktop/baby_crying"

# Specify the common base name
base_name="sample"

# Navigate to the folder
cd "$folder_path" || exit

# Counter for numerical suffix
counter=1

# Iterate through each file in the folder
for file in *; do
    # Check if the item is a file (not a directory)
    if [ -f "$file" ]; then
        # Create the new file name with the common base name and numerical suffix
        new_name="${base_name} (${counter})"

        # Rename the file
        mv "$file" "$new_name"

        # Increment the counter
        ((counter++))
    fi
done

echo "Files renamed successfully."

