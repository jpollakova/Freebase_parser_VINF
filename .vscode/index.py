import os, os.path
import re
from whoosh import index
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import Schema, ID, TEXT, STORED, IDLIST
import pickle


if not os.path.exists('indexdir'):
    os.mkdir("indexdir")

#schema = Schema(name = ID(stored=True, unique=True), award_list = IDLIST(stored=True, expression=re.compile(r"[^;]+")))
schema = Schema(name = TEXT(stored=True), award_list = TEXT(stored=True))

ix = index.create_in("indexdir", schema)
writer = ix.writer()


#loading dictionaries
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

print(len(artist_name))

x=0
for key, values in artist_name.items():
    x = x+1
    if x % 10000 == 0:
        print(x)
    if x == 10000:
        break

    for name in values:

        list_id_awards = []
        for k, v in artist_awards.items():
            if k == key :
                list_id_awards = v
                break
        
        list_id_award_honor = []
        for aw in list_id_awards:
            for k, v in award_award_honor.items():
                if k == aw:
                    list_id_award_honor.append(award_award_honor[aw])

        list_awards_names = []
        for aw in list_id_award_honor:
            if aw in award_honor_name:
                list_awards_names.append(award_honor_name[aw])


        '''
        if name == 'Melissa Joan Hart,en':
            print("name: " + name)
            clear_award_name = str(list_awards_names[1]).replace('[','').replace(']','')
            clear_award_name = clear_award_name[1:-1]
            print(clear_award_name)
            break
        '''        

        string_cleared_award_names = ''

        for aw in list_awards_names:
            clear_name = str(aw).replace('[','').replace(']','')
            clear_name = clear_name[1:-1]
            if string_cleared_award_names == '':
                string_cleared_award_names = clear_name
            else:
                string_cleared_award_names = string_cleared_award_names + ';' + clear_name

        #print(name)
        #print(string_cleared_award_names)
        

        #Melissa Joan Hart,en
        #Young Artist Award Best Performance in a Feature Film - Leading Young Actress,en;Young Artist Award Best Performance in a Feature Film - Leading Young Actress,en
        
        '''
        print('name> ' + name)
        if len(list_cleared_award_names)>1:
            print(list_cleared_award_names[1])
        print(list_cleared_award_names)
        '''     
        #name = name.encode()
        #string_cleared_award_names = string_cleared_award_names.encode()

        writer.add_document(name = name, award_list = string_cleared_award_names)


writer.add_document(name = 'aha', award_list = 'b;c;d')
writer.commit()