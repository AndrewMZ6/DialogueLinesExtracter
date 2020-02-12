import os 
from bs4 import BeautifulSoup as bs

# Creating a list containing all the file names in a directory
xmlList = os.listdir(r'D:\...\Skyrim Special Edition\Data\DialogueViews') 

# So the list looks like this xmlList = ['01003076.xml', '0004AFD5.xml', '0003F89A.xml', ...]

r = 0

for file in xmlList:

	r += 1
	
	# This is the directory where the extracted files loaded. Extracted file names look like "1.txt", "2.txt", ...
	name = r'C:\...\Desktop\ExtractedFiles\\' + str(r) + '.txt'
	
	writefile = open(name, mode='w')
	
	infile = open(path, 'r')
	
	content = infile.read()
	
	soup = bs(content, 'lxml')
	
	texts = soup.find_all('text')
	
	x = 0
	
	for i in texts:
	
		x += 1
		
		l = i.get_text()
		
		if l:      # We don't need empty lines
		
			writefile.write(str(x) + ' -- ' + l + '\n')  # The record looks like '1 -- extracted lines', '2 -- extracted lines', ...
			
	writefile.close()
