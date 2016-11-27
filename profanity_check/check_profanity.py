#module urllib helps to get info from internet having function urlopen.
#open helps to read file from computer and returns object of type File.
#wydl is a google based website to check profanity.

import urllib

def read_text():
    quotes = open("""Enter file location""")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check) 
    output = connection.read()
    connection.close()
    if "true" in output:
        print "This document has curse words!!"
    else:
        print "No curse words are present in this document"
read_text()
