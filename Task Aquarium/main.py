def find_dominant_piranha(n, sizes):
    max_size = max(sizes)
    max_count = sizes.count(max_size)

    if max_count == 1:
        return sizes.index(max_size) + 1
    else:
        for i in range(n):
            if sizes[i] == max_size:
                if i > 0 and sizes[i - 1] != max_size:
                    return i + 1
                elif i < n - 1 and sizes[i + 1] != max_size:
                    return i + 1
    return -1


t = int(input())  
for _ in range(t):
    n = int(input())  
    sizes = list(map(int, input().split())) 
    result = find_dominant_piranha(n, sizes)
    print(result)