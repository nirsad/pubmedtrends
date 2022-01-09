#csv file to write to

csvfile = open('article_data.csv', 'w+', encoding = 'utf-8')

#number of trending pages to webscrape

pages = 10

titles = []
authors = []
journals = []

for i in range(1,pages + 1,1):

    time.sleep(0.2)
	
    link = 'https://pubmed.ncbi.nlm.nih.gov/trending/?page=' + str(i)

	#get html from trending page

    source = requests.get(link).text

    source = BeautifulSoup(source, 'lxml')

    for j in range(1,11,1):
    
		#search html for article titles
	
        fulldocsum = source.find('article', attrs = {'class':'full-docsum', 'data-rel-pos': str(j)})
        title = fulldocsum.find('a', attrs = {'class':'docsum-title'}).text
        titles.append(title)
        author = fulldocsum.find('span', attrs = {'class':'docsum-authors full-authors'}).text
        authors.append(author)
        journal = fulldocsum.find('span', attrs = {'class':'docsum-journal-citation full-journal-citation'}).text
        journals.append(journal)


#write csv file with each article's title, authors, and citation

for index, title in enumerate(titles):
    titles[index] = title.strip()

csvwriter = csv.writer(csvfile)

fields = ['Title', 'Authors', 'Citations']

csvwriter.writerow(fields)

for i in range (len(titles)):
    csvwriter.writerow([titles[i], authors[i], journals[i]])
                        
csvfile.close()

