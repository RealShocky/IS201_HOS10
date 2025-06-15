# HOS10 - Manipulating Images and GUI Automation

## Overview
This project demonstrates image manipulation using Python's Pillow (PIL) module. The assignment focuses on learning how to programmatically rotate images and save them with new filenames.

## Learning Objectives
- Manipulate images with Python's Pillow module
- Understand RGBA color values and image properties
- Implement image rotation functionality
- Save processed images to disk

## Prerequisites
- Python 3.x installed
- Pillow module installed (`pip install Pillow`)

## Project Structure
```
PE09/HOS10/
├── HOS10.py                    # Main Python script
├── README.md                   # This documentation file
├── cityU_test_image.jpg        # Test image with graphics and text
├── rotated_image.jpg           # Output: 90-degree rotated image
└── test_image.jpg              # Simple red square test image
```

## Installation
1. Ensure Python is installed on your system
2. Install the required Pillow module:
   ```bash
   pip install Pillow
   ```

## Usage
Run the main script to rotate an image:
```bash
python HOS10.py
```

The script will:
1. Open the test image (`cityU_test_image.jpg`)
2. Rotate it 90 degrees clockwise
3. Save the rotated image as `rotated_image.jpg`
4. Print a confirmation message

## Code Explanation

### Main Function: `rotate_image(image_path, degrees)`
```python
def rotate_image(image_path, degrees):
    """
    Rotate an image by specified degrees and save it as a new file.
    
    Args:
        image_path (str): Path to the input image file
        degrees (int): Degrees to rotate the image (positive for clockwise)
    """
    # Open the image file using PIL
    image = Image.open(image_path)
    
    # Rotate the image by the specified degrees
    rotated_image = image.rotate(degrees)
    
    # Save the rotated image with a new filename
    rotated_image.save("rotated_image.jpg")
    
    # Print confirmation message
    print("Image rotated and saved as rotated_image.jpg")
```

### Key Features
- **Image Loading**: Uses `Image.open()` to load image files
- **Image Rotation**: Uses `image.rotate()` method for rotation
- **Image Saving**: Uses `rotated_image.save()` to save processed images
- **Error Handling**: Basic file operations with PIL

## Test Images
The project includes two test images:

1. **cityU_test_image.jpg**: A colorful 400x300 image featuring:
   - Light blue background
   - Red rectangle with black border
   - Yellow circle with green border
   - Purple polygon shape
   - Text labels demonstrating PIL capabilities

2. **test_image.jpg**: A simple 200x200 red square for basic testing

## Expected Output
When you run the program, you should see:
```
Image rotated and saved as rotated_image.jpg
```

The rotated image will be saved in the same directory as the script.

## Customization
You can modify the script to:
- Use different input images by changing the filename in the function call
- Rotate by different angles (e.g., 45, 180, 270 degrees)
- Save with different output filenames
- Add additional image processing operations

## Example Variations
```python
# Rotate by different angles
rotate_image("cityU_test_image.jpg", 45)   # 45 degrees
rotate_image("cityU_test_image.jpg", 180)  # 180 degrees
rotate_image("cityU_test_image.jpg", 270)  # 270 degrees

# Use your own image
rotate_image("my_photo.jpg", 90)
```

## Assignment Requirements Met
✅ Created Python file named HOS10.py  
✅ Installed Pillow module  
✅ Downloaded/created test images  
✅ Implemented rotate_image() function  
✅ Successfully rotated and saved images  
✅ Demonstrated image manipulation with Python  

## Course Information
- **Course**: IS201 Fundamentals of Computing
- **Assignment**: HOS10 Manipulating Images and GUI Automation
- **Institution**: City University of Seattle (CityU)
- **School**: School of Technology & Computing (STC)

## Author
Mark Varkevisser

## Resources
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- [Pillow Documentation](https://pillow.readthedocs.io/)
- [Python PIL Tutorial](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html)
