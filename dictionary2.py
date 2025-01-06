def word_frequencies(sentence):
    
    words = sentence.lower().split()

    frequency = {}
    
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

sentence = "This is the girl, the girl i always tell you about."
frequencies = word_frequencies(sentence)

print(frequencies)
