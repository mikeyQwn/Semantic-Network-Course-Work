from formOfWordNN import normalize_link
import linkCreator
import networkPlotter
import syntaxNN

text = "Я любила гранат. Миша тоже любил гранат. Я ем яблоко. Ялоко - это хорошо. Люди едят яблоки"


def main():
    text = input("Введите текст: ")
    array_of_sentences = text.split(".")
    sentence_links_array = []
    index = 1
    for sentence in array_of_sentences:
        if len(sentence) == 0:
            continue
        print(index, " ", sentence)
        sentance_arr = syntaxNN.parse_setence(sentence)
        links_arr = linkCreator.create_links(sentance_arr)
        for link in links_arr:
            normalize_link(link)
        print(links_arr)
        sentence_links_array.append(links_arr)
        index += 1
    networkPlotter.plot_sentence_links_array(sentence_links_array)


if __name__ == "__main__":
    main()
