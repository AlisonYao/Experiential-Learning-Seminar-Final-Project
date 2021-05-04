from collections import defaultdict, Counter
import os
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk import word_tokenize, sent_tokenize, FreqDist
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
# https://becominghuman.ai/nlp-for-beginners-using-nltk-f58ec22005cd


def wordFreq(directory, k):
    ### read all txt files in the directory
    txtPaths = []
    for filename in os.listdir(directory):
        if '.txt' in filename:
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                txtPaths.append(os.path.join(directory, filename))
    assert len(txtPaths) > 0
    print('#txt:', len(txtPaths))

    ### loop through all txt files
    allTxt = ''
    for txtPath in txtPaths:
        file1 = open(txtPath, 'r')
        allText = file1.readlines()
        if len(allText) > 0:
            print('ACCESSING:', txtPath)
            transcript = [allText[2].strip('\n')]
            for line in allText[3:]:
                line = line[6:].strip('\n')
                transcript.append(line)
            transcriptStr = ' '.join(transcript)
            allTxt += transcriptStr

    ### data cleaning
    transcriptTokens = word_tokenize(allTxt.lower())
    print('#transcriptTokens:', len(transcriptTokens))
    transcriptTokensLemmatized = [lemmatizer.lemmatize(word) for word in transcriptTokens]
    transcriptTokensLemmatizedCleaned = [word for word in transcriptTokensLemmatized if word not in allStopwords + meaninglessWords]
    print('#transcriptTokensLemmatizedCleaned:', len(transcriptTokensLemmatizedCleaned))
    for i in range(len(transcriptTokensLemmatizedCleaned)):
        if transcriptTokensLemmatizedCleaned[i] == 'making':
            transcriptTokensLemmatizedCleaned[i] = 'make'
        elif transcriptTokensLemmatizedCleaned[i] == 'learning':
            transcriptTokensLemmatizedCleaned[i] = 'learn'
    # getting frequency & output
    freq = FreqDist(transcriptTokensLemmatizedCleaned)
    print(type(freq), freq.most_common(100))
    return freq.most_common(k)

def visulization(l):
    words, frequencies = [], []
    for word_frequency in l:
        word, frequency = word_frequency
        words.append(word)
        frequencies.append(frequency)
    print(words)
    print(frequencies)
    plt.bar(words, frequencies)
    plt.show() 


if __name__ == '__main__':
    directory = './data'
    allStopwords = stopwords.words('english')
    lemmatizer = WordNetLemmatizer()
    meaninglessWords = ['.', ',', "'s", "'re", "'d", "'ve", ":", "'m", "n't", "?", "like", '’', ')', '(', 'also', 'data', 'scientist', 'science', 'company', 'thing', 'people', 'think', 'really', 'get', 'one', 'would', 'also', 'work', 'working', 'might', 'job', 'go', '”', '“', 'could', 'wa', 'lot', 'something', 'need', 'want', 'actually', 'startup', 'take', 'say', 'kind', 'even', 'much', 'going', 'ha', 'u', 'know', 'probably', 'may', 'got', 'today', 'bit', 'two', 'yeah', 'yea', 'use', 'course', 'thank']
    mostFreqPairs = wordFreq(directory, 10)
    visulization(mostFreqPairs)
