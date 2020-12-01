import re
from itertools import islice
import pickle
import json

def create_artist_dict():
    f = open('PARSED_DATA/artist_id.txt', 'rt', encoding="utf-8")

    artist_dict = {}

    for line in f:
        line = line.strip('\n')
        artist_dict[line] = []

    f.close()
    return artist_dict


def create_artist_awards_dict():
    f = open('PARSED_DATA/award_id.txt', 'rt', encoding="utf-8")

    artist_awards_dict = {}

    for line in f:
        line = line.strip('\n')
        id_artist = line[:re.search(',',line).span()[0]]
        id_award = line[re.search(',',line).span()[1]:]

        if id_artist not in artist_awards_dict:
            artist_awards_dict[id_artist] = []

        artist_awards_dict[id_artist].append(id_award)

    f.close()
    return artist_awards_dict


def create_artist_tracks_dict():
    f = open('PARSED_DATA/track_id.txt', 'rt', encoding="utf-8")

    artist_tracks_dict = {}
    track_dict = {}

    for line in f:
        line = line.strip('\n')
        id_artist = line[:re.search(',',line).span()[0]]
        id_track = line[re.search(',',line).span()[1]:]

        if id_artist not in artist_tracks_dict:
            artist_tracks_dict[id_artist] = []

        artist_tracks_dict[id_artist].append(id_track)
        track_dict[id_track] = []

    f.close()
    return (artist_tracks_dict,track_dict)



def create_awards_dicts():

    award_id_dict , award_honor_id_dict= {}, {}

    f = open('PARSED_DATA/award_honor_ids.txt', 'rt', encoding="utf-8")

    for line in f:
        line = line.strip('\n')
        award_id_dict[line[0:re.search(',',line).span()[0]]] = line[re.search(',',line).span()[1]:]
        award_honor_id_dict[line[re.search(',',line).span()[1]:]] = []

    f.close()
    return (award_id_dict,award_honor_id_dict)


def save_dict_to_pickle(dict, file_name):
    f = open(file_name + ".pkl","wb")
    pickle.dump(dict,f)
    f.close()



artist_dict = create_artist_dict()
artist_awards_dict = create_artist_awards_dict()
award_id_dict , award_honor_id_dict= create_awards_dicts()
artist_tracks_dict, track_dict = create_artist_tracks_dict()

'''
x=0
for key, value in artist_awards_dict.items() :
    x = x+1
    print (key, value)
    if x == 100:
        break
'''

f_all_names = open('PARSED_DATA/all_names.txt', 'rt', encoding="utf-8")

for line in f_all_names:
    line = line.strip('\n')
    id = line[:re.search(',',line).span()[0]]
    #print(id)

    if id in artist_dict:
        #uloz name k idcku
        artist_dict[id].append(line[re.search(',',line).span()[1]:])
        continue

    if id in award_honor_id_dict:
        award_honor_id_dict[id].append(line[re.search(',',line).span()[1]:])
        continue

    if id in track_dict:
        track_dict[id].append(line[re.search(',',line).span()[1]:])
        continue

f_all_names.close()


x=0
for key, value in track_dict.items() :
    x = x+1
    print (key, value)
    if x == 500:
        break


save_dict_to_pickle(artist_dict,"dict_artist_name")
save_dict_to_pickle(award_honor_id_dict,"dict_award_honor_name")
save_dict_to_pickle(artist_awards_dict,"dict_artist_awards")

save_dict_to_pickle(award_id_dict,"dict_award_award_honor")
save_dict_to_pickle(track_dict,"dict_track_id")
save_dict_to_pickle(artist_tracks_dict,"dict_artist_track_id.pkl")

'''
DICT_artist_name = open("dict_artist_name.pkl","wb")
pickle.dump(artist_dict,DICT_artist_name)
DICT_artist_name.close()

DICT_award_honor_name = open("dict_award_honor_name.pkl","wb")
pickle.dump(award_honor_id_dict,DICT_award_honor_name)
DICT_award_honor_name.close()

DICT_artist_awards = open("dict_artist_awards.pkl","wb")
pickle.dump(artist_awards_dict,DICT_artist_awards)
DICT_artist_awards.close()

DICT_award_award_honor = open("dict_award_award_honor.pkl","wb")
pickle.dump(award_id_dict,DICT_award_award_honor)
DICT_award_award_honor.close()

DICT_track_id = open("dict_track_id.pkl","wb")
pickle.dump(track_dict,DICT_track_id)
DICT_track_id.close()

DICT_artist_track_id = open("dict_artist_track_id.pkl","wb")
pickle.dump(artist_tracks_dict,DICT_artist_track_id)
DICT_artist_track_id.close()
'''
artist_awards_dict.clear()
artist_dict.clear()
artist_tracks_dict.clear()
award_honor_id_dict.clear()
award_id_dict.clear()
track_dict.clear()


'''
#DICT_artist_name = open("dict_artist_name.pkl", "rb")
#outofpickledict = pickle.load(DICT_artist_name)
#DICT_artist_name.close()

x=0
for key, value in outofpickledict.items() :
    x = x+1
    print (key, value)
    if x == 500:
        break


'''


# create final dicts 
# - artist_name - list_of_his_awards
# - artist_name - list_of_his_tracks
# - artist_name - wikipage_link