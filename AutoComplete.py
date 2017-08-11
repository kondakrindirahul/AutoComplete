import datetime

word_list = []

def initialize():
    file = open('words.txt', 'r')
    for line in file:
        for word in line.split():
            word_list.append(word)

    #print(word_list[1:100])
    #print(len(word_list))

def autocomplete(partial_word):
    output_list = []
    for each_word in word_list:
        if str(each_word).startswith(partial_word):
            output_list.append(str(each_word))
            #print(str(each_word))
    output_list.sort(key=len)
    print(output_list)

if __name__ == '__main__':
    initialize()
    prefix = str(raw_input("enter a prefix"))
    print datetime.datetime.now()
    autocomplete(prefix)
    print datetime.datetime.now()

