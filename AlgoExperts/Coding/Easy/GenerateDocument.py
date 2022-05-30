from collections import Counter


def generateDocument(characters, document):
    # Write your code here.
    char_dict = Counter(list(characters))
    doc_dict = Counter(list(document))
    check = True
    for _ in doc_dict.keys():
        if _ in char_dict.keys() and char_dict[_] >= doc_dict[_]:
            continue
        else:
            check = False
            break
    return check
