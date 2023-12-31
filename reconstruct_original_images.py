# -*- coding: utf-8 -*-
"""reconstruct_original_images.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iny-pnRZ2vUOU6L9TZ1qpeval5IrV9-m
"""

import os
from tqdm import tqdm
import numpy as np
import cv2
import warnings

# Suppressing warnings for a cleaner output
warnings.filterwarnings("ignore")

# Creating a directory to store the final images
os.mkdir("big_ones")

# Reading the metadata CSV file
df = pd.read_csv("/kaggle/input/hubmap-hacking-the-human-vasculature/tile_meta.csv")

# Grouping and processing data based on the source WSI
for wsi, group in df.groupby(['source_wsi']):
    # Sorting data based on spatial coordinates
    group = group.sort_values(by=['i', 'j'])

    # Adjusting spatial coordinates to ensure they start from 0
    group['i'] = group['i'] - min(group['i'])
    group['j'] = group['j'] - min(group['j'])

    # Determining maximum spatial dimensions
    max_x = group['i'].max()
    max_y = group['j'].max()

    # Creating an expanded canvas for composite image
    big_one = np.zeros((max_y + 512, max_x + 512, 3))

    # Iterating over each element in the group and positioning them in the canvas
    for idx, row in enumerate(tqdm(group.iterrows())):
        path = '/kaggle/input/hubmap-hacking-the-human-vasculature/test/' + row[1]['id'] + '.tif'
        if os.path.isfile(path):
            img = cv2.imread(path)
            x, y = row[1]['i'], row[1]['j']
            big_one[y:y + 512, x:x + 512, :] = img

    # Validating whether the canvas contains data
    if np.sum(big_one) > 0:
        # Saving the composite image in an organized manner
        cv2.imwrite("big_ones/" + str(wsi) + '.jpg', big_one)