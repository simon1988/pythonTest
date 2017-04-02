import re


def print_statistics(text):
    n_sentences = len(re.findall(r'[\.?!:]', text))
    words = re.findall(r'[\w\-\']+', text)
    n_words = len(words)
    n_complex_words = len([word for word in words if len(word) >= 5 and len(re.findall(r'[aeiou]', word)) >= 2])
    average_words_per_sentence = n_words / n_sentences
    fog_index = 0.4 * average_words_per_sentence + 100 * (n_complex_words / n_words)

    print('The fog index is', str(fog_index))
    print('The total number of words is {0} and sentences in the document is {1}'.format(n_words, n_sentences))
    print('The average number of words per sentence is', str(average_words_per_sentence))
    print('The fog index per sentence is', str(fog_index / n_sentences))


def calculate_fog(file):
    with open(file, 'r') as f:
        print('Calculating fog index for file', file, '...')
        print_statistics(f.read())


calculate_fog('test.txt')
