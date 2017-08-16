#train
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
#         uid +=word
#         beforeWriter = line[1]
#     else:
#         sentence.append(line[3])
#
# model = gensim.models.Word2Vec(sentences, min_count=5)
#
# model.save('word2vec_test_pychar_model')
import gensim
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import pandas as pd
model = gensim.models.Word2Vec.load('word2vec_test_pychar_model')
# scatter
#print(new_model.wv['선보'])
#
# vocab = list(model.wv.vocab)
# X = model[vocab]
# sample_X = X[:100]
#
# tsne = TSNE(n_components=2)
# X_tsne = tsne.fit_transform(sample_X)
# print("df start")
# df = pd.concat([pd.DataFrame(X_tsne),
#                 pd.Series(vocab)],
#                axis=1)
#
# print("df finish")
# df.columns = ['x', 'y', 'word']
#
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
#
# ax.scatter(df['x'], df['y'])
#
# #for i, txt in enumerate(df['word']):
# #    ax.annotate(txt, (df['x'].iloc[i], df['y'].iloc[i]))
#
# fig.show()

# test
print(model.most_similar(positive=['보영','정석']))