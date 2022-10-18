"""
Определить самую высокую температуру и самый теплый день в мае.
"""

may_temp = [13, 15, 26, 23, 5, -5, 4, 24, 3, 7, -2, 0, 5, 23,
            12, 15, 18, 24, -5, 23, 18, 17, 19, 21, 10, 22, 9, 5, 10, 21, 25]

max_temp = max(may_temp)
print('Max temp = ', max_temp)

index_max_temp = may_temp.index(max_temp)
print('Day: ', index_max_temp + 1)