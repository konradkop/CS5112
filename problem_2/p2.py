def interval_covering(M: int, intervals: list) -> list:
    # Convert intervals to tuples and sort by start time
    intervals = sorted((tuple(i) for i in intervals), key=lambda x: (x[0], -x[1]))
    
    j = []  # List to store selected intervals
    min_start = 0  # Start covering from 0
    index = 0  # Index to iterate through sorted intervals

    while min_start < M:
        max_end = -1  # To track the farthest end we can cover
        best_interval = None  # To store the best interval to pick
        
        # Find the interval that extends the coverage the most
        while index < len(intervals) and intervals[index][0] <= min_start:
            if intervals[index][1] > max_end:
                max_end = intervals[index][1]
                best_interval = intervals[index]
            index += 1
        
        if best_interval is None:
            # No interval can cover the current min_start
            break
        
        # Update min_start and add the picked interval to the result
        min_start = max_end
        j.append(best_interval)

    return sorted(j)

# Example usage
# print(interval_covering(5, [[0, 2], [1, 3], [2, 5], [3, 4]]))
