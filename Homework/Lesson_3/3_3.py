def ScrPoints(letter):
    Alphabet = {1:"AEIOULNSTRАВЕИНОРСТ",
               2:"DGДКЛМПУ",
               3:"BCMPБГЁЬЯ",
               4:"FHVWYЙЫ",
               5:"KЖЗХЦЧ",
               8:"JXШЭЮ",
               10:"QZФЩЪ"}
    for key, value in Alphabet.items():
        if letter in value:
            letterValue=key
    return letterValue
def Scrabble(word):
    ScrSum=0
    for letter in word:
        ScrSum+=ScrPoints(letter)
    return ScrSum
word=(input("Input word:")).upper()
print(Scrabble(word))