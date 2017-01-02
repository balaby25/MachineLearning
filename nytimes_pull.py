import urllib.request
import json

def main(api_key, category, label):

    Content = []
    for i in range(1,8):
        urlData = "http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:(\"%s\")&api-key=%s&page=%d" % (category, api_key,i)
        webURL = urllib.request.urlopen(urlData)
        Data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        try:
            result = json.loads(Data.decode(encoding))
            Content.append(result)
        except ValueError:
            print ("Malformed JSON: " + data)
            continue #In te rare cases that JSON refuses to parse

    f = open(label,'w')

    for line in Content:
        # print ( line )
        try:
            f.write('%s\n' % line)
        except UnicodeEncodeError:
            pass

    f.close ()

if __name__ == '__main__':
    main("0f8b796919ee4e9ab96874776d9a6bec", "Arts", "Balarts.txt")
    main("0f8b796919ee4e9ab96874776d9a6bec", "Sports", "BalaSports.txt")
#        main("0f8b796919ee4e9ab96874776d9a6bec", "Sports", "BalaSports")
