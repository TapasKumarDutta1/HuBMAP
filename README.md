## Overview

![alt text](submission_overview.jpg)

Combined the samples using metadata(x, y coordinates) to get `Reconstructed Original Image`. For each sample take global information of 512 in each direction if possible else more information in the opposite direction if sample is present near the edge of the `Reconstructed Original Image` this is referenced as `Image with Global Information`. Have the model predict the segmentation mask of this image this mask will be referred as `Global Information Mask`. From this image take mask of region of interest according to metadata this is referred as `Mask of Region of Interest`. Thus global information is incorporated in prediction. Used test time augmentation and ensembling to improve performance.
