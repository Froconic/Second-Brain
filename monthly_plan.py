import monthly_forecast as mf
import weekly_plan as wp
import datetime, os


date = datetime.date.today()
year = date.year
title = input("Month: ")
folderPath = "/home/rivre/Documents/Synced Files/Daily-Journal/" + str(year) + "/Monthly/Outline/"
testPath = "/home/rivre/Documents/Synced Files/Daily-Journal/" + str(year) + "/Monthly/Outline/Test/"

# Table of Contents
pn = input("Personal number for the month: ")
pnSection = "### PN: " + str(pn) + "\n\n"
forecastSection = "### Forecasts\n"
forecast = f"[[Daily-Journal/" + str(year) + "/Monthly/Forecasts/" + title + "]]\n"
# energyMapInsert = input("Energy Map for the month: ")
# energyMap = "[[Daily-Journal/" + str(year) + "/Energy maps/" + energyMapInsert + "]]\n\n"
startWeek = input("Starting week number: ")
startWeek = int(startWeek)
weeklySection = "### Weekly \n"
firstWeek = "[[Daily-Journal/" + str(year) + "/Weekly/Outline/W" + str(startWeek) + "]]\n"
secondWeek = "[[Daily-Journal/" + str(year) + "/Weekly/Outline/W" + str(startWeek+1) + "]]\n"
thirdWeek = "[[Daily-Journal/" + str(year) + "/Weekly/Outline/W" + str(startWeek+2) + "]]\n"
fourthWeek = "[[Daily-Journal/" + str(year) + "/Weekly/Outline/W" + str(startWeek+3) + "]]\n\n"
# firstWeek = "[[Daily-Journal/" + str(year) + "/Weekly/Outline/Test/W" + str(month[0]) + "]]\n"
# secondWeek = "[[Daily-Journal/" + str(year) + "/Weekly/Outline/Test/W" + str(month[1]) + "]]\n"
# thirdWeek = "[[Daily-Journal/" + str(year) + "/Weekly/Outline/Test/W" + str(month[2]) + "]]\n"
# fourthWeek = "[[Daily-Journal/" + str(year) + "/Weekly/Outline/Test/W" + str(month[3]) + "]]\n\n"

# print(firstWeek)
# print(secondWeek)
# print(thirdWeek)
# print(fourthWeek)
focusesSection = "### Focuses\n- \n\n"
monthlyGoalsSection = "### Monthly Goals\n---\n"
externalGoalsSection = "#### External \n- [ ] \n\n"
internalGoalsSection = "#### Internal \n- [ ] \n\n"

monthlyTasksSection = "### Monthly Tasks\n---\n"
dailiesSection = "#### Dailies \n- [ ] \n\n"
externalTasksSection = "#### Internal \n- [ ] \n\n"
futureSection = "### Future\n---\n- [ ] \n\n"

reflectionSection = "### Reflection\n---\n"


# print(wp.weekNumber)
# wp.weekNumber = startWeek
# print(startWeek)
# print(wp.weekNumber)


def createPlan():
  print("Monthly Forecast being created")
  mf.pageBuilder(title)
  print("Monthly outline being created")
  fileInsert = title + ".md"
  file = os.path.join(folderPath,fileInsert)
  print(f"File full path: {file}")
  
  with open(file, "w+") as f:
    f.write(pnSection)
    f.write(forecastSection)
    f.write(forecast)
    energyMapInsert = input("Energy Map for the month: ")
    energyMap = "[[Daily-Journal/" + str(year) + "/Energy maps/" + energyMapInsert + "]]\n\n"
    f.write(energyMap)
    f.write(weeklySection)
    f.write(firstWeek)
    sunday = input("Sunday of the week: ")
    monday = input("Monday of the week: ")
    tuesday = input("Tuesday of the week: ")
    wednesday = input("Wednesday of the week: ")
    thursday = input("Thursday of the week: ")
    friday = input("Friday of the week: ")
    saturday = input("Saturday of the week: ")
    sunday = int(sunday)
    monday = int(monday)
    tuesday = int(tuesday)
    wednesday = int(wednesday)
    thursday = int(thursday)
    friday = int(friday)
    saturday = int(saturday)
    week = [sunday,monday,tuesday,wednesday,thursday,friday,saturday]
    wp.createWeek(startWeek,week,int(title))
    f.write(secondWeek)
    sunday = input("Sunday of the week: ")
    monday = input("Monday of the week: ")
    tuesday = input("Tuesday of the week: ")
    wednesday = input("Wednesday of the week: ")
    thursday = input("Thursday of the week: ")
    friday = input("Friday of the week: ")
    saturday = input("Saturday of the week: ")
    sunday = int(sunday)
    monday = int(monday)
    tuesday = int(tuesday)
    wednesday = int(wednesday)
    thursday = int(thursday)
    friday = int(friday)
    saturday = int(saturday)
    week = [sunday,monday,tuesday,wednesday,thursday,friday,saturday]
    wp.createWeek(startWeek+1,week,int(title))
    f.write(thirdWeek)
    sunday = input("Sunday of the week: ")
    monday = input("Monday of the week: ")
    tuesday = input("Tuesday of the week: ")
    wednesday = input("Wednesday of the week: ")
    thursday = input("Thursday of the week: ")
    friday = input("Friday of the week: ")
    saturday = input("Saturday of the week: ")
    sunday = int(sunday)
    monday = int(monday)
    tuesday = int(tuesday)
    wednesday = int(wednesday)
    thursday = int(thursday)
    friday = int(friday)
    saturday = int(saturday)
    week = [sunday,monday,tuesday,wednesday,thursday,friday,saturday]
    wp.createWeek(startWeek+2,week,int(title))
    f.write(fourthWeek)
    sunday = input("Sunday of the week: ")
    monday = input("Monday of the week: ")
    tuesday = input("Tuesday of the week: ")
    wednesday = input("Wednesday of the week: ")
    thursday = input("Thursday of the week: ")
    friday = input("Friday of the week: ")
    saturday = input("Saturday of the week: ")
    sunday = int(sunday)
    monday = int(monday)
    tuesday = int(tuesday)
    wednesday = int(wednesday)
    thursday = int(thursday)
    friday = int(friday)
    saturday = int(saturday)
    week = [sunday,monday,tuesday,wednesday,thursday,friday,saturday]
    wp.createWeek(startWeek+3,week,int(title))
    f.write(focusesSection)
    f.write(monthlyGoalsSection)
    f.write(externalGoalsSection)
    f.write(internalGoalsSection)
    f.write(monthlyTasksSection)
    f.write(dailiesSection)
    f.write(externalGoalsSection)
    f.write(futureSection)
    f.write(reflectionSection)

createPlan()