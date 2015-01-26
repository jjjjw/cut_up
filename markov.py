"""
Neat resources:
http://setosa.io/blog/2014/07/26/markov-chains/
http://www.dartmouth.edu/~chance/teaching_aids/books_articles/probability_book/Chapter11.pdf
https://github.com/substack/node-markov/blob/master/index.js
https://golang.org/doc/codewalk/markov/
"""

from normalizer import Normalizer
from random import Random


class Markov(object):

  def __init__(self, prefix_len = 3, corpus = None, seed = 1):
    self.prefix_len = prefix_len
    self.normalizer = Normalizer()
    self.random = Random(seed)
    self.chain = {}

    if corpus:
      self.ingest(corpus)

  def ingest(self, corpus):
    # TODO(jj): improve tokenizer ("tokenizer")
    tokens = self.normalizer.normalize_symbol_boundaries(corpus).split()

    for ii, token in enumerate(tokens):
      if (ii + self.prefix_len) > len(tokens) - 1:
        continue

      prefix = ' '.join(tokens[ii:ii + self.prefix_len])
      suffix = tokens[ii + self.prefix_len]

      if not self.chain.get(prefix):
        self.chain[prefix] = []

      self.chain[prefix].append(suffix)

  def next(self, key):
    choices = self.chain[key]
    if not len(choices):
      return None

    choice = self.random.randint(0, len(choices) - 1)

    return choices[choice]

  def get_key(self):
    keys = self.chain.keys()
    choice = self.random.randint(0, len(keys) - 1)
    return list(keys)[choice]


if __name__ == '__main__':
  markov = Markov()
