import pickle

def get_id_artist(term_searched):

    for key, values in artist_name.items():
        for v in values:
            if v == term_searched :
                return key

    return None

def get_id_award_honor(term_searched):

    for key, values in award_honor_name.items():
        for v in values:
            if v == term_searched :
                return key

    return None

def get_id_award(id_award_honor):

    for key, values in award_award_honor.items():
        if values == id_award_honor:
            return key

    return None

def get_list_of_artists_awards(id_artist):

    list_id_awards = []
    for key, values in artist_awards.items():
        if key == id_artist :
            list_id_awards = values

    #print(list_id_awards)

    list_id_award_honor = []
    for aw in list_id_awards:
        for key, values in award_award_honor.items():
            if key == aw:
                list_id_award_honor.append(award_award_honor[aw])

    #print(list_id_award_honor)

    list_awards_names = []
    for aw in list_id_award_honor:
        if aw in award_honor_name:
            list_awards_names.append(award_honor_name[aw])

    #print(list_awards_names)

    return list_awards_names

def get_list_of_artists_won_this_award(id_award):

    list_artists_won_this_award = []
    for key, values in artist_awards.items():
        for v in values:
            if v == id_award :
                list_artists_won_this_award.append(key)

    #print(list_artists_won_this_award)

    list_artists_won_this_award_names = []
    for ar in list_artists_won_this_award:
        if ar in artist_name:
            list_artists_won_this_award_names.append(artist_name[ar])

    #print(list_artists_won_this_award_names)

    return list_artists_won_this_award_names


DICT_artist_name = open("dict_artist_name.pkl", "rb")
artist_name = pickle.load(DICT_artist_name)
DICT_artist_name.close()

DICT_artist_awards = open("dict_artist_awards.pkl", "rb")
artist_awards = pickle.load(DICT_artist_awards)
DICT_artist_awards.close()

DICT_award_award_honor = open("dict_award_award_honor.pkl", "rb")
award_award_honor = pickle.load(DICT_award_award_honor)
DICT_award_award_honor.close()

DICT_award_honor_name = open("dict_award_honor_name.pkl", "rb")
award_honor_name = pickle.load(DICT_award_honor_name)
DICT_award_honor_name.close()

'''
x=0
for key, value in artist_name.items() :
    x = x+1
    print (key, value)
    if x == 500:
        break
'''
print('\n________________________________________________________\n')

term_searched = 'Anne Murray,es'
print('SEARCHED TERM - ARTIST: ' + term_searched)
id = get_id_artist(term_searched)

if id == None :
    print('The term does not occur in the dictionary')
else:
    print('ID is : ' + str(id))
    his_awards = get_list_of_artists_awards(id)
    print('\nThe artist ' + term_searched + ' has won these awards:')
    for x in range(len(his_awards)):        
        print(x+1, end = '. ')
        print(his_awards[x])


print('\n________________________________________________________\n')

#term_searched = 'Billboard Music Award for Modern Rock Artist of the Year,en'
term_searched = 'Country Music Association Award for Vocal Duo of the Year,en'
print('SEARCHED TERM - AWARD: ' + term_searched)

idcko_honor = get_id_award_honor(term_searched)
id_awardu = get_id_award(idcko_honor)

if idcko_honor == None or id_awardu == None:
    print('Sorry, but this award does not occur in the database.')
else:
    print('ID award honor: ' + idcko_honor)
    print('ID award id: ' + id_awardu)
    list_of_artists_won_this_award = get_list_of_artists_won_this_award(id_awardu)

    print('\nThese artists won the searched award:')
    for x in range(len(list_of_artists_won_this_award)):
        print(x+1, end = '. ')
        print(list_of_artists_won_this_award[x])


print('\n________________________________________________________\n')

'''
for key, value in artist_awards.items():
    #print value
    number_of_values = len([item for item in value if item])
    if number_of_values > 2:
        if key in artist_name:
            print(key, artist_name[key])
'''
