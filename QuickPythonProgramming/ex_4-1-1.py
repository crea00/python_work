# -*- conding : utf-8 -*-
# 연속된 if / elif 구문

# 사용자에게 점수를 입력받아 int type으로 변환
score = int(input(('Input Score : ')))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 90:
    grade = "B" 
elif 70 <= score <= 80:
    grade = "C"
elif 60 <= score <= 70:
    grade = "D"
else :
    grade = "F"

print("Grade is " + grade)