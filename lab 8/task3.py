def is_sentence_palindrome(sentence):
    """
    Checks if the given sentence is a palindrome, ignoring case, punctuation, and spaces.
    
    Args:
        sentence (str): The sentence to check.
        
    Returns:
        bool: True if the sentence is a palindrome, False otherwise.
    """
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in sentence if c.isalnum())
    return cleaned == cleaned[::-1]

    # INSERT_YOUR_CODE
    if __name__ == "__main__":
        user_input = input("Enter a sentence: ")
        if is_sentence_palindrome(user_input):
            print("Palindrome")
        else:
            print("Not a palindrome")
