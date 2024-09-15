import streamlit as st
import joblib
# from sklearn.ensemble import RandomForestClassifier
import re
#model = joblib.load('spam_classifier_model.pkl')
# Load the model once

# Load the saved model
@st.cache(allow_output_mutation=True)  # Cache to avoid reloading the model multiple times
def load_model():
    model = joblib.load('spam_classifier_model.pkl')
    return model

# Load the model once
model = load_model()

#stop words
stop_words = {
    'a', 'about', 'above', 'after', 'again', 'against', 'ain', 'all', 'am', 'an', 'and', 'any', 'are', 'aren', "aren't",
    'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'couldn',
    "couldn't", 'd', 'did', 'didn', "didn't", 'do', 'does', 'doesn', "doesn't", 'doing', 'don', "don't", 'down',
    'during', 'each', 'few', 'for', 'from', 'further', 'had', 'hadn', "hadn't", 'has', 'hasn', "hasn't", 'have', 'haven',
    "haven't", 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into',
    'is', 'isn', "isn't", 'it', "it's", 'its', 'itself', 'just', 'll', 'm', 'ma', 'me', 'mightn', "mightn't", 'more',
    'most', 'mustn', "mustn't", 'my', 'myself', 'needn', "needn't", 'no', 'nor', 'not', 'now', 'o', 'of', 'off', 'on',
    'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 're', 's', 'same', 'shan', "shan't",
    'she', "she's", 'should', "should've", 'shouldn', "shouldn't", 'so', 'some', 'such', 't', 'than', 'that', "that'll",
    'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to',
    'too', 'under', 'until', 'up', 've', 'very', 'was', 'wasn', "wasn't", 'we', 'were', 'weren', "weren't", 'what', 'when',
    'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'won', "won't", 'wouldn', "wouldn't", 'y', 'you',
    "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves', 'guys', 'vid', 'vids', 'hey', 'u'
}

# Function to clean the comment (same logic as your clean_comment function)
def clean_comment(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\d+', '', text)
    text = text.lower()
    text = ' '.join([word for word in text.split() if word not in stop_words])
    text = re.sub(r'\s+', ' ', text).strip()
    return text

st.title("YouTube Spam Comment Classifier")
# Add a text input for entering the comment
comment = st.text_input("Enter a YouTube comment:")
# Add a slider to adjust the threshold
threshold = st.slider("Select the spam threshold", min_value=0.0, max_value=1.0, value=0.8)

# Info about the slider
url = "https://www.streamlit.io"
multi = '''Think of the threshold as a spam "confidence meter." The model looks at each comment and assigns it a probability score, indicating how likely it is to be spam.,
If the score is above the threshold you set, the comment will be flagged as spam. If it’s below the threshold, it won’t be.
'''
st.markdown(multi)
st.markdown("check out this [link](%s)" % url)
# Placeholder for prediction result
if comment.strip():
    # Clean the comment
    cleaned_comment = clean_comment(comment)
    
     # Make the prediction
    prediction_prob = model.predict_proba([cleaned_comment])[0][1]  # Get the probability of being spam
    
    # Set a threshold (you can change this value if needed)
    #threshold = 0.8
    result = "Spam" if prediction_prob > threshold else "Not Spam"
    st.success(f"This comment is {result}")
    #st.write(f"This comment is : {result}, with a prediction probability of {round(prediction_prob,2)}")
else:
    st.warning("Please enter a YouTube comment.")

#st.title("YouTube Spam Comment Classifier")
#st.write(f"Model Info: {model}")
#prediction_prob = model.predict_proba([cleaned_comment])[0][1]
#st.write(f"Prediction Probability: {prediction_prob}")
