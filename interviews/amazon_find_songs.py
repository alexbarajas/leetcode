"""
My approach for this code question was using left and right pointers to see if I would get a match,
but later on I realized that it would only work for arrays that have song lengths in ascending order.
I then thought of using a hashmap to map the required song lengths and their index in the songDurations
array for each song duration. This solved the problem of the array not being sorted, but then I ran into the
problem of having multiple pairs of songs and needing to chose the one with the longest song. I assumed
that there would not be many pairs to choose from in most cases, so making another hashmap to map the
pairs came to my mind. I set the pairs as the keys in the hashmap, and the length of the longest song
in that pair as the value in the hashmap. At the end the pair that would be returned would be the one
with the highest value in the pairs hashmap. I set the program to go through each key, value pair
in the hashmap, and once the highest value was seen, the pair set as the key would be returned.
If the answers hashmap was empty after searching for a pair, then the program would return [-1, -1].

The run time complexity of the solution would be O(n) or linear time since the program would go over
the songDurations array once, and then go over the pairs in the answers hashmap which at worst has a
length of n/2, n being the length of the songDurations array. O(n) + O(n / 2) simplifies to a run time of O(n).
"""

"""
find pairs of song lengths that equal rideDuration - 30, return the pair that has the longest song
"""


def findSongs(rideDuration, songDurations):
    # THIS WORKS
    if len(songDurations) < 2:
        return [-1, -1]
    songs = {}
    answers = {}
    for song in range(len(songDurations)):
        if songDurations[song] in songs:
            answers[songs[songDurations[song]], song] = max(rideDuration - 30 - songDurations[song], songDurations[song])
        songs[rideDuration - 30 - songDurations[song]] = song
    if not answers:
        return [-1, -1]
    answer = max(answers.values())
    for key, value in answers.items():
        if value == answer:
            return key

rideDuration = 90
songDurations = [15, 10, 25, 35, 45, 60]
print(findSongs(rideDuration, songDurations))
rideDuration = 90
songDurations = [15, 10]
print(findSongs(rideDuration, songDurations))