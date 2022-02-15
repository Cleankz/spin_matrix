def MatrixTurn(matrix,m,n,t):
    matr = []
    for str in range(len(matrix)):
        matr.append(list(matrix[str]))
    for i in range(t):
        plus = -1
        minus = 1
        for circle in range(int((n/2))):
            if plus < m-1:
                plus += 1
            for j in range(m):
                last_num = matr[j + plus][len(matr[j])-minus]
                first_num = matr[j + plus][plus]
                if j != m-1:
                    del matr[j + plus][len(matr[j])-minus]
                if j != 0:
                    del matr[j + plus][plus]
                if plus == m - 1 or j == 0 and circle == 0:
                    matr[j+1].insert(len(matr[m-1])-1,last_num)
                elif j == m-1:
                    matr[j-1].insert(plus,first_num)
                elif j + 1 == m-1:
                    matr[j + 1].insert(len(matr[plus]),last_num)
                    matr[j-1].insert(plus,first_num)
                elif j == 0 and circle !=0:
                    first_num = matr[j + plus + 1][plus]
                    matr[j + 2].insert(len(matr[plus]),last_num)
                    matr[j + 1].insert(plus,first_num)
                else:
                    if j == 1 and circle ==1 and m/2 == 2:
                        matr[j + 1].insert((len(matr[plus]) - 3),last_num)
                        break
                    else:
                        matr[j + 1].insert(len(matr[plus]) - 1,last_num)
                        matr[j - 1].insert(plus,first_num)
            if j == 1 and circle ==1 and m/2 == 2:
                break
            minus += 1
    matrix.clear()
    for s in range(len(matr)):
        matrix.append(''.join((matr[s])))
    return matrix