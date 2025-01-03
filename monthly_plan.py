import monthly_forecast as mf
import weekly_plan as wp
import datetime, os


date = datetime.date.today()
# year = date.year
# title = input("Month: ")
# folderPath = "/home/rivre/Documents/Synced Files/Daily-Journal/" + str(year) + "/Monthly/Outline/"
# folderPath = "/home/akira/Documents/Synced Files/Daily-Journal/" + year + "/Monthly/Outline/"
# testPath = "/home/rivre/Documents/Synced Files/Daily-Journal/" + str(year) + "/Monthly/Outline/Test/"

# Table of Contents
# pn = input("Personal number for the month: ")
# pnSection = "### PN: " + str(pn) + "\n\n"
forecastSection = "### Forecasts\n"
# forecast = f"[[Daily-Journal/" + str(year) + "/Monthly/Forecasts/" + title + "]]\n"
# energyMapInsert = input("Energy Map for the month: ")
# energyMap = "[[Daily-Journal/" + str(year) + "/Energy maps/" + energyMapInsert + "]]\n\n"
# startWeek = input("Starting week number: ")
# startWeek = int(startWeek)
weeklySection = "### Weekly \n"
# firstWeek = "[[Daily-Journal/" + str(year) + "/Weekly/Outline/W" + str(startWeek) + "]]\n"
# secondWeek = "[[Daily-Journal/" + str(year) + "/Weekly/Outline/W" + str(startWeek+1) + "]]\n"
# thirdWeek = "[[Daily-Journal/" + str(year) + "/Weekly/Outline/W" + str(startWeek+2) + "]]\n"
# fourthWeek = "[[Daily-Journal/" + str(year) + "/Weekly/Outline/W" + str(startWeek+3) + "]]\n\n"
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
budgetSection = "| Item        | Expected | Actual | Paid |\n| ----------- | -------- | ------ | ---- |\n| Rent        | 833      |        |      |\n| Wifi        | 25       |        |      |\n| Electricity | 150      |        |      |\n| Youtube     | 25       |        |      |\n| Food        | 500      |        |      |\n| Weed        | 280      |        |      |\n\n"
futureSection = "### Future\n---\n- [ ] \n\n"

reflectionSection = "### Reflection\n---\n"


# print(wp.weekNumber)
# wp.weekNumber = startWeek
# print(startWeek)
# print(wp.weekNumber)

def monthCheck(month, year):
  if "January" in month:
    monthNumber = 1
  if "February" in month:
    monthNumber = 2
  if "March" in month:
    monthNumber = 3
  if "April" in month:
    monthNumber = 4
  if "May" in month:
      monthNumber = 5
  if "June" in month:
      monthNumber = 6
  if "July" in month:
      monthNumber = 7
  if "August" in month:
      monthNumber = 8
  if "September" in month:
      monthNumber = 9
  if "October" in month:
      monthNumber = 10
  if "November" in month:
      monthNumber = 11
  if "December" in month:
      monthNumber = 12
  return monthNumber


def createDays(month, year):
  monthNumber = monthCheck(month,year)
  if monthNumber == 1:
    days = 31
  if monthNumber == 2:
    if int(year) % 4 == 0:
      days = 29
    else:
      days = 28
  if monthNumber == 3:
    days = 31
  if monthNumber == 4:
    days = 30
  if monthNumber == 5:
      days = 31
  if monthNumber == 6:
      days = 30
  if monthNumber == 7:
      days = 31
  if monthNumber == 8:
      days = 31
  if monthNumber == 9:
      days = 30
  if monthNumber == 10:
      days = 31
  if monthNumber == 11:
      days = 30
  if monthNumber == 12:
      days = 31
  for day in range(days):
    print(f"Day {day} being generated")
    wp.dailyNote(day+1, monthNumber, year)
    print(f"Day {day} creation complete")
    
# def monthReset(month,day,year):
#   monthNumber = monthCheck(month,year)
#   if monthNumber == 1 or monthNumber == 3 or monthNumber == 5 or monthNumber == 7 or monthNumber == 8 or monthNumber == 10 or monthNumber == 12:
#     if day > 31:
#       day = 1
#       print("Day reset")
#   if monthNumber == 4 or monthNumber == 6 or monthNumber == 9 or monthNumber == 11:
#     if day > 30:
#       day = 1
#       print("Day reset")
#   if monthNumber == 2 and year % 4 == 0:
#     if day > 29:
#       day = 1
#       print("Day reset")
#   if monthNumber == 2:
#     if day > 28:
#       day = 1
#       print("Day reset")
#   return day


