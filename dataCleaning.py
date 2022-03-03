#read csv file

article_data = pd.read_csv(os.path.join(os.getcwd(), '..','article_data.csv'), encoding = 'utf-8')

words2lists = []
words1list = []

#split all titles into words

for line in article_data['Title']:
    
    if (line.split() == []):
        continue
    else:
        words2lists.append(line.split())

for x in words2lists:
    for y in x:
        words1list.append(y)


#clean data


for index, word in enumerate(words1list):
    #convert to lowercase
    lowercaseword = word.lower()
	#remove special characters other than hyphens (-) and periods (.)
    charrw1 = re.sub('[^0-9a-zA-Z-\.]', '', lowercaseword)
	#remover periods (.) at the ends of words
    charrw2 = re.sub('\.$', '', charrw1)
    words1list[index] = charrw2
	#remove words with only special characters and numbers
    if (re.match('[^a-zA-Z]', charrw2)):
        words1list[index] = ''

#remove empty strings

for word in words1list:
    if (word == ''):
        words1list.remove(word)


#write all words to a text file

wordsfile = open(os.path.join(os.getcwd(), '..','words.txt'), 'w+')

for word in words1list:
    wordsfile.write(word + ' ')

wordsfile.close()

