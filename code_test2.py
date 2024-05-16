import json
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.patches as patches

# Path to the image
image_path = 'dataset/VAT/vat_train_imgs/1.jpg'
# Bounding box data in the provided format
bbox_data = '{"name":"rect","x":130,"y":12,"width":439,"height":109}'

# Parse the bounding box data
bbox = json.loads(bbox_data.replace('""', '"'))

# Open the image
img = Image.open(image_path)
fig, ax = plt.subplots(1)

# Display the image
ax.imshow(img)

# Extract the bounding box coordinates
x = bbox['x']
y = bbox['y']
width = bbox['width']
height = bbox['height']

# Create a rectangle patch
rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='r', facecolor='none')
ax.add_patch(rect)

# Show the plot with the bounding box
plt.show()
