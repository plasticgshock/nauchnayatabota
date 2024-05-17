from transformers import pipeline
pipe = pipeline("text-classification", model="akshayvkt/detect-ai-text")
from googletrans import Translator as T

trans = T()


def toTokens(bred: str) -> str:
    src_lang = trans.detect(bred).lang
    if src_lang == 'en':
        return bred
    tar_lang = 'en'
    res = trans.translate(bred, src=src_lang, dest=tar_lang)
    return res.text


def classificate(bred: str) -> dict:
    to_classif = toTokens(bred)
    classification = pipe(to_classif)
    return classification[0]

