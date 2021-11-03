class ParsedText:
    
    def __init__(self, filename):
        self.f = open(filename)

    def get_particular_tag(self, tag_list):
        dic = {}
        for line in self.f:
             l = line.split('\t')
             try:
                if l[3] in tag_list:
                   dic[l[1]] = 1
             except:
                continue
        return dic 

fname = '../data/novel/parsed/sentence_tokenised/sentence_tokenised_parsed.txt'
ob = ParsedText(fname)
adverb_dict = ob.get_particular_tag(['RB'])
for key, value in adverb_dict.items():
    print(key)
