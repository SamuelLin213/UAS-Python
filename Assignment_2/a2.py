madLib = "There once was a [noun] named [name]. They enjoyed [verb] on a [adjective] day"

while madLib.find("[") != -1:
    start = madLib.find("[")
    end = madLib.find("]")

    blank = madLib[start:end+1]

    wordInput = input("Enter a " + blank[1:len(blank)-1] + ": ")

    madLib = madLib.replace(blank, wordInput)

print("\n" + madLib)
