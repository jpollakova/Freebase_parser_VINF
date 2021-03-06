import re
import gzip
import os.path


with gzip.open('C:/Users/janep/Desktop/Škola/ING/1.ročník/1.semester/VINF/fb2w.nt.gz','rt',encoding="utf-8") as f:
    x = 0    
    #wiki_mappings = open('wikipage_mappings.txt','ab')
    wiki_mappings = open('PARSED_DATA/wikipage_mappings.txt', 'w', encoding="utf-8")

    for line in f:
        x = x + 1

        if x % 1000000 == 0:
            print(x)

        match = re.search('sameAs *>',line)
        if match:
            y = re.search('/ns/[m|g]\.', line)
            if y:
                wiki_mappings.write(line[y.span()[0] + 4:re.search('>', line).span()[0]] + ',')
                line = line[re.search('http:\/\/www.wiki',line).span()[0]:]
                line = line[:re.search('>',line).span()[0]]
                wiki_mappings.write(line + '\n')
            continue

        