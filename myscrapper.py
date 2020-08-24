from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import csv 

ourlink = 'https://bluelimelearning.github.io/my-fav-quotes/'
"""link is open, connection is activated"""
urlobj = urlopen(ourlink)
#rint(urlobj)
#print(type(urlobj))
"""it reads the data and creates html page data with html tags"""
html_page = urlobj.read()
urlobj.close()
#print(type(html_page)) exist in the form of bytes data 
"""unnecesaary details are removed
type : beautifulsoup object 
still with all the html tags"""
parsed_obj = bs(html_page,"html.parser")
#print(parsed_obj)
quote_section  = parsed_obj.findAll("div",{"class":"quotes"})
#print(quote_section)

"""writing to csv as well"""
f = csv.writer(open('csvscrapper.csv','w'))
f.writerow(['author','quote'])

"""opening a text file"""
text_f = open('new_file.txt','w')

for quote in quote_section:
    quote_lines = quote.findAll("p",{"class":"aquote"})
    aquote = quote_lines[0].text.strip()
    author = quote.findAll("p",{"class":"author"})
    author = author[0].text.strip()
    #csv writing
    f.writerow([author,aquote])
    #file writing
    text_f.write(author+'\n')
    text_f.write(aquote+'\n')
    print(aquote)
    print(author)
text_f.close()
