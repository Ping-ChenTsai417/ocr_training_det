import json
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.patches as patches

# Path to the image
#image_path = 'dataset/icdar2015/text_localization/icdar_c4_train_imgs/img_61.jpg'
image_path = './dataset/VAT/vat_train_imgs/22.jpg'

# Bounding box data
bbox_data = '''[
{"transcription":"###","points":[[87,24],[349,24],[349,77],[87,77]]}, {"transcription":"###","points":[[632,452],[758,452],[758,503],[632,503]]}, {"transcription":"###","points":[[661,500],[770,500],[770,550],[661,550]]}, {"transcription":"###","points":[[870,478],[1079,490],[1077,528],[869,518]]}]'''

# Parse the bounding box data
boxes = json.loads(bbox_data)

# Open the image
img = Image.open(image_path)
fig, ax = plt.subplots(1)

# Display the image
ax.imshow(img)

# Add bounding boxes
for box in boxes:
    points = box['points']
    polygon = patches.Polygon(points, closed=True, linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(polygon)

    # Optionally add the transcription text
    transcription = box['transcription']
    if transcription != "###":
        x, y = points[0]
        ax.text(x, y, transcription, color='blue', fontsize=12, verticalalignment='top')

# Show the plot with bounding boxes
plt.show()

