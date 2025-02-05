def reverse_sentence(sentence):
    reversed_sentence = " ".join(sentence.split()[::-1])
    print(reversed_sentence)
sentence = str(input("enter a sentence: "))
reverse_sentence(sentence)