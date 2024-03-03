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
month = [startWeek,startWeek+1,startWeek+2,startWeek+3]
startDay = input("Sunday of the first full week: ")
startDay = int(startDay)
week1 = [startDay,startDay+1,startDay+2,startDay+3,startDay+4,startDay+5,startDay+6]
week2 = [startDay+7,startDay+8,startDay+9,startDay+10,startDay+11,startDay+12,startDay+13]
week3 = [startDay+14,startDay+15,startDay+16,startDay+17,startDay+18,startDay+19,startDay+20]
week4 = [startDay+21,startDay+22,startDay+23,startDay+24,startDay+25,startDay+26,startDay+27]
weeklySection = "### Weekly \n"
firstWeek = "[[Daily-Journal/" + str(year) + "/Weekly/Outline/W" + str(month[0]) + "]]\n"
secondWeek = "[[Daily-Journal/" + str(year) + "/Weekly/Outline/W" + str(month[1]) + "]]\n"
thirdWeek = "[[Daily-Journal/" + str(year) + "/Weekly/Outline/W" + str(month[2]) + "]]\n"
fourthWeek = "[[Daily-Journal/" + str(year) + "/Weekly/Outline/W" + str(month[3]) + "]]\n\n"
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
    wp.createWeek(month[0], week1,int(title))
    f.write(secondWeek)
    wp.createWeek(month[1],week2,int(title))
    f.write(thirdWeek)
    wp.createWeek(month[2],week3,int(title))
    f.write(fourthWeek)
    wp.createWeek(month[3],week4,int(title))
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