# Automated_Blanks_Game
This is an automated version of the Blanks game: a player provides a term that will be looked up on Wikipedia, then random words from the first paragraph of the Wikipedia entry are chosen to be replaced by their part-of-speech (POS) tags. Another player is then prompted to give a word to replace each POS tag. The output is a (hopefully humorous) version of the original paragraph.

Web scraping is done with the help of the requests library, with xml patterns being removed by regular expressions in the manual_retrieve_from_wikipedia function, and xml patterns being removed by the beautifulsoup library in the automatic_retrieve_from_wikipedia function. 

Libraries used: re, requests, Beautiful Soup, nltk. 
This project was one of the assignments for the NYU class: CSCI-UA 381 Programming Tools for the Data Scientist 


Logic of Blanks program:
1. prompt to ask what to search on Wiki
2. returns first paragraph of the article
3. Use nltk.sent_tokenize, nltk.word_tokenize and nltk.pos_tag, to divide into tokens and assign parts of speech to the words.
4. remove stop words
5. only choose words with the following parts of speech: {JJ, JJR, JJS, NN, NNS, NNP, RB, RBR, RBS, VB, VBD, VBG, VBN, VBP, VBZ}
6. prompt to ask how many words to replace, default N = 10
7. choose by random N words to replace
8. interpret what part of speech each of the N words are 
9. prompt to ask for a word to replace each of the N words (no need validation) -> assign to dictionary
10. replace words
11. output final paragraph with replaced words
