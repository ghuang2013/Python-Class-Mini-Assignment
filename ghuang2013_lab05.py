# COT 4930  Python Programming
# name: Guan Huang
# id  : ghuang2013
# lab : 05


def make_xml(catagory, content):
    return "<{0}>{1}</{0}>".format(catagory, content)


def commands(command_token, command):
    (token) = command.split(' ', 1)
    if len(token) > 1:
        if token[0] in command_token:
            print(make_xml(command_token[token[0]], token[1]))
        else:
            print("+++ unknown: ", token[0], "an invalid command here.")
    elif len(command) == 0:
        print("</doi>")
    elif command.startswith("\\bibitem"):
        print("<doi>")


def read_file(filename):
    try:
        file_in = open(filename)
    except FileNotFoundError as e:
        print("Error: ", e.strerror)
        quit()
    return file_in


def main():
    command_tokens = {
        "\\bibitem": "bib",
        "\\A": "author",
        "\\B": "book",
        "\\P": "publisher",
        "\\R": "article",
        "\\J": "journal",
        "\\Y": "year"
    }
    filep = read_file("bib.txt")
    for line in filep:
        commands(command_tokens, line.strip("\n\t .,"))
    filep.close()


if __name__ == "__main__":
    main()
