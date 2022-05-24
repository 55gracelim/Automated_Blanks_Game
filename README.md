# Automated_Blanks_Game
This is an automated version of the Blanks game: a player provides a term that will be looked up on Wikipedia, then random words from the first paragraph of the Wikipedia entry are chosen to be replaced by their part-of-speech (POS) tags. Another player is then prompted to give a word to replace each POS tag. The output is a (hopefully humorous) version of the original paragraph.

Web scraping is done with the help of the requests library, with xml patterns being removed by regular expressions in the manual_retrieve_from_wikipedia function, and xml patterns being removed by the beautifulsoup library in the automatic_retrieve_from_wikipedia function. 

Libraries used: re, requests, Beautiful Soup, nltk. 
This project was one of the assignments for the NYU class: CSCI-UA 381 Programming Tools for the Data Scientist 
