# Q: List the documents that does not contain any digit and any of the following character
# {:,",{,},(,),@,#,&}

import re
documents = ['asjghsdgsdf1287hgg:"sg()', 'asjhg****hagsghd', 'jhre876@']
regExp = '[^0-9:"(@{#})]'

for doc in documents:
    res = len(re.findall(regExp, doc))
    if res == len(doc):
        print(doc)

        