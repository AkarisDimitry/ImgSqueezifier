# Batch Image Resizer

## Overview

This Python script offers a comprehensive utility for batch resizing of image files in a specified directory. It leverages the Python Imaging Library (PIL) for image manipulation and the `os` library for file and directory operations. The script provides functionalities for specifying target dimensions, file weight, and supports recursive directory resizing. Additionally, it includes an optional flag for the removal of original images after resizing.

## Installation

To install the required packages, run:

```bash
pip install Pillow
```

## Functionality Breakdown

### `resize_image()`

This function takes care of the core resizing task. It accepts the path of the image to be resized, the output path, target dimensions, target file weight, and an optional flag to remove the original image.

### `explore_directory()`

This function walks through the specified directory, identifies image files, and then calls `resize_image()` on each one. It can also optionally traverse subdirectories.

### Command-Line Arguments

- `--dir`: Specifies the directory to explore.
- `--recursive`: Optional flag to explore subdirectories.
- `--size`: Specifies the target dimensions as two integers.
- `--weight`: Specifies the target file weight in bytes.
- `--remove`: Optional flag to remove original images after resizing.

## Usage Examples

1. Resize images to 300x300 pixels:
   ```
   python script.py --dir my_images --size 300 300
   ```
   
2. Resize images to approximately 20,000 bytes:
   ```
   python script.py --dir my_images --weight 20000
   ```
   
3. Resize images in a directory and its subdirectories to 300x300 pixels:
   ```
   python script.py --dir my_images --size 300 300 --recursive
   ```
   
4. Resize images in a directory and its subdirectories to 20,000 bytes:
   ```
   python script.py --dir my_images --weight 20000 --recursive
   ```
   
5. Resize images to 300x300 pixels and a weight of 20,000 bytes:
   ```
   python script.py --dir my_images --size 300 300 --weight 20000
   ```

6. Remove original images after resizing:
   ```
   python script.py --dir my_images --size 300 300 --remove
   ```
   
7. Resize images to 400x400 pixels:
   ```
   python script.py --dir my_images --size 400 400
   ```
   
8. Resize images to approximately 25,000 bytes:
   ```
   python script.py --dir my_images --weight 25000
   ```
   
9. Resize images in a directory and its subdirectories, and remove originals:
   ```
   python script.py --dir my_images --size 300 300 --recursive --remove
   ```
   
10. Resize images to 200x200 pixels and approximately 15,000 bytes:
    ```
    python script.py --dir my_images --size 200 200 --weight 15000
    ```

## Additional Technical Notes

- The weight-based resizing is an approximation. It uses a linear extrapolation based on the original file size, which may not be precise due to compression algorithms.
- The script is designed to handle `.png`, `.jpg`, and `.jpeg` files by default. Further extensions
