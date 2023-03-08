import random
import csv

# Load a list of English words
with open('english_words.txt') as f:
    wordlist = [word.strip().lower() for word in f.readlines()]

# Generate a blank crossword grid
grid = [[' ' for _ in range(26)] for _ in range(26)]

# Choose random words to fill in the crossword
for word in wordlist:
    orientation = random.choice(['horizontal', 'vertical'])
    if orientation == 'horizontal':
        row = random.randint(0, 25)
        max_col = 25 - len(word)
        if max_col < 0:
            continue
        col = random.randint(0, max_col)
        for i in range(len(word)):
            grid[row][col+i] = word[i]
    else:
        col = random.randint(0, 25)
        max_row = 25 - len(word)
        if max_row < 0:
            continue
        row = random.randint(0, max_row)
        for i in range(len(word)):
            grid[row+i][col] = word[i]


# Save the crossword as a CSV file
with open('crossword2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in grid:
        writer.writerow(row)
