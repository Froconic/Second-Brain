# TODO figure a way to make folder selection relative or dynamic to work on other systems
# TODO Refactor things and compartmentalize things to ease flow


import weekly_forecast as wf
import datetime, os

# Setting all global variables
date = datetime.date.today()
year = date.year
leapYear = year % 4
yearString = str(year)
months = [1,2,3,4,5,6,7,8,9,10,11,12]
# monthString = str(month)
firstDay = 1
# weekNumber = input("Week number: ")
weekNumber = ""
# weekStart = input("Sunday's date: ")
# weekStart = int(weekStart)
# energyMapInsert = input("energy map for this week: ")
folderPath = "/home/rivre/Documents/Synced Files/Daily-Journal/" + str(year) + "/Weekly/Outline"
testWeeklyFolderPath = "/home/rivre/Documents/Synced Files/Daily-Journal/" + str(year) + "/Weekly/Outline/Test"
testFolderPath = "/home/rivre/Documents/Synced Files/Daily-Journal/" + str(year) + "/Dailies/Test"
# print(folderPath)

# Table of contents
forecast = "[[Daily-Journal/" + str(year) + "/Weekly/Forecasts/" + weekNumber + "|Forecast]]\n"
tasks = "[[#Major Tasks]]\n"
movement = "[[#Movement]]\n\n"

# Each day in the obsidian backlink format
days = "### Days\n"
# week = [weekStart,weekStart+1,weekStart+2,weekStart+3,weekStart+4,weekStart+5,weekStart+6]
# Energy Map section (moon log)
energyMapTitle = "### Energy Map\n"
# energyMap = "- [[Daily-Journal/2024/Energy Maps/" + energyMapInsert + "|" + energyMapInsert + "]]\n\n"

# Focus Section
focuses = "### Focuses\n- \n\n"

# Weekly events section
events = "### Events\n"
sun = "#### Sun\n- \n\n"
mon = "#### Mon\n- \n\n"
tues = "#### Tues\n- \n\n"
wed = "#### Wed\n- \n\n"
thurs = "#### Thurs\n- \n\n"
fri = "#### Fri\n- \n\n"
sat = "#### Sat\n- \n\n"

# tasks section
majorTasks = "# Major Tasks\n- [ ] \n\n"
dailyActions = "# Daily Actions\n- \n\n"
moves = "# Movement\n- [ ] \n\n"
meals = "# Meals\n- \n\n"

# Check current month amongst year
def monthCheck(check):
  temp = 0
  # print(temp)
  if check == 1:
    temp = months[0]
    # print(temp)
    return temp
  if leapYear == 0 and check == 2:
    temp = months[1]
    # print(temp)
    return temp
  if check == 2:
    temp = months[1]
    # print(temp)
    return temp
  if check == 3:
    temp = months[2]
    # print(temp)
    return temp
  if check == 4:
    temp = months[3]
    # print(temp)
    return temp
  if check == 5:
    temp = months[4]
    # print(temp)
    return temp
  if check == 6:
    temp = months[5]
    # print(temp)
    return temp
  if check == 7:
    temp = months[6]
    # print(temp)
    return temp
  if check == 8:
    temp = months[7]
    # print(temp)
    return temp
  if check == 9:
    temp = months[8]
    # print(temp)
    return temp
  if check == 10:
    temp = months[9]
    # print(temp)
    return temp
  if check == 11:
    temp = months[10]
    # print(temp)
    return temp
  if check == 12:
    temp = months[11]
    # print(temp)
    return temp

def monthPlus(day,month):
  if day == firstDay:
    print("Next month detected")
    month = month + 1
    print(f"Next month: {month}")
    return month
  else:
    return month

