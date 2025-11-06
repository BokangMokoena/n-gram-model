#  this is where we will calculate probabilities for n-grams

def calc_probabilities(n_grams_list):
    total_ngrams = len(n_grams_list)
    ngram_freq = {}
    
    # calculates frequency of each n-gram
    for ngram in n_grams_list:
        if ngram in ngram_freq:
            ngram_freq[ngram] += 1
        else:
            ngram_freq[ngram] = 1
    
    # calculates probabilities
    ngram_probabilities = {ngram: freq / total_ngrams for ngram, freq in ngram_freq.items()}
    
    return ngram_probabilities