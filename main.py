from formOfWordNN import normalize_link
import linkCreator
import linkConnector
import networkPlotter
import syntaxNN

text = "Я любила гранат. Миша тоже любил гранат. Я ем яблоко. Ялоко это круто."


def main():
    array_of_sentences = text.split(".")
    print(array_of_sentences)
    sentence_links_array = []
    for sentence in array_of_sentences:
        if len(sentence) == 0:
            continue
        sentance_arr = syntaxNN.parse_setence(sentence)
        links_arr = linkCreator.create_links(sentance_arr)
        print(links_arr)
        for link in links_arr:
            normalize_link(link)
        # print(links_arr[0])
        sentence_links_array.append(links_arr)
    networkPlotter.plot_sentence_links_array(sentence_links_array)


if __name__ == "__main__":
    main()
