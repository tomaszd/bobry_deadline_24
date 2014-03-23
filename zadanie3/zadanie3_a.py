import sys
sys.path.append("..")
import common

'''tutaj leci kod''' 

def calc_price(word):
	price = {}
	for i in word:
		if(price.has_key(i)):
			price[i] += 1
		else:
			price[i] = 1
	return price;


i = 2;
data = common.load_data('../dane/sets/inter0' + str(i) + '.in')
alph = 'abcdefghijklmnopqrstuvwxyz'
al = {}

left_data = data[0]
left_data = left_data.split(' ')

for i in range(0,26):
	al[alph[i]] = int(left_data[i])

lines = int(data[1])

words = []
sents = []

#read lines
for i in range(2, lines+2):
		
	if data[i][-1] == '\n':
		data[i] = data[i][:-1]
	if data[i][-1] == ' ':
		data[i] = data[i][:-1]
	line_data = data[i].split(' ')
	s = int(line_data[0])
	m = int(line_data[1])
	for word in line_data[2:]:
		words.append(word)
	sents.append({
			's' : s,
			'm' : m,
			'words' : line_data[2:]
		})
#all data loaded

print words

best_result = []
best_result_score = 0


print 'calculating'
print '-' * 40
def rec(word, curr_al, word_list, possible_words):
	price = calc_price(word)
	for i in price:
		if(curr_al[i] < price[i]):
			#print word_list, ' ', word, ' -'
			return 0
	for i in price:
		curr_al[i] -= price[i]
	#print word_list, ' ', word, ' +'
	word_list.append(word)
	ways_of_dev = 0

	pos = 0
	if possible_words.count(word) > 1:
		possible_words.remove(word)
		u_possible_words = unique(possible_words)
		pos = u_possible_words.index(word)
	else:
		u_possible_words = unique(possible_words)
		pos = u_possible_words.index(word)
		possible_words.remove(word)
		u_possible_words = unique(possible_words)
	for i in u_possible_words[pos:]:
		ways_of_dev += rec(i,dict(curr_al), list(word_list), list(possible_words))

	if ways_of_dev == 0:
		result = 0
		for sent in sents:
			occur = 0
			local_word_list = list(word_list)
			for word in sent['words']:
				if word in local_word_list:
					occur += 1
					result += sent['s']
					local_word_list.remove(word)

			if occur == len(sent['words']):
				result += sent['m']

		global best_result_score
		global best_result
		if(best_result_score < result):
			print ' calculating: ', word_list
			best_result_score = result
			best_result = word_list
	return 1

words.sort()

def unique(list):
	ret = []
	for i in list:
		if(i not in ret):
			ret.append(i)
	return ret

u_words = unique(words)
for i in u_words:
	rec(i,dict(al), [], list(words))

print '*' * 30
print best_result
print best_result_score



