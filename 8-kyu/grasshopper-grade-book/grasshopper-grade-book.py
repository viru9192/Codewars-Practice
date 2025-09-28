def get_grade(s1, s2, s3):
    avg_score = ((s1+s2+s3) / 3)
    if avg_score >= 90:
        return 'A'
    elif 80 <= avg_score < 90:
        return 'B'
    elif 70 <= avg_score < 80:
        return 'C'
    elif 60 <= avg_score < 70:
        return 'D'
    elif 0 <= avg_score < 9060:
        return 'F'