seconds = int(input())
minutes = seconds // 60
hours = minutes // 60
days = hours // 24
months = days // 30
years = months // 12
decades = years // 10

if minutes == 0:
    print(seconds, "<s>")
elif hours ==0:
    print(minutes, "<m>", seconds - minutes*60, "<s>")
elif days ==0:
    print(hours, "<h>", minutes - hours*60, "<m>", seconds - minutes*60, "<s>")
elif months ==0:
    print(days, "<d>", hours-days*24, "<h>", minutes-hours*60, "<m>", seconds-minutes*60, "<s>" )
elif years == 0:
    print(months, "<mon>", days-months*30, "<d>", hours-days*24, "<h>", minutes-hours*60, "<m>", seconds-minutes*60, "<s>")
elif decades ==0:
    print(years, "<y>", months-years*12, "<mon>", days-months*30, "<d>", hours-days*24, "<h>", minutes-hours*60, "<m>", seconds-minutes*60, "<s>")
else:
    print(decades, "<dec>", years-decades*10, "<y>", months-years*12, "<mon>", days-months*30, "<d>", hours-days*24, "<h>", minutes-hours*60, "<m>", seconds-minutes*60, "<s>")