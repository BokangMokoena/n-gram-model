from n_gram import n_grams
from probabilites import calc_probabilities
from predictions import predict_next
from nltk.corpus import brown

# this is the main function of the project
def main():
    n = 3
    
    # Get tokens from the Brown Corpus and convert to lowercase
    print("Loading Brown Corpus...")
    tokens = [word.lower() for word in brown.words()]
    print("Corpus loaded.")

    # Generate and print n-grams
    n_tuples = n_grams(tokens, n)

    # Calculate the n-gram probabilities
    ngram_probs = calc_probabilities(n_tuples)

    # get input and predict next word
    predict_next(n, ngram_probs)


main()
