#2447 별 찍기 -10
#20200728

def star_10(n):

    if n == 3:
        print('***')
        print('* *')
        print('***')
        '''
        for i in range(3):
            if i == 1:
                print('*'*(n//3)+' '*(n//3)+'*'*(n//3))
            else:
                print('*'*n)
        

        print('***'*(n//3))
        print('* *'*(n//3))
        print('***'*(n//3))
        '''

        
    else:
        star_10(n//3)
        star_10(n//3)
        star_10(n//3)
        star_10(n//3)
        star_10(n//3)
        

            



n = int(input())
star_10(n)
