# NLP-Question-Answering-Generation
This is a project I created for my Natural Language Processing class that takes as input any Wikipedia article and answers questions about the article or generates questions from the article.

answer.py is a demo of question answering using the AllenNLP's Bidaf model for text comprehension. A passage is created using the wikipedia library and a simple question is assigned to String query. 
The Predictor object from AllenNLP is trained on the Bidaf model and the passage and query are passed to the predict function for question answering.

ask.py will be released soon. 
