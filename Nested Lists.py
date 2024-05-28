if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    score=[]
    for student in students:
        score.append(student[1])
    sec_low=sorted(set(score))[1]
    name=[]
    for student in students:
        if student[1]==sec_low:
            name.append(student[0])
    for n in sorted(name):
        print(n)
