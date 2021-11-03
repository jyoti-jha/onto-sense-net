import gensim, logging
import os
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# or run truncated Singular Value Decomposition (SVD) on the streamed corpus



class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()
 
sentences = MySentences('../data/novel/sentence_tokenized/combined/wx/') # a memory-friendly iterator
print("sentence objected created")
model = gensim.models.Word2Vec(sentences,min_count=1,vector_size=100,sg=1)
print("model built")
model.save('model_dim_100_sg.word2vec')
print("model saved")
