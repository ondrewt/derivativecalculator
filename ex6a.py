import string
def wordlist(prose):
    prose=prose.lower()
    translator = prose.maketrans('', '', string.punctuation)
    prose=prose.translate(translator)
    prose=prose.split()
    uniquewords=[]
    prosecounter=0
    while prosecounter<len(prose):
        word=prose[prosecounter]
        if word in prose and word not in uniquewords:
                uniquewords.append(word)
                print(uniquewords)
        prosecounter+=1
