import string
from collections import Counter

def most_common_word(paragraph):
    # Convert to lowercase
    paragraph = paragraph.lower()
    # Remove punctuation
    paragraph = paragraph.translate(str.maketrans('', '', string.punctuation))
    # Split into words
    words = paragraph.split()
    # Count word frequencies
    word_counts = Counter(words)
    # Find the most common word
    if word_counts:
        return word_counts.most_common(1)[0][0]
    else:
        return None