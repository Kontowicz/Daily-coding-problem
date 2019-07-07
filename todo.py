import re

def find(path):
	numbers = set()
	with open(path + 'README.md', 'r') as file:
		data = file.readlines()
		pattern = r'\| (\d+).*'
		for line in data:
			match = re.search(pattern, line)
			if match:
				numbers.add(int(match.group(1)))
				
	m = max(numbers)
	
	for i in range(1, m + 1):
		if i not in numbers:
			print(i)
			
find('./')