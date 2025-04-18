#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minCost' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER numProjects
#  2. INTEGER_ARRAY projectId
#  3. INTEGER_ARRAY bid
#

def minCost(numProjects, projectId, bid):
    projects = {i: float("inf") for i in range(numProjects)}
    for project in range(len(projectId)):
        if bid[project] < projects[projectId[project]]:
            projects[projectId[project]] = bid[project]
    totalCost = 0
    for key, value in projects.items():
        if value == float("inf"):
            return -1
        else:
            totalCost += value
    return totalCost

    # Write your code here


numProjects = 3
projectId = [2, 0, 1, 2]
bid = [6, 7, 8, 9]
print(minCost(numProjects, projectId, bid))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     numProjects = int(input().strip())
#
#     projectId_count = int(input().strip())
#
#     projectId = []
#
#     for _ in range(projectId_count):
#         projectId_item = int(input().strip())
#         projectId.append(projectId_item)
#
#     bid_count = int(input().strip())
#
#     bid = []
#
#     for _ in range(bid_count):
#         bid_item = int(input().strip())
#         bid.append(bid_item)
#
#     result = minCost(numProjects, projectId, bid)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
