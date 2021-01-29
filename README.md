**General Overview**
Train multilingual model xlmrobert on training data (originally english converted to 6 different languages used in testing data). Predict test data for each language then test predictions is the mean of these 6 languages. Train monolingual model for each of these 6 languages on training data and testing data with soft labels and predicted test data only in that language. Repeated this provess until no further improvement. Final prediction is mean predictions of xlmrobert trained on 6 different languages and 6 monolingual models.

**Monolingual models**




## Results

language| type of model | auc(public)|auc(private)
--- | --- | ---| ---
spanish|monolingual||
french|monolingual||
italian|monolingual||
russian|monolingual||
turkish|monolingual||
portuguese|multilingual||
spanish|multilingual||
french|multilingual||
italian|multilingual||
russian|multilingual||
turkish|multilingual||
portuguese|multilingual||



## Ensemble Results

 number of repetation|auc(public)|auc(private)
 |---|--- | ---
 ||0.952 | 0.921
 
 
 
 ### Correrelaion among predictions of best models.
![alt text]()
