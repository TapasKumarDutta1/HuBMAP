# General Overview
Train multilingual model xlmrobert on training data (originally english converted to 6 different languages used in testing data). Predict test data for each language then test predictions is the mean of these 6 languages. Train monolingual model for each of these 6 languages on training data and testing data with soft labels and predicted test data only in that language. Repeated this provess until no further improvement. Final prediction is mean predictions of xlmrobert trained on 6 different languages and 6 monolingual models.

## Ensemble multilingual and monolingual Results

 number of repetation|auc(private)|auc(public)|used
 |---|---|---|---
 0|0.9449|0.9457|multilingual
 0|0.9261|0.9283|monolingual
 0|0.9459|0.9471|monolingual+multilingual
 0|0.9475|0.9485|multilingual+monolingual+multilingual+monolingual+multilingual+monolingual
 

## References
- https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification/discussion/160862
- https://huggingface.co/models
