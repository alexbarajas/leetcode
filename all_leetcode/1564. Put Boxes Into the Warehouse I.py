from typing import List


def maxBoxesInWarehouse(boxes: List[int], warehouse: List[int]) -> int:
    # 1. sort the boxes so that we fit the max possible number, and make a count variable
    boxes.sort()
    count = 0  # count == the number of boxes that can fit in the warehouse

    # 2. modify warehouse so that each room is not larger than the last, and then sort it
    for i in range(1, len(warehouse)):
        warehouse[i] = min(warehouse[i - 1], warehouse[i])
    warehouse.sort()

    # 3. go thru the boxes, for each box that can fit, increment count, and then keep checking until you finish going thru the boxes
    for room in warehouse:
        # 3.1. count has to be less than len(boxes) because count is the number of boxes that can fit in the warehouse
        if count < len(boxes) and boxes[count] <= room:
            count += 1
            # 3.2. if count == len(boxes) then that means every box can fit, and you don't need to keep checking the rooms
            if count == len(boxes):
                break

    # 4. return the count
    return count


print(maxBoxesInWarehouse(boxes=[4, 3, 4, 1], warehouse=[5, 3, 3, 4, 1]) == 3)