# Match last day of the month to the current month
def lastDayOfMonthCheck(check):
  temp = 0
  # print(temp)
  if check == 1:
    temp = 31
    # print(temp)
    return temp
  if leapYear == 0 and check == 2:
    temp = 29
    # print(temp)
    return temp
  if check == 2:
    temp = 28
    # print(temp)
    return temp
  if check == 3:
    temp = 31
    # print(temp)
    return temp
  if check == 4:
    temp = 30
    # print(temp)
    return temp
  if check == 5:
    temp = 31
    # print(temp)
    return temp
  if check == 6:
    temp = 30
    # print(temp)
    return temp
  if check == 7:
    temp = 31
    # print(temp)
    return temp
  if check == 8:
    temp = 31
    # print(temp)
    return temp
  if check == 9:
    temp = 30
    # print(temp)
    return temp
  if check == 10:
    temp = 31
    # print(temp)
    return temp
  if check == 11:
    temp = 30
    # print(temp)
    return temp
  if check == 12:
    temp = 31
    # print(temp)
    return temp

# lastDay = lastDayOfMonthCheck(month)
# print(lastDay)

# Check to see if the week crosses over to the next month and adjust list
def EOM(week, lastDay):
  limitExceeded = False
  
  for i in range(len(week)):
    if week[i] > lastDay:
      limitExceeded = True
      print("end of the month detected")
      # month = month + 1
      week[i] = 1
      
    if limitExceeded:
      for j in range(i + 1, len(week)):
        week[j] = week[j-1] + 1
        # print(week[j])
  # print(week)
  return week

# EOM(week,lastDay)

