import re,collections

def words(text):	#获取数据集的小写字母版本
	return re.findall('[a-z]+',text.lower())

def train(features):
	model = collections.defaultdict(lambda:1)	#单词个数至少为1
	for f in features:
		model[f] += 1
	return model

NEWORDS = train(words(open('big.txt').read()))	#获取一个字典，key为单词，lambda值为单词出现个数
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edist1(word):
	n = len(word)
	return set([word[0:i] + word[i+1:] for i in range(n)] + 
		[word[0:i] + c + word[i+1:] for i in range(n+1) for c in alphabet] + 
		[word[0:i] + word[i+1] + word[i] + word[i+2:] for i in range(n-1)] + 
		[word[0:i] + c + word[i+1:] for i in range(n) for c in alphabet])

def edist2(word):
	return set(e2 for e1 in edist1(word) for e2 in edist1(e1))


def known(words):
	return set(w for w in words if w in NEWORDS)

def correct(word):
	candidates = known([word]) or known(edist1(word)) or known(edist2(word)) or [word]
	return max(candidates,key = lambda w :NEWORDS[w])
