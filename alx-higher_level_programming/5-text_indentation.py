#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1


# Example usage
if __name__ == "__main__":
    text_indentation("""Lorem ipsum dolor sit amet,
    consectetur adipiscing elit.
    Quonam modo? Utrum igitur tibi litteram videor an totas paginas
    commovere?
    Non autem hoc: igitur ne illud quidem. Fortasse id optimum,
    sed ubi illud:
    Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
    Transfer idem ad modestiam vel temperantiam, quae est moderatio
    cupiditatum
    rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex
    illa a Dipylo
    stadia confecimus. Sin aliud quid voles, postea. Quae animi
    affectio suum
    cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
    beatiorem! Iam ruinas videres""")
