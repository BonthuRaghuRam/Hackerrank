if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
original_list=list(set(arr))
original_list.sort(reverse=True)
print(original_list[1])
