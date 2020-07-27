#1018 체스판 다시 칠하기
#20200723

def chess(N,M,L):
    different = 0
    want1 = [[WBWBWBWB],[BWBWBWBW],[WBWBWBWB],[BWBWBWBW],[WBWBWBWB],[BWBWBWBW],[WBWBWBWB],[BWBWBWBW]]
    want2 = [[BWBWBWBW],[WBWBWBWB],[BWBWBWBW],[WBWBWBWB],[BWBWBWBW],[WBWBWBWB],[BWBWBWBW],[WBWBWBWB]]
    count_list = []


    for a in range(8):   # 시작점 L[a][b]
        for b in range(M-7):
            for c in range(8):
                for d in range(8):    # c -> 01234567

                    if want1[a][b][d] == L

                



N,M = input().split()
N,M = int(N),int(M)
L = []

for i in range(N):
    L.append(input())

chess(N,M,L)


    
