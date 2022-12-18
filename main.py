import linkCreator
import linkConnector
import networkPlotter
import syntaxNN

text = "Я люблю кушать сосиски"


def main():
    sentance_arr = syntaxNN.parse_setence(text)
    links_arr = linkCreator.create_links(sentance_arr)
    print(links_arr)


if __name__ == "__main__":
    main()
