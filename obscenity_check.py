import requests

def obscenity():
	file = open('filename.txt', 'r')
	content = file.read()
	file.close()
	check_func(content)

def check_func(text):
	response = requests.get('http://www.wdylike.appspot.com/?q=' + str(text))
	if 'true' in response.text:
		print("Alert! Check your document. Curse words found")
	elif 'false' in respose.text:
		print("No curse words found")
	else:
		print("Unable to scan the document")


if __name__ == '__main__':
	obscenity()
