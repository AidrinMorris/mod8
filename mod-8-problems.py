#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
with open('gardening_tips.txt', 'w') as file:
    file.write("1. Water your vegetables and/or fruit early in the morning to reduce evaporation.\n")
    file.write("2. Use compost to enrich your soil and promote healthy plant growth.\n")
    file.write("3. Rotate your vegetables and/or fruit each season to prevent soil depletion and pest buildup.\n")

with open('gardening_tips.txt', 'r') as file:
    tips = file.readlines()
    for tip in tips:
        print(tip.strip())

#2. Write a Python program that allows users to log their hiking trips.
def log_hiking_trips():
    with open('hiking_log.txt', 'a') as log_file:
        while True:
            hike_name = input("Enter the hike name (or press 0 to exit): ")
            if hike_name == '0':
                break
            distance = input("Enter the distance in miles: ")
            log_file.write(f"{hike_name}: {distance} miles\n")

    print("\nHiking Log Contents:")
    with open('hiking_log.txt', 'r') as log_file:
        print(log_file.read())

log_hiking_trips()

#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it.
with open('song_lyrics.txt', 'w') as file:
    file.write("""Your song lyrics go here. Replace this text with the lyrics of a song.""")

def count_word_frequency():
    with open('song_lyrics.txt', 'r') as file:
        lyrics = file.read()

    words_to_count = []
    for i in range(5):
        word = input(f"Enter word {i + 1} to count: ")
        words_to_count.append(word)

    word_count = {word: lyrics.lower().split().count(word.lower()) for word in words_to_count}

    print(word_count)

count_word_frequency()

#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
with open('poll.txt', 'w') as file:
    file.write('Replace this with votes')

# Read the poll.txt file and count votes
with open('poll.txt', 'r') as file:
    votes = file.read().strip().split(', ')

yea_count = votes.count('yea')
nay_count = votes.count('nay')

print(f'Yea votes: {yea_count}')
print(f'Nay votes: {nay_count}')
