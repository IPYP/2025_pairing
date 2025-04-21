import csv


#Pre-process mentors
mentor = []

with open("test.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    temp = []
    for row in reader:
        mentor.append(row)

mentors_all = []

for i in range(1, len(mentor[0])):
    mentors_all.append([mentor[0][i], {}])
    for k in range(1, 8): #Change to amount of time slots - 1
        days = mentor[k][i]
        if bool(days):
            mentors_all[i-1][1].update({str(mentor[k][0]): mentor[k][i].split(", ")})


#Pre-process mentees
mentee = []

with open("test.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    temp = []
    for row in reader:
        mentee.append(row)

mentees_all = []

for i in range(1, len(mentee[0])):
    mentees_all.append([mentee[0][i], {}])
    for k in range(1, 8): #Change to amount of time slots - 1
        days = mentee[k][i]
        if bool(days):
            mentees_all[i-1][1].update({str(mentee[k][0]): mentee[k][i].split(", ")})


def find_match(mentor_full, mentee_full):
    mentor = mentor_full[1]
    mentee = mentee_full[1]
    same = list(set(mentor) & set(mentee))
    timing_match = {"Sunday": [], "Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": []}
    for i in same:
        temp = list(set(mentor[i]) & set(mentee[i]))
        for k in temp:
            timing_match[k].append(i)
    length = len([x for x in timing_match.values() if x!=[]])
    return [length, mentee_full[0]]


matches = []

for m in range(len(mentors_all)):
    matches = []
    for n in range(len(mentees_all)):
        matches.append(find_match(mentors_all[m], mentees_all[n]))
    matches.sort(reverse=True)
    print(mentors_all[m][0], matches)