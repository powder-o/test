from PIL import Image
import os

def convert_to_grayscale(image_path):
# Create output directory if it doesn't exist
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Load and convert image
img = Image.open(image_path).convert("L")

# Extract original filename
filename = os.path.basename(image_path)
output_path = os.path.join(output_dir, filename)

# Save the grayscale image
img.save(output_path)
print(f"Saved grayscale image to {output_path}")

def rotate_image_90(image_path):
# Create output directory if it doesn't exist
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Load and rotate image
img = Image.open(image_path)
rotated = img.rotate(-90, expand=True) # rotate clockwise

# Modify filename to indicate it's rotated
filename = os.path.basename(image_path)
name, ext = os.path.splitext(filename)
output_path = os.path.join(output_dir, f"{name}_rotated{ext}")

# Save the rotated image
rotated.save(output_path)
print(f"Saved rotated image to {output_path}")

# Example usage
image_path = input("Enter image path: ")
convert_to_grayscale(image_path)
rotate_image_90(image_path)

