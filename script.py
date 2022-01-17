# Reads file with possible answers
with open('answers.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

letter_counts = {}

# Counts occurances of all letters in all possible answers
for line in lines:
    for letter in line:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

print(letter_counts)

# Writes csv file with letter frequencies in alphabetical order
output = open('letterfrequencies.csv', 'w')
output.write('letter,frequency\n')
# Total characters, used for calculating letter frequency as a percentage
total = len(lines)*5
letter_frequencies = {}
for letter_count in sorted(letter_counts):
    output.write(f'{letter_count},{letter_counts[letter_count]}\n')
    letter_frequencies[letter_count] = letter_counts[letter_count]/total

output.close()

# Reads file with possible word guesses (includes more words than the possible answers file)
with open('guesses.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

word_scores = {}

# Calculates a score for each word based on the letter frequencies of all letters in word added up
for line in lines:
    score = 0
    # Adds letters to a set so words with duplicate letters can be ignored
    letters = set()
    for letter in line:
        letters.add(letter)
        score += letter_frequencies[letter]
    if len(letters) == 5:
        word_scores[line] = score

# Sorts words by score, highest to lowest
sorted_word_scores = dict(sorted(word_scores.items(), key=lambda x:x[1], reverse=True))

# Writes csv file with sorted word scores
output = open('wordscores.csv', 'w')
output.write('word,score\n')
for word in sorted_word_scores:
    output.write(f'{word},{sorted_word_scores[word]}\n')

output.close()

# Note: The top 3 words (which contain the same letters, and thus have the same score) are all not possible answers.