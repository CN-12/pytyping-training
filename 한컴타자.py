정확도 = 100
글자 = "\033[30m"
배경 = "\033[47m"
with open('RE.txt','r', encoding='utf-8') as File:
    for i in File:
        출문장 = i.replace('\n', "")
        print(글자 + 배경 + 출문장 + "\033[0m")
        입문장 = input()
        if 출문장 != 입문장:
            정확도 -= 10
print("정확도는 ", 정확도 , "%입니다.")
print("\033[0m")