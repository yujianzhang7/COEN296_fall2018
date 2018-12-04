# Chinese Poetry Generator with Extended Input Format

We are doing an improvement on the [An RNN-based Chinese Poem Generator](https://github.com/DevinZ1993/Chinese-Poetry-Generation). The program is based on this paper: [Wang et al. 2016](https://arxiv.org/abs/1610.09889). 

## problem
The problem with our basement program is that it cannot handle more than 4 keywords input. 

Another problem is that the rhyme functionality is not working. 

## solution
We extended the input formating. Now it would extract keywords from the user input, no matter sentences or words. We use [Jieba](https://pypi.org/project/jieba/) module to split input sentence input word phrase. We use [Gensim](https://pypi.org/project/gensim/), [word2vec](https://pypi.org/project/word2vec/), 