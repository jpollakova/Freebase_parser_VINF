import re
import gzip
import os.path


with gzip.open('C:/Users/janep/Desktop/Škola/ING/1.ročník/1.semester/VINF/freebase-rdf-latest.gz','rb') as f:
    
    x = 0
    last_name = ''
    #skusobny = open('skusobny.txt', 'w', encoding="utf-8")

    #subory
    f_artist_id = open('artist_id.txt', 'w', encoding="utf-8")
    #f_artist_id.write(headerSwitcher('artist_id'))

    f_all_names = open('all_names.txt', 'w', encoding="utf-8")
    #f_all_names.write(headerSwitcher('all_names'))

    f_award_id = open('award_id.txt', 'w', encoding="utf-8")
    #f_award_id.write(headerSwitcher('award_id'))

    f_award_honor_id = open('award_honor_ids.txt', 'w', encoding="utf-8")
    #f_award_honor_id.write(headerSwitcher('award_honor_id'))

    f_award_honor_winner = open('award_honor_winner_id.txt', 'w', encoding="utf-8")
    #f_award_honor_winner.write(headerSwitcher('award_honor_winner'))

    #prechod freebasom
    for l in f:
        x = x + 1
        line = l.decode("utf-8")

        match = re.search('/type\.object\.name *>',line)
        if match:
            lang = line[line.find('@')+1:line.find('@')+3]
            if lang == 'en' or lang == 'es' or lang == 'sk':
                y = re.search('/ns/[m|g]\.', line)
                if y:
                    name = line[re.search('\"', line).span()[1] : re.search('\" *@', line).span()[0]]
                    if name == last_name:
                        continue
                    f_all_names.write(line[y.span()[0] + 4:re.search('>', line).span()[0]] + ',' + name + ',' + lang +'\n')
                    last_name = name
            
            continue

        match = re.search('/music\.artist *>',line)
        if match:
            y = re.search('/ns/[m|g]\.', line)
            if y:
                f_artist_id.write(line[y.span()[0] + 4:re.search('>', line).span()[0]] + '\n')

            continue

        match = re.search('\/award\.award_winner\.awards_won *>',line)
        if match:
            y = re.search('/ns/[m|g]\.', line)
            if y:
                f_award_id.write(line[y.span()[0] + 4:re.search('>', line).span()[0]] + ',')
                line = line[-20: -1]
                f_award_id.write(line[re.search('/ns/[m|g]\.', line).span()[0] + 4:re.search('>', line).span()[0]] + '\n')

            continue

        match = re.search('\/award\.award_honor\.award *>',line)
        if match:
            y = re.search('/ns/[m|g]\.', line)
            if y:
                f_award_honor_id.write(line[y.span()[0] + 4:re.search('>', line).span()[0]] + ',')
                line = line[-20: -1]
                f_award_honor_id.write(line[re.search('/ns/[m|g]\.', line).span()[0] + 4:re.search('>', line).span()[0]] + '\n')
            continue

        match = re.search('\/award\.award_honor\.award_winner *>',line)
        if match:
            y = re.search('/ns/[m|g]\.', line)
            if y:
                f_award_honor_winner.write(line[y.span()[0] + 4:re.search('>', line).span()[0]] + ',')
                line = line[-20: -1]
                f_award_honor_winner.write(line[re.search('/ns/[m|g]\.', line).span()[0] + 4:re.search('>', line).span()[0]] + '\n')
            continue
        

        if x == 1000000000 :
            break
        if x % 10000000 == 0:
            print(x)

f.close()
f_all_names.close()
f_award_honor_id.close()
f_artist_id.close()
f_award_honor_winner.close()
f_award_id.close()
