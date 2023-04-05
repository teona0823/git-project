total_credits = 0
total_grades = 0
minus_credits = 0

while True:
    val = int(input("작업을 선택하세요.\n1. 입력\n2. 계산\n"))
    if (val == 1):
        credits = int(input("학점을 입력하세요: "))
        grade = input("평점을 입력하세요 (A+, A, B+, B, C+, C, D+, D, F): ")
    
        if grade == 'A+':
            total_grades += credits * 4.5
        elif grade == 'A':
            total_grades += credits * 4
        elif grade == 'B+':
            total_grades += credits * 3.5
        elif grade == 'B':
            total_grades += credits * 3
        elif grade == 'C+':
            total_grades += credits * 2.5
        elif grade == 'C':
            total_grades += credits * 2
        elif grade == 'D+':
            total_grades += credits * 1.5
        elif grade == 'D':
            total_grades += credits * 1
        elif grade == 'F':
            total_grades += credits * 0
            minus_credits += credits
        
        total_credits += credits
        print("입력되었습니다.")

    elif (val == 2):
        submit_gpa = total_grades / (total_credits - minus_credits)
        view_gpa = total_grades / total_credits
        
        print("제출용: %d학점 (GPA: %.2lf)" % (total_credits - minus_credits, submit_gpa))
        print("열람용: %d학점 (GPA: %.2lf)" % (total_credits, view_gpa))

        break
