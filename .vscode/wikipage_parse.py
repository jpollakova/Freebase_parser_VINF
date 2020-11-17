import re
import gzip
import os.path



with gzip.open('C:/Users/janep/Desktop/Škola/ING/1.ročník/1.semester/VINF/fb2w.nt.gz','rt',encoding="utf-8") as f:
    x = 0    
    skuska = open('skuska.txt','ab')

    for line in f:
        x = x + 1

        skuska.write(line.encode('utf-8'))

        #if x == 10000000000 :
        #    break
        if x % 1000000 == 0:
            print(x)