from nltk.corpus import stopwords
import nltk

def plural(word):
	if word.endswith("y"):
		return word[:-1] +"ies"
	elif word[-1] in "sx" or word[-2:] in ["sh", "ch"]:
		return word + "es"
	elif word.endswith("an"):
		return word[:-2] + "en"
	else:
		return word + "s"


def unusual_words_en(text):
	text_vocab = set(w.lower() for w in text if w.isalpha())
	english_vocab = set(w.lower() for w in nltk.corpus.words.words())
	unusual = text_vocab - english_vocab
	return sorted(unusual)


def vocab_wo_noise(atext, lang="english"):
	'''removes noise (stopwords, urls, punctuation) from a list of words'''
	stop_words = nltk.corpus.stopwords.words(lang)
	content = [w for w in atext if w.lower() not in stop_words]
	content = [w for w in content if len(w) > 2 and not "/" in w]
	return content


def lexical_diversity(text):
	return len(set(text)) / len(text)