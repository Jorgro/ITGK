def findAge(bYear, bMonth, bDay):
    [yyyy, mm, dd] = [2012, 12, 10]
    if bMonth <= mm and bDay <= dd:
        age = yyyy - bYear
    else:
        age = yyyy - bYear - 1
    return age
print(findAge(2000, 12, 15))
