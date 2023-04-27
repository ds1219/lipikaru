import json


def transliterate(input_text, language):
    # load json language map
    letters, diacritics = readMap("si")

    output_text = " "  # Do not remove space

    # remove unwanted unicode data
    junk = ["\u200d"]
    for j in junk:
        input_text = input_text.replace(j, "")

    # convert text
    for i in input_text:
        if i in diacritics.keys():  # handle diacritics (pili)
            if output_text[-1] == "a":
                output_text = output_text[:-1]
            output_text += diacritics[i]
        else:  # handle letters
            try:
                output_text += letters[i]
            except:
                output_text += i

    output_text = output_text.strip()
    return output_text


# read character map from json file
def readMap(language):
    with open(f"{language}.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    letters = data["letters"]
    diacritics = data["diacritics"]
    return (letters, diacritics)


# testing
if __name__ == "__main__":
    string = """"""
    string = string.strip()

    print(transliterate(string, "si"))
