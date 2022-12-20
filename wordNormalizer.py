from natasha import MorphVocab

morph_vocab = MorphVocab()


def normalize_link(semanticLinkObject):
    # semanticLinkObject.subject = semanticLinkObject.subject.lemma
    semanticLinkObject.subject = (
        semanticLinkObject.subject.text
        if (hasattr(semanticLinkObject.subject, "text"))
        else semanticLinkObject.subject
    )
    semanticLinkObject.predicate = (
        semanticLinkObject.predicate.text
        if (hasattr(semanticLinkObject.predicate, "text"))
        else semanticLinkObject.predicate
    )
    semanticLinkObject.addition = semanticLinkObject.addition.lemma
