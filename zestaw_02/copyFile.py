def copyFile(infileName, outfileName):
    """Funkcja kopiująca pliki z pominieciem lini komentarzy zaczynających się od #"""
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")
    while True:
        if infile.read(1) == '#':
            pass
        else:
            text = infile.read(50)
            outfile.write(text)
    infile.close()
    outfile.close()

file1 = input("file1:\n")
file2 = input("file2:\n")
copyFile(file1, file2)