from natasha import Segmenter, NewsEmbedding, NewsSyntaxParser, Doc

emb = NewsEmbedding()
segmenter = Segmenter()
syntax_parser = NewsSyntaxParser(emb)


def parse_setence(text):
    doc = Doc(text)
    doc.segment(segmenter)
    doc.parse_syntax(syntax_parser)
    return doc.sents[0].syntax
