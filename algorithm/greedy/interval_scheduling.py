def interval_scheduling(intervals):
    """
    Solve interval scheduling problem with greedy algorithm
    
    Args:
        intervals: List of intervals, each of which: (start, end)
    
    Returns:
        selected_intervals: compatible intervals selected
        count: The number of interval selected
    """
    # sort with finish time
    intervals_sorted = sorted(intervals, key=lambda x: x[1])
    
    selected_intervals = []
    last_end = -float('inf')
    
    for interval in intervals_sorted:
        start, end = interval
        
        if start >= last_end:
            selected_intervals.append(interval)
            last_end = end
    
    return selected_intervals, len(selected_intervals)

if __name__ == "__main__":
	print(interval_scheduling([
	(0,6),(3,4),(3,5),(3,8),(4,6),(5,9),(6,10),(8,11)]))
