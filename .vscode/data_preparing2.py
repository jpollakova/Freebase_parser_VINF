import re
from itertools import islice
import pickle
import json

DICT_artist_name = open("dict_artist_name.pkl", "rb")
ARTIST_NAMES = pickle.load(DICT_artist_name)
DICT_artist_name.close()

DICT_artist_tracks = open("dict_artist_track_id.pkl", "rb")
ARTIST_TRACKS = pickle.load(DICT_artist_tracks)
DICT_artist_tracks.close()

DICT_track_name = open("dict_track_id.pkl", "rb")
TRACK_NAME = pickle.load(DICT_track_name)
DICT_track_name.close()

DICT_wikipage_links = open("dict_artist_wikipage.pkl", "rb")
WIKIPAGE_LINKS = pickle.load(DICT_wikipage_links)
DICT_wikipage_links.close()


x=0
for key, value in ARTIST_NAMES.items() :
    x = x+1
    if key == 'm.012_53':
        print (key, value)
    #if x == 50:
    #    break


# create final dicts 
# - artist_name - list_of_his_awards
# - artist_name - list_of_his_tracks OK
# - artist_name - wikipage_link OK
'''
x=0
for key, value in artist_tracks_dict.items() :
    x = x+1
    print (key, value)
    if x == 50:
        break
'''


#------FINAL ARTIST-TRACKS DICT-----#
final_artist_track_dict = {}

for key, values in ARTIST_TRACKS.items():
    #print('key> ', key)
    artist_id = key
    
    if artist_id in ARTIST_NAMES:
        artist_name = ARTIST_NAMES.get(artist_id)        
        artist_name = str(artist_name)
        artist_name = artist_name.replace('[','').replace(']','')
        #print(artist_name)
        final_artist_track_dict[artist_name] = []

        for track in values:
            if track in TRACK_NAME:
                track_name = TRACK_NAME.get(track)
                track_name = str(track_name)
                track_name = track_name.replace('[','').replace(']','')
                final_artist_track_dict[artist_name].append(track_name)



#-----FINAL WIKIPAGE DICT-----#
final_wikipage_dict = {}

for key, values in WIKIPAGE_LINKS.items():
    #print('key> ', key)
    artist_id = key
    
    if artist_id in ARTIST_NAMES:
        artist_name = ARTIST_NAMES.get(artist_id)        
        artist_name = str(artist_name)
        artist_name = artist_name.replace('[','').replace(']','')
        #print(artist_name)
        final_wikipage_dict[artist_name] = values




x=0
for key, value in final_wikipage_dict.items() :
    x = x+1
    key = str(key)
    print (key, value)

    if x == 100:
        break
          






ARTIST_NAMES.clear()
ARTIST_TRACKS.clear()
TRACK_NAME.clear()
WIKIPAGE_LINKS.clear()