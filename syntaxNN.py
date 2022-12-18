from natasha import (
    Segmenter,
    NewsEmbedding,
    NewsSyntaxParser,
    Doc,
    NewsMorphTagger,
    MorphVocab,
)

emb = NewsEmbedding()
segmenter = Segmenter()
syntax_parser = NewsSyntaxParser(emb)
morph_tagger = NewsMorphTagger(emb)
morph_vocab = MorphVocab()


def parse_setence(text):
    doc = Doc(text)
    doc.segment(segmenter)

    doc.tag_morph(morph_tagger)
    print("--Tokens--")
    for token in doc.tokens:
        token.lemmatize(morph_vocab)
        print(token)

    print("--Tokens--")
    doc.parse_syntax(syntax_parser)
    # for sent in doc.sents[0]:
    #     print("Sentance: ", sent)
    # (doc.sents[0].syntax).print()
    return doc.sents[0]
