
def get_verb_type_distribution(f):
	verb_type = {}
	count = 0
	total = 0
	for line in f:
		line = line.strip('\n')
		l = line.split('\t')

		try:
			root_word = l[0]
			freq = int(l[1])
			try:
				a = word_class[root_word]
				total = total + 1
				if len(a) > 1:
					count = count + 1
					print(root_word,a)
					continue
			except:
				try:
					verb_type[a[0]] = verb_type[a[0]] + freq
				except:
					verb_type[a[0]] = freq
		except:
			continue
	f.close()
	return verb_type

f = open('/Users/jyotijha/Desktop/thesis/ThesisTemplate/data/Hindi_Data/adverb_wordnet/adverb_class_wx.txt','r')

word_class = {}
st_line = 2
lc = 0
temp_d = {}
wrong_temp_d = {}
for line in f:
	line = line.strip('\n')
	l = line.split('\t')
	pos_class1 = l[1]	
	
#	pos_class1 = l[-3]
#	pos_class2 = l[-2]

	if len(pos_class1)==0:# or len(pos_class2)==0:
		continue
	if pos_class1=='TBA':# or pos_class2=='TBA':
		continue
	word = l[0]

#	word = l[0]
	
	result = ''.join([i for i in word if not i.isdigit()])	
	result.replace('_','-')
	try:
		temp_list = word_class[result]
		if pos_class1[0] not in word_class[result]:
			word_class[result].append(pos_class1[0])
#		if pos_class2[0] not in word_class[result]:
#			word_class[result].append(pos_class2[0])
	except:
		word_class[result] = [pos_class1[0]]
#		if pos_class2[0] not in word_class[result]:
#			word_class[result].append(pos_class2[0])

f.close()

f = open('/Users/jyotijha/Desktop/thesis/ThesisTemplate/data/Hindi_Data/novel/Adverb/Premchand/Premchand_total_adverb_wx.txt','r')
n1 = get_verb_type_distribution(f)

f = open('/Users/jyotijha/Desktop/thesis/ThesisTemplate/data/Hindi_Data/novel/Adverb/Agey/Agey_total_adverb_wx.txt','r')

n2 = get_verb_type_distribution(f)

print(n1,sum(n1.values()))
print(n2,sum(n2.values()))
