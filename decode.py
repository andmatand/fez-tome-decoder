#!/usr/bin/python3

tomeFile = open('tome.txt', 'r')

pages = {}

# Read all the pages from the tome file
y = 1
pageNum = 0
for line in tomeFile:
    # If this is a blank line or no pages have been added yet
    if len(line.strip()) == 0 or len(pages) == 0:
        # Add a new page, which is a dictionary
        pageNum += 1
        pages[pageNum] = dict()
        y = 1

    if len(line.strip()) > 0:
        x = 0
        for char in line:
            if char != '\n':
                x = x + 1

                # Add this character with its tupled (x, y) position as the key
                pages[pageNum][(x, y)] = char
        y += 1

tomeFile.close()


# Display the characters in order
for x in range(7, 0, -1):
    for y in range(1, 9):
        for pageNum in 1, 5, 2, 6, 3, 7, 4, 8:
            char = pages[pageNum][(x, y)]
            if char != ' ':
                print(char, end = '')

        print(' ', end = '')

    print()
