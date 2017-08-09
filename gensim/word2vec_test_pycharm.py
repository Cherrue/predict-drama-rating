# import gensim, logging
# import codecs
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#
# fileObj = codecs.open("pos_list.txt", "r", "utf-8")
# u = fileObj.readlines()
# uid = 0
# beforeWriter = u[0][1]
# sentence = []
# sentences = []
# for row in u:
#     line = row.split("\t")
#     if beforeWriter != line[1]:
#         print(line[0], line[1], sentence)
#         sentences.append(sentence)
#         sentence = [line[3]]
#         uid += 1
#         beforeWriter = line[1]
#     else:
#         sentence.append(line[3])
#
# model = gensim.models.Word2Vec(sentences, min_count=5)
#
# model.save('word2vec_test_pychar_model')
import gensim
new_model = gensim.models.Word2Vec.load('word2vec_test_pychar_model')
print(new_model.wv['선보'])