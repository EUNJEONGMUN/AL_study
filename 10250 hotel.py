#10250 ACM hotel
#20200714

def hotel(H, W, N):
    floor = N%H

    if floor==0:
        floor = H
        room = N//H
    else:
        room = N//H + 1
        
    if room<10:
        room = '0'+str(room)
        
        

    print("{}{}".format(floor,room))

count = int(input())
for i in range(count):
    H, W, N = input().split()
    H, W, N = int(H), int(W), int(N)
    hotel(H,W,N)
    
