def minMovesToSeat(seats, students):
    
    seats.sort()
    students.sort()

    total_moves = 0
    for i in range(len(seats)):
        total_moves += abs(seats[i] - students[i])

    return total_moves
'''seats= [2,2,6,6]
students = [1,3,2,6]
'''
seats = [4,1,5,9]
students = [1,3,2,6]
print(minMovesToSeat(seats,students))
