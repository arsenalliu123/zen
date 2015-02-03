import string
import collections

def q2(sentence):
	alpha = collections.OrderedDict()
	for char in string.lowercase:
		alpha[char] = 1
	for char in sentence:
		char = char.lower()
		if len(alpha) == 0: return ""
		if char in alpha and alpha[char] == 1: alpha[char] -= 1
	ret = ""
	for char in alpha:
		if alpha[char] > 0:
			ret += char
	return ret

if __name__ == "__main__":
	sentence = raw_input()
	print q2(sentence)