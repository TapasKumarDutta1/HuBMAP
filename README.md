## Overview

![alt text](overview_of_submission.jpg)

Utilizing metadata comprising x and y coordinates, the provided samples were amalgamated to generate a `Reconstructed Original Image`. Each sample was processed to extract a contextual window of 512 units in both dimensions, unless proximity to the image boundary necessitated a larger contextual area on the opposite side. This resulting composition is denoted as the `Image with Global Information`.

A predictive model was subsequently employed to generate a segmentation mask for the `Image with Global Information`, henceforth termed as `Global Information Mask`. Further refinement was achieved by isolating the region of interest based on x and y coordinates in metadata, yielding the `Mask of Region of Interest`. This strategic integration of global information substantiates the precision of the predictive outcome.

The implementation also embraced advanced techniques such as test time augmentation and ensembling to enhance the model's performance, thereby exemplifying a comprehensive approach to refining predictive accuracy.

## Training Overview

Trained the model for each `wsi` reconstructed image with 3 for training and 1 for validation by taking a slice of 1536 x 1536 such that 10% of the image has segmentation mask if not select other slice. 

## Inference Overview

The model was trained iteratively, yielding four distinct training and validation sets. During the prediction phase, the most probable class was inferred from multiple augmentations for each unique model. The culmination of the four models involved determining the most probable class for every pixel. Subsequently, instances were segmented using the `cv2.connectedComponentsWithStats` method, with the prediction score for each instance being calculated as the average of the prediction scores attributed to individual pixels.
