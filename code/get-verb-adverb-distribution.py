root_dic = {}
f = open('/Users/jyotijha/Desktop/thesis/Phase-2/MorphRootTotal_wx.txt','r')
for line in f:
	line = line.strip('\n')
	l = line.split('\t')
	if '-' in l[0] or '_' in l[0]:
		continue
	root_dic[l[0][1:]] = [l[1][1:]+'nA']
f.close()
print(root_dic)
