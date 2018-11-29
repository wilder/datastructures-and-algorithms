'''
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

'''
    Creates a timeline keeping track the number of the class(interval) with the time
    Iterates through the timeline keeping track if there is a class ongoing,
    Increment the room count every time a class starts and another one is in progress
    Time Complexity = O(n)
    Space Complexity = O(n)
'''
def minimumNumberOfRooms1(intervals):

    if not intervals:
        return 0

    minTime = min(intervals)[0]
    maxTime = max(intervals)[1]

    print('min ', minTime)
    print('max ', maxTime)
    
    # Creates a array bounded by the minimun and max element
    timeline = [(False, -1) for i in range(minTime-1, maxTime+1)]

    # sets the intervals in the timeline and keep track of the number of the interval att each populated position
    interval_num = 0
    for interval in intervals:

        start = interval[0]
        end = interval[1]
        print('end ', end)

        timeline[start] = (True, interval_num)
        timeline[end] = (True, interval_num)

        interval_num+=1


    # map of (interval_num -> true) to check if the interval is closing
    classIsOpen = {} 

    '''
    Iterates through the timeline and keeps track of the last seen interval
    
    if the current_interval is already in the dict (the class is in progress), finish the class and don't update the last seen

    Add the interval num to the interval_dict
    
    if the current interval number is different from the last seen, increment the count
    set it as last_interval_seen

    '''
    last_interval_seen = None
    room_count = 0
    for time in timeline:
        has_class = time[0]
        if has_class:
            current_class = time[1]
            print("checking: ", current_class)

            if current_class not in classIsOpen:
                print("opening: ",current_class)
                classIsOpen[current_class] = True
                if last_interval_seen != None and classIsOpen[last_interval_seen]: # there is a class ongoing
                    print("there is already one in progress... ", last_interval_seen)
                    room_count += 1
                last_interval_seen = current_class
            else:
                classIsOpen[current_class] = False

    if not room_count:
        #no times overlap
        return 1

    return room_count



if __name__ == "__main__":
    print(minimumNumberOfRooms1([(30, 75), (0, 50), (60, 150)]))
    assert minimumNumberOfRooms1([(30, 75), (0, 50), (60, 150)]) == 2
    assert minimumNumberOfRooms1([(1,2), (3,4), (5,6)]) == 1
    assert minimumNumberOfRooms1([]) == 0


