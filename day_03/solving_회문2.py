# 2 5 7 9 오답
# k = length 빼면 2, 7, 9오답

'''
#1 18
#2 17
#3 17
#4 20
#5 18
#6 21
#7 18
#8 18
#9 17
#10 18
'''

# 1~100까지 올라가면서 탐색하는거 답 맞춘 후, 
# 100부터 내려오는 알고리즘도 짜보자

# 2 5 7 9 오답
# k = length 빼면 2, 7, 9오답
T = 10

def pal(x):
    return True if x == x[::-1] else False

for t in range(1, T+1):
    test_num = int(input())
    matrix = []

    for i in range(100):
        sentence = list(map(str, input()))
        matrix.append(sentence)
    
    temp = 1
    length = 1
    # 2부터 100까지 글자수 늘리며 pal검사할 것.
    for p in range(2, 101):
        F = 100 - (p-1)  # p에 따라 찾을 index가 달라짐
        for r in range(100):  # 0~99행 row 탐색
            for f in range(F):  # 0~f index까지만 탐색
                test = ''  # 회문 검사할 test 단어 만들기
                for i in range(p):  # 탐색할 글자수
                    test += matrix[r][f+i]

                if pal(test) == True:
                    temp = p
                
                if temp >= length:
                    length = temp
                else:
                    length = length
    k = length

    for p in range(k, 101):  # 가로의 length 이상부터 탐색
        F = 100 - (p-1)
        for r in range(100):
            for f in range(F):
                test = ''
                # 회문 검사할 test 단어 만들기
                for i in range(p):
                    test += matrix[f+i][r]

                if pal(test) == True:
                    temp = p
                
                if temp >= length:
                    length = temp
                else:
                    length = length

    print('#%d %d' % (t, length))
