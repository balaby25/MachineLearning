import urllib.request
import json

Content = []
forDir = []
urlData = "http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:(\"Arts\")&api-key=0f8b796919ee4e9ab96874776d9a6bec&page=1"
webURL = urllib.request.urlopen(urlData)
Data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
result = json.loads(Data.decode(encoding))

Content.append(result)
forDir.append(dir(json))

f = open("bala.txt",'w')

for line in Content:
    f.write('%s \n' % line)

#for line in forDir:
#    f.write('%s \n' % line )

f.close ()
