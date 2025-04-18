"""
Your monthly phone bill has just arrived, and it's unexpectedly
large. You decide to verify the amount by recalculating the bill
based on your phone call logs and the phone company's
charges.
The logs are given as a string S consisting of N lines separated
by end-of-line characters (ASCII code 10). Each line describes
one phone call using the following for-nat: "hh:mm:SS, nnn-
nnn-nnn", where "hh: mm:ss" denotes the duration of the call
(in "hh" hours,
"'mm" minutes and "ss" seconds) and "nnn-
nnn-nnn" denotes the 9-digit phone number of the recipient
(with no leading zeros).
Each call is billed separately. The billing rules are as follows:
If the call was shorter than 5 minutes, then you pay
3 cents for every started second of the call (e.g.
for duration "00: 01: 07" you pay 67 * 3 = 201
cents).
If the call was at least 5 minutes long, then you
pay 150 cents for every started minute of the call
(e.g. for duration
"00: 05:00"
you pay 5 * 150 =
750 cents and for duration "00:05: 01" you pay 6
* 150 = 900 cents).
All calls to the phone number that has the longest
total duration of calls are free. In the case of a tie,
if more than one phone number shares the longest
total duration, the promotion is applied only to the
phone number whose numerical value is the
smallest among these phone numbers.
"""

import math







def solution(S):  # THIS IS CORRECT

    calls = S.split("\n")
    log = {}
    payment = 0

    # log all calls into a hashmap with their duration
    for call in calls:
        duration = call.split(",")[0].split(":")
        phone_number = call.split(",")[1]
        seconds = 3600 * int(duration[0]) + 60 * int(duration[1]) + int(duration[2])
        log[phone_number] = log.get(phone_number, 0) + seconds

    # get the number that will have free calls
    free = float("inf")
    free_calls = max(log.values())
    for number, duration in log.items():
        if duration == free_calls:
            free = min(free, int("".join(number.split("-"))))

    free = str(free)
    free = "-".join([free[:3], free[3:6], free[6:]])
    for call in calls:
        if call[9:] == free:
            continue
        duration = call.split(",")[0].split(":")
        seconds = 3600 * int(duration[0]) + 60 * int(duration[1]) + int(duration[2])
        if seconds < 300:
            payment += (3 * seconds)
        elif seconds >= 300:  # can be an else statement
            payment += (150 * math.ceil(seconds / 60))

    return payment

S =   "00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090\n00:01:07,400-235-090\n00:05:00,400-235-090"
print(solution(S))






