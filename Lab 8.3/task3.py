def is_sentence_palindrome(sentence):
    """
    Checks if the given sentence is a palindrome, ignoring case, punctuation, and spaces.

    Args:
        sentence (str): The sentence to check.

    Returns:
        bool: True if the sentence is a palindrome, False otherwise.
    """
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in sentence if char.isalnum())
    return cleaned == cleaned[::-1]
