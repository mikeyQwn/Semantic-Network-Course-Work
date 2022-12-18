from natasha import MorphVocab

morph_vocab = MorphVocab()


def normalize_link(semanticLinkObject):
    semanticLinkObject.subject = semanticLinkObject.subject.lemma
    # semanticLinkObject.predicate = semanticLinkObject.predicate.lemma
    semanticLinkObject.addition = semanticLinkObject.addition.lemma
