import re


def validateInput(input):
    """
    Validates the input for a Bible verse reference.

    Args:
        input (str): The input string representing a Bible verse reference.

    Raises:
        ValueError: If the input is not a valid Bible verse reference.

    Returns:
        None
    """

    bible_books = [
        "Genesis",
        "Exodus",
        "Leviticus",
        "Numbers",
        "Deuteronomy",
        "Joshua",
        "Judges",
        "Ruth",
        "1 Samuel",
        "2 Samuel",
        "1 Kings",
        "2 Kings",
        "1 Chronicles",
        "2 Chronicles",
        "Ezra",
        "Nehemiah",
        "Esther",
        "Job",
        "Psalms",
        "Proverbs",
        "Ecclesiastes",
        "Song of Solomon",
        "Isaiah",
        "Jeremiah",
        "Lamentations",
        "Ezekiel",
        "Daniel",
        "Hosea",
        "Joel",
        "Amos",
        "Obadiah",
        "Jonah",
        "Micah",
        "Nahum",
        "Habakkuk",
        "Zephaniah",
        "Haggai",
        "Zechariah",
        "Malachi",
        "Matthew",
        "Mark",
        "Luke",
        "John",
        "Acts",
        "Romans",
        "1 Corinthians",
        "2 Corinthians",
        "Galatians",
        "Ephesians",
        "Philippians",
        "Colossians",
        "1 Thessalonians",
        "2 Thessalonians",
        "1 Timothy",
        "2 Timothy",
        "Titus",
        "Philemon",
        "Hebrews",
        "James",
        "1 Peter",
        "2 Peter",
        "1 John",
        "2 John",
        "3 John",
        "Jude",
        "Revelation",
    ]

    split_input = input.split()

    if split_input[0].isnumeric() and " ".join(split_input[0:2]) in bible_books:
        pass
    elif split_input[0] in bible_books:
        pass
    else:
        raise ValueError("Invalid input")

    verse = split_input[-1]

    if re.match("[0-9]+:[0-9]+", verse):
        pass
    else:
        raise ValueError("Invalid input")
