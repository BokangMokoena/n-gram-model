from n_gram import n_grams
from probabilites import calc_probabilities
from predictions import predict_next
from nltk.corpus import brown
from nltk.data import find
from nltk import download
import sys

# this is the main function of the project
def main():

    try:
        find('corpora/brown') #Search for brown
        print("Brown corpus found")
        
    except LookupError:
        print("Brown corpus not found.")
        prompt_response = str(input("Automatically install (Y/N):")) #After not finding it prompt the user to download it
        
        if prompt_response != "Y" and prompt_response != "y":
            print("Please download Brown corpus to continue") #Option to not auto install but instead exit the programme
            sys.exit()
        else:
            download('brown') #NLTK Download
            print("Download complete") 
            #main() Previous print statement makes assumption that the download succeeded.
            
        
    # print('Welcome to Bokang\'s Language Model!')
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
