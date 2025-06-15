from PIL import Image

def rotate_image(image_path, degrees):
    """
    Rotate an image by specified degrees and save it as a new file.
    
    Args:
        image_path (str): Path to the input image file
        degrees (int): Degrees to rotate the image (positive for clockwise)
    """
    # Open the image file
    image = Image.open(image_path)
    
    # Rotate the image by the specified degrees
    rotated_image = image.rotate(degrees)
    
    # Save the rotated image with a new filename
    rotated_image.save("rotated_image.jpg")
    
    # Print confirmation message
    print("Image rotated and saved as rotated_image.jpg")

# Example usage with the CityU test image
rotate_image("cityU_test_image.jpg", 90)
