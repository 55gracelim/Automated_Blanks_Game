import requests
import re
import random
import bs4
import nltk
#nltk.download('averaged_perceptron_tagger')

basic_wikipedia_search_url = "https://en.wikipedia.org/wiki/"
xml_pattern = re.compile(r'<([/!?]?)([a-z?\-]+)[^>]*>',re.I)

stop_words = ['a','the','an','and','or','but','about','above','after','along','amid','among',\
                           'as','at','by','for','from','in','into','like','minus','near','of','off','on',\
                           'onto','out','over','past','per','plus','since','till','to','under','until','up',\
                           'via','vs','with','that','can','cannot','could','may','might','must',\
                           'need','ought','shall','should','will','would','have','had','has','having','be',\
                           'is','am','are','was','were','being','been','get','gets','got','gotten',\
                           'getting','seem','seeming','seems','seemed',\
                           'enough', 'both', 'all', 'your' 'those', 'this', 'these', \
                           'their', 'the', 'that', 'some', 'our', 'no', 'neither', 'my',\
                           'its', 'his' 'her', 'every', 'either', 'each', 'any', 'another',\
                           'an', 'a', 'just', 'mere', 'such', 'merely' 'right', 'no', 'not',\
                           'only', 'sheer', 'even', 'especially', 'namely', 'as', 'more',\
                           'most', 'less' 'least', 'so', 'enough', 'too', 'pretty', 'quite',\
                           'rather', 'somewhat', 'sufficiently' 'same', 'different', 'such',\
                           'when', 'why', 'where', 'how', 'what', 'who', 'whom', 'which',\
                           'whether', 'why', 'whose', 'if', 'anybody', 'anyone', 'anyplace', \
                           'anything', 'anytime' 'anywhere', 'everybody', 'everyday',\
                           'everyone', 'everyplace', 'everything' 'everywhere', 'whatever',\
                           'whenever', 'whereever', 'whichever', 'whoever', 'whomever' 'he',\
                           'him', 'his', 'her', 'she', 'it', 'they', 'them', 'its', 'their','theirs',\
                           'you','your','yours','me','my','mine','I','we','us','much','and/or']
    
tags = ['JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'RB', 'RBR', 'RBS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

def non_match(entry):
    if re.search('<b>Wikipedia does not have an article with this exact name.</b>',entry,re.I):
        return(True)
    else:
        return(False)

def remove_xml(string):
    global xml_pattern
    output = xml_pattern.sub('',string)
    return(output)

def look_up_wikipedia_page_from_internet(search_term):
    global basic_wikipedia_search_url
    search_term = search_term.replace(' ','_')
    url = basic_wikipedia_search_url+search_term
    response = requests.get(url).text
    return(response)

def manual_retrieve_from_wikipedia(search_term):
    full_page = look_up_wikipedia_page_from_internet(search_term)

    if non_match(full_page):
        first_paragraph = "***No Wikipedia Entry Found***" 
    else:
        paragraph_start = re.compile('<p[^>]*>')
        paragraph_end = re.compile('</p>')
        start = 0
        output = ""
        next_paragraph_start = paragraph_start.search(full_page,start)
        if next_paragraph_start:
            start = next_paragraph_start.end()
            next_paragraph_end = paragraph_end.search(full_page,start)
            if next_paragraph_end:
                end = next_paragraph_end.start()
                text = remove_xml(full_page[start:end])
                if re.search('[a-z]{3}',text):
                    output += text           
        first_paragraph = re.sub('&#[0-9][0-9][0-9]?;[0-9]*[a-zA-Z]*&#[0-9][0-9][0-9]?;',' ',output)
    
    return(first_paragraph)

def automatic_retrieve_from_wikipedia(search_term):
    full_page = look_up_wikipedia_page_from_internet(search_term)

    if non_match(full_page):
        first_paragraph = "***No Wikipedia Entry Found***"
    else:
        html = bs4.BeautifulSoup(full_page, 'html.parser')
        paragraphs = html.select("p")
        first_paragraph = paragraphs[0].text
        first_paragraph = re.sub('\[[0-9]*[a-zA-Z]*\]',' ',first_paragraph)
    return(first_paragraph) 

def interpret_pos(pos_tag):
    pos_dict = {'NNP':"Name", 'NN':"Singular Noun", 'NNS':"Plural Noun", 'VB':"Simple Verb",\
                'VBD':"Past Tense Verb",'VBG':"-ing Verb",'VBN':"Past Participle Verb",'VBP':"Simple Verb",\
                'VBZ':"-s Verb",'JJ':"Adjective",'JJR':"Comparative Adjective",'JJS':"Superlative Adjective",\
                'RB':"Adverb",'RBR':"Comparative Adverb",'RBS':"Superlative Adverb"}
    return(pos_dict[pos_tag])

def automated_blanks_game():
    entry = str(input("What would you like your Blanks game to be about? "))
    first_paragraph = manual_retrieve_from_wikipedia(entry)
    
    words_plus_pos_2 = []
    sentences = nltk.sent_tokenize(first_paragraph)
    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)
        words_plus_pos = nltk.pos_tag(tokens) #assign parts of speech to tokens
    
        for (word, tag) in words_plus_pos:
            #only choose words with pos in wanted tags list, not choose words in the stop_words list, make sure chosen words are fully letters
            if (tag in tags) and (word not in stop_words) and (word.isalpha()): 
                pos_tuple = (word,tag)
                if pos_tuple not in words_plus_pos_2: 
                    words_plus_pos_2.append(pos_tuple) #make list of distinct words to be replaced             
    first_paragraph_tokenized = words_plus_pos_2

    print()
    print("Here is the first paragraph of that search:")
    print(first_paragraph)
   
    wordAmt = int(input("How many words do you want to replace? "))
    if (isinstance(wordAmt, int)) == False:
        wordAmt = 10 #default N=10
            
    randomWordList = random.sample(first_paragraph_tokenized, wordAmt) #randomize N (distinct) words to be replaced
    
    old_new_dict = {}
    k = 0
    while k < wordAmt:
        pos = interpret_pos(randomWordList[k][1]) #translate from NLTK pos jargon to English
        word = str(input("Give me a word belonging to the category *" + str(pos) + "*: " )) #prompt user to replace each of the N words
        old_new_dict[randomWordList[k][0]] = word
        k += 1
 
    #replace all occurences of word by using dictionary
    first_prgph_final = []
    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)
        for token in tokens:
            first_prgph_final.append(old_new_dict.get(token,token))
    first_prgph_final = ' '.join(first_prgph_final)

    output = str(first_prgph_final)
    print()
    print("Thanks for playing Blanks! Here's your edited search:")
    print(output)
    
automated_blanks_game()