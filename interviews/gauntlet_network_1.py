"""
given an array of tuples containing song titles and their lengths, return 2 songs that add up to a given duration
"""

songs1 = [("ligma", "1:34"), ("sigma", "1:45"), ("based", "2:52"), ("hittas", "2:08")]
total_duration1 = "5:00"
songs2 = [("ligma", "1:34"), ("sigma", "1:45"), ("based", "2:52"), ("hittas", "2:08")]
total_duration2 = "6:00"


def jukebox(songs, total_duration):
    total_duration = int(total_duration.split(":")[0]) * 60 + int(total_duration.split(":")[1])
    song_array = []
    for song in songs:
        song_duration = int(song[1].split(":")[0]) * 60 + int(song[1].split(":")[1])
        song_array.append((song_duration, song[0]))
    n = len(song_array)
    for left in range(n - 1):
        for right in range(left + 1, n):
            if song_array[left][0] + song_array[right][0] == total_duration:
                return [song_array[left][1], song_array[right][1]]

    return []


print(jukebox(songs1, total_duration1) == ["based", "hittas"])
print(jukebox(songs2, total_duration2) == [])
