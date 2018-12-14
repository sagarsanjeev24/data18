from stanfordcorenlp import StanfordCoreNLP
from newspaper import Article
import json

def churn(url):
    article = Article(url)
    article.download()
    article.parse()
    sentence = article.text
    nlp = StanfordCoreNLP('http://localhost', port=9000)
    output = nlp.annotate(sentence)
    nlp.close()
    return output


def ner():
    output_file = '/home/rockerzsag24/Data18/1.txt'
    input = open('/home/rockerzsag24/Data18/2018one.txt', 'r').read()
    input = input.replace('\t', '\n')
    input = input.split('News')
    input = list(map(lambda s: s.strip(), input))
    i = 0
    for article in input:
        output_file = '/home/rockerzsag24/Data18/1/News18_' + str(i) + '.json'
        if article:
            try:
                article_triplet = article.split('|', 3)
                print(article_triplet[2])
            except:
                print('article extraction failed')
                pass
            try:
                output = churn(article_triplet[2])
            except:
                print('churn failed')
                pass
            try:
                with open(output_file, 'w') as f1:
                    #json.dump(output, f1, ensure_ascii=False)
                    #json.dump(article_triplet[0], f1, ensure_ascii=False)
                    js = {"link": article_triplet[2]}
                    js["data"] = output
                    js = json.dumps(js)
                    json.dump(js, f1, ensure_ascii=False)
                    # f1.write('SNOOPER_URL=' + article_triplet[0]+'\n')
                    # f1.write(output)
                    # f1.write('\n')
                    # f1.close()
            except:
                print('file write exception')
        i = i + 1

if __name__ == '__main__':
    ner()
