from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir
from whoosh import qparser
from whoosh.fields import Schema, TEXT, ID
from whoosh import index
import output_formatting


ix = open_dir("indexdir")

#query_str = u'"green day"'
#query_str = 'green day'
#query_str = 'jozef "voda čo ma"'
#query_str = '"green day" AND "21 guns"'

query_str = input("Enter search term : ")

print('\n####################################\nSEARCHED TERM > ', query_str, '\n####################################\n')
 

with ix.searcher(weighting=scoring.Frequency) as searcher:
    #query = QueryParser("name", ix.schema).parse(query_str)
    query = qparser.MultifieldParser(["name", "award_list", "track_list"], ix.schema).parse(query_str)
    results = searcher.search(query, terms= True, limit=10)
    print('Number of results: ', len(results))

    for i in results:
        #print(i,'\n\n\n')

        x = output_formatting.process_search_hit(i,'en', 'artist')
        #x = outSput_formatting.process_search_hit(i, query_str)
