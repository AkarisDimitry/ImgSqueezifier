# Import necessary modules
import os
from PIL import Image
import argparse

# Function to resize an individual image
def resize_image(image_path, output_path, target_size=None, target_weight=None, remove_original=False):
    # Open the image file
    img = Image.open(image_path)
    # Get the original file size in bytes
    original_weight = os.path.getsize(image_path)
    
    # If a target size is specified, resize the image
    if target_size is not None:
        img = img.resize(target_size)
    
    # If a target weight is specified, calculate the scaling factor
    if target_weight is not None:
        scale_factor = (target_weight / original_weight) ** 0.5  # Square root is used due to two dimensions
        # Calculate the new size based on the scaling factor
        new_size = tuple([int(dim * scale_factor) for dim in img.size])
        img = img.resize(new_size)
    
    # Save the resized image
    img.save(output_path)
    
    # If the remove_original flag is True, remove the original image
    if remove_original:
        os.remove(image_path)

# Function to explore a directory and resize images within it
def explore_directory(directory, recursive=False, target_size=None, target_weight=None, remove_original=False):
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for name in files:
            # Check for image files based on file extension
            if name.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(root, name)
                output_path = os.path.join(root, "resized_" + name)
                # Call the resize_image function on each image file
                resize_image(image_path, output_path, target_size, target_weight, remove_original)

        # If not recursive, break after the first level
        if not recursive:
            break

# Main function to handle command-line arguments
if __name__ == "__main__":
    # Initialize argument parser
    parser = argparse.ArgumentParser(description='Resize images in a directory.')
    # Define command-line arguments
    parser.add_argument('--dir', required=True, help='Directory to explore')
    parser.add_argument('--recursive', action='store_true', help='Whether to explore subdirectories')
    parser.add_argument('--size', nargs=2, type=int, help='Target size as two integers: width height')
    parser.add_argument('--weight', type=int, help='Target weight in bytes')
    parser.add_argument('--remove', action='store_true', help='Remove original images after resizing')
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
	# Example 1: Resize all images in the directory "my_images" to a size of 300x300 pixels
    # Usage: python script.py --dir my_images --size 300 300
    
    # Example 2: Resize all images in the directory "my_images" to approximately 20,000 bytes
    # Usage: python script.py --dir my_images --weight 20000
    
    # Example 3: Resize all images in the directory "my_images" and its subdirectories to a size of 300x300 pixels
    # Usage: python script.py --dir my_images --size 300 300 --recursive
    
    # Example 4: Resize all images in the directory "my_images" and its subdirectories to approximately 20,000 bytes
    # Usage: python script.py --dir my_images --weight 20000 --recursive
    
    # Example 5: Resize all images in the directory "my_images" to a size of 300x300 pixels and a weight of 20,000 bytes
    # Usage: python script.py --dir my_images --size 300 300 --weight 20000

    # Call the explore_directory function with parsed arguments
    explore_directory(args.dir, args.recursive, tuple(args.size) if args.size else None, args.weight, args.remove)