def dailyNote(day,month):
  title = str(day) + '.md'
  # folder = "/home/rivre/Documents/Synced Files/Daily-Journal/" + str(year) + "/Dailies/Test/" + str(month)
  folder = "/home/rivre/Documents/Synced Files/Daily-Journal/" + str(year) + "/Dailies/" + str(month)
  # Join path and create file
  path = os.path.join(folder,title)
  print(f"Day: {day}")
  with open(path, 'w+') as f:
    f.write("# TOC\n")
    f.write("[[#Interpretation]]\n")
    f.write("[[#Deep Work Focus]]\n")
    f.write("[[#Daily Practice]]\n")
    f.write("[[#TODO]]\n")
    f.write("[[#Syncs / Signs]]\n")
    f.write("[[#Brain Dump]]\n\n\n")
    
    f.write("# Daily Conditions\n\n")
    f.write("# PN\n")
    f.write("- [ ] 1\n")
    f.write("- [ ] 2\n")
    f.write("- [ ] 3\n")
    f.write("- [ ] 4\n")
    f.write("- [ ] 5\n")
    f.write("- [ ] 6\n")
    f.write("- [ ] 7\n")
    f.write("- [ ] 8\n")
    f.write("- [ ] 9\n\n")
    
    f.write("# Mansion:\n")
    f.write("- [ ] 1\n")
    f.write("- [ ] 2 \n")
    f.write("- [ ] 3 \n")
    f.write("- [ ] 4 \n")
    f.write("- [ ] 5 \n")
    f.write("- [ ] 6 \n")
    f.write("- [ ] 7 \n")
    f.write("- [ ] 8 \n")
    f.write("- [ ] 9 \n")
    f.write("- [ ] 10 \n")
    f.write("- [ ] 11 \n")
    f.write("- [ ] 12 \n")
    f.write("- [ ] 13 \n")
    f.write("- [ ] 14 \n")
    f.write("- [ ] 15 \n")
    f.write("- [ ] 16 \n")
    f.write("- [ ] 17 \n")
    f.write("- [ ] 18 \n")
    f.write("- [ ] 19 \n")
    f.write("- [ ] 20 \n")
    f.write("- [ ] 21 \n")
    f.write("- [ ] 22 \n")
    f.write("- [ ] 23 \n")
    f.write("- [ ] 24 \n")
    f.write("- [ ] 25 \n")
    f.write("- [ ] 26 \n")
    f.write("- [ ] 27 \n")
    f.write("- [ ] 28 \n\n")
    
    f.write("# Planet: \n")
    f.write("- [ ] Sun\n")
    f.write("- [ ] Moon\n")
    f.write("- [ ] Mars\n")
    f.write("- [ ] Mercury\n")
    f.write("- [ ] Jupiter\n")
    f.write("- [ ] Venus\n")
    f.write("- [ ] Saturn\n\n")
    
    f.write("# Lunar Age:\n")
    f.write("- [ ] 1\n")
    f.write("- [ ] 2 \n")
    f.write("- [ ] 3 \n")
    f.write("- [ ] 4 \n")
    f.write("- [ ] 5 \n")
    f.write("- [ ] 6 \n")
    f.write("- [ ] 7 \n")
    f.write("- [ ] 8 \n")
    f.write("- [ ] 9 \n")
    f.write("- [ ] 10 \n")
    f.write("- [ ] 11 \n")
    f.write("- [ ] 12 \n")
    f.write("- [ ] 13 \n")
    f.write("- [ ] 14 \n")
    f.write("- [ ] 15 \n")
    f.write("- [ ] 16 \n")
    f.write("- [ ] 17 \n")
    f.write("- [ ] 18 \n")
    f.write("- [ ] 19 \n")
    f.write("- [ ] 20 \n")
    f.write("- [ ] 21 \n")
    f.write("- [ ] 22 \n")
    f.write("- [ ] 23 \n")
    f.write("- [ ] 24 \n")
    f.write("- [ ] 25 \n")
    f.write("- [ ] 26 \n")
    f.write("- [ ] 27 \n")
    f.write("- [ ] 28 \n")
    f.write("- [ ] 29 \n\n")

    f.write("# Lunar Sign: \n")
    f.write("- [ ] Aries\n")
    f.write("- [ ] Taurus\n")
    f.write("- [ ] Gemini\n")
    f.write("- [ ] Cancer\n")
    f.write("- [ ] Leo\n")
    f.write("- [ ] Virgo\n")
    f.write("- [ ] Libra\n")
    f.write("- [ ] Scorpio\n")
    f.write("- [ ] Sagittarius\n")
    f.write("- [ ] Capricorn\n")
    f.write("- [ ] Aquarius\n")
    f.write("- [ ] Pisces\n\n")

    f.write("# Solar Sign: \n")
    f.write("- [ ] Aries\n")
    f.write("- [ ] Taurus\n")
    f.write("- [ ] Gemini\n")
    f.write("- [ ] Cancer\n")
    f.write("- [ ] Leo\n")
    f.write("- [ ] Virgo\n")
    f.write("- [ ] Libra\n")
    f.write("- [ ] Scorpio\n")
    f.write("- [ ] Sagittarius\n")
    f.write("- [ ] Capricorn\n")
    f.write("- [ ] Aquarius\n")
    f.write("- [ ] Pisces\n\n")

    f.write("# Interpretation\n")
    f.write("---\n")
    f.write("Today aids in \n\n")
    f.write("Today hinders in \n\n\n")
    
    f.write("# TODO\n")
    f.write("### Events\n- \n\n")
    f.write("#### Tomorrow\n- \n\n")
    
    f.write("### Ideal\n- [ ] \n\n")
    f.write("#### Tomorrow\n- [ ] \n\n")
    
    f.write("### Deep Work Focus\n- [ ] \n\n")
    f.write("#### Tomorrow\n- [ ] \n\n")
    f.write("### Done\n- \n\n")
    
    f.write("# Daily Practice\n")
    f.write("### Morning\n")
    f.write("### Sacred Space\n")
    f.write("- [ ] Move\n")
    f.write("- [ ] 10 mins\n")
    f.write("- [ ] 15 mins\n")
    f.write("- [ ] 30 mins\n")
    f.write("- [ ] 45 mins\n")
    f.write("- [ ] 1 hour\n")
    f.write("    - [ ] Stretch\n")
    f.write("    - [ ] Mobility\n")
    f.write("    - [ ] Primal\n")
    f.write("    - [ ] Taichi\n")
    f.write("    - [ ] Qi Gong\n")
    f.write("    - [ ] Capoeira\n")
    f.write("    - [ ] Staff\n")
    f.write("    - [ ] Mace\n")
    f.write("    - [ ] Animal\n")
    f.write("    - [ ] Calisthenics\n")
    f.write("    - [ ] Box\n")
    f.write("    - [ ] Walk\n")
    f.write("    - [ ] Jog\n")
    f.write("- [ ] Tea time\n")
    f.write("- [ ] Thought Space\n")
    f.write("- [ ] Plan / Review\n")
    f.write("- [ ] Check in\n")
    f.write("- [ ] Meditate\n")
    f.write("    - [ ] Contemplation\n")
    f.write("    - [ ] Art\n")
    f.write("    - [ ] Music\n")
    f.write("    - [ ] Taichi\n")
    f.write("    - [ ] Qi gong\n")
    f.write("    - [ ] Movement\n")
    f.write("    - [ ] Walk\n")
    f.write("    - [ ] Energy Cycles\n")
    f.write("    - [ ] Flow Work\n\n")
    f.write("### Deep work\n")
    f.write("- [ ] 1 hour\n")
    f.write("- [ ] 2 hour\n")
    f.write("- [ ] 3 hour\n")
    f.write("- [ ] 4 hour\n")
    f.write("- [ ] Plan next session\n")
    f.write("- [ ] Admin\n")
    f.write("- [ ] Code\n")
    f.write("- [ ] Art\n")
    f.write("- [ ] Magick\n")
    f.write("- [ ] Side gig\n")
    f.write("- [ ] Study / Research\n")
    f.write("- [ ] Practice\n")
    f.write("- [ ] Creative Project\n")
    f.write("- [ ] Second Brain\n\n")
    
    f.write("### Hygiene\n")
    f.write("- [ ] Shower\n")
    f.write("- [ ] Brush teeth\n")
    f.write("- [ ] Wash Face\n")
    f.write("- [ ] Wash Pits\n")
    f.write("- [ ] Moisturize\n")
    f.write("- [ ] Spray pits\n\n")
    
    f.write("### Evening\n")
    f.write("- [ ] Review day\n")
    f.write("- [ ] Plan next day\n")
    f.write("    - [ ] Deep work\n")
    f.write("    - [ ] Events\n")
    f.write("    - [ ] Tasks\n")
    f.write("    - [ ] Moves\n")
    f.write("    - [ ] Daily Conditions\n")
    f.write("- [ ] Oil Pulling\n")
    f.write("- [ ] Brush Teeth\n")
    f.write("- [ ] Put phone away\n")
    f.write("- [ ] Set up for next day\n")
    f.write("- [ ] Stretch\n")
    f.write("- [ ] Meditate\n")
    f.write("- [ ] Story time\n\n")

    f.write("# Gratitude\n- \n\n")
    
    f.write("# Mental focuses\n- \n\n")
    
    f.write("# Body\n")
    f.write("## Start\n- \n\n")
    f.write("## Middle\n- \n\n")
    f.write("## End\n- \n\n")
    
    f.write("# Energy\n")
    f.write("## Start\n- \n\n")
    f.write("## Middle\n- \n\n")
    f.write("## End\n- \n\n")
    
    f.write("### Morning Levels\n")
    f.write("##### Mental:\n\n")
    f.write("##### Physical:\n\n")
    f.write("##### Emotional:\n\n")
    f.write("##### Social:\n\n")
    f.write("##### Creative:\n\n")
    f.write("##### Total:\n\n")

    f.write("### Evening Levels\n")
    f.write("##### Mental:\n\n")
    f.write("##### Physical:\n\n")
    f.write("##### Emotional:\n\n")
    f.write("##### Social:\n\n")
    f.write("##### Creative:\n\n")
    f.write("##### Total:\n\n")
    
    f.write("# Syncs / Signs\n- \n\n")
    f.write("# Reflections / Highlights\n")
    f.write("### What drained me today?\n- \n\n")
    f.write("### What energized me today?\n- \n\n")
    f.write("# Brain Dump\n- \n\n")
    f.write("# Related\n")
    f.write("[[#TOC]]\n")
    f.write("[[#Deep Work Focus]]\n")
    f.write("[[#Daily Practice]]\n")
    f.write("[[#TODO]]\n")
    f.write("[[#Syncs / Signs]]\n")
    

