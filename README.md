# General Overview
Train multilingual model xlmrobert on training data (originally english converted to 6 different languages used in testing data). Predict test data for each language then test predictions is the mean of these 6 languages. Train monolingual model for each of these 6 languages on training data and testing data with soft labels and predicted test data only in that language. Repeated this provess until no further improvement. Final prediction is mean predictions of xlmrobert trained on 6 different languages and 6 monolingual models.

## Models used




## Results

language| type of model | auc(private)|auc(public)|number of repetation
--- | --- | ---| ---|---
spanish|multilingual|0.9393|0.9389|0
french|multilingual|0.9369|0.9359|0
italian|multilingual|0.9374|0.9387|0
russian|multilingual|0.9353|0.9369|0
turkish|multilingual|0.9386|0.9390|0
portuguese|multilingual|0.9360|0.9361|0



## Ensemble Results

 number of repetation|auc(public)|auc(private)
 |---|--- | ---
 || | 
 
 
 
 ### Correrelaion among predictions of best models.
![alt text]()
