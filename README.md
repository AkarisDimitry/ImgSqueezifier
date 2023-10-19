<img src="https://github.com/AkarisDimitry/ImgSqueezifier/assets/34775621/0468430a-58e6-4a69-af9f-f1b10f280a90" alt="DALL·E 2023-10-19 04 48 03 - Photo logo" width="200" height="200">
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

## C++ Version

### Installation

#### Windows

1. Install OpenCV using the official [OpenCV for Windows Guide](https://docs.opencv.org/master/d3/d52/tutorial_windows_install.html).
2. Configure your project to include the OpenCV headers and libraries. You can use CMake or directly configure it in your IDE.

#### Ubuntu

1. Open a terminal and run:

   ```bash
   sudo apt-get update
   sudo apt-get install libopencv-dev
   ```

#### macOS

1. Install Homebrew if you haven't:

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. Install OpenCV:

   ```bash
   brew install opencv
   ```

### Compilation

#### Windows

1. Open your IDE and configure the project to use OpenCV.
2. Build the project.

#### Ubuntu

1. Open a terminal and navigate to the directory containing your C++ file.
2. Run:

   ```bash
   g++ your_file.cpp -o output_name `pkg-config --cflags --libs opencv4`
   ```

#### macOS

1. Open a terminal and navigate to the directory containing your C++ file.
2. Run:

   ```bash
   g++ your_file.cpp -o output_name `pkg-config --cflags --libs opencv4`
   ```

### Usage

Replace the placeholders in the `main()` function with appropriate command-line arguments (this part is to be implemented).

1. To execute the program, run:

   ```bash
   ./output_name
   ```

#### Examples

Usage examples remain similar to the Python version; however, the command-line argument parsing is yet to be implemented in the C++ version.
