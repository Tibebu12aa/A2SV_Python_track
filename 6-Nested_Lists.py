if __name__ == '__main__':
    python_students=[]
    scores_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name,score])
        scores_list.append(score)
    python_students.sort(key = lambda score: (score[1],score))
    second_lowest = sorted(list(set(scores_list)))[1]
    names = [name for name,marks in sorted(python_students) if marks == second_lowest]
    print('\n'.join(names))
