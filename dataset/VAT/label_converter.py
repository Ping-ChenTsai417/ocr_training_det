import json
import pandas as pd

# Path to the CSV file
csv_file_path = './dataset/VAT/label10.csv'

# Reading the CSV file
df = pd.read_csv(csv_file_path)

# Display the first few rows of the DataFrame
print(df.head())
print(df['region_shape_attributes'][0])
print(type(df['region_shape_attributes'][0]))

output_file_path = 'output.txt'
with open(output_file_path, 'a') as file:
    for j in range(10):
        image_path = 'vat_train_imgs/' + str(j+1) + '.jpg'
        annotations_list = []
        for i in range(4):
            idx = j*4+i
            dict_obj = json.loads(df['region_shape_attributes'][idx])
            
            if dict_obj['name'] == "rect":
                x = dict_obj['x']
                y = dict_obj['y']
                width = dict_obj['width']
                height = dict_obj['height']


                points = [
                    [x, y],
                    [x + width, y],
                    [x + width, y + height],
                    [x, y + height]
                ]
            elif dict_obj['name'] == "polygon":
                x1, x2, x3, x4 = dict_obj['all_points_x']
                y1, y2, y3, y4 = dict_obj['all_points_y']
                points = [
                    [x1, y1],
                    [x2, y2],
                    [x3, y3],
                    [x4, y4]
                ]
                

            data = {
                "transcription": "###",
                "points": points
            }

            json_string = json.dumps(data, separators=(',', ':'))

            annotations_list.append(json_string)
            # Print the JSON string
            #print(json_string)
            #print(type(json_string))

        #annotations_json = json.loads(annotations)
        annotations_json = "[" + ", ".join(str(item) for item in annotations_list) + "]"
        output_string = f'{image_path}\t{annotations_json}'
        file.write(output_string + '\n')
        print(output_string)

# Step 4: Save the JSON string to a file
#with open('data.json', 'w') as json_file:
#    json.dump(data, json_file, indent=4)

