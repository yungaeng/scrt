import random


def generate_score():
    # score = { 'kor':[random.randint(0, 100) for n in range(20)], 'eng':[], 'math':[] } #dictionary
    score = [[random.randint(0, 100) for j in range(3)] for n in range(20)]
    return score


def process_score(score):
    student_avg = [sum(score[n]) / 3 for n in range(20)]
    subject_avg = [sum([score[n][j] for n in range(20)]) / 20 for j in range(3)]
    return subject_avg, student_avg


def print_score(score, student_avg, subject_avg):
    for n, s in enumerate(score):
        print(f"{n+1:2d} {s[0]:6d} {s[1]:6d} {s[2]:6d} {student_avg[n]:8.2f}")
    print(f"sub:{subject_avg[0]:6.2f} {subject_avg[1]:6.2f} {subject_avg[2]:6.2f}")


score = generate_score()
subject_avg, student_avg = process_score(score)
print_score(score, student_avg, subject_avg)
