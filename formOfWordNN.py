from natasha import MorphVocab

morph_vocab = MorphVocab()


def normalize_link(semanticLinkObject):
    semanticLinkObject.subject = semanticLinkObject.subject.lemma
    semanticLinkObject.predicate = (
        semanticLinkObject.predicate.text
        if (hasattr(semanticLinkObject.predicate, "text"))
        else semanticLinkObject.predicate
    )
    semanticLinkObject.addition = semanticLinkObject.addition.lemma
