def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * number_of_characters
    print(result)


yell("You're doing great!")
yell("Dont forget to Ask for help!")
yell("Do not repeat yourself. Keep things Dry!")
