import json

ignoredCharacters = [" "]


def transliterate(input_text: str, language: str, passthrough: bool = True):
    """
    returns a string of romanized input text
        Parameters:
            input_text (str): text to be romanized
            language (str): the name of the character map file to be used
            passthrough (bool): should unknown characters be passed through to the output string

        Returns:
            output_text (str): the romanized text
    """
    # load json language map
    try:
        letters, diacritics = readMap(language)
    except IOError:
        print("Invalid Character Map Name")
        return None

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
        else:  # handle other characters
            try:
                output_text += letters[i]
            except:
                if passthrough or i in ignoredCharacters:
                    output_text += i
                else:
                    print(f"Unmapped Character {i}")

    output_text = output_text.strip()
    return output_text


# read character map from json file
def readMap(language):
    """
    loads the character map file
        Parameters:
            language (str): the name of the character map file to be used

        Returns:
            letters (dict): the letters and their romanized equivalent
            diacritics (dict): the vowel diacritics and their romanized equivalent

    """
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
