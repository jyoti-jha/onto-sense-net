import os
import codecs
dir = '../treebank_data/'
authors = os.listdir(dir)
op_dir = '../parsed_treebank_combined/'
if not os.path.exists(op_dir):
    	os.makedirs(op_dir)
op_file = op_dir + 'total.txt'
print(op_file)

w = codecs.open(op_file,'w',encoding='utf-8')
for author in authors:
	print author
	if author=='.DS_Store':
		continue
	novels = os.listdir(dir + author)
#	op_dir = '../Phase-2/novels/combined_Premchand/' + novel + "/"
#	w = codecs.open(op_dir + novel + ".txt",'w',encoding='utf-8')
	for novel in novels:
		if novel == '.DS_Store':
			continue
		chapters = os.listdir(dir + author + "/" + novel )
		for chapter in chapters:
			if chapter=='.DS_Store':
				continue
			FileName = dir +   author + "/" + novel + "/" + chapter
			print FileName
			f =  codecs.open(FileName,'r',encoding='utf-8')
			for line in f:
				w.write(line)
			f.close()
#	w.close()
w.close()
