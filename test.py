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

# Example usage
image_path = input("Enter image path: ")
convert_to_grayscale(image_path)
