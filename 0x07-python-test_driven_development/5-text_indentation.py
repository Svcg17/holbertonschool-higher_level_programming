""" The 5-text_indentation module"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: '.\
            ', '?', ':'
        Args:
            text (str): Text to change

        Returns:
            the changed text

    """
    if text == "\n":
        print()
    if text is None:
        raise TypeError("text must be a string")
    if type(text) != str:
        raise TypeError("text must be a string")
    delims = ".?:"
    nen = ""
    for i in text:
        nen += i
        if i in delims:
            print(nen.strip())
            print()
            nen = ""
    print(nen.strip(), end="")
