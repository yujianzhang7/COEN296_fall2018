# Chinese Poetry Generator with Extended Input Format

We are doing an improvement on the [An RNN-based Chinese Poem Generator](https://github.com/DevinZ1993/Chinese-Poetry-Generation). The program is based on this paper: [Wang et al. 2016](https://arxiv.org/abs/1610.09889). 

We would only deal with 7-char 4-sentences Quatrain. 

## problem
The problem with our basement program is that it cannot handle more than 4 keywords input. 

Another problem is that the rhyme functionality is not working. 

## solution
We extended the input formating. Now it would extract keywords from the user input, no matter sentences or words. We use [Jieba](https://pypi.org/project/jieba/) module to split input sentence input word phrase. We use [Gensim](https://pypi.org/project/gensim/), [word2vec](https://pypi.org/project/word2vec/) and [word rank algorithm](https://github.com/classactcollin/WordRank) to extract from the input value. When the extracted keywords count is less than 4, we could fill up some similar keywords to make it be 4; when the keywords count is more than 4, we could use the highest scored 4 keywords as our input keywords. 

We tried to fix the bug that rhyme funtionality is not working. We also tried to optimize the rhyme detecting algorithm to make it better. However, this seeems not working. 

## system requirement
python 3.6.6

tensorflow 1.8

gensim 3.6.0

jieba 0.39

numpy 1.15.4

## usage
We keep the original usage from the basement project. 

Since the dataset is too large to use the mail system, we put our dataset in the [Github](https://github.com/yujianzhang7/COEN296_fall2018).
### data processing
```
python3 data_utils.py
```
### training
To train both planner model and generator model
```
python3 train.py -a
```
To train only planner model
```
python3 train.py -p
```
To train only generator model
```
python3 train.py -g
```
To erase all trained model
```
python3 train.py -- clean
```
### run 
```
python3 main.py
```
then input the sentence or keywords via stdin 

## 
