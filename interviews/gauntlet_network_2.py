"""
given an array of songs as strings, return the longest chain of songs where the first word of the ith song must be the last word of the i-1th song given a starting word
songs can't be used more than once in a chain
"""

songs1 = ["based in atlanta", "atlanta bois", "sick beats", "ligma", "ligma real based", "beats", "beats bois", "bois based", "bois", "I'm so based", "based hittas", "hittas chicken", "based chicken", "hittas whippet"]
starting_song1 = "I'm so based"
songs2 = ["based in atlanta", "atlanta bois", "sick beats", "ligma", "ligma real based", "beats", "beats bois", "bois based", "bois", "I'm so based", "based hittas", "hittas chicken", "based chicken"]
starting_song2 = "sick beats"
songs3 = ["based in atlanta", "atlanta bois", "sick beats", "ligma", "ligma real based", "beats", "beats bois", "bois based", "bois", "I'm so based", "based hittas", "hittas chicken", "based chicken"]
starting_song3 = "trench dawgs"


def longest_chain(songs, starting_song):
    song_starts = {}
    song_ends = {}

    answer = [[]]
    answer_length = [0]

    for song in songs:
        if song == starting_song:
            continue
        split_song = song.split(" ")
        if len(split_song) > 1:
            start_word = split_song[0]
            end_word = split_song[-1]
        else:
            start_word = end_word = song
        song_starts[start_word] = song_starts.get(start_word, []) + [song]
        song_ends[end_word] = song_ends.get(end_word, []) + [song]

    def dfs(current_word, chain, current_visited):
        possible_next_songs = song_starts.get(current_word, [])
        if not possible_next_songs:
            if len(chain) > answer_length[0]:
                answer_length[0] = len(chain)
                answer[0] = chain.copy()
            return
        for next_song in possible_next_songs:
            if next_song not in visited:
                current_visited.add(next_song)
                chain.append(next_song)
                dfs(next_song.split(" ")[-1], chain, current_visited)
                current_visited.remove(next_song)
                chain.pop()

    visited = set()
    visited.add(starting_song)

    dfs(starting_song.split(" ")[-1], [starting_song], visited)

    return answer[0]


print(longest_chain(songs1, starting_song1) in (["I'm so based", 'based in atlanta', 'atlanta bois', 'bois', 'bois based', 'based hittas', 'hittas whippet'], ["I'm so based", 'based in atlanta', 'atlanta bois', 'bois', 'bois based', 'based hittas', 'hittas chicken']))
print(longest_chain(songs2, starting_song2) == ['sick beats', 'beats', 'beats bois', 'bois', 'bois based', 'based hittas', 'hittas chicken'])
print(longest_chain(songs3, starting_song3) == ['trench dawgs'])
