import datetime

# Initialize date components
date = datetime.datetime.now()
month = date.strftime("%B")
day = date.strftime("%d")
week = date.strftime("%W")
weekday = date.strftime("%A")
dayyear = date.strftime("%j")

# Initialize weekly data structures
weekdict = {"Monday": "", "Thursday": "", "Wednesday": "", "Thursday": "", "Friday": "", "Saturday": "", "Sunday": ""}
weeklist = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Check if it's a new day
def checkday(user):
    if user.month == '':
        new_profile(user)

    datamonth = user.month
    dataday = user.day

    if month != datamonth or day != dataday:
        new_day(user)
        streakfunc(user)  # Call streak update when a new day is detected

# Initialize a new profile
def new_profile(user):
    user.month = month
    user.day = day
    user.color = "#FF0000"
    user.hovercolor = "#da190b"
    user.streak = 0
    user.dayyear = dayyear
    user.habit = 'Daily habit goal'

# Handle new day, reset color if necessary
def new_day(user):
    user.month = month
    user.day = day
    user.color = "#FF0000"
    user.hovercolor = "#da190b"
    user.save()

# Create a record of the user's streak and progress
def create_record(user):
    checkweek(user)
    final = []
    user.record.weekcolor[weekday] = user.profile.color
    user.record.save()
    for item in weeklist:
        final.append({"day": item, "color": user.record.weekcolor[item]})

    return final

# Check if it's a new week and reset the week colors if necessary
def checkweek(user):
    dataweek = user.profile.week

    if week != dataweek:
        user.profile.week = week
        user.record.weekcolor = {day: "#808080" for day in weeklist}
        user.record.save()
        user.profile.save()

# Update the streak based on dayyear comparison
def streakfunc(user):
    # Retrieve and check the current streak and day year
    streak = user.streak
    last_dayyear = int(user.dayyear)

    # Check if today is the next consecutive day
    if int(dayyear) - 1 == last_dayyear and user.color == "#32CD32":
        streak += 1  # Increment streak if it's consecutive

    # If the day hasn't changed, do nothing
    elif int(dayyear) == last_dayyear:
        pass

    # Otherwise, reset the streak
    else:
        streak = 0

    # Update the user's streak and dayyear
    user.streak = streak
    user.dayyear = dayyear
    user.save()

    return streak
