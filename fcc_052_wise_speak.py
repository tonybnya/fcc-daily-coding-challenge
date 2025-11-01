"""
Script Name : challenge_052_wise_speak.py
Description : Speak Wisely, You Must
Author      : @tonybnya

Given a sentence, return a version of it that sounds like advice from a Wise
teacher using the following rules:

- Words are separated by a single space.
- Find the first occurrence of one of the following words in the sentence:
  "have", "must", "are", "will", "can".
- Move all words before and including that word to the end of the sentence and:
    - Preserve the order of the words when you move them.
    - Make them all lowercase.
    - And add a comma and space before them.
- Capitalize the first letter of the new first word of the sentence.
- All given sentences will end with a single punctuation mark. Keep the original
  punctuation of the sentence and move it to the end of the new sentence.
- Return the new sentence, make sure there's a single space between each word
  and no spaces at the beginning or end of the sentence.

For example, given "You must speak wisely." return "Speak wisely, you must."
"""


def wise_speak(sentence: str) -> str:
    punctuation: str = sentence[-1]
    chars: str = sentence[:-1]
    sep: str = ""
    if chars.find("have") != -1:
        sep = "have"
    elif chars.find("must") != -1:
        sep = "must"
    elif chars.find("are") != -1:
        sep = "are"
    elif chars.find("will") != -1:
        sep = "will"
    elif chars.find("can") != -1:
        sep = "can"
    words: list[str] = chars.split(sep)
    return (
        words[1].strip().capitalize()
        + ", "
        + words[0].strip().lower()
        + " "
        + sep
        + punctuation
    )
