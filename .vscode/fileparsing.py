import re


# Regex dictionary - there are regexes for parsing data related to artist and their awards. Each regular expression
# (except 'artis_id') includes group for subject and object - this makes easier to write these data to textfiles.

rx_dict = {
    'artist_id':re.compile('\/(?P<subject>[gm]\..+)>.+<.+>.+\/music\.artist *>'),
    'award_id':re.compile('\/(?P<subject>[gm]\..+)>.+\/award\.award_winner\.awards_won *>.+\/(?P<object>[gm]\..+)>'),
    'track':re.compile('\/(?P<subject>[gm]\..+)>.+\/music\.artist\.track *>.+\/(?P<object>[gm]\..+)>')

}

# The function returns string representing the name of the textfile according to key from regex.

def fileSwitcher(key):
    switcher = {
        'artist_id': 'artist_id.txt',
        'award_id': 'awards.txt',
        'track': 'tracks.txt'
    }
    return switcher.get(key, 'Invalid key!')


# The function for parsing data and writing data to textfiles. The function gets the line and determines if there is 
# any match with our declared regexes. If so, the data are stored in the particular textfile. 

def parse_line(line):

    delimiter = ','

    for key, rx in rx_dict.items():
        match = rx.search(line)
        if match:
            #if key == 'track':
             #   print(line)

            FBsubject = match.group('subject')

            print(' subject: ', FBsubject )                        

            f = open(fileSwitcher(key),'a')
            f.write(FBsubject)

            if key != 'artist_id':                
                FBobject = match.group('object')
                f.write(delimiter + FBobject)
                print(' object: ', FBobject )  

            f.write('\n')
            f.close


            return key, match
    
    return None, None
    