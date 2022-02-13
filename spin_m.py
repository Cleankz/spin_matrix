def MatrixTurn(matrix,m,n,t):
    matr = []
    for str in range(len(matrix)):
        matr.append(list(matrix[str]))
    plus = 0
    for i in range(t):
        last_num = matr[i][len(matr[i])-1]
        if plus < m:
            plus += 1
        first_num = matr[plus][0]
        del matr[i][len(matr[i])-1]
        del matr[plus][0]
        if plus == m - 1 or plus == 0:
            matr[plus].insert(len(matr[m-1]),last_num)
        else:
            matr[plus].insert(len(matr[plus])-1,last_num)
            matr[i].insert(0,first_num)
    matrix.clear()
    for s in range(len(matr)):
        matrix.append(''.join((matr[s])))
    return matrix