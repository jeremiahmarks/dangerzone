#!/usr/bin/python

##lifted from http://gulzarmanzil.wordpress.com/2012/09/22/google-dictionary-api/

from urllib2 import urlopen
keyword = raw_input("Enter the keyword for search: ")
 
null = None
data = urlopen("http://www.google.com/dictionary/json?callback=dict_api.callbacks.id100&q="+keyword+"&sl=en&tl=en&restrict=pr%2Cde&client=te").read()[25:-1]
 
d = eval('('+data+')')
if d[1] == 200:
    result = d[0]
    print '> Query:',result.get('query')
 
    if 'primaries' in result:
        print '> Primaries'
        primaries = result.get('primaries')
 
        for primary in primaries:
            print '-\tTerms'
            for term in primary.get('terms'):
                if 'labels' in term:
                    for label in term.get('labels'):
                        print '\t',label['title'],' '*6,':',label['text']
                print '\t',term.get('type'),' '*(20 - len(term.get('type'))),':',term.get('text')
            print '-\tEntries'
            for entry in primary.get('entries'):
                for term in entry.get('terms'):
                    print '\t',term.get('text'),
                    if 'labels' in term:
                        for label in term.get('labels'):
                            print '-',label['text']
                    else: print
            print '*'*40
 
    if 'webDefinitions' in result:
        webd = result.get('webDefinitions')[0]
        print '> webDefinitions'
        entries = webd.get('entries')
        for entry in entries:
            for term in entry.get('terms'):
                if term.get('type') == 'text':
                    print '*\t',term.get('text')