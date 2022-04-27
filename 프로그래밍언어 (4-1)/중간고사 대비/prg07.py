matrix = [[10,20,30],
          [40,50,60],
          [70,80,90]]
t_matrix=[[0,0,0],
          [0,0,0],
          [0,0,0]]

for row in range(len(matrix)):   #len(matrix)->3
    for col in range(len(matrix[row])):
        t_matrix[col][row] = matrix[row][col]
print("원본행렬=", matrix)
print("전치행렬=", t_matrix)
t1=[ ]