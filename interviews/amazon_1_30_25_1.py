"""
The developers at Amazon SQS are working on optimizing the message queue algorithm. There are n events to be

sent through a queue, and the size of the th event payload is denoted by payload[il. The queue performs more efficiently if a subset of the events can be selected and rearranged into a new array called optimizedPayload,

which satisfies the following conditions, regardless of the original order of the elements:
2
1. The first part of optimizedPayload forms an increasing sequence:
optimizedPayload[1] < optimizedPayload[2] < ... ‹ optimizedPayload[i - 1] < optimizedPayload i] (Increasing order from the start to l).
dc2-b7b5
2. The second part of optimizedPayload forms a decreasing sequence:
optimizedPayload[i] > optimizedPayload[i + 1] > ... › optimizedPayloadlj - 1] > optimizedPayload[i] (Decreasing order from / to .

3. The third part of optimizedPayload forms an increasing sequence:
optimizedPayloadi] < optimizedPayload[j + 1] < ... < optimizedPayloadin] (Increasing order from /to the end), sade
The order of elements in optimizedPayload can be rearranged to meet these conditions, meaning the original order of the payload array does not matter when forming the subset,
dential
The task is to determine the maximum number of events that can be selected and rearranged to form
optimizedPayload that satisfies the increasing-decreasing-increasing configuration.

Given n events and all allay paylode, lina the maximum number of events that can be selected to form the optimizedPayload array that meets these conditions.
Example
n = 9
payload = [1, 3, 5, 4, 2, 6, 8, 7, 9]

Consider the subset optimizedPayload = [1, 3, 5, 4, 2, 6, 7, 8, 91. This satisfies the conditions as follows:
1. Increasing part (1 to i): [1, 3, 51, with i = 3.
2. Decreasing part (i to j): [5, 4, 21, with j = 5.
3. Increasing part (j to end): [2, 6, 7, 8, 97 al
All conditions are met, and the maximum number of events selected is 9.
Hence, the answer is 9.
Function Description
Complete the function getMaximumEvents in the editor below.
k Confidential
getMaximumEvents has the following parameter: int payloadin]: the size of the different event payloads
Returns
int: the maximum number of events that can be
selected for the queue
"""