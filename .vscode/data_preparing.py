import re
from itertools import islice

#def parse_all_names():



def create_artist_dict():
    f = open('artist_id.txt', 'rt', encoding="utf-8")

    artist_dict = {}

    for line in f:
        line = line.strip('\n')
        artist_dict[line] = []

    f.close()
    return artist_dict

def create_awards_dicts():

    award_id_dict , award_honor_id_dict= {}, {}

    f = open('award_honor_ids.txt', 'rt', encoding="utf-8")

    for line in f:
        line = line.strip('\n')
        award_id_dict[line[0:re.search(',',line).span()[0]]] = line[re.search(',',line).span()[1]:]
        award_honor_id_dict[line[re.search(',',line).span()[1]:]] = []

    f.close()
    return (award_id_dict,award_honor_id_dict)




#vytvorit dictionaries z artist_id a award_honor_id

artist_dict = create_artist_dict()
award_id_dict , award_honor_id_dict= create_awards_dicts()

x=0
for key, value in award_honor_id_dict.items() :
    x = x+1
    print (key, value)
    if x == 100:
        break
