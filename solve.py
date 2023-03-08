import csv

# Read the crossword puzzle from the CSV file
with open('crossword2.csv', 'r') as f:
    puzzle_reader = csv.reader(f)
    puzzle = [row for row in puzzle_reader]

# Read the list of words to search for from the text file
with open('english_words.txt', 'r') as f:
    words = [word.strip() for word in f]

found_words = []  # create an empty list to store found words

# Search for words in the puzzle
for word in words:
    # Search horizontally from left to right
    for row in puzzle:
        if word in ''.join(row):
            print(f'Found {word} horizontally in row {puzzle.index(row)}')
            found_words.append(word)
            break
    else:
        # Search horizontally from right to left
        for row in puzzle:
            if word in ''.join(row)[::-1]:
                print(f'Found {word} horizontally in reverse in row {puzzle.index(row)}')
                found_words.append(word)
                break
        else:
            # Search vertically from top to bottom
            for i in range(len(puzzle)):
                if word in ''.join([row[i] for row in puzzle]):
                    print(f'Found {word} vertically in column {i}')
                    found_words.append(word)
                    break
            else:
                # Search vertically from bottom to top
                for i in range(len(puzzle)):
                    if word in ''.join([row[i] for row in puzzle])[::-1]:
                        print(f'Found {word} vertically in reverse in column {i}')
                        found_words.append(word)
                        break
                else:
                    # Search diagonally from top left to bottom right
                    for i in range(len(puzzle)-len(word)+1):
                        for j in range(len(puzzle[i])-len(word)+1):
                            if word == ''.join([puzzle[i+k][j+k] for k in range(len(word))]):
                                print(f'Found {word} diagonally from ({i},{j}) to ({i+len(word)-1},{j+len(word)-1})')
                                found_words.append(word)
                                break
                        else:
                            continue
                        break
                    else:
                        # Search diagonally from top right to bottom left
                        for i in range(len(puzzle)-len(word)+1):
                            for j in range(len(word)-1, len(puzzle[i])):
                                if word == ''.join([puzzle[i+k][j-k] for k in range(len(word))]):
                                    print(f'Found {word} diagonally from ({i},{j}) to ({i+len(word)-1},{j-len(word)+1})')
                                    found_words.append(word)
                                    break
                            else:
                                continue
                                break

print("Found words:", found_words)  # print all found words
