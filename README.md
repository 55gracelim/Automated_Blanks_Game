# Automated_Blanks_Game
This is an automated version of the Blanks game: a player provides a term that will be looked up on Wikipedia, then random words from the first paragraph of the Wikipedia entry are chosen to be replaced by their part-of-speech (POS) tags. Another player is then prompted to give a word to replace each POS tag. The output is a (hopefully humorous) version of the original paragraph.
web scraping is done with the help of the requests library in two ways: manual and automated
    manual: makes use of regular expressions to remove the xml patterns
    automated: makes use of the beautifulsoup library to remove the xml patterns
libraries used: re, requests, Beautiful Soup, nltk
this project was one of the assignments for the NYU class CSCI-UA 381 Programming Tools for the Data Scientist 
