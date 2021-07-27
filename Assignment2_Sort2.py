# Assignment for Compsci 220, by David Wagstaff (UPI: dwag351 ID: 543114591)
# This file takes an input of songs and ouputs n number of songs which
# are sorted by runtime, then title and then composer.

# Setting up n (number of items to output) and a temporary set for sorting the
# valid songs.
n = int(input())
temp_set = set([])

# We need to use try/except to catch the EOF error that will end the infinite
# while loop that takes in the input from the system.
try:
    while True:
        # Taking in new lines from the system and setting up some variables.
        new_input = input()
        count = 0
        song_title = ""
        song_composer = ""
        song_runtime = ""

        # This for loop splits each input line into the songs title, composer and
        # runtime.
        for item in new_input.split("&"):
            if count == 0:
                song_title = item
            elif count == 1:
                song_composer = item
            else:
                song_runtime = item
            count += 1
        
        # This try/except is used to make sure only valid songs are added to
        # the temporary set.
        try:
            if song_runtime != "":
                temp_set.add((int(song_runtime), song_title, song_composer))
        except:
            continue
except:
    # Once a temporary set of all valid songs are collected, we need to sort them.
    # It is vital that python sorts the first element backwards so the largest runtimes
    # are at the top of the list, then the second and third elements are sorted normally
    # (alphabetically).
    temp_set = sorted(temp_set, key=lambda x: (-x[0], x[1], x[2]))

    # After sorting the set, we print the first n elements of the list.
    for index in range(0, n):
        print ("{}&{}&{}".format(temp_set[index][1], temp_set[index][2], temp_set[index][0]))
