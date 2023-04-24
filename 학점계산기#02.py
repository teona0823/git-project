def point1(point):
    match point:
        case "A+":
            return 4.5
        case "A":
            return 4
        case "B+":
            return 3.5
        case "B":
            return 3
        case "C+":
            return 2.5
        case "C":
            return 2
        case "D+":
            return 1.5
        case "D":
            return 1
        case "F":
            return 0
dic = {}
입력 = 0
평가 = 0
과목수 = 0
제출총점 = 0
학점 = 0
열람총점 = 0
제출학점 = 0
열람학점 = 0

while True:
    print("\n\n\n작업을 선택하세요")
    print("1. 입력")
    print("2. 입력 정보")
    print("3. 출력")
    점수 = int(input())
    if 점수 == 1:
        print("\n\n과목을 입력해주세요")
        name = input()
        print("\n\n학점을 적어주세요")
        입력 = float(input())
        학점 = 입력
        print("\n\n평가를 입력해주세요")
        알파벳 = input()
        평가 = point1(알파벳)
        if 평가 > 0:
            제출총점 += 학점
            제출학점 += 학점*평가
        열람총점 += 학점
        열람학점 += 학점*평가
        과목수 += 1
        dic[name] = (입력, 알파벳)
        print("입력되었습니다.")
    elif 점수 == 2:
        if 과목수 == 0:
            print("\n\n아직 입력된것이 없습니다")
            
        else:
            print("\n\n과목 목록입니다")
            for key, value in dic.items():
                반올림 = round(float(value[0]))
                print('['+(f"{key}")+']'+str(반올림)+'학점:'+(f"{value[1]}"))
#+(f"{key}: {value[0:]}"))
    elif 점수 == 3:
        if 제출학점 == 0:
            print("아직 계산하지 못합니다")
            continue
        열람학점 /= 열람총점
        round(열람학점,2)
        print("\n\n열람용 학점은 " + str(열람총점)+"입니다  "+"GPA("+str(열람학점)+")\n")    
        제출학점 /= 제출총점
        round(제출학점,2)
        print("제출용 학점은 " + str(제출총점) + "입니다 "+"GPA("+str(제출학점)+")")
        print("\n프로그램을 종료합니다")
        break