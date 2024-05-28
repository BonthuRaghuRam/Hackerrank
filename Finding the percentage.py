if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for name in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum=0
    for value in student_marks[query_name]:
        sum+=value
    average=sum/3
    rounded_off=format(average,".2f")
    print(rounded_off)
