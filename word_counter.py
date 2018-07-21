#!/usr/bin/python3.6

f = open("file.txt", "r")
data = f.read()
f.close()

# print(data)

def count_lines(data):
	lines = data.split("\n")
	for l in lines:
		if not l:
			lines.remove(l)
 
	return len(lines)

def count_words(data):
	words = data.split(" ")
	word_count = len(words)
	return word_count


print('Words - {}'.format(count_words(data)))
print('Lines - {}'.format(count_lines(data)))
