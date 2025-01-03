# TODO figure a way to make folder selection relative or dynamic to work on other systems
# TODO Refactor things and compartmentalize things to ease flow


import weekly_forecast as wf
import datetime, os

# Setting all global variables
date = datetime.date.today()
# year = date.year
# leapYear = year % 4
# yearString = str(year)
months = [1,2,3,4,5,6,7,8,9,10,11,12]
week1 = []
week2 = []
week3 = []
week4 = []
weeks = []
weekNumber = ""
# folderPath = "/home/akira/Documents/Synced Files/Daily-Journal/" + str(year) + "/Weekly/Outline"
# folderPath = "Daily-Journal/" + str(year) + "/Weekly/Outline"
# testWeeklyFolderPath = "Daily-Journal/" + str(year) + "/Weekly/Outline/Test"
# testFolderPath = "Daily-Journal/" + str(year) + "/Dailies/Test"

def dailyNote(day,monthNumber, year):
  title = str(day) + '.md'
  # folder = "Daily-Journal/" + str(year) + "/Dailies/Test/" + str(monthNumber)
  # Join path and create file
  # folder = "/home/akira/Documents/Synced Files/Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber)
  folder = "/home/rivre/Documents/Synced Files/Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber)
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
    f.write("### Boons\n")
    f.write("- \n\n")
    f.write("### Banes \n")
    f.write("- \n\n")
    
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
    f.write("    - [ ] Shaolin\n")
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
    f.write("- [ ] Thought Space\n")
    f.write("- [ ] Art\n")
    f.write("- [ ] Music\n")
    f.write("- [ ] Side gig\n")
    f.write("- [ ] Magick\n")
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
    f.write("- [ ] Check in\n")
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
    
    f.write("# Check in\n\n")
    f.write("## Sun time?\n\n")
    f.write(" - [ ] Yes\n")
    f.write("### Time:\n")
    f.write(" - [ ] No\n\n")
    
    
    f.write("## Sleep Quality\n")
    f.write("### Time:\n")
    f.write("### Broken?\n")
    f.write(" - [ ] Yes\n")
    f.write(" - [ ] No\n\n")
    
    f.write("## Meals\n- \n\n")
    f.write("## Hydration\n- \n\n")
    
    f.write("# Body\n")
    f.write("## Start\n- \n\n")
    f.write("## Middle\n- \n\n")
    f.write("## End\n- \n\n")
    
    f.write("# Energy\n")
    f.write("## Start\n- \n\n")
    f.write("## Middle\n- \n\n")
    f.write("## End\n- \n\n")
    
    f.write("### Morning Levels\n")
    f.write("##### Mental: \n\n")
    f.write("##### Physical: \n\n")
    f.write("##### Emotional: \n\n")
    f.write("##### Social: \n\n")
    f.write("##### Creative: \n\n")
    f.write("##### Total: \n\n")

    f.write("### Evening Levels\n")
    f.write("##### Mental: \n\n")
    f.write("##### Physical: \n\n")
    f.write("##### Emotional: \n\n")
    f.write("##### Social: \n\n")
    f.write("##### Creative: \n\n")
    f.write("##### Total: \n\n")
    
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
    
# def monthCheck(week,monthNumber,f):
#   for day in week:
#     if day > 25:
#       check = input(f"Is this day ({day}) from last month? Y/N ")
#       if check == "Y":
#         f.write(f"[[Daily-Journal/{yearString}/Dailies/{monthNumber-1}/{day}|{day}]]\n")
#         dailyNote(day,monthNumber-1)
#       else:
#         f.write(f"[[Daily-Journal/{yearString}/Dailies/{monthNumber}/{day}|{day}]]\n")
#         dailyNote(day,monthNumber)
#     else:
#       f.write(f"[[Daily-Journal/{yearString}/Dailies/{monthNumber}/{day}|{day}]]\n")
#       dailyNote(day,monthNumber)


