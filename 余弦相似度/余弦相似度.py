import jieba
import math
s1 = '雅诗兰黛（Estee Lauder） 雅诗兰黛眼霜肌透修护眼部精华霜小棕瓶眼霜 ANR眼霜15ml'
s1_cut = [i for i in jieba.cut(s1, cut_all=True) if i != '']
s2 = '雅诗兰黛（Estee Lauder）肌透修护眼部精华霜 15ml（眼霜 ANR 提拉紧致 淡化细纹 黑眼圈）'
s2_cut = [i for i in jieba.cut(s2, cut_all=True) if i != '']
# print(s1_cut)
# print(s2_cut)



word_set = set(s1_cut).union(set(s2_cut))
print(word_set)

word_dict = dict()
i = 0
for word in word_set:
    word_dict[word] = i
    i += 1
print(word_dict)

s1_cut_code = [word_dict[word] for word in s1_cut]
print(s1_cut_code)
s1_cut_code = [0]*len(word_dict)

for word in s1_cut:
    s1_cut_code[word_dict[word]]+=1
# print(s1_cut_code)

s2_cut_code = [word_dict[word] for word in s2_cut]
# print(s2_cut_code)
s2_cut_code = [0]*len(word_dict)
for word in s2_cut:
    s2_cut_code[word_dict[word]]+=1
# print(s2_cut_code)

# 计算余弦相似度
sum = 0
sq1 = 0
sq2 = 0
for i in range(len(s1_cut_code)):
	sum += s1_cut_code[i] * s2_cut_code[i]
	sq1 += pow(s1_cut_code[i], 2)
	sq2 += pow(s2_cut_code[i], 2)

try:
	result = round(float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)), 2)
except ZeroDivisionError:
    result = 0.0
print(result)