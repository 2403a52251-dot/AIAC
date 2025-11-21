import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

data = {
    'post_id': [1,2,3,4,5],
    'text': [
        "I love this product!  Check it out: https://example.com",
        "Worst service ever!! #fail ",
        "Not bad, could be better... ",
        "Totally amazing experience!!! @brand",
        "Meh... it's okay. http://test.com "
    ]
}

df = pd.DataFrame(data)
print("Original Dataset:")
print(df)

def clean_text(text):
    # Remove URLs
    text = re.sub(r'http\S+|www.\S+', '', text)
    # Remove mentions and hashtags
    text = re.sub(r'@\w+|#\w+', '', text)
    # Remove emojis and special characters
    text = re.sub(r'[^\w\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    return text

df['clean_text'] = df['text'].apply(clean_text)

stop_words = set(stopwords.words('english'))
df['tokens'] = df['clean_text'].apply(lambda x: [word for word in x.split() if word not in stop_words])

lemmatizer = WordNetLemmatizer()
df['lemmatized'] = df['tokens'].apply(lambda x: [lemmatizer.lemmatize(word) for word in x])

df['processed_text'] = df['lemmatized'].apply(lambda x: ' '.join(x))

print("\nProcessed Dataset:")
print(df[['post_id','processed_text']])

df.to_csv('social_media_cleaned.csv', index=False)
