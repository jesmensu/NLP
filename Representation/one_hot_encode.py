from sklearn.preprocessing import OneHotEncoder
import itertools

document = ["The","boy","sat","on","the","floor"]
# we have to convert these tokens to a dictionary with the key as word and value as position

tokens = [doc.split(" ") for doc in document]
print(tokens)
token_chain = itertools.chain.from_iterable(tokens)
word_to_id = {token: idx for idx, token in enumerate(set(token_chain))}

# word_to_id is our required dictionary
# Get the corresponding values for each word
token_ids = [[word_to_id[token] for token in toke] for toke in tokens]

vec = OneHotEncoder(categories="auto")
V = vec.fit_transform(token_ids)
print(V.toarray())
