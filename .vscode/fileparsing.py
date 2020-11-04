import re


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

def parse_line(line):

    delimiter = ','
    #last_name, FBsubject , FBobject = '' ,'', ''
    

    for key, rx in rx_dict.items():
        match = rx.search(line)
        if match:            
            
            if key == 'name':                
                if match.group('lang')!='en' and match.group('lang')!='es' and match.group('lang')!='sk':
                    continue                
                #if last_name == str(match.group('object')):
                    #continue                    
                key = key + '_' + match.group('lang')

            #    if last_music_artist_id =='':                    
            #        continue
            #    if FBsubject != last_music_artist_id or isArtist(FBsubject)==False:        
            #        continue
            
            FBsubject = match.group('subject')            
            
            f = open(fileSwitcher(key),'ab')
            f.write(FBsubject.encode('utf-8'))

            if key != 'artist_id':                
                FBobject = match.group('object')
                f.write((delimiter + FBobject).encode('utf-8'))

            if key.startswith('name'):
                #last_name = FBobject
                f.write((delimiter + match.group('lang')).encode('utf-8'))

            if key == 'artist_id': 
               last_music_artist_id = FBsubject
            
            f.write('\n'.encode('utf-8'))
            f.close

            return key, match
    
    return None, None


def isArtist(id_name):
    f = open('artist_id.txt','r')

    for line in f: 
        if line == id_name:
            f.close()
            return True 
    f.close()
    return False


