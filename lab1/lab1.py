import collections
import math
import matplotlib.pyplot as plt

def calculate_entropy(text):
    counter = collections.Counter(text)
    total_chars = len(text)
    entropy = -sum((freq / total_chars) * math.log2(freq / total_chars) for freq in counter.values())
    return entropy

def load_and_clean_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    text = ''.join(filter(str.isalnum, text)) 
    return text.lower()

def plot_entropy(texts, labels):
    sizes = [len(text) for text in texts]
    entropies = [calculate_entropy(text) for text in texts]
    
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, entropies, marker='o', linestyle='-', color='b')
    plt.xlabel('Text size (number of characters)')
    plt.ylabel('Entropy (bits per character)')
    plt.title('Graph of entropy dependence on text size')
    plt.xticks(sizes, labels)
    plt.grid(True)
    plt.show()


ukr_text = load_and_clean_text('ukrainian.txt')
eng_text = load_and_clean_text('english.txt')
chi_text = load_and_clean_text('chinese.txt')


entropy_ukr = calculate_entropy(ukr_text)
entropy_eng = calculate_entropy(eng_text)
entropy_chi = calculate_entropy(chi_text)


print(f'Entropy of Ukrainian text: {entropy_ukr:.4f}')
print(f'Entropy of English text: {entropy_eng:.4f}')
print(f'Entropy of Chinese text: {entropy_chi:.4f}')


plot_entropy([ukr_text, eng_text, chi_text], ['Ukrainian', 'English', 'Chinese'])
