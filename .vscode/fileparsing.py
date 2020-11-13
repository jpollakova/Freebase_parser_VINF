import re
import gzip
import os.path


# Regex dictionary - there are regexes for parsing data related to artist and their awards. Each regular expression
# (except 'artis_id') includes group for subject and object - this makes easier to write these data to textfiles.

rx_dict = {
    'artist_id':re.compile('\/(?P<subject>[gm]\..+)>.+<.+>.+\/music\.artist *>'),
    'award_id':re.compile('\/(?P<subject>[gm]\..+)>.+\/award\.award_winner\.awards_won *>.+\/(?P<object>[gm]\..+)>'),
    'track':re.compile('\/(?P<subject>[gm]\..+)>.+\/music\.artist\.track *>.+\/(?P<object>[gm]\..+)>'),
    'name':re.compile('\/(?P<subject>[gm]\..+)>.+((\/type\.object\.name)|(label)) *>.+\"(?P<object>.+)\".*@(?P<lang>[a-zA-Z]{1,})')

}

# The function returns string representing the name of the textfile according to key from regex.

def fileSwitcher(key):
    switcher = {
        'artist_id': 'artist_id.txt',
        'award_id': 'awards.txt',
        'track': 'tracks.txt',
        'name_en': 'artists_names_EN.txt',
        'name_es': 'artists_names_ES.txt',
        'name_sk': 'artists_names_SK.txt'
    }
    return switcher.get(key, 'Invalid key!')


# The function for parsing data and writing data to textfiles. The function gets the line and determines if there is 
# any match with our declared regexes. If so, the data are stored in the particular textfile. 
 
last_name, last_music_artist_id = '', ''
delimiter = ','

def parse_line(line):

    FBsubject , FBobject = '',''  

    for key, rx in rx_dict.items():
        match = rx.search(line)
        if match:
                       
            FBsubject = match.group('subject') 

            if key == 'name':
                global last_name, last_music_artist_id

                if match.group('lang')!='en' and match.group('lang')!='es' and match.group('lang')!='sk':
                    continue                
                if last_name == str(match.group('object')):
                    continue 
                if last_music_artist_id =='':                    
                    continue
                #if (isArtist(FBsubject))==False:        
                #    continue
                if (last_music_artist_id == FBsubject):
                    print('muhahaaaaaaaaaa', match.group('object'))

                key = key + '_' + match.group('lang')
                       
            
            f = open(fileSwitcher(key),'ab')
            f.write(FBsubject.encode('utf-8'))

            if key != 'artist_id':                
                FBobject = match.group('object')
                f.write((delimiter + FBobject).encode('utf-8'))

            if key.startswith('name'):
                last_name = FBobject
                f.write((delimiter + match.group('lang')).encode('utf-8'))

            if key == 'artist_id': 
               last_music_artist_id = FBsubject
            
            f.write('\n'.encode('utf-8'))
            f.close
            
            #if (FBsubject == 'm.011ncp6d') or (FBobject == 'Michael Jackson'):
            #if (line.__contains__('m.011ncp6d')):
            #    print(line)

            return key, match
    
    return None, None


def isArtist(id_name):
    myfile='artist_id.txt'
    #if ( os.path.exists(myfile) == False):
    #    print('fuck')
    #    return False   

    try:
        ids = open(myfile,'r')
    except FileNotFoundError:
        # doesn't exist
        print('doesnt exist')
        return False
    
    for id in ids: 
        #print('1.',id,'2.', id_name)
        if id == id_name:
            ids.close()
            print('success')
            return True 
        ids.close()
        return False



with gzip.open('C:/Users/janep/Desktop/Škola/ING/1.ročník/1.semester/VINF/freebase-rdf-latest.gz','rt',encoding="utf-8") as f:
    x = 0
    last_name, last_music_artist_id = '', ''
    for line in f:
        x = x + 1
        #if (line.__contains__('music.artist')):
        #    print(line)
        key, match = parse_line(line)
        
        #if match != None:
            #print(x)
            #print(x , 'key: ', key, ' match: ', match)

        if x == 10000000 :
            break
