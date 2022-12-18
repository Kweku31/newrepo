import random

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Generate a list of random courses
courses = []
num_courses = 11
for i in range(num_courses):
    name = f'Course {i+1}'
    days = random.sample(days_of_week, random.randint(1, 7))
    start_time = f'{random.randint(8, 22)}:00'
    hour, minute = start_time.split(':')
    end_time = f'{int(hour)+random.randint(1, 3)}:00'
    # end_time = f'{random.randint(1, 3)+int(start_time[0:2])}:00'
    courses.append({'name': name, 'days': days, 'start_time': start_time, 'end_time': end_time})

# Generate the timetable
timetable = {}
for course in courses:
    for day in course['days']:
        if day not in timetable:
            timetable[day] = []
        timetable[day].append({'start_time': course['start_time'], 'end_time': course['end_time'], 'name': course['name']})

print(timetable)
