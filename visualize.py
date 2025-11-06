
import matplotlib.pyplot as plt

def plot_next_word_probabilities(ngram_probs, context):
    next_words = {ngram[-1]: prob for ngram, prob in ngram_probs.items() if ngram[:-1] == context}

    if not next_words:
        print(f"No predictions found for context '{ ' '.join(context)}'")
        return

    # Sort the words by probability for a cleaner plot
    sorted_next_words = sorted(next_words.items(), key=lambda item: item[1], reverse=True)
    words, probabilities = zip(*sorted_next_words)

    plt.figure(figsize=(10, 6))
    plt.bar(words, probabilities)
    plt.xlabel("Next Word")
    plt.ylabel("Probability")
    plt.title(f"Next Word Probabilities for Context: '{' '.join(context)}'")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the plot to a file
    plt.savefig("next_word_probabilities.png")
    # print("Plot saved to next_word_probabilities.png")
