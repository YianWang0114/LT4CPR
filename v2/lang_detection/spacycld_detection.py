import spacy
from spacy.language import Language
from spacy_cld import LanguageDetector
from spacy.tokens import Doc

#Doc.set_extension(default, force=True)
language_detector = LanguageDetector()

@Language.component("language_detector")
def custom_language_detector(doc):
    language_detector(doc)
    return doc

nlp = spacy.load('en_core_web_sm')

# Check if the language_detector pipe is already added
if "language_detector" not in nlp.pipe_names:
    nlp.add_pipe("language_detector")

doc = nlp('Kailangan ko ng mas maraming karanasan sa trabaho.')

print(doc._.languages)
print(doc._.language_scores['tl'])