def createWeeks(startWeek, month, year):
  monthNumber = monthCheck(month, year)
  pn = input(f"Personal number for the month of {month}: ")
  pnSection = "### PN: " + str(pn) + "\n\n"
  energyMapInsert = input("Energy Map for the month: ")

  firstWeek = "[[Daily-Journal/" + str(year) + "/Weekly/Outline/W" + str(startWeek) + "]]\n"
  secondWeek = "[[Daily-Journal/" + str(year) + "/Weekly/Outline/W" + str(startWeek+1) + "]]\n"
  thirdWeek = "[[Daily-Journal/" + str(year) + "/Weekly/Outline/W" + str(startWeek+2) + "]]\n"
  fourthWeek = "[[Daily-Journal/" + str(year) + "/Weekly/Outline/W" + str(startWeek+3) + "]]\n\n"
  forecast = f"[[Daily-Journal/" + str(year) + "/Monthly/Forecasts/" + str(monthNumber) + ' ' + month + "]]\n"

  print("Monthly Forecast being created")
  # mf.pageBuilder(month)
  print("Monthly outline being created")
  fileInsert = str(monthNumber) + ' ' + month + ".md"
  folderPath = "/home/rivre/Documents/Synced Files/Daily-Journal/" + str(year) + "/Monthly/Outline/"
  file = os.path.join(folderPath,fileInsert)
  print(f"File full path: {file}")
  
  with open(file, "w+") as f:
    f.write(pnSection)
    f.write(forecastSection)
    f.write(forecast)
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
    # sunday = monthReset(sunday,monthNumber,year)
    
    monday = int(monday)
    # monday = monthReset(monday,monthNumber,year)
    
    tuesday = int(tuesday)
    # tuesday = monthReset(tuesday,monthNumber,year)
    
    wednesday = int(wednesday)
    # wednesday = monthReset(wednesday,monthNumber,year)
    
    thursday = int(thursday)
    # thursday = monthReset(thursday,monthNumber,year)
    
    friday = int(friday)
    # friday =  monthReset(friday,monthNumber,year)
    
    saturday = int(saturday)
    # saturday = monthReset(saturday,monthNumber,year)
    
    week = [sunday,monday,tuesday,wednesday,thursday,friday,saturday]
    wp.createWeek(startWeek,week,monthNumber,pn,year)
    print(f"Week {startWeek} Complete")
    
    f.write(secondWeek)
    sunday = saturday + 1
    # sunday = monthReset(sunday,monthNumber,year)

    monday = sunday + 1
    # monday = monthReset(monday,monthNumber,year)

    tuesday = monday + 1
    # tuesday = monthReset(tuesday,monthNumber,year)

    wednesday = tuesday + 1
    # wednesday = monthReset(wednesday,monthNumber,year)

    thursday = wednesday + 1
    # thursday = monthReset(thursday,monthNumber,year)

    friday = thursday + 1
    # friday =  monthReset(friday,monthNumber,year)

    saturday = friday + 1
    # saturday = monthReset(saturday,monthNumber,year)

    week = [sunday,monday,tuesday,wednesday,thursday,friday,saturday]
    wp.createWeek(startWeek+1,week,monthNumber,pn,year)
    print(f"Week {startWeek+1} Complete")
    
    f.write(thirdWeek)
    sunday = saturday + 1
    # sunday = monthReset(sunday,monthNumber,year)

    monday = sunday + 1
    # monday = monthReset(monday,monthNumber,year)

    tuesday = monday + 1
    # tuesday = monthReset(tuesday,monthNumber,year)

    wednesday = tuesday + 1
    # wednesday = monthReset(wednesday,monthNumber,year)

    thursday = wednesday + 1
    # thursday = monthReset(thursday,monthNumber,year)

    friday = thursday + 1
    # friday =  monthReset(friday,monthNumber,year)

    saturday = friday + 1
    # saturday = monthReset(saturday,monthNumber,year)

    week = [sunday,monday,tuesday,wednesday,thursday,friday,saturday]
    wp.createWeek(startWeek+2,week,monthNumber,pn,year)
    print(f"Week {startWeek+2} Complete")
    
    f.write(fourthWeek)
    sunday = saturday + 1
    # sunday = monthReset(sunday,monthNumber,year)

    monday = sunday + 1
    # monday = monthReset(monday,monthNumber,year)

    tuesday = monday + 1
    # tuesday = monthReset(tuesday,monthNumber,year)

    wednesday = tuesday + 1
    # wednesday = monthReset(wednesday,monthNumber,year)

    thursday = wednesday + 1
    # thursday = monthReset(thursday,monthNumber,year)

    friday = thursday + 1
    # friday =  monthReset(friday,monthNumber,year)

    saturday = friday + 1
    # saturday = monthReset(saturday,monthNumber,year)

    week = [sunday,monday,tuesday,wednesday,thursday,friday,saturday]
    wp.createWeek(startWeek+3,week,monthNumber,pn,year)
    print(f"Week {startWeek+3} Complete")
    
    f.write(focusesSection)
    f.write(monthlyGoalsSection)
    f.write(externalGoalsSection)
    f.write(internalGoalsSection)
    f.write(monthlyTasksSection)
    f.write(dailiesSection)
    f.write(externalGoalsSection)
    f.write(budgetSection)
    f.write(reflectionSection)
    f.write(futureSection)
    print(f'{month} plan complete')

# createPlan()