import gzip

import fileparsing

# This part of code opens the Freebase dump and reads the data by line. Each line is then checked by function for parsing.

with gzip.open('C:/Users/janep/Desktop/Škola/ING/1.ročník/1.semester/VINF/freebase-rdf-latest.gz','rt',encoding='utf8') as f:
    x = 0
    for line in f:
        x = x + 1
        key, match = fileparsing.parse_line(line)
        #if match != None:
            #print(line)
            #print(x , 'key: ', key, ' match: ', match)

        if x == 10000000 :
            break