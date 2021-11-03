
def get_verb_type_distribution(f):
	verb_type = {}
	count = 0
	total = 0
	for line in f:
		line = line.strip('\n')
		l = line.split('\t')

		try:
			root_word = root_dic[l[0]][0]
			freq = int(l[1])
			try:
				a = word_class[root_word]
				total = total + 1
				if len(a) > 1:
					count = count + 1
					print root_word,a
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

root_dic = {}
f = open('/Users/jyotijha/Desktop/thesis/Phase-2/MorphRootTotal_wx.txt','r')
for line in f:
	line = line.strip('\n')
	l = line.split('\t')
	if '-' in l[0] or '_' in l[0]:
		continue
	root_dic[l[0][1:]] = [l[1][1:]+'nA']
f.close()
f = open('/Users/jyotijha/Desktop/thesis/ThesisTemplate/data/Hindi_Data/verbs_parsed_data_tok-corpus/verb_root_wx.txt','r')

for line in f:
	line = line.strip('\n')
	l = line.split(',')
	if '-' in l[0] or '_' in l[0]:
		continue
	try:
		if l[1] in root_dic[l[0]]:
			continue
		root_dic[l[0]].append(l[1] + 'nA')
	
	except:
		root_dic[l[0]] = [l[1] + 'nA']

f.close()

f = open('/Users/jyotijha/Desktop/thesis/ThesisTemplate/data/Hindi_Data/verb_wordnet/Verb_onto_wx.txt','r')

word_class = {}
st_line = 2
lc = 0
temp_d = {}
wrong_temp_d = {}
for line in f:
	lc = lc + 1
	if lc < st_line:
		continue
	line = line.strip('\n')
	l = line.split('\t')
	pos_class1 = l[-4]
	pos_class2 = l[-3]	
	
#	pos_class1 = l[-3]
#	pos_class2 = l[-2]

	if len(pos_class1)==0:# or len(pos_class2)==0:
		continue
	if pos_class1=='TBA':# or pos_class2=='TBA':
		continue
	word = l[1]

#	word = l[0]
	
	result = ''.join([i for i in word if not i.isdigit()])	

	if pos_class1 == 'Means|End':
		pos_class1 = 'A'
#	if pos_class2 == 'Means|End':
#		pos_class2 = 'A'
#	if pos_class2[0] == 'Q':
#		pos_class2 = 'Know|Known'
        if pos_class1[0] == 'Q':
		pos_class1 = 'Know|Known'

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

print(word_class)
print word_class.keys()
print "***************************************************************************************************"
#f = open('/Users/jyotijha/Desktop/thesis/ThesisTemplate/data/Hindi_Data/novel/Verb/Premchand/Premchand_total_verb_wx.txt','r')
#f = open('/Users/jyotijha/Desktop/thesis/ThesisTemplate/data/Hindi_Data/novel/Verb/Premchand/Premchand_total_verb_wx.txt','r')
#n1 = get_verb_type_distribution(f)

#f = open('/Users/jyotijha/Desktop/thesis/ThesisTemplate/data/Hindi_Data/novel/Verb/Agey/Agey_total_verb_wx.txt','r')

#n2 = get_verb_type_distribution(f)

#print n1,sum(n1.values())
#print n2,sum(n2.values())
