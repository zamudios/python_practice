def better_largest_sum(list, n):
    if n == len(list):
        return sum(list)
    largest_sum = 0
    left = 0
    right = n - 1
    current_sum = 0 
    for num in list:
        if right >= len(list):
            return largest_sum

        if largest_sum == 0:
            current_sum = sum(list[left:right+1])
        else:
            current_sum = list[right] + current_sum - list[left - 1]
        largest_sum = max(largest_sum, current_sum)
        left += 1
        right += 1


def largest_sum_of_size_n(list, n):
    if n == len(list):
        return sum(list)

    largest_sum = 0
    left = 0
    right = n - 1
    for num in list:
        if (right >= len(list)):
            return largest_sum
        count = left
        curr_sum = 0
        while count <= right:
            curr_sum += list[count]
            count += 1
        largest_sum = max(largest_sum, curr_sum)
        left = left + 1
        right = right + 1

def largest_sum_of_size_3(list, n=3):

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

answer = largest_sum_of_size_3(input_list, sub_array_size)
print(answer)
answer = largest_sum_of_size_n(input_list, 4)
print(answer)
answer = better_largest_sum(input_list, 4)
print(answer)
