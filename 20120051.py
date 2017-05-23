t = int(input())


bingo = [2 for a in range(0,5)  for b in range(0,5)]
for a in range(t) :
    for a in range(0,5) :
        bingo[a] = [int(x) for x in input().split()] 
    number = [int(x) for x in input().split()]

    for c in range(len(number)) :
    
        for a in range(0,5) :
            for b in range(0,5) :
                if(bingo[a][b] == number[c]) :
                    bingo[a][b] = 0
                    break
        if((bingo[0][0]==0) and(bingo[0][1]==0) and (bingo[0][2]==0) and (bingo[0][3]==0) and (bingo[0][4]==0)):
            print(c+1)
            break
        elif((bingo[1][0]==0) and(bingo[1][1]==0) and (bingo[1][2]==0) and (bingo[1][3]==0) and (bingo[1][4]==0)):
            print(c+1)
            break
        elif((bingo[2][0]==0) and(bingo[2][1]==0) and (bingo[2][2]==0) and (bingo[2][3]==0) and (bingo[2][4]==0)):
            print(c+1)
            break
        elif((bingo[3][0]==0) and(bingo[3][1]==0) and (bingo[3][2]==0) and (bingo[3][3]==0) and (bingo[3][4]==0)):
            print(c+1)
            break
        elif((bingo[4][0]==0) and(bingo[4][1]==0) and (bingo[4][2]==0) and (bingo[4][3]==0) and (bingo[4][4]==0)):
            print(c+1)
            break
#이곳까지 가로조건
        elif((bingo[0][0]==0) and(bingo[1][0]==0) and (bingo[2][0]==0) and (bingo[3][0]==0) and (bingo[4][0]==0)):
            print(c+1)
            break
        elif((bingo[0][1]==0) and(bingo[1][1]==0) and (bingo[2][1]==0) and (bingo[3][1]==0) and (bingo[4][1]==0)):
            print(c+1)
            break
        elif((bingo[0][2]==0) and(bingo[1][2]==0) and (bingo[2][2]==0) and (bingo[3][2]==0) and (bingo[4][2]==0)):
            print(c+1)
            break
        elif((bingo[0][3]==0) and(bingo[1][3]==0) and (bingo[2][3]==0) and (bingo[3][3]==0) and (bingo[4][3]==0)):
            print(c+1)
            break
        elif((bingo[0][4]==0) and(bingo[1][4]==0) and (bingo[2][4]==0) and (bingo[3][4]==0) and (bingo[4][4]==0)):
            print(c+1)
            break
#여기까지 세로조건
        elif((bingo[0][0]==0) and(bingo[1][1]==0) and (bingo[3][3]==0) and (bingo[4][4]==0)):
            print(c+1)
            break
        elif((bingo[0][4]==0) and(bingo[1][3]==0) and (bingo[3][1]==0) and (bingo[4][0]==0)):
            print(c+1)
            break

#여기까지 대각선조건
        elif((bingo[0][0]==0) and(bingo[0][4]==0) and (bingo[4][0]==0) and (bingo[4][4]==0)):
            print(c+1)
            break
#마지막 모서리조건입니다
             
             
