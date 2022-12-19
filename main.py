from formOfWordNN import normalize_link
import linkCreator
import linkConnector
import networkPlotter
import syntaxNN

text = "Я любила гранат. Миша тоже любил гранат. Я ем яблоко. Ялоко это круто."


def main():
    array_of_sentances = text.split(".")
    print(array_of_sentances)
    parsed_sentances = []
    sentance_arr = syntaxNN.parse_setence(text)
    links_arr = linkCreator.create_links(sentance_arr)
    print(links_arr)
    for link in links_arr:
        normalize_link(link)
    print(links_arr[0])
    networkPlotter.plot_links_array(links_arr)


if __name__ == "__main__":
    main()
