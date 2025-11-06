def generate_text(seed_text, n, ngram_probs, max_words=20):

    tokens = seed_text.lower().strip().split()
    
    for _ in range(max_words):
        # Determine current context
        if len(tokens) < n - 1:
            context = tuple(tokens)
        else:
            context = tuple(tokens[-(n-1):])

        # Find next word candidates
        next_words = {ngram[-1]: prob for ngram, prob in ngram_probs.items() if ngram[:-1] == context}

        if not next_words:
            break  # no predictions, stop generation

        # Pick most probable next word
        next_word = max(next_words, key=next_words.get)
        tokens.append(next_word)

    return ' '.join(tokens)
