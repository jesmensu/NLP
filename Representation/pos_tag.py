import nltk
# nltk.download('averaged_perceptron_tagger')

text = 'Barack Obama was the president of the United States of America'
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
print(tokens)

from nltk.tag import pos_tag
pos_tags = pos_tag(tokens)
print(pos_tags)

# OUT: [('Barack', 'NNP'), ('Obama', 'NNP'), ('was', 'VBD'), ('the', 'DT'), ('president', 'NN'), ('of', 'IN'), ('the', 'DT'), ('United', 'NNP'), ('States', 'NNPS'), ('of', 'IN'), ('America', 'NNP')]

from nltk.chunk import RegexpParser
chunker = RegexpParser(r'''
NP:
{<DT><NN.*><.*>*<NN.*>}
}<VB.*>{
''')
chunker.parse(pos_tags)



