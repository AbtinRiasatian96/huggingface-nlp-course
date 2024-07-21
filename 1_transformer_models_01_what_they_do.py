from transformers import pipeline
from flair.data import Sentence
from flair.models import SequenceTagger

# sentiment_classifier = pipeline("sentiment-analysis")
# sentiment = sentiment_classifier("I've been waiting for a HuggingFace course my whole life.")

# sentence_list = ["I've been waiting for a HuggingFace course my whole life.", "I F'in hate this shit!"]
# sentiment_list = sentiment_classifier(sentence_list)
# print(sentiment_list)

# feature_extractor = pipeline("feature-extraction")
# feature_list = feature_extractor(sentence_list)
# print(len(feature_list[1][0]))

# zero_shot_classifier = pipeline("zero-shot-classification")
# sentence = "This is a course about the Transformers library"
# label_list = ["education", "politics", "business"]
# output = zero_shot_classifier(sentence, candidate_labels=label_list)
# print(output)

# text_generator = pipeline("text-generation", model="distilgpt2")
# output = text_generator("My favorite sports club is not", num_return_sequences=2, max_length=200)
# print(output)

# unmasker = pipeline("fill-mask")
# output = unmasker("This  movie will teach you all about <mask> models.", top_k=4)
# print(output)
# for dict_ in output:
#     print(dict_['token_str'])

# text = "My name is Sylvain and I work at Hugging Face in Brooklyn."
# ner = pipeline("ner", grouped_entities=True, model='bert-base-uncased')
# output = ner(text)
# print(output)

# tagger = SequenceTagger.load("flair/pos-english")
# sentence = Sentence("I love Berlin.")
# tagger.predict(sentence)
# print(sentence)
# print('The following NER tags are found:')
# for entity in sentence.get_spans('pos'):
#     print(entity)

# question_answerer = pipeline("question-answering")
# question_ = "Where do I work?"
# context_ = "My name is Sylvain and I work at an early stage startup in Brooklyn"
# output = question_answerer(question=question_, context=context_)
# print(output)


# text = """
#         America has changed dramatically during recent years. Not only has the number of 
#         graduates in traditional engineering disciplines such as mechanical, civil, 
#         electrical, chemical, and aeronautical engineering declined, but in most of 
#         the premier American universities engineering curricula now concentrate on 
#         and encourage largely the study of engineering science. As a result, there 
#         are declining offerings in engineering subjects dealing with infrastructure, 
#         the environment, and related issues, and greater concentration on high 
#         technology subjects, largely supporting increasingly complex scientific 
#         developments. While the latter is important, it should not be at the expense 
#         of more traditional engineering.

#         Rapidly developing economies such as China and India, as well as other 
#         industrial countries in Europe and Asia, continue to encourage and advance 
#         the teaching of engineering. Both China and India, respectively, graduate 
#         six and eight times as many traditional engineers as does the United States. 
#         Other industrial countries at minimum maintain their output, while America 
#         suffers an increasingly serious decline in the number of engineering graduates 
#         and a lack of well-educated engineers.
#     """
# summarizer = pipeline("summarization")
# output = summarizer(text)
# print(output)

# translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
# output = translator("Bonjour! Ce cours est produit par Hugging Face.")
# print(output)