import codecs
from konlpy.tag import Twitter
import gensim, logging
pos_tagger = Twitter()
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#C:\\Users\\TH-home\\Desktop\\TH_room\\Lab\\tv_rating\\workspace\\predictDramaRating\\gensim
fileObj = codecs.open("comment_list.txt", "r", "utf-8")
data = [row.split('\t') for row in fileObj.readlines()]
data = data[1:]
datas = []
for row in data:
    temp = [row[1],row[3],row[5]]
    datas.append(temp)
# 1h 16m 47.21s
def tokenize(doc):
    return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]
docs = [(tokenize(row[1]), row[2]) for row in datas]

from pprint import pprint
pprint(docs[0])

from collections import namedtuple

taggedDoc = namedtuple('TaggedDocument','words tags')
tagged_docs = [taggedDoc(d,[c]) for d, c in docs]

sentences=[]
for doc in docs:
    sentences.append(doc[0])
model = gensim.models.Word2Vec(sentences, min_count=5)

model.save('comment_list.model')

###########################################################################

