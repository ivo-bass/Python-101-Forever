def group(items):
    result = []
    for index in range(len(items)):
        item = items[index]
        if not result or not result[-1][0] == item:
            result.append([item])
        else:
            result[-1].append(item)
    return result


print(group([1, 1, 1, 2, 3, 1, 1]))

print(group([1, 1, 1, 2, 3, 1, 1]) == [[1, 1, 1], [2], [3], [1, 1]])
print(group([1, 2, 1, 2, 3, 3]) == [[1], [2], [1], [2], [3, 3]])
print(group([]) == [])
print(group([1]) == [[1]])
print(group([1, 1, 1, 1]) == [[1, 1, 1, 1]])
