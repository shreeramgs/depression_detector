# Data-Challenge-2022-UB

### Description :
Accurate intervention of suicidal ideation and behavior in depressed people can help them get the therapeutic help and care they need, which can save their lives in many scenarios. The goal is to precisely anticipate data in order to avert incidents such as suicide and to assist people in overcoming depression. 

### Formulation: 
1.	Creation of a dataset from Twitter and Reddit that suicidal thought intention.
2.	Preprocess sentences and identify new features from textual data.   
3.	Make use of deep learning approaches such as RNN, CNN-LSTM and pre-trained models like BERT to classify text. 

### Dataset: 
We develop a primary dataset to help us figure out whether someone is suicidal or depressed. This information was taken from the Reddit. We collect data from parts of the internet using the Python Reddit API. We scrape from subreddits that relate to depression and suicidal thoughts. We also make use of Twitter API to collect tweets that were tagged suicidal. The dataset has two columns, the text and column indicating suicide or not. 

### Preprocessing and Feature Extraction: 
Text data require lot of preprocessing before they could be analyzed or modelled. We would perform following techniques to make the dataset usable. 

*	Remove non-English words
*	Remove mentions, hashtags, external links 
*	Remove stop words
*	Stemming, Lemmatization

The features following are used to model the data. 
*	Unigrams, Bigrams 
*	Length and Count 
*	Part of Speech Count (noun, adverbs, adjectives)
*	TF-IDF (term frequency-inverse document frequency  can quantify the importance or relevance of string representations in a document amongst a collection of documents)
*	LWIC  Linguistic Inquiry and Word Count (labels reflecting psychological state of the author)
*	Sentiment level of the author.

### Modeling:
Suicidal text detection is a supervised binary classification problem. For every text, in the database, a binary valued variable y ∈ {0, 1} is introduced, where y = 1 denotes that the text exhibits Suicidal Ideation. We have planned to use machine learning based approaches like SVM, XGBoost to classify texts. Accuracy, Precision, Recall and F-1 Score are the evaluation metrics used for comparison.

### Output:
Create a web-app where users have the option to check if the text is suicidal or not. Develop a API so that 3rd party websites can make use of the model. 
