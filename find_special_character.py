import re

Str ="Alexmaxwell@gmail.com"

regex=re.compile('[@_!#$%]')

if(regex.search(Str)==None):
    print("No anyone special character")
else:
    print("special character are included")