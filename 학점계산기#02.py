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
input = 0
rate = 0
sjnum = 0
submit_score = 0
grade = 0
view_score = 0
submit_gpa = 0
view_gpa = 0

while True:
    print("\n\n\n작업을 선택하세요")
    print("1. 입력")
    print("2. 입력 정보")
    print("3. 출력")
    score = int(input())
    if score == 1:
        print("\n\n과목을 입력해주세요")
        name = input()
        print("\n\n학점을 적어주세요")
        input = float(input())
        grade = input
        print("\n\n평가를 입력해주세요")
        alphabet = input()
        rate = point1(alphabet)
        if rate > 0:
            submit_score += grade
            submit_gpa += grade * rate
        view_score += grade
        view_gpa += grade * rate
        sjnum += 1
        dic[name] = (input, alphabet)
        print("입력되었습니다.")
    elif score == 2:
        if sjnum == 0:
            print("\n\n아직 입력된것이 없습니다")
            
        else:
            print("\n\n과목 목록입니다")
            for key, value in dic.items():
                round = round(float(value[0]))
                print('['+(f"{key}")+']'+str(round)+'학점:'+(f"{value[1]}"))
#+(f"{key}: {value[0:]}"))
    elif score == 3:
        if submit_gpa == 0:
            print("아직 계산할 수 없습니다")
            continue
        view_gpa /= view_score
        round(view_gpa,2)
        print("\n\n열람용 학점은 " + str(view_score)+"입니다  "+"GPA("+str(view_gpa)+")\n")    
        submit_gpa /= submit_score
        round(submit_gpa,2)
        print("제출용 학점은 " + str(submit_score) + "입니다 "+"GPA("+str(submit_gpa)+")")
        print("\n프로그램을 종료합니다")
        break