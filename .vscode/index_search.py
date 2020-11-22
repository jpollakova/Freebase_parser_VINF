import os, os.path
import re
from whoosh import index
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import Schema, ID, TEXT, STORED, IDLIST
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from lexicon import Lexicon

ix = open_dir("indexdir")

searched_term = 'Young Artist Award Best Performance in a Feature Film'
#searched_term = searched_term.encode()
#print(searched_term)

with ix.searcher() as searcher:
    query = QueryParser('award_list', schema = ix.schema).parse(searched_term)
    results = searcher.search(query)

    if len(results) != 0:
        print('Number of results: ', len(results))
        for i in results:     
            print(i)
    else:
        print('Sooooorrryyyy')

    print(ix.schema)
    #print(list(searcher.lexicon('name')))