def createWeek(weekNumber,week,month):
  # Create title and folder path
  # print(month)
  wf.pageBuilder(str(weekNumber))
  lastDay = lastDayOfMonthCheck(month)
  # print(lastDay)
  
  EOM(week,lastDay)
  print(f"{weekNumber} outline being created")
  # print(weekNumber)
  # weekStart = input("Sunday's date: ")
  # weekStart = int(weekStart)
  # week = [weekStart,weekStart+1,weekStart+2,weekStart+3,weekStart+4,weekStart+5,weekStart+6]
  energyMapInsert = input("energy map for this week: ")
  energyMap = "- [[Daily-Journal/2024/Energy Maps/" + energyMapInsert + "|" + energyMapInsert + "]]\n\n"

  print("Weekly outline creation commencing")
  title = "W" + str(weekNumber) + ".md"
  # print(f"File name:{title}")
  folder = folderPath
  # print(f"Folder path for outline: {folder}")
  path = os.path.join(folder,title)
  print(path)
  # print(month)
  
  # Open file and insert layout
  with open(path, "w+") as f:
    f.write(f"[[Daily-Journal/" + str(year) + "/Weekly/Forecasts/" + str(weekNumber) + "|Forecast]]\n")
    f.write(tasks)
    f.write(movement)
    f.write(days)
    print("Generating days of the week")
    month = monthPlus(week[0], month)
    # print(month)
    # f.write(f"[[Daily-Journal/{yearString}/Dailies/Test/{month}/{week[0]}|{week[0]}]]\n")
    f.write(f"[[Daily-Journal/{yearString}/Dailies/{month}/{week[0]}|{week[0]}]]\n")
    dailyNote(week[0],month)
    print("Sunday generated")
    month = monthPlus(week[1], month)
    # print(month)
    # f.write(f"[[Daily-Journal/{yearString}/Dailies/Test/{month}/{week[1]}|{week[1]}]]\n")
    f.write(f"[[Daily-Journal/{yearString}/Dailies/{month}/{week[1]}|{week[1]}]]\n")
    dailyNote(week[1],month)
    print("Monday generated")
    month = monthPlus(week[2], month)
    # print(month)
    # f.write(f"[[Daily-Journal/{yearString}/Dailies/Test/{month}/{week[2]}|{week[2]}]]\n")
    f.write(f"[[Daily-Journal/{yearString}/Dailies/{month}/{week[2]}|{week[2]}]]\n")
    dailyNote(week[2],month)
    print("Tuesday generated")
    month = monthPlus(week[3], month)
    # print(month)
    # f.write(f"[[Daily-Journal/{yearString}/Dailies/Test/{month}/{week[3]}|{week[3]}]]\n")
    f.write(f"[[Daily-Journal/{yearString}/Dailies/{month}/{week[3]}|{week[3]}]]\n")
    dailyNote(week[3],month)
    print("Wednesday generated")
    month = monthPlus(week[4], month)
    # print(month)
    # f.write(f"[[Daily-Journal/{yearString}/Dailies/Test/{month}/{week[4]}|{week[4]}]]\n")
    f.write(f"[[Daily-Journal/{yearString}/Dailies/{month}/{week[4]}|{week[4]}]]\n")
    dailyNote(week[4],month)
    print("Thursday generated")
    month = monthPlus(week[5], month)
    # print(month)
    # f.write(f"[[Daily-Journal/{yearString}/Dailies/Test/{month}/{week[5]}|{week[5]}]]\n")
    f.write(f"[[Daily-Journal/{yearString}/Dailies/{month}/{week[5]}|{week[5]}]]\n")
    dailyNote(week[5],month)
    print("Friday generated")
    month = monthPlus(week[6], month)
    # print(month)
    # f.write(f"[[Daily-Journal/{yearString}/Dailies/Test/{month}/{week[6]}|{week[6]}]]\n\n")
    f.write(f"[[Daily-Journal/{yearString}/Dailies/{month}/{week[6]}|{week[6]}]]\n\n")
    dailyNote(week[6],month)
    print("Saturday generated")
    f.write(energyMapTitle)
    f.write(energyMap)
    f.write(focuses)
    f.write(events)
    f.write(sun)
    f.write(mon)
    f.write(tues)
    f.write(wed)
    f.write(thurs)
    f.write(fri)
    f.write(sat)
    f.write(majorTasks)
    f.write(dailyActions)
    f.write(moves)
    f.write(meals)
    

# create()