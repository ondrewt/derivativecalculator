import string
def igpay(pigmouth):
    v="aeiouyAEIOUY"
    cap="BCDEFGHIJKLMNPQRSTVWXZ"
    pigmouth=pigmouth.split()
    piglet=[]
    for word in pigmouth:
        word=str(word)
        if word[0] in v:
            word+='way'
            piglet.append(word)
        else:
            lettercounter=0
            while lettercounter<len(word):
                if word[lettercounter] in v:
                    cut=word[:lettercounter]
                    lettercounter+=10000
                    for i in range(len(cut)):
                        word=list(word)
                        if word[0] not in v:
                            word.pop(0)
                        else:
                            lettercounter+=10000
                    word=''.join(word)
                    word=word+cut
                lettercounter+=1
            word=word+'ay'
            for letter in word:
                if letter in cap:
                    word=word.lower()
                    word=word.title()
            piglet.append(word)
            translation=' '.join(piglet)
            print(translation)

        #print(piglet)

        #    lol=word[0]
        #    if lol in cap:
        #        word=word.lower()
        #        word=list(word)
        #        word.append(lol)
        #        word=''.join(word)
        #        word=word.title()
        #    else:
        #    word=list(word)
        #    word.pop(0)
        #    word.append(lol)
        #    word=''.join(word)
        #    word+='ay'
        #    piglet.append(word)
        #print(piglet)
    #count=0
