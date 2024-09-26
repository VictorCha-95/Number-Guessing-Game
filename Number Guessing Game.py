print("1부터 100 사이의 정수를 입력하세요.") 
print("최대 시도 횟수는 10번입니다.") 
print("만점은 100점이며, 1회 시도할 때마다 10점씩 차감됩니다.")

import random  #랜덤 모듈 불러오기
random_number = random.randint(1, 100)  #1부터 100 사이의 랜덤 숫자 생성 
X = 0  #시도 횟수

while True:  #무한 반복문
    try:
        number_input = int(input("숫자 입력: ")) #정수 입력

        X += 1 #시도 횟수 1씩 증가
        SCORE = 110 - 10 * X

        if X > 10:
            print("정답 시도 횟수 10회를 초과하였습니다.")
            break
        else:        
            if random_number > number_input:
                print(f"정답은 더 큰 숫자입니다. 시도 횟수: {X}회")
            elif random_number < number_input:
                print(f"정답은 더 작은 숫자입니다. 시도 횟수: {X}회")
            else:
                print(f"정답입니다! 시도 횟수: {X}회 점수: {SCORE}점")
                break
    except ValueError: #시도 오류가 났을 때 출력
        print(f"정수를 입력하세요. 시도 횟수: {X}회")