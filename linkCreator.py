import numpy as np

import syntaxNN
import formOfWordNN


class SemanticLink:
    def __init__(self, subject, predicate, addition):
        self.subject = subject
        self.predicate = predicate
        self.addition = addition

    def __str__(self):
        result = []
        result.append(
            self.subject.text if hasattr(self.subject, "text") else self.subject
        )
        result.append(
            self.predicate.text if hasattr(self.predicate, "text") else self.predicate
        )
        result.append(
            self.addition.text if hasattr(self.addition, "text") else self.addition
        )
        return " ".join(result)

    def __repr__(self):
        result = []
        result.append(
            self.subject.text if hasattr(self.subject, "text") else self.subject
        )
        result.append(
            self.predicate.text if hasattr(self.predicate, "text") else self.predicate
        )
        result.append(
            self.addition.text if hasattr(self.addition, "text") else self.addition
        )
        return " ".join(result)


def find_if_is_positive(array, token):
    for second_token in array:
        if not second_token.head_id == token.id:
            continue
        if second_token.feats.get("Polarity") == "Neg":
            return False
    return True


def no_predicate_case(result_array, subject, addition, is_positive):
    result_array.append(
        SemanticLink(subject, "является" if is_positive else "не является", addition)
    )


def pointing_to_itself_case(array, result_array, subject):
    for second_token in array:
        if not second_token.head_id == subject.id:
            continue
        if second_token.id == subject.id:
            continue
        if second_token.rel == "punct":
            continue
        if second_token.rel == "cc":
            continue
        is_positive = find_if_is_positive(array, second_token)
        no_predicate_case(result_array, subject, second_token, is_positive)


def predicate_root_case(array, result_array, subject, predicate):
    for token in array:
        if not token.head_id == predicate.id:
            continue
        # Нейтроны состоят из кварков
        if token.rel == "obl":
            result_array.append(SemanticLink(subject, predicate, token))
        # Я люблю кушать сосиски
        if token.rel == "xcomp":
            result_array.append(SemanticLink(subject, predicate, token))
        # Я любила гранат
        if token.rel == "obj":
            result_array.append(SemanticLink(subject, predicate, token))


def create_links(semantics_aray):
    numpy_array = np.array(semantics_aray.tokens)
    links = []
    for token in numpy_array:
        print(token)
    for subject in numpy_array:
        if subject.rel != "nsubj":
            continue

        # ()
        if subject.id == subject.head_id:
            pointing_to_itself_case(numpy_array, links, subject)

        for second_token in numpy_array:
            if not subject.head_id == second_token.id:
                continue

            # Я - человек // Оно - не робот (Главная часть, нет сказуемого в виде глагола)
            if second_token.rel == "root" and second_token.pos == "NOUN":
                is_positive = find_if_is_positive(numpy_array, second_token)
                no_predicate_case(links, subject, second_token, is_positive)
                continue

            if second_token.rel == "root" and second_token.pos == "VERB":
                predicate_root_case(numpy_array, links, subject, second_token)
    return links
