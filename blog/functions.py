import datetime

date = datetime.datetime.now()
month = date.strftime("%B")
day = date.strftime("%d")
week = date.strftime("%W")
weekday = date.strftime("%A")
dayyear = date.strftime("%j")

weekdict = {"Monday": "", "Thursday": "", "Wednesday": "", "Thursday": "", "Friday": "", "Saturday": "", "Sunday": ""}
weeklist = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]





def checkday(user):
    if user.month == '':
        new_profile(user)

    datamonth = user.month
    dataday = user.day

    if month != datamonth or day != dataday:
        new_day(user)

def new_profile(user):
    user.month = month
    user.day = day
    user.color = "#FF0000"
    user.hovercolor = "#da190b"
    user.streak = 0
    user.dayyear = '1'
    user.habit = 'Daily habit goal'

def new_day(user):
    user.month = month
    user.day = day
    user.color = "#FF0000"
    user.hovercolor = "#da190b"
    user.save()

def create_record(user):
    checkweek(user)
    final = []
    user.record.weekcolor[weekday] = user.profile.color
    user.record.save()
    for item in weeklist:
        final.append({"day": item, "color": user.record.weekcolor[item]})

    return final

def checkweek(user):
    dataweek = user.profile.week

    if week != dataweek:
        user.profile.week = week
        user.record.weekcolor = {"Monday": "#808080", "Tuesday": "#808080", "Wednesday": "#808080",
                                 "Thursday": "#808080", "Friday": "#808080", "Saturday": "#808080", "Sunday": "#808080"}
        user.record.save()
        user.profile.save()


def streakfunc(user):
    streak = user.streak
    if int(dayyear) - 1 == int(user.dayyear) and user.color == "#32CD32":
        pass

    elif int(dayyear) == int(user.dayyear):
        pass

    else:
        streak = 0

    user.streak = streak
    user.dayyear = dayyear
    user.save()
    return streak
