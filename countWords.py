def count_words(sentence):
    '''
    this function takes in a string and counts the number of words present in that string.

    INPUT: {
        sentence = a type string of words or 1 word.
    }
    OUTPUT: {
        returns a count of words in that string (type int).
    }
    '''

    word_list = sentence.split()
    return len(word_list)


if __name__ == '__main__':

    user_sentence = input('Hello, please type in a text to return the word count.\n')

    print(count_words(user_sentence))
