# Python list (原生)

# 1D example
math_scores = [59, 65, 70, 40, 100, 70] # 1D list
eng_scores = [80, 90, 85, 91, 100, 83] # 2D list
ch_scores = [90, 91, 89, 93, 95, 100]

# 2D example
scores1 = [math_scores, eng_scores, ch_scores] # 2D List = List of List
scores2 = [[59, 65, 70, 40, 100, 70],
           [80, 90, 85, 91, 100, 83],
           [90, 91, 89, 93, 95, 100]]

# len(scores1): length of scores1
for i in range(len(scores1)): # i: row(列) index
    for j in range(len(scores1[i])): # j: column(行) index
        print(i, j, scores1[i][j])

# for-each loop
for class_scores in scores1:
    for score in class_scores:
        print(score, end=', ')
    print()
    
for class_scores in scores1:
    for i in range(len(class_scores)):
        print(class_scores[i], end=', ')
    print()    