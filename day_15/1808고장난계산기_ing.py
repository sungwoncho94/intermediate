
'''
3
0 1 1 0 0 1 0 0 0 0
60
1 1 1 1 1 1 1 1 1 1
128
0 1 0 1 0 1 0 1 0 1
128

#1 5
#2 4
#3 -1

0 0 0 0 0 0 0 0 0 1
793881

#1 10
'''
# 주어진 숫자로 만들 수 있는 num인지 아닌지 체크하는 함수
def check(num):
    target = str(num)
    for t in target:
        if t in num_list:
            


T = int(input())

for t in range(1, T+1):
    temp_list = list(map(int, input().split()))
    num_list = []
    target = int(input())  # input 받은 숫자
    div_target = []  # target을 나눈 값들을 넣어둘 list
    result = 99999
    flag1 = 1
    
    # 누를 수 있는 숫자 뽑기
    for p in range(10):
        if temp_list[p] == 1:
            num_list.append(p)
    # print(num_list) = [1, 2, 5]

    # 1. 누를 수 있는 숫자 조합으로 만들 수 있는지 확인
    str_target = str(target)
    for tar in str_target:
        div_target.append(int(tar))
    # print(div_target) = [6, 0]

    for div in div_target:
        # target을 나눈 숫자가 num_list안에 없으면 flag1을 0으로 만든다.
        if div not in num_list:
            flag1 = 0
            break
    
    # 숫자조합만으로 target을 만들 수 있다면 그대로 출력하고 끝
    if flag1 == 1:
        print('숫자조합으로 가능!')
        print('#{} {}'.format(t, len(div_target)+1))
        
    else:
        