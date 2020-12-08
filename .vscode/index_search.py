import os, os.path
import re
from whoosh import index
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import Schema, ID, TEXT, STORED, IDLIST
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from lexicon import Lexicon

def sub_langs(lang):
    if lang == 'en':
        lang2 = 'es'
        lang3 = 'sk'
    elif lang == 'es':
        lang2 = 'en'
        lang3 = 'sk'
    else:
        lang2 = 'en'
        lang3 = 'es'

    return (lang2, lang3)

def get_cleared_name(p,lang):

    sign = p[(p.find(','+lang)+3)]
    cleared = p[:p.find(','+lang)]
    rev_name = cleared[::-1]
    rev_name = rev_name[:rev_name.find(sign)]
    cleared = rev_name[::-1]

    return cleared


def check_lang_version_of_name(s,lang):   
    if s.find('][') >= 0:
        parts = s.split('][')
    else:
        parts = s.split('] [')

    lang2, lang3 = sub_langs(lang)
    cleared_results = []

    for p in parts:
        if p.__contains__(','+lang):
            cleared = get_cleared_name(p,lang)
        elif p.__contains__(','+lang2):
            cleared = get_cleared_name(p,lang2)
        elif p.__contains__(','+lang3):
            cleared = get_cleared_name(p,lang3)
        else:
            cleared = None

        if cleared != None and cleared not in cleared_results:
            cleared_results.append(cleared)        

    return cleared_results


def process_search_hit(search_hit, lang, category):

    name = check_lang_version_of_name(search_hit['name'],lang)
    awards = check_lang_version_of_name(search_hit['award_list'],lang)
    tracks = check_lang_version_of_name(search_hit['track_list'],lang)
    wikilink = search_hit['wikilink']
    
    if category == 'artist':

        print('_____________________________________________')
        print('LANGUGE > ', lang)        
        print('ARTIST NAME > ', name[0],' - > ', wikilink)        
        print('AWARDS > ')
        for aw in awards:
            print('   ',aw)
    
        print('TRACKS > ')
        count = 0
        for tr in tracks:
            count = count + 1
            print('   ',tr)
            if count == 150:
                print('   ... and ' + str(len(tracks)-150) + ' more tracks...')
                break
    
        print('_____________________________________________')

        return None
    if category == 'award' or category == 'track':
        return (name, wikilink)



#searched_term = 'Billboard Music Award for Modern Rock'
#searched_term = 'green day'
#searched_term = 'American Music Award al Nuevo Artista Favorito de Country,es'
#searched_term = 'Melissa Joan'
 
ix = open_dir("indexdir")
status = 'y'

with ix.searcher() as searcher:

    while(status == 'y'):
        print('\n_____________________________________________\n')
        search_category = input("Enter search category ('artist' / 'award' / 'track' ) : ")
        searched_language = input("Enter search language ( 'en' / 'es' / 'sk' ) : ")
        searched_term = input("Enter search term : ")

        print('\n####################################\nSEARCHED TERM > ', searched_term, '\n####################################\n') 

        if search_category == 'artist':
            query = QueryParser('name', schema = ix.schema).parse(searched_term)
            results = searcher.search(query)

            if len(results) != 0:
                print('Number of results: ', len(results))
                for i in results:     
                    #print(i)
                    none = process_search_hit(i,searched_language, search_category)
            else:
                print('Sorry, but the searched term does not occur in the index')

        if search_category == 'award':
            query = QueryParser('award_list', schema = ix.schema).parse(searched_term)
            results = searcher.search(query, limit = 20)

            artists_won = []
            if len(results) != 0:
                print('Number of results: ', len(results))
                for i in results:     
                    #print(i)
                    name, wikilink = process_search_hit(i,searched_language, search_category)
                    coupled = name[0] + ' - > ' + str(wikilink)
                    artists_won.append(coupled)

                print('_____________________________________________')
                for ar in artists_won:
                    print(ar)
                print('_____________________________________________')
                
            else:
                print('Sorry, but the searched term does not occur in the index')

        if search_category == 'track':
            query = QueryParser('track_list', schema = ix.schema).parse(searched_term)
            results = searcher.search(query, limit = 20)

            artists_recorded = []
            if len(results) != 0:
                print('Number of results: ', len(results))
                for i in results:     
                    #print(i)
                    name, wikilink = process_search_hit(i,searched_language, search_category)
                    coupled = name[0] + ' - > ' + str(wikilink)
                    artists_recorded.append(coupled)

                print('_____________________________________________')
                for ar in artists_recorded:
                    print(ar)
                print('_____________________________________________')

            else:
                print('Sorry, but the searched term does not occur in the index')

        status = input("Do you want to search one more time? (y/n) : ")
    
    
    print(ix.schema)

