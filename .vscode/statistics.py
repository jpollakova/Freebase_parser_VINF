import pickle

def check_lang(values, lang):
    count = 0
    for v in values:
        if str(v).__contains__(lang):
            count = count + 1
       
    return count


DICT_artist_awards = open("FINAL_artist_awards_dict.pkl", "rb")
artist_awards = pickle.load(DICT_artist_awards)
DICT_artist_awards.close()

DICT_artist_tracks = open("FINAL_artist_tracks_dict.pkl", "rb")
artist_tracks = pickle.load(DICT_artist_tracks)
DICT_artist_tracks.close()

DICT_wikipage = open("FINAL_wikipage_dict.pkl", "rb")
wikipage_links = pickle.load(DICT_wikipage)
DICT_wikipage.close()

print('\n___________________________artist_tracks___________________________________\n')

#average number of tracks
number_of_artists = len(artist_tracks)
total_num_of_tracks = 0
max_tracks = 0
min_tracks = 100
empty_tracks = 0
en, es, sk = 0,0,0

print('NUMBER OF ARTISTS WITH AT LEAST ONE TRACK > ', number_of_artists)


for key, values in artist_tracks.items():
    empty_in_line = values.count('[]')
    empty_tracks = empty_tracks + empty_in_line

    en = en + check_lang(values,",en'") + check_lang(values,',en"')
    sk = sk + check_lang(values,",sk'") + check_lang(values,',sk"')
    es = es +check_lang(values,",es'") + check_lang(values,',es"')
    
    number_of_tracks = len(values)
    if number_of_tracks > max_tracks:
        max_tracks = number_of_tracks
    if number_of_tracks < min_tracks:
        min_tracks = number_of_tracks
    total_num_of_tracks = total_num_of_tracks + number_of_tracks

print('NUMBER OF ALL TRACKS > ', total_num_of_tracks)
average_num_of_tracks = total_num_of_tracks / number_of_artists
print('AVERAGE NUMBER OF TRACKS PER ARTIST > ', "{:.2f}".format(average_num_of_tracks))

print('MAXIMUM NUMBER OF TRACKS PER ARTIST > ', max_tracks)

print('MINIMUM NUMBER OF TRACKS PER ARTIST > ', min_tracks)

print('NUMBER OF EMPTY TRACK NAMES > ', empty_tracks)

print('AVERAGE NUM OF EMPTY TRACK NAME PER ARTIST > ', "{:.2f}".format(empty_tracks / number_of_artists))

print('PERCENTAGE OF EMPTY TRACK NAMES > ', "{:.2f}".format(empty_tracks*100 / total_num_of_tracks), '%')

print('NUMBER OF ENGLISH TRACK NAMES > ', en, '->', "{:.2f}".format(en*100 / total_num_of_tracks), '%')
print('NUMBER OF SPANISH TRACK NAMES > ', es, '->', "{:.2f}".format(es*100 / total_num_of_tracks), '%')
print('NUMBER OF SLOVAK TRACK NAMES > ', sk, '->', "{:.2f}".format(sk*100 / total_num_of_tracks), '%')

    
print('\n___________________________artist_awards___________________________________\n')

#average number of awards
number_of_artists = len(artist_awards)
total_num_of_awards = 0
max_awards = 0
min_awards = 100
en, es, sk = 0,0,0

print('NUMBER OF ARTISTS WITH AT LEAST ONE AWARD > ', number_of_artists)


for key, values in artist_awards.items():

    en = en + check_lang(values,",en'") + check_lang(values,',en"')
    sk = sk + check_lang(values,",sk'") + check_lang(values,',sk"')
    es = es +check_lang(values,",es'") + check_lang(values,',es"')

    number_of_awards = len(values)
    if number_of_awards > max_awards:
        max_awards = number_of_awards
    if number_of_awards < min_awards:
        min_awards = number_of_awards
    total_num_of_awards = total_num_of_awards + number_of_awards

print('NUMBER OF ALL AWARDS > ', total_num_of_awards)
average_num_of_awards = total_num_of_awards / number_of_artists
print('AVERAGE NUMBER OF AWARDS PER ARTIST> ', "{:.2f}".format(average_num_of_awards))

print('MAXIMUM NUMBER OF AWARDS PER ARTIST > ', max_awards)

print('MINIMUM NUMBER OF AWARDS PER ARTIST > ', min_awards)

print('NUMBER OF ENGLISH AWARD NAMES > ', en, '->', "{:.2f}".format(en*100 / total_num_of_awards), '%')
print('NUMBER OF SPANISH AWARD NAMES > ', es, '->', "{:.2f}".format(es*100 / total_num_of_awards), '%')
print('NUMBER OF SLOVAK AWARD NAMES > ', sk, '->', "{:.2f}".format(sk*100 / total_num_of_awards), '%')

print('\n')
