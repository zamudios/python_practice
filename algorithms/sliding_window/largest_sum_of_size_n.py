def largest_sum(list, n):

    largest_sum = 0
    left = 0
    right = n - 1
    count = 0 
    curr_sum = 0
    for num in list:
        if right >= len(list):
            return largest_sum
        curr_sum = list[left] + list[left+1] + list[right]
        largest_sum = max(largest_sum, curr_sum)

        left += 1
        right += 1


input_list = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
sub_array_size = 3

answer = largest_sum(input_list, sub_array_size)
print(answer)
