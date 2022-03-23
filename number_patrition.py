# Решение задачи поиска Алгоритма. Генерация разбиений числа
def get_next_partition(partition):
    if len(partition) == 1:
        return None
    min_index = 0
    for i in range(0, len(partition)-1):
        if partition[i] < partition[min_index]:
            min_index = i
    partition[min_index] += 1
    partition[-1] -= 1
    part_sum = sum(partition[min_index+1::])
    return partition[0:min_index+1:]+[1 for i in range(part_sum)]


def print_all_number_partition(number):
    partition = [1 for i in range(number)]
    count=0
    while partition is not None:
        print(partition)
        count+=1
        partition = get_next_partition(partition)
    return count


number = 50
print(print_all_number_partition(number))