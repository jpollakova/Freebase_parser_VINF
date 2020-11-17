import re
import gzip
import os.path


# Regex dictionary - there are regexes for parsing data related to artist and their awards. Each regular expression
# (except 'artis_id') includes group for subject and object - this makes easier to write these data to textfiles.

rx_dict = {
    'artist_id':re.compile('\/(?P<subject>[gm]\..+)>.+<.+>.+\/music\.artist *>'),
    'award_id':re.compile('\/(?P<subject>[gm]\..+)>.+\/award\.award_winner\.awards_won *>.+\/(?P<object>[gm]\..+)>'),
    'award_honor_id':re.compile('\/(?P<subject>[gm]\..+)>.+\/award\.award_honor\.award *>.+\/(?P<object>[gm]\..+)>'),
    'name':re.compile('\/(?P<subject>[gm]\..+)>.+((\/type\.object\.name)|(label)) *>.+\"(?P<object>.+)\".*@(?P<lang>[a-zA-Z]{1,})'),
    'award_honor_winner': re.compile('\/(?P<subject>[gm]\..+)>.+\/award\.award_honor\.award_winner *>.+\/(?P<object>[gm]\..+)>')

}


def headerSwitcher(key):
    switcher = {
        'artist_id': 'artist_id\n',
        'award_id': 'artist_id,award_id\n',
        'award_honor_id': 'award_id,award_honor_id\n',   # medzikrok
        'all_names': 'subject,name,lang\n',
        'award_honor_winner' : 'award_honor_id, award_honor_winner_id\n'
    }
    return switcher.get(key, 'Invalid key!')


with gzip.open('C:/Users/janep/Desktop/Škola/ING/1.ročník/1.semester/VINF/freebase-rdf-latest.gz','rb') as f:
    
    x = 0
    last_name = '', ''
    delimiter = ','
    FBsubject,FBobject,lang = '','',''

    #subory
    f_artist_id = open('artist_id.txt', 'w', encoding="utf-8")
    f_artist_id.write(headerSwitcher('artist_id'))

    f_all_names = open('all_names.txt', 'w', encoding="utf-8")
    f_all_names.write(headerSwitcher('all_names'))

    f_award_id = open('award_id.txt', 'w', encoding="utf-8")
    f_award_id.write(headerSwitcher('award_id'))

    f_award_honor_id = open('award_honor_ids.txt', 'w', encoding="utf-8")
    f_award_honor_id.write(headerSwitcher('award_honor_id'))

    f_award_honor_winner = open('award_honor_winner_id.txt', 'w', encoding="utf-8")
    f_award_honor_winner.write(headerSwitcher('award_honor_winner'))


    #prechod freebasom
    for l in f:
        x = x + 1
        line = l.decode("utf-8")

        for key, rx in rx_dict.items():
            match = rx.search(line)

            if match:
                FBsubject = match.group('subject')

                if key != 'artist_id':                
                    FBobject = match.group('object')
                    if key == 'name':
                        lang = match.group('lang')

                if key == 'artist_id':
                    f_artist_id.write(FBsubject + '\n')
                
                if key == 'name':
                    if lang!='en' and lang!='es' and lang!='sk':
                        continue
                    if FBobject == last_name:
                        continue
                    key = 'all_names'
                    f_all_names.write(FBsubject + delimiter + FBobject + delimiter + lang + '\n')
                    last_name = FBobject
                

                if key == 'award_id':
                    f_award_id.write(FBsubject + delimiter + FBobject + '\n')

                if key == 'award_honor_id':
                    f_award_honor_id.write(FBsubject + delimiter + FBobject + '\n')

                if key == 'award_honor_winner':
                    f_award_honor_winner.write(FBsubject + delimiter + FBobject + '\n')

        

        if x == 1000000000 :
            break
        if x % 10000000 == 0:
            print(x)


f_award_honor_winner.close()
f_all_names.close()
f_artist_id.close()
f_award_id.close()
f_award_honor_id.close()