def createWeek(weekNumber,week,monthNumber,pn, year):
  # Table of contents
  tasks = "[[#Major Tasks]]\n"
  movement = "[[#Movement]]\n\n"

  # Each day in the obsidian backlink format
  days = "### Days\n"
  sunday = week[0]
  monday = week[1]
  tuesday = week[2]
  wednesday = week[3]
  thursday = week[4]
  friday = week[5]
  saturday = week[6]
  check = ''


  
  # Energy Map section (moon log)
  energyMapTitle = "### Energy Map\n"

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
  spent = "# Spent this week\n"
  table = "| Spent on | Amount | Total in Bank |\n| -------- | ------ | ------------- |\n|          |        |               |"

  # Create title and folder path
  wf.pageBuilder(str(weekNumber),pn,year)

  print(f"Week {weekNumber} outline being created")
  energyMapInsert = input("energy map for this week: ")
  energyMap = "- [[Daily-Journal/2024/Energy Maps/" + energyMapInsert + "|" + energyMapInsert + "]]\n\n"

  print("Weekly outline creation commencing")
  folderPath = "/home/rivre/Documents/Synced Files/Daily-Journal/" + str(year) + "/Weekly/Outline"
  title = "W" + str(weekNumber) + ".md"
  folder = folderPath
  path = os.path.join(folder,title)
  print(path)
  
  # Open file and insert layout
  with open(path, "w+") as f:
    f.write(f"[[Daily-Journal/" + str(year) + "/Weekly/Forecasts/" + str(weekNumber) + "|Forecast]]\n")
    f.write(tasks)
    f.write(movement)
    f.write(days)
    
    if monthNumber == 3 and sunday >= 23:
      check = input(f"Is this day the {week[0]} from last month? Y/N")

      if check == 'Y' or check == 'y':
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber-1) + "/" + str(sunday) + '|' + str(sunday) + ']]\n')
      else:
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(sunday) + '|' + str(sunday) + ']]\n')
    elif monthNumber == 3 and sunday <= 23:
      f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(sunday) + '|' + str(sunday) + ']]\n')
      
    if monthNumber != 3 and sunday >= 26:
      check = input(f"Is this day the {week[0]} from last month? Y/N")

      if check == 'Y' or check == 'y':
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber-1) + "/" + str(sunday) + '|' + str(sunday) + ']]\n')
      else:
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(sunday) + '|' + str(sunday) + ']]\n')
    elif monthNumber != 3 and sunday <= 26:
      f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(sunday) + '|' + str(sunday) + ']]\n')
    
    if monthNumber == 3 and monday >= 23:
      check = input(f"Is this day the {week[1]} from last month? Y/N")

      if check == 'Y' or check == 'y':
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber-1) + "/" + str(monday) + '|' + str(monday) + ']]\n')
      else:
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(monday) + '|' + str(monday) + ']]\n')
    elif monthNumber == 3 and monday <= 23:
      f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(monday) + '|' + str(monday) + ']]\n')
       
    elif monthNumber != 3 and monday <= 26:
      f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(monday) + '|' + str(monday) + ']]\n')
      
    if monthNumber != 3 and monday >= 26:
      check = input(f"Is this day the {week[1]} from last month? Y/N")

      if check == 'Y' or check == 'y':
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber-1) + "/" + str(monday) + '|' + str(monday) + ']]\n')
      else:
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(monday) + '|' + str(monday) + ']]\n')

    if monthNumber == 3 and tuesday >= 23:
      check = input(f"Is this day the {week[2]} from last month? Y/N")

      if check == 'Y' or check == 'y':
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber-1) + "/" + str(tuesday) + '|' + str(tuesday) + ']]\n')
      else:
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(tuesday) + '|' + str(tuesday) + ']]\n')
    elif monthNumber == 3 and tuesday <= 23:
      f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(tuesday) + '|' + str(tuesday) + ']]\n')
      
    if monthNumber != 3 and tuesday >= 26:
      check = input(f"Is this day the {week[2]} from last month? Y/N")

      if check == 'Y' or check == 'y':
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber-1) + "/" + str(tuesday) + '|' + str(tuesday) + ']]\n')
      else:
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(tuesday) + '|' + str(tuesday) + ']]\n')
    elif monthNumber != 3 and tuesday <= 26:
      f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(tuesday) + '|' + str(tuesday) + ']]\n')
    
    if monthNumber == 3 and wednesday >= 23:
      check = input(f"Is this day the {week[3]} from last month? Y/N")

      if check == 'Y' or check == 'y':
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber-1) + "/" + str(wednesday) + '|' + str(wednesday) + ']]\n')
      else:
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(wednesday) + '|' + str(wednesday) + ']]\n')
    elif monthNumber == 3 and wednesday <= 23:
      f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(wednesday) + '|' + str(wednesday) + ']]\n')
      
    if monthNumber != 3 and wednesday >= 26:
      check = input(f"Is this day the {week[3]} from last month? Y/N")

      if check == 'Y' or check == 'y':
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber-1) + "/" + str(wednesday) + '|' + str(wednesday) + ']]\n')
      else:
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(wednesday) + '|' + str(wednesday) + ']]\n')
    elif monthNumber != 3 and wednesday <= 26:
      f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(wednesday) + '|' + str(wednesday) + ']]\n')
        
    if monthNumber == 3 and thursday >= 23:
      check = input(f"Is this day the {week[4]} from last month? Y/N")

      if check == 'Y' or check == 'y':
          f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber-1) + "/" + str(thursday) + '|' + str(thursday) + ']]\n')
      else:
          f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(thursday) + '|' + str(thursday) + ']]\n')
    elif monthNumber == 3 and thursday <= 23:
      f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(thursday) + '|' + str(thursday) + ']]\n')
    
    if monthNumber != 3 and thursday >= 26:
      check = input(f"Is this day the {week[4]} from last month? Y/N")

      if check == 'Y' or check == 'y':
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber-1) + "/" + str(thursday) + '|' + str(thursday) + ']]\n')
      else:
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(thursday) + '|' + str(thursday) + ']]\n')
    elif monthNumber != 3 and thursday <= 26:
      f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(thursday) + '|' + str(thursday) + ']]\n')

    if monthNumber == 3 and friday >= 23:
      check = input(f"Is this day the {week[5]} from last month? Y/N")

      if check == 'Y' or check == 'y':
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber-1) + "/" + str(friday) + '|' + str(friday) + ']]\n')
      else:
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(friday) + '|' + str(friday) + ']]\n')
    elif monthNumber == 3 and friday <= 23:
      f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(friday) + '|' + str(friday) + ']]\n')
        
    if monthNumber != 3 and friday >= 26:
      check = input(f"Is this day the {week[5]} from last month? Y/N")

      if check == 'Y' or check == 'y':
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber-1) + "/" + str(friday) + '|' + str(friday) + ']]\n')
      else:
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(friday) + '|' + str(friday) + ']]\n')
    elif monthNumber != 3 and friday <= 26:
      f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(friday) + '|' + str(friday) + ']]\n')

    if monthNumber == 3 and saturday >= 23:
      check = input(f"Is this day the {week[6]} from last month? Y/N")

      if check == 'Y' or check == 'y':
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber-1) + "/" + str(saturday) + '|' + str(saturday) + ']]\n')
      else:
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(saturday) + '|' + str(saturday) + ']]\n')
    elif monthNumber == 3 and saturday <= 23:
      f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(saturday) + '|' + str(saturday) + ']]\n')
        
    if monthNumber != 3 and saturday >= 26:
      check = input(f"Is this day the {week[6]} from last month? Y/N")

      if check == 'Y' or check == 'y':
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber-1) + "/" + str(saturday) + '|' + str(saturday) + ']]\n')
      else:
        f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(saturday) + '|' + str(saturday) + ']]\n')
    elif monthNumber != 3 and saturday <= 26:
      f.write(f"[[Daily-Journal/" + str(year) + "/Dailies/" + str(monthNumber) + "/" + str(saturday) + '|' + str(saturday) + ']]\n')



    print("Grouping days of the week")
    print("Grouping complete")
    # monthCheck(week,monthNumber,f)
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
    f.write(spent)
    f.write(table)
    

# create()