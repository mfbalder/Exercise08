f = open('combined.txt')
tracy = open('tracy.txt', "w")
for line in f:
    line = line.strip().split("    ")
    quote = line[1:]
    print quote
    if quote != []:
        tracy.write(quote[0])
    #print line[1:]



