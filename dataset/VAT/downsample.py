from PIL import Image

def downsample_image(input_image_path, output_image_path, size=(1280, 720)):
    # Open an image file
    with Image.open(input_image_path) as img:
        # Get image size
        width, height = img.size
        print(width, height)
        # Resize the image
        resized_img = img.resize(size, Image.Resampling.LANCZOS)
        width, height = resized_img.size
        print(width, height)
        # Save it back to disk
        resized_img.save(output_image_path)
        print(f"Image saved to {output_image_path}")

# Example usage
for i in range(889):
    input_image_path = './dataset/VAT/vat_train_imgs/'+str(i+1)+'.jpg'
    output_image_path = './dataset/VAT/vat_train_imgs/'+str(i+1)+'.jpg'
    downsample_image(input_image_path, output_image_path)

