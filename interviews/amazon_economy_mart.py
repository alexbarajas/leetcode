"""
For this question since we had to sort in terms of the cheapest items, I knew I had to use a heap.
I put each INSERT entry into the heap and it was sorted from cheapest to most expensive. After each
VIEW entry, it would view the item according to how many times a VIEW entry has been used.



The run time is O(n log n), with n being the length of the entries. The program goes through the
entries, and then finds the kth smallest value in the heap, with k being the amount of times a
VIEW entry has been called
"""

"""
https://leetcode.com/discuss/interview-question/1484843/amazon-online-assessment-question-doubts
"""



def getItems(entries):
    import heapq
    heap = []
    heapq.heapify(heap)
    answer = []
    count = 0
    for entry in entries:
        if entry[0] == "INSERT":
            heapq.heappush(heap, [int(entry[2]), entry[1]])
        elif entry[0] == "VIEW":
            count += 1
            answer.append(heapq.nsmallest(count, heap)[-1])
            print(answer[-1][1])


entries = [["INSERT", "milk", "4"], ["INSERT", "coffee", 3], ["VIEW", "-", "-"], ["INSERT", "pizza", 5],
           ["INSERT", "gum", 1], ["VIEW", "-", "-"]]
print(getItems(entries))
