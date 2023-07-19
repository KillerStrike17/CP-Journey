def isSafe(i,j,row,col,arr,visited):
    if (i>=0 and i<row) and (j>=0 and j<col) and (arr[i][j] == 1) and (visited[i][j]==0):
        return True
    else:
        return False


def solveMaze(arr,row,col,i,j,visited,path,output):
    if i == row -1 and j == col-1:
        # print("Here",output)
        path.append(output)
        return

    #Down
    if isSafe(i+1,j,row,col,arr,visited):
        visited[i+1][j] = True
        solveMaze(arr,row,col,i+1 ,j,visited,path,output+"D")
        visited[i+1][j] = False

    #Left
    if isSafe(i,j-1,row,col,arr,visited):
        visited[i][j-1] = True
        solveMaze(arr,row,col,i ,j-1,visited,path,output+"L")
        visited[i][j-1] = False
    
    #Right
    if isSafe(i,j+1,row,col,arr,visited):
        visited[i][j+1] = True
        solveMaze(arr,row,col,i ,j+1,visited,path,output+"R")
        visited[i][j+1] = False

    #Up
    if isSafe(i-1,j,row,col,arr,visited):
        visited[i-1][j] = True
        solveMaze(arr,row,col,i-1 ,j,visited,path,output+"U")
        visited[i-1][j] = False



maze = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
rows = 4
cols = 4

visited = []
for i in range(rows): 
    temp = []
    for j in range(cols):
        temp.append(False)
    visited.append(temp)

# visited = [[False]*cols]*rows 
visited[0][0] = True 
print(visited)
path = []
output = ""
solveMaze(maze,rows,cols,0,0,visited,path,output)
print(path)