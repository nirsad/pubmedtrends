def getFrequencyDictForText(sentence):
    fullTermsDict = multidict.MultiDict()
    tmpDict = {}

    # making dictionary for counting word frequencies
    for text in sentence.split(" "):
        # remove irrelevant words
        if re.match("a|the|an|the|to|in|for|of|or|by|with|is|on|that|but|from|than|be", text):
            continue
        val = tmpDict.get(text, 0)
        tmpDict[text.lower()] = val + 1
    for key in tmpDict:
        fullTermsDict.add(key, tmpDict[key])
    return fullTermsDict

def makeImage(text):

    wc = WordCloud(width = 3000, height = 1080, background_color="white", colormap = 'Dark2', max_words=200)
    # generate word cloud
    wc.generate_from_frequencies(text)

    # save
    plt.imshow(wc)
    plt.axis("off")
    datestring = date.today().strftime("%b-%d-%Y")
    plt.text(860, -50, 'Date Generated: ' + datestring)
    filename = datestring + '.png'
    plt.savefig(os.path.join(os.getcwd(), '..', './static', filename), dpi = 400, bbox_inches='tight')

# get text from existing word file

tifile = open(os.path.join(os.getcwd(), '..','words.txt'), 'r')
text = tifile.read()
makeImage(getFrequencyDictForText(text))
tifile.close()
