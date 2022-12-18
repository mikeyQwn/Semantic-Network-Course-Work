from formOfWordNN import normalize_link
import linkCreator
import linkConnector
import networkPlotter
import syntaxNN

text = "Я любила гранат"


def main():
    sentance_arr = syntaxNN.parse_setence(text)
    links_arr = linkCreator.create_links(sentance_arr)
    print(links_arr)
    for link in links_arr:
        normalize_link(link)
    print(links_arr)


if __name__ == "__main__":
    main()
