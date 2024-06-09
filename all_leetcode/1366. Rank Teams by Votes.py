from typing import List


def rankTeams(votes: List[str]) -> str:
    n = len(votes[0])

    hashmap = {}

    for vote in votes:
        for i in range(n):
            letter = vote[i]
            if letter not in hashmap:
                hashmap[letter] = [0 for _ in range(n)]
            hashmap[letter][i] += 1

    sorted_teams = []

    for team, vote_counts in hashmap.items():
        sorted_teams.append((team, vote_counts))

    sorted_teams.sort(key=lambda x: (x[1], -ord(x[0])), reverse=True)

    return "".join(team[0] for team in sorted_teams)


print(rankTeams(["ABC", "ACB", "ABC", "ACB", "ACB"]) == "ACB")
print(rankTeams(["WXYZ", "XYZW"]) == "XWYZ")
