import pickle

def get_awards(name):
    name = name.lower()

    for key in artist_awards:        
        current_name = str(key).lower()
        if current_name.__contains__(name):
            return (key, artist_awards.get(key))

    return None, None


def get_tracks(name):
    name = name.lower()

    for key in artist_tracks:
        #print('KEY> ', key)
        current_name = str(key).lower()
        if current_name.__contains__(name):
            return (key, artist_tracks.get(key))

    return None, None

def get_wikipage_link(name):
    name = name.lower()

    for key in wikipage_links:
        #print('KEY> ', key)
        current_name = str(key).lower()
        if current_name.__contains__(name):
            return (key, wikipage_links.get(key))

    return None, None

def check_lang_version_of_name(s,lang):
    s = str(s)
    s = s[1:-1]
    
    if s.__contains__(','+lang):
        sign = s[(s.find(','+lang)+3)]
        s = s[:s.find(','+lang)]        
        #print('VO FCII : ',s)
        #print('SIGN : ',sign)
        rev_name = s[::-1]
        #print("REVERSED : ", rev_name)
        rev_name = rev_name[:rev_name.find(sign)]
        s = rev_name[::-1]
        #print("TOTOOOOO : ", s) 
    return s

def get_artists_won_the_award(term_searched):

    artist_list = []

    for key, values in artist_awards.items():
        #print('KEY> ', key)
        current_name = str(key)
        for v in values:
            aw = str(v).lower()
            if aw.__contains__(str(term_searched).lower()):
                artist_list.append(current_name)
                break
        #if current_name.__contains__(name):
        #    return (key, artist_tracks.get(key))

    return artist_list

def get_track_author(term_searched):
    track_name = term_searched.lower()

    potential_authors_list = []

    for key, values in artist_tracks.items():
        current_author = str(key)
        for v in values:
            tr = str(v).lower()
            if tr.__contains__(str(term_searched).lower()):
                potential_authors_list.append(current_author)
                break

    return potential_authors_list


DICT_artist_awards = open("FINAL_artist_awards_dict.pkl", "rb")
artist_awards = pickle.load(DICT_artist_awards)
DICT_artist_awards.close()

DICT_artist_tracks = open("FINAL_artist_tracks_dict.pkl", "rb")
artist_tracks = pickle.load(DICT_artist_tracks)
DICT_artist_tracks.close()

DICT_wikipage = open("FINAL_wikipage_dict.pkl", "rb")
wikipage_links = pickle.load(DICT_wikipage)
DICT_wikipage.close()


search_category = input("Enter search category ('artist' / 'award' / 'track' ) : ")
search_language = input("Enter search language ( 'en' / 'es' / 'sk' ) : ")
term_searched = input("Enter search term : ")

print('\n________________________________________________________\n')

if search_category == 'artist':
    #search_category = 'artist'
    #search_language = 'en'
    
    print('SEARCHED TERM - ARTIST: ' + term_searched)

    aw_key, searched_awards = get_awards(term_searched)
    tr_key, searched_tracks = get_tracks(term_searched)
    wi_key, searched_wikilink = get_wikipage_link(term_searched)

    if searched_awards == None :
        print('No awards for this author')
    else:
        print('\nThe artist ' + aw_key + ' has won these awards:')
        for aw in range(len(searched_awards)):
            checked_name = check_lang_version_of_name(searched_awards[aw],search_language)
            print('   ',aw+1, end = '. ')
            print(checked_name)

    if searched_awards == None :
        print('No tracks by this author')
    else:
        print('\nThe artist ' + tr_key + ' has recorded these tracks:')
        for tr in range(len(searched_tracks)):
            checked_name = check_lang_version_of_name(searched_tracks[tr],search_language)
            print('   ',tr+1, end = '. ')
            print(checked_name)

    if searched_wikilink == None :
        print('No wikipage link for this author')
    else:
        print('\nThe artist ' + wi_key + ' corresponds to this wikipage:')        
        print('   ', check_lang_version_of_name(searched_wikilink,search_language))
    

    print('\n________________________________________________________\n')

if search_category == 'award':
    #search_language = 'en'
    #term_searched = 'Billboard Music Award for Modern Rock Artist of the Year,en'
    #term_searched = 'Country Music Association Award for Vocal Duo of the Year,en'
    #term_searched = "People's Choice Award for "
    
    print('SEARCHED TERM - AWARD: ' + term_searched)

    list_of_artists_won_the_award = get_artists_won_the_award(term_searched)

    if len(list_of_artists_won_the_award) == 0:
        print('Sorry, nobody has won this award yet.')
    else:
        print('\nThese artists won the searched award:')
        for ar in range(len(list_of_artists_won_the_award)):
            print('   ',ar+1, end = '. ')
            print(list_of_artists_won_the_award[ar])


    print('\n________________________________________________________\n')


if search_category == 'track':
    #search_language = 'en'

    #term_searched = "your song"
    print('SEARCHED TERM - TRACK: ' + term_searched)

    potential_track_authors = get_track_author(term_searched)

    if len(potential_track_authors) == 0:
        print('Sorry, this track was not found in the database.')
    elif len(potential_track_authors) == 1:
        print('\nThe author of the track is :')
        print(potential_track_authors[0])
    else:    
        print('\nThese artists may be author of the track:')
        for ar in range(len(potential_track_authors)):
            print('   ',ar+1, end = '. ')
            print(potential_track_authors[ar])

    print('\n________________________________________________________\n')