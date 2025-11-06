# this is the function that puts the tokens into tuples of length n

def n_grams(tokens, n):
    n_grams_list = []
    for i in range(len(tokens) - n + 1):
        n_gram = tuple(tokens[i:i + n])
        n_grams_list.append(n_gram)
    return n_grams_list