def miniMaxSum(arr):
    # Write your code here
    smallest_sum = 0
    biggest_sum = 0
    
    current_sum = 0
    for i in range(0, len(arr)):
        for element in range(len(arr)):
            if element != i:
                current_sum += arr[element]
          
        if i == 0:
            smallest_sum = current_sum
        if current_sum < smallest_sum:
            smallest_sum = current_sum
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            
        current_sum = 0
            
    print(smallest_sum, biggest_sum)


miniMaxSum([1,2,3,4,5])

