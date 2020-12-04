import os, os.path
import re
from whoosh import index
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import Schema, ID, TEXT, STORED, IDLIST
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from lexicon import Lexicon

ix = open_dir("indexdir")

#searched_term = 'Billboard Music Award for Modern Rock'
#searched_term = 'Kerrang! Award pre najlepšiu medzinárodnú skupinu'
searched_term = 'b'
#print(searched_term)

with ix.searcher() as searcher:
    query = QueryParser('award_list', schema = ix.schema).parse(searched_term)
    results = searcher.search(query)

    if len(results) != 0:
        print('Number of results: ', len(results))
        for i in results:     
            print(i)
    else:
        print('Sorry, but the searched term does not occur in the index')

    print(ix.schema)
    #print(list(searcher.lexicon('name')))

