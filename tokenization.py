
import re

def tokenize(text):
    """
    Tokenizes the input text by converting to lowercase, removing punctuation,
    and splitting into words.
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Split into words
    tokens = text.split()
    
    return tokens
