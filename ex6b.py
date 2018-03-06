import string
def main():
    phrase=input("Put in phrase here: ")
    separate(phrase)
    combine(phrase)
def separate(phrase):
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    newphrase=''
    oldphrase=''
    count=0
    for iterator in phrase:
        if iterator in uppercase:
            newphrase+=iterator
            print(newphrase)
        else:
            oldphrase+=iterator
            print(oldphrase)

            #if
def combine(phrase):
    phrase=phrase.title()
    translator = phrase.maketrans('', '', string.whitespace)
    phrase=phrase.translate(translator)
    print(phrase)
if __name__=="__main__":
    main()
