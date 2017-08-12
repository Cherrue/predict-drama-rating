#import gensim, logging
#import codecs
#from gensim.models import Doc2Vec
#from gensim.models.doc2vec import LabeledSentence

#fileObj = codecs.open("comment_list.txt", "r", "utf-8")
#u = fileObj.readlines()
#uid = 0

#doc=[]
#docs = []
#for row in u:
    #line = row.split("\t")
    #line[3] = line[3].replace('"','')
    #doc = LabeledSentence(line[3].strip().split(" "), ['SENT_'+str(uid)])
    #docs.append(doc)
    #uid+=1

#model = Doc2Vec(size=10,alpha=.025, min_alpha=.025,seed=1234,min_count=1,workers=4,window=8)
#model.build_vocab(docs)

##sentence0 = LabeledSentence(['some','words','here'],['SENT_0'])
##sentence1 = LabeledSentence(['here','we','go'],['SENT_1'])
##sentences = [sentence0,sentence1]
##model.build_vocab(sentences)

#for epoch in range(10):
    #model.train(docs)
    #model.alpha -= 0.002
    #model.min_alpha = model.alpha
    
import codecs    
from konlpy.tag import Twitter
pos_tagger = Twitter()

fileObj = codecs.open("comment_list.txt", "r", "utf-8")
data = [row.split('\t') for row in fileObj.readlines()]
data = data[1:]
datas = []
for row in data:
    temp = [row[1],row[3],row[5]]
    datas.append(temp)

def tokenize(doc):
    # norm, stem은 optional
    return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]
docs = [(tokenize(row[1]), row[2]) for row in datas]

from pprint import pprint
pprint(docs[0])

from collections import namedtuple

taggedDoc = namedtuple('TaggedDocument','words tags')
tagged_docs = [taggedDoc(d,[c]) for d, c in docs]

from gensim.models import doc2vec
doc_vectorizer = doc2vec.Doc2Vec(size=300,alpha=0.025,min_alpha=0.025,seed=1234)
doc_vectorizer.build_vocab(tagged_docs,total_words=len(tagged_docs),epochs=epoch)
for epoch in range(10):
    doc_vectorizer.train(tagged_docs,total_words=len(tagged_docs),epochs=epoch)
    doc_vectorizer.alpha -= 0.002
    doc_vectorizer.min_alpha = doc_vectorizer.alpha
