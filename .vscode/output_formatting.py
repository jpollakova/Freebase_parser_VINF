
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
        count = 0
        for aw in awards:
            count = count + 1
            print('   ',aw)
            if count == 20:
                print('   ... and ' + str(len(awards)-20) + ' more awards...')
                break
    
        print('TRACKS > ')
        count = 0
        for tr in tracks:
            count = count + 1
            print('   ',tr)
            if count == 20:
                print('   ... and ' + str(len(tracks)-20) + ' more tracks...')
                break
    
        print('_____________________________________________')

        return None
    if category == 'award' or category == 'track':
        return (name, wikilink)

