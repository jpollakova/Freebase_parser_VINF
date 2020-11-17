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

# The function returns string representing the name of the textfile according to key from regex.

def fileSwitcher(key):
    switcher = {
        'artist_id': 'artist_id.txt',
        'award_id': 'awards.txt',
        'award_honor_id': 'award_honor_ids.txt',  #medzikrok
        #'award_name': 'award_name.txt',
        #'name_en': 'artists_names_EN.txt',
        #'name_es': 'artists_names_ES.txt',
        #'name_sk': 'artists_names_SK.txt',
        'all_names': 'all_names.txt',
        'award_honor_winner' : 'award_honor_winner_id.txt'
    }
    return switcher.get(key, 'Invalid key!')

def headerSwitcher(key):
    switcher = {
        'artist_id': 'artist_id\n',
        'award_id': 'artist_id,award_id\n',
        'award_honor_id': 'award_id,award_honor_id\n',   # medzikrok
        #'award_name': 'award_honor_id,award_name\n',
        #'name_en': 'artist_id,name_en\n',
        #'name_es': 'artist_id,name_es\n',
        #'name_sk': 'artist_id,name_sk\n',
        'all_names': 'subject,name,lang\n',
        'award_honor_winner' : 'award_honor_id, award_honor_winner_id\n'
    }
    return switcher.get(key, 'Invalid key!')


# The function for parsing data and writing data to textfiles. The function gets the line and determines if there is 
# any match with our declared regexes. If so, the data are stored in the particular textfile. 
 
#last_name_es, last_name_sk, last_name_en,
last_music_artist_id, last_name = '', ''

delimiter = ','

def parse_line(line):

    FBsubject , FBobject = '',''  

    for key, rx in rx_dict.items():
        match = rx.search(line)
        if match:
                       
            FBsubject = match.group('subject')             

            if key == 'name':                
                #global last_name_es, last_name_sk, last_name_en, last_music_artist_id
                global last_name

                lang = match.group('lang')

                if lang!='en' and lang!='es' and lang!='sk':
                    continue
                if match.group('object') == last_name:
                    continue
                """
                if (lang == 'en' and last_name_en == match.group('object')) or (lang == 'es' and last_name_es == match.group('object')) or (lang == 'sk' and last_name_sk == match.group('object')):
                    continue
                if last_music_artist_id =='':
                    continue
                if (last_music_artist_id == FBsubject) or (isArtist(FBsubject)):
                    #print('muhahaaaaaaaaaa', match.group('object'))
                    key = key + '_' + lang
                #elif (isAwardHonor(FBsubject)):
                #    print(line)
                #    key = 'award_name'
                """
                key = 'all_names'
                
                       
            
            f = open(fileSwitcher(key),'ab')
            if os.path.getsize(fileSwitcher(key)) == 0:
                f.write(headerSwitcher(key).encode('utf-8'))

            f.write(FBsubject.encode('utf-8'))

            if key != 'artist_id':                
                FBobject = match.group('object')
                f.write((delimiter + FBobject).encode('utf-8'))

            """
            if key.startswith('name'):
                #last_name = FBobject
                lang = match.group('lang')
                if (lang == 'en'):
                    last_name_en = FBobject
                elif (lang == 'es'):
                    last_name_es = FBobject
                else:
                    last_name_sk = FBobject    
                f.write((delimiter + lang).encode('utf-8'))
            """

            if key == 'all_names':
                lang = match.group('lang')
                last_name = FBobject
                f.write((delimiter + lang).encode('utf-8'))

            #if key == 'artist_id': 
            #   last_music_artist_id = FBsubject
            
            f.write('\n'.encode('utf-8'))
            f.close

            return key, match
    
    return None, None


def isArtist(id_name):
    try:
        ids = open('artist_id.txt','rb')
    except FileNotFoundError:
        # doesn't exist
        print('File doesnt exist')
        return False
    
    for id in ids:         
        decoded = id.decode('utf-8')
        decoded = decoded.strip('\n')
        #print('1.',decoded,'2.', id_name)
        if decoded == id_name:
            ids.close()
            #print('success')
            return True

    ids.close()
    return False

def isAwardHonor(award_honor_id):
    try:
        ids = open('award_honor_ids.txt','rb')
    except FileNotFoundError:
        # doesn't exist
        print('File doesnt exist')
        return False
    
    for id in ids:         
        decoded = id.decode('utf-8')
        decoded = decoded.strip('\n')
        decoded = decoded.split(',')
        #aw_id = delimiter.index
        #print('AWARDSNAME > 1.',decoded[1],'2.', award_honor_id)
        if decoded[1] == award_honor_id:
            ids.close()
            print('success')
            return True

    ids.close()
    return False



with gzip.open('C:/Users/janep/Desktop/Škola/ING/1.ročník/1.semester/VINF/freebase-rdf-latest.gz','rt',encoding="utf-8") as f:
    x = 0    
    for line in f:
        x = x + 1

        #if line.__contains__('m.09889g>') and line.__contains__('m.011ncp6d'):
        #    print(line)
        key, match = parse_line(line)

        if x == 1000000000 :
            break
        if x % 10000000 == 0:
            print(x)
