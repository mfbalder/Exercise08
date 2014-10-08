def edit_30rock():
    f = open('combined.txt')
    tracy = open('tracy.txt', "w")
    for line in f:
        line = line.strip().split("    ")
        quote = line[1:]
        print quote
        if quote != []:
            tracy.write(quote[0])
        #print line[1:]

def edit_bigbang():
    f = open('big_bang.txt')
    new_f = open('bigbangtrek.txt', 'w')

    for line in f:
        line = line.replace('-', '')
        new_f.write(line)

edit_bigbang()



