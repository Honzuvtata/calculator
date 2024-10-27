def writeToMemory(text):
    with open('memory.txt', 'a') as file:
        file.write((text + "\n"))