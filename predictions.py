from tokenization import tokenize
from probabilites import calc_probabilities
import random
import matplotlib.pyplot as plt

def predict_next(n, ngram_probs, seed_text=None, max_words=20):

    if seed_text is None:
        seed_text = input('Enter a sequence of words: ')

    tokens = seed_text.lower().strip().split()
    
    for i in range(max_words - len(tokens)):
        if len(tokens) < n - 1:
            context = tuple(tokens)
        else:
            context = tuple(tokens[-(n-1):])

        next_words = {ngram[-1]: prob for ngram, prob in ngram_probs.items() if ngram[:-1] == context}

        if not next_words:
            break  # No continuation available

        # Plot the probabilities
        plot_next_word_probabilities(next_words, context, i + 1)

        next_word = sample_next_word(next_words)
        tokens.append(next_word)

    generated_text = ' '.join(tokens)
    print("Generated text:", generated_text)

    return generated_text


def sample_next_word(next_words):
    # next_words: dict mapping word to probability
    words = list(next_words.keys())
    probs = list(next_words.values())
    # Normalize probabilities
    total = sum(probs)
    probs = [p / total for p in probs]
    # Randomly select based on probability
    return random.choices(words, weights=probs, k=1)[0]

def plot_next_word_probabilities(next_words, context, step_number):
    """
    Plots a bar chart of the probabilities of the next word, given a context.
    """
    sorted_next_words = sorted(next_words.items(), key=lambda item: item[1], reverse=True)
    words, probabilities = zip(*sorted_next_words)

    plt.figure(figsize=(10, 6))
    plt.bar(words, probabilities)
    plt.xlabel("Next Word")
    plt.ylabel("Probability")
    plt.title(f"Step {step_number}: Next Word Probabilities for Context: '{' '.join(context)}'")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the plot to a file
    plt.savefig(f"step_{step_number}_probabilities.png")
    plt.close() # Close the plot to avoid displaying it in interactive environments
    print(f"Plot saved to step_{step_number}_probabilities.png")
