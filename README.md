**Procedure**
Train multilingual model xlmrobert on training data (originally english converted to 6 different languages used in testing data). Predict test data for each language then test predictions is the mean of these 6 languages. Train monolingual model for each of these 6 languages on training data and testing data with soft labels and predicted test data only in that language. Final prediction is mean predictions of xlmrobert trained on 6 different languages and 6 monolingual models.

**Config. for training xlmrobert**



**Config. for training monolingual models**


**public leaderboard roc of each model ingividually**

**public leaderboard roc of ensembles**
