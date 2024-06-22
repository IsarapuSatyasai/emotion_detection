### Text Emotion Detection


<img src="emotion_detection.jpg" alt="screenshot of emotion level" />
Text emotion detection is a branch of natural language processing (NLP) that aims to identify and classify emotions expressed in written text. By analyzing linguistic cues, sentiment, and context, algorithms can categorize text into various emotional states such as happiness, sadness, anger, or fear. This technology finds applications in diverse fields, from customer feedback analysis to mental health monitoring and social media sentiment analysis.

Text emotion detection using logistic regression and multinomial Naive Bayes (MultinomialNB) with the Neattext module in Python involves utilizing machine learning algorithms to classify text into different emotional categories. Here's a breakdown:

1. **Logistic Regression**: Logistic regression is a statistical method used for binary classification problems. In text emotion detection, it can be adapted to handle multi-class classification by using techniques like one-vs-rest or multinomial logistic regression. It works by modeling the probability of each class as a logistic function.

2. **Multinomial Naive Bayes (MultinomialNB)**: MultinomialNB is a variant of the Naive Bayes algorithm that is well-suited for text classification tasks where the features are discrete word counts. It calculates the probability of a document belonging to a particular class based on the frequency of words in the document.

3. **Neattext Module**: Neattext is a Python library for text preprocessing and cleaning tasks. It provides functionalities to clean and preprocess text data efficiently, which is crucial for improving the performance of machine learning models. It can handle tasks like removing special characters, stop words, punctuation, and normalizing text.

Combining these elements, you would first preprocess your text data using the Neattext module to clean and prepare it for analysis. Then, you would use logistic regression or MultinomialNB algorithms to train a model on the preprocessed text data and its corresponding emotional labels. Finally, you can evaluate the model's performance and use it to predict emotions in new unseen text data.

This approach allows you to build a text emotion detection system in Python that can classify text into different emotional categories using logistic regression or MultinomialNB algorithms with the assistance of the Neattext module for text preprocessing. For deployment, I'm leveraging the Streamlit framework.
## Installation
Install all streamlit requirements by run the following command

> pip install requirements.txt

## Run Streamlit

To access and use the application,donwoload or clone the repository and then run the command below.
> streamlit run app.py

Lastly, open the provided link in your web browser.

## Access the Streamlit App

You can access the Streamlit app through the following link:
> [Streamlit App](http://13.234.112.53:8501/)
