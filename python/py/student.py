# 평균을 내는 함수
def _avg(scores):
    try:
        return sum(scores) / len(scores)
    except ZeroDivisionError:
        return 0

def class_avg(students):
    for scores in students.values():
        print(_avg(scores))
