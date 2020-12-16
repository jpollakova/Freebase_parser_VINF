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

DICT_artist_name = open("dict_artist_name.pkl", "rb")
all_artist_name = pickle.load(DICT_artist_name)
DICT_artist_name.close()

print('\n___________________________artists__________________________________\n')
en_artist, es_artist, sk_artist = 0,0,0

for key, values in all_artist_name.items():
    
    if str(values).__contains__(',en'):
            en_artist = en_artist + 1
    if str(values).__contains__(',es'):
            es_artist = es_artist + 1
    if str(values).__contains__(',sk'):
            sk_artist = sk_artist + 1
    #en_artist = en_artist + check_lang(values,",en'") + check_lang(values,',en"')
    #sk_artist = sk_artist + check_lang(values,",sk'") + check_lang(values,',sk"')
    #es_artist = es_artist + check_lang(values,",es'") + check_lang(values,',es"')

print('NUMBER OF ALL MUSIC ARTISTS > ', len(all_artist_name))
print('NUMBER OF ENGLISH ARTIST NAMES > ', en_artist, '->', "{:.3f}".format(en_artist*100 / len(all_artist_name)), '%')
print('NUMBER OF SPANISH ARTIST NAMES > ', es_artist, '->', "{:.3f}".format(es_artist*100 / len(all_artist_name)), '%')
print('NUMBER OF SLOVAK ARTIST NAMES > ', sk_artist, '->', "{:.3f}".format(sk_artist*100 / len(all_artist_name)), '%')

print('\n___________________________tracks___________________________________\n')

#average number of tracks
number_of_artists = len(artist_tracks)
total_num_of_tracks = 0
max_tracks = 0
max_artist = ''
min_tracks = 100
empty_tracks = 0
en, es, sk = 0,0,0
artists_with_wiki = 0


print('NUMBER OF ARTISTS IN TRACK DICTIONARY > ', number_of_artists)


for key, values in artist_tracks.items():

    empty_in_line = values.count('[]')
    empty_tracks = empty_tracks + empty_in_line

    en = en + check_lang(values,",en'") + check_lang(values,',en"')
    sk = sk + check_lang(values,",sk'") + check_lang(values,',sk"')
    es = es + check_lang(values,",es'") + check_lang(values,',es"')
    
    number_of_tracks = len(values)
    if number_of_tracks > max_tracks:
        max_tracks = number_of_tracks
        max_artist = key
    if number_of_tracks < min_tracks:
        min_tracks = number_of_tracks
    total_num_of_tracks = total_num_of_tracks + number_of_tracks

    if key in wikipage_links:
        artists_with_wiki = artists_with_wiki + 1



print('NUMBER OF ALL TRACKS > ', total_num_of_tracks)
average_num_of_tracks = total_num_of_tracks / number_of_artists
print('AVERAGE NUMBER OF TRACKS PER ARTIST (artists having at least one track) > ', "{:.3f}".format(average_num_of_tracks))
print('AVERAGE NUMBER OF TRACKS PER ARTIST (all music artists) > ', "{:.3f}".format(total_num_of_tracks / len(all_artist_name)))

print('MAXIMUM NUMBER OF TRACKS PER ARTIST > ', max_tracks, ' artist: ',max_artist[1:-4])

print('MINIMUM NUMBER OF TRACKS PER ARTIST > ', min_tracks)

print('NUMBER OF EMPTY TRACK NAMES > ', empty_tracks)

print('AVERAGE NUM OF EMPTY TRACK NAME PER ARTIST > ', "{:.3f}".format(empty_tracks / number_of_artists))

print('PERCENTAGE OF EMPTY TRACK NAMES > ', "{:.3f}".format(empty_tracks*100 / total_num_of_tracks), '%')

print('NUMBER OF ENGLISH TRACK NAMES > ', en, '->', "{:.3f}".format(en*100 / total_num_of_tracks), '%')
print('NUMBER OF SPANISH TRACK NAMES > ', es, '->', "{:.3f}".format(es*100 / total_num_of_tracks), '%')
print('NUMBER OF SLOVAK TRACK NAMES > ', sk, '->', "{:.3f}".format(sk*100 / total_num_of_tracks), '%')

    
print('\n___________________________artist_awards___________________________________\n')

#average number of awards
number_of_artists = len(artist_awards)
total_num_of_awards = 0
max_awards = 0
min_awards = 100
en, es, sk = 0,0,0


print('NUMBER OF ARTISTS IN AWARD DICTIONARY > ', number_of_artists)


for key, values in artist_awards.items():

    en = en + check_lang(values,",en'") + check_lang(values,',en"')
    sk = sk + check_lang(values,",sk'") + check_lang(values,',sk"')
    es = es +check_lang(values,",es'") + check_lang(values,',es"')

    number_of_awards = len(values)
    if number_of_awards > max_awards:
        max_awards = number_of_awards
        max_artist = key
    if number_of_awards < min_awards:
        min_awards = number_of_awards
    total_num_of_awards = total_num_of_awards + number_of_awards


print('NUMBER OF ALL AWARDS > ', total_num_of_awards)
average_num_of_awards = total_num_of_awards / number_of_artists
print('AVERAGE NUMBER OF AWARDS PER ARTIST (artists having at least one award) > ', "{:.3f}".format(average_num_of_awards))
print('AVERAGE NUMBER OF AWARDS PER ARTIST (all music artists) > ', "{:.3f}".format(total_num_of_awards / len(all_artist_name)))

print('MAXIMUM NUMBER OF AWARDS PER ARTIST > ', max_awards, ' artist: ', max_artist[1:-4])

print('MINIMUM NUMBER OF AWARDS PER ARTIST > ', min_awards)

print('NUMBER OF ENGLISH AWARD NAMES > ', en, '->', "{:.3f}".format(en*100 / total_num_of_awards), '%')
print('NUMBER OF SPANISH AWARD NAMES > ', es, '->', "{:.3f}".format(es*100 / total_num_of_awards), '%')
print('NUMBER OF SLOVAK AWARD NAMES > ', sk, '->', "{:.3f}".format(sk*100 / total_num_of_awards), '%')

print('\n___________________________wikipage___________________________________\n')

wiki_csv = open('PARSED_DATA/wikipage_mappings.txt', 'rt', encoding="utf-8")

num_of_all_wikipage_links = 0

for line in wiki_csv:
    num_of_all_wikipage_links = num_of_all_wikipage_links + 1

print('NUMBER OF ALL WIKIPAGE LINKS > ', num_of_all_wikipage_links)
#print('NUMBER OF ARTIST WITH WIKIPAGE LINK > ', artists_with_wiki)
print('NUMBER OF ARTIST WITH WIKIPAGE LINK > ', len(wikipage_links))

print('PERCENTAGE OF ARTISTS IN WIKI MAPPINGS DICTIONARY > ', "{:.3f}".format(len(wikipage_links)*100 / num_of_all_wikipage_links), '%')

print('\n\n\n')

