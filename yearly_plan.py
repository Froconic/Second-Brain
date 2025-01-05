import yearly_forecast as yf
import monthly_plan as mp
import year_preview as yp
import os, random

year = input("Year: ")
lastYear = str(int(year)-1)

january = "/home/rivre/Documents/Synced Files/Daily-Journal/" + year + "/Monthly/Outline/1 January.md"
february = "/home/rivre/Documents/Synced Files/Daily-Journal/" + year + "/Monthly/Outline/2 February.md"
march = "/home/rivre/Documents/Synced Files/Daily-Journal/" + year + "/Monthly/Outline/3 March.md"
april = "/home/rivre/Documents/Synced Files/Daily-Journal/" + year + "/Monthly/Outline/4 April.md"
may = "/home/rivre/Documents/Synced Files/Daily-Journal/" + year + "/Monthly/Outline/5 May.md"
june = "/home/rivre/Documents/Synced Files/Daily-Journal/" + year + "/Monthly/Outline/6 June.md"
july = "/home/rivre/Documents/Synced Files/Daily-Journal/" + year + "/Monthly/Outline/7 July.md"
august = "/home/rivre/Documents/Synced Files/Daily-Journal/" + year + "/Monthly/Outline/8 August.md"
september = "/home/rivre/Documents/Synced Files/Daily-Journal/" + year + "/Monthly/Outline/9 September.md"
october = "/home/rivre/Documents/Synced Files/Daily-Journal/" + year + "/Monthly/Outline/10 October.md"
november = "/home/rivre/Documents/Synced Files/Daily-Journal/" + year + "/Monthly/Outline/11 November.md"
december = "/home/rivre/Documents/Synced Files/Daily-Journal/" + year + "/Monthly/Outline/12 December.md"
outline = "/home/rivre/Documents/Synced Files/Daily-Journal/" + year + "/Yearly/Outline.md"
focuses = "/home/rivre/Documents/Synced Files/Daily-Journal/" + year + "/Yearly/Focuses.md"
preview = "/home/rivre/Documents/Synced Files/Daily-Journal/" + year + "/Yearly/Preview.md"
gbuPath = "/home/rivre/Documents/Synced Files/Daily-Journal/" + year + "/Yearly/" + lastYear + " Good Bad Ugly.md"


# yf.yearlyForecast(year)

def generateJanuary(year):
  print("January Outline Being Generated")
  mp.createDays("January",int(year))
  print("January Outline Complete")
  print("January Weekly Outlines being Generated")
  mp.createWeeks(1,"January", int(year))

def generateFebruary(year):
  print("February Outline Being Generated")
  mp.createDays("February",int(year))
  print("February Outline Complete")
  print("February Weekly Outlines being Generated")
  mp.createWeeks(5,"February", int(year))

def generateMarch(year):
  print("March Outline Being Generated")
  mp.createDays("March",int(year))
  print("March Outline Complete")
  print("March Weekly Outlines being Generated")
  mp.createWeeks(9,"March", int(year))

def generateApril(year):
  print("April Outline Being Generated")
  mp.createDays("April",int(year))
  print("April Outline Complete")
  print("April Weekly Outlines being Generated")
  mp.createWeeks(14,"April", int(year))

def generateMay(year):
  print("May Outline Being Generated")
  mp.createDays("May",int(year))
  print("May Outline Complete")
  print("May Weekly Outlines being Generated")
  mp.createWeeks(18,"May", int(year))

def generateJune(year):
  print("June Outline Being Generated")
  mp.createDays("June",int(year))
  print("June Outline Complete")
  print("June Weekly Outlines being Generated")
  mp.createWeeks(23,"June", int(year))

def generateJuly(year):
  print("July Outline Being Generated")
  mp.createDays("July",int(year))
  print("July Outline Complete")
  print("July Weekly Outlines being Generated")
  mp.createWeeks(27,"July", int(year))

def generateAugust(year):
  print("August Outline Being Generated")
  mp.createDays("August",int(year))
  print("August Outline Complete")
  print("August Weekly Outlines being Generated")
  mp.createWeeks(31,"August", int(year))

def generateSeptember(year):
  print("September Outline Being Generated")
  mp.createDays("September",int(year))
  print("September Outline Complete")
  print("September Weekly Outlines being Generated")
  mp.createWeeks(36,"September", int(year))

def generateOctober(year):
  print("October Outline Being Generated")
  mp.createDays("October",int(year))
  print("October Outline Complete")
  print("October Weekly Outlines being Generated")
  mp.createWeeks(40,"October", int(year))

def generateNovember(year):
  print("November Outline Being Generated")
  mp.createDays("November",int(year))
  print("November Outline Complete")
  print("November Weekly Outlines being Generated")
  mp.createWeeks(44,"November", int(year))

def generateDecember(year):
  print("December Outline Being Generated")
  mp.createDays("December",int(year))
  print("December Outline Complete")
  print("December Weekly Outlines being Generated")
  mp.createWeeks(49,"December", int(year))

def generateYear(year):
  generateJanuary(year)
  generateFebruary(year)
  generateMarch(year)
  generateApril(year)
  generateMay(year)
  generateJune(year)
  generateJuly(year)
  generateAugust(year)
  generateSeptember(year)
  generateOctober(year)
  generateNovember(year)
  generateDecember(year)
  
def chooser(system):
  length = len(system)
  choice = random.randint(0, length-1)
  # print(choice)
  return choice

def position(choice):
  face = random.randint(1,2)
  if face == 2:
    return "Reverse"
  else:
    return ''
  
def goodBadUgly(file, year):
  year = int(year)-1
  planets = {
    1: "Sun",
    2: "Moon",
    3: "Jupiter",
    4: "Uranus",
    5: "Mercury",
    6: "Venus",
    8: "Saturn",
    9: "Mars",
    7: "Neptune",
    0: "Pluto"
}

  zodiac = {
      0: "Aries",
      1: "Taurus",
      2: "Gemini",
      3: "Cancer",
      4: "Leo",
      5: "Virgo",
      6: "Libra",
      7: "Scorpio",
      8: "Sagittarius",
      9: "Capricorn",
      10: "Aquarius",
      11: "Pisces"
  }

  runes = {
    1: "Fehu",
    2: "Uruz",
    3: "Thurisaz",
    4: "Ansuz",
    5: "Raidho",
    6: "Kenaz",
    7: "Gebo",
    8: "Wunjo",
    9: "Haglaz",
    10: "Naudhiz",
    11: "Isa",
    12: "Jera",
    13: "Eihwaz",
    14: "Pertho",
    15: "Algiz",
    16: "Sowilo",
    17: "Tiwaz",
    18: "Berkano",
    19: "Ehwaz",
    20: "Mannaz",
    21: "Laguz",
    22: "Inguz",
    23: "Othala",
    24: "Dagaz",
    0: "Wyrd",
  }

  ogham = {
    1: "B Beith",
    2: "L Luis",
    3: "F Fearn",
    4: "S Saille",
    5: "N Nuin",
    6: "H Uath",
    7: "D Duir",
    8: "T Tinne",
    9: "C Coll",
    10: "Q Quert",
    11: "M Muin",
    12: "G Gort",
    13: "NG Ngetal",
    14: "Z Straif",
    15: "R Ruis",
    16: "A Ailm",
    17: "O Onn",
    18: "U Ur",
    19: "E Eadhadh",
    20: "I Iodhadh",
    21: "EA Koad",
    22: "OI Or",
    23: "UI Uilleand",
    24: "IO Phagos",
    25: "AE Mor",
    26: "P Peith",
    27: "Start",
    0: "Space",
    28: "End",
  }
  
  figureOne = chooser(runes)
  figureOneFace = position(figureOne)
  figureOne = runes[figureOne]
  
  figureTwo = chooser(runes)
  figureTwoFace = position(figureTwo)
  figureTwo = runes[figureTwo]
  
  figureThree = chooser(runes)
  figureThreeFace = position(figureThree)
  figureThree = runes[figureThree]
  
  figureFour = chooser(runes)
  figureFourFace = position(figureFour)
  figureFour = runes[figureFour]

  figureFive = chooser(ogham)
  figureFiveFace = position(figureFive)
  figureFive = ogham[figureFive]

  figureSix = chooser(ogham)
  figureSixFace = position(figureSix)
  figureSix = ogham[figureSix]

  figureSeven = chooser(ogham)
  figureSevenFace = position(figureSeven)
  figureSeven = ogham[figureSeven]

  figureEight = chooser(ogham)
  figureEightFace = position(figureEight)
  figureEight = ogham[figureEight]

  figureNine = chooser(ogham)
  figureNineFace = position(figureNine)
  figureNine = ogham[figureNine]

  figureTen = chooser(ogham)
  figureTenFace = position(figureTen)
  figureTen = ogham[figureTen]

  figureEleven = chooser(ogham)
  figureElevenFace = position(figureEleven)
  figureEleven = ogham[figureEleven]

  figureTwelve = chooser(ogham)
  figureTwelveFace = position(figureTwelve)
  figureTwelve = ogham[figureTwelve]

  figureThirteen = chooser(ogham)
  figureThirteenFace = position(figureThirteen)
  figureThirteen = ogham[figureThirteen]

  figureFourteen = chooser(ogham)
  figureFourteenFace = position(figureFourteen)
  figureFourteen = ogham[figureFourteen]

  figureFifteen = chooser(ogham)
  figureFifteenFace = position(figureFifteen)
  figureFifteen = ogham[figureFifteen]

  figureSixteen = chooser(ogham)
  figureSixteenFace = position(figureSixteen)
  figureSixteen = ogham[figureSixteen]

  figureSeventeen = chooser(planets)
  figureSeventeenFace = position(figureSeventeen)
  figureSeventeen = planets[figureSeventeen]

  figureEighteen = chooser(zodiac)
  figureEighteenFace = position(figureEighteen)
  figureEighteen = zodiac[figureEighteen]

  figureNineteen = chooser(planets)
  figureNineteenFace = position(figureNineteen)
  figureNineteen = planets[figureNineteen]
  
  figureTwenty = chooser(zodiac)
  figureTwentyFace = position(figureTwenty)
  figureTwenty = zodiac[figureTwenty]

  figureTwentyOne = chooser(planets)
  figureTwentyOneFace = position(figureTwentyOne)
  figureTwentyOne = planets[figureTwentyOne]

  figureTwentyTwo = chooser(zodiac)
  figureTwentyTwoFace = position(figureTwentyTwo)
  figureTwentyTwo = zodiac[figureTwentyTwo]
  print(f"Good Bad Ugly reading for the year {str(year)} being generated")
  
  with open(file, 'w+') as f:
    f.write(f"### Overall Theme: [[{figureOne}]] {figureOneFace}\n \n\n")
    f.write(f"### Overall Good: [[{figureTwo}]] {figureTwoFace}\n \n\n")
    f.write(f"### Overall Bad: [[{figureThree}]] {figureThreeFace}\n \n\n")
    f.write(f"### Overall Ugly: [[{figureFour}]] {figureFourFace}\n \n\n")
    f.write(f"### Mind Theme: [[{figureFive}]] {figureFiveFace}\n \n\n")
    f.write(f"### Mind Good: [[{figureSix}]] {figureSixFace}\n \n\n")
    f.write(f"### Mind Bad: [[{figureSeven}]] {figureSevenFace}\n \n\n")
    f.write(f"### Mind Ugly: [[{figureEight}]] {figureEightFace}\n \n\n")
    f.write(f"### Body Theme: [[{figureNine}]] {figureNineFace}\n \n\n")
    f.write(f"### Body Good: [[{figureTen}]] {figureTenFace}\n \n\n")
    f.write(f"### Body Bad: [[{figureEleven}]] {figureElevenFace}\n \n\n")
    f.write(f"### Body Ugly: [[{figureTwelve}]] {figureTwelveFace}\n \n\n")
    f.write(f"### Soul Theme: [[{figureThirteen}]] {figureThirteenFace}\n \n\n")
    f.write(f"### Soul Good: [[{figureFourteen}]] {figureFourteenFace}\n \n\n")
    f.write(f"### Soul Bad: [[{figureFifteen}]] {figureFifteenFace}\n \n\n")
    f.write(f"### Soul Ugly: [[{figureSixteen}]] {figureSixteenFace}\n \n\n")
    f.write(f"### Mind Broad Takeaway: [[{figureSeventeen}]] {figureSeventeenFace}\n \n\n")
    f.write(f"### Mind Narrow Takeaway: [[{figureEighteen}]] {figureEighteenFace}\n \n\n")
    f.write(f"### Body Broad Takeaway: [[{figureNineteen}]] {figureNineteenFace}\n \n\n")
    f.write(f"### Body Narrow Takeaway: [[{figureTwenty}]] {figureTwentyFace}\n \n\n")
    f.write(f"### Soul Broad Takeaway: [[{figureTwentyOne}]] {figureTwentyOneFace}\n \n\n")
    f.write(f"### Soul Narrow Takeaway: [[{figureTwentyTwo}]] {figureTwentyTwoFace}\n \n\n\n")
    f.write("### Summary\n---\n")

  print("Good bad ugly reading complete")


def yearOutline(year):
  jan = "### [[Daily-Journal/" + year + "/Monthly/Outline/1 January|1 January]]\n"
  feb = "### [[Daily-Journal/" + year + "/Monthly/Outline/2 February|2 February]]\n"
  mar = "### [[Daily-Journal/" + year + "/Monthly/Outline/3 March|3 March]]\n"
  apr = "### [[Daily-Journal/" + year + "/Monthly/Outline/4 April|4 April]]\n"
  may = "### [[Daily-Journal/" + year + "/Monthly/Outline/5 May|5 May]]\n"
  jun = "### [[Daily-Journal/" + year + "/Monthly/Outline/6 June|6 June]]\n"
  jul = "### [[Daily-Journal/" + year + "/Monthly/Outline/7 July|7 July]]\n"
  aug = "### [[Daily-Journal/" + year + "/Monthly/Outline/8 August|8 August]]\n"
  sep = "### [[Daily-Journal/" + year + "/Monthly/Outline/9 September|9 September]]\n"
  octo = "### [[Daily-Journal/" + year + "/Monthly/Outline/10 October|10 October]]\n"
  nov = "### [[Daily-Journal/" + year + "/Monthly/Outline/11 November|11 November]]\n"
  dec = "### [[Daily-Journal/" + year + "/Monthly/Outline/12 December|12 December]]\n\n\n"
  monthlySavings = "| Monthly Savings | Amount |\n| --------------- | ------ |\n| Jan             |        |\n| Feb             |        |\n| Mar             |        |\n| Apr             |        |\n| May             |        |\n| Jun             |        |\n| Jul             |        |\n| Aug             |        |\n| Sept            |        |\n| Oct             |        |\n| Nov             |        |\n| Dec             |        |\n\n"
  bigSpending = "| Big Spending | Amount |\n| --------------- | ------ |\n|             |        |\n"
  yearlyBills = "| Yearly Bills   | Amount | Date Due | Paid? |\n| -------------- | ------ | -------- | ----- |\n| Phone          | 240    | Jan 11   |       |\n| Obsidian       | 96     | Dec 29   |       |\n| akiraallen.com | 17     | Apr 30   |       |\n\n"
  
  print("Outline for the year being generated")
  with open(outline, 'w+') as f:
    f.write("# TOC\n---\n")
    f.write(jan)
    f.write(feb)
    f.write(mar)
    f.write(apr)
    f.write(may)
    f.write(jun)
    f.write(jul)
    f.write(aug)
    f.write(sep)
    f.write(octo)
    f.write(nov)
    f.write(dec)
    f.write("## Major Events\n---\n- \n\n")
    f.write("##### Wins\n---\n- \n\n")
    f.write("##### Losses\n---\n- \n\n\n")
    f.write("## Budget\n---\n\n")
    f.write(monthlySavings)
    f.write(yearlyBills)
    f.write(bigSpending)
    
    
  print("TOC Complete")

def yearFocuses():
  print("Focus Page being generated")
  with open(focuses, 'w+') as f:
    f.write("# Mind\n---\n\n")
    f.write("### First Focus: \n")
    f.write("### Intention: \n\n")
    f.write("### Primary Channels\n- \n- \n- \n\n")
    f.write("### Benchmarks\n- \n- \n- \n\n")
    f.write("### Habits\n- \n- \n- \n\n")
    f.write("### Things to Avoid\n- \n- \n- \n\n")
    f.write("### Second Focus: \n\n")
    f.write("### Intention: \n\n")
    f.write("### Primary Channels\n- \n- \n- \n\n")
    f.write("### Benchmarks\n- \n- \n- \n\n")
    f.write("### Habits\n- \n- \n- \n\n")
    f.write("### Things to Avoid\n- \n- \n- \n\n")
    f.write("### Third Focus: \n\n")
    f.write("### Intention: \n\n")
    f.write("### Primary Channels\n- \n- \n- \n\n")
    f.write("### Benchmarks\n- \n- \n- \n\n")
    f.write("### Habits\n- \n- \n- \n\n")
    f.write("### Things to Avoid\n- \n- \n- \n\n")
    
    f.write("# Body\n---\n\n")
    f.write("### First Focus: \n")
    f.write("### Intention: \n\n")
    f.write("### Primary Channels\n- \n- \n- \n\n")
    f.write("### Benchmarks\n- \n- \n- \n\n")
    f.write("### Habits\n- \n- \n- \n\n")
    f.write("### Things to Avoid\n- \n- \n- \n\n")
    f.write("### Second Focus: \n\n")
    f.write("### Intention: \n\n")
    f.write("### Primary Channels\n- \n- \n- \n\n")
    f.write("### Benchmarks\n- \n- \n- \n\n")
    f.write("### Habits\n- \n- \n- \n\n")
    f.write("### Things to Avoid\n- \n- \n- \n\n")
    f.write("### Third Focus: \n\n")
    f.write("### Intention: \n\n")
    f.write("### Primary Channels\n- \n- \n- \n\n")
    f.write("### Benchmarks\n- \n- \n- \n\n")
    f.write("### Habits\n- \n- \n- \n\n")
    f.write("### Things to Avoid\n- \n- \n- \n\n")
    
    f.write("# Soul\n---\n\n")
    f.write("### First Focus: \n")
    f.write("### Intention: \n\n")
    f.write("### Primary Channels\n- \n- \n- \n\n")
    f.write("### Benchmarks\n- \n- \n- \n\n")
    f.write("### Habits\n- \n- \n- \n\n")
    f.write("### Things to Avoid\n- \n- \n- \n\n")
    f.write("### Second Focus: \n\n")
    f.write("### Intention: \n\n")
    f.write("### Primary Channels\n- \n- \n- \n\n")
    f.write("### Benchmarks\n- \n- \n- \n\n")
    f.write("### Habits\n- \n- \n- \n\n")
    f.write("### Things to Avoid\n- \n- \n- \n\n")
    f.write("### Third Focus: \n\n")
    f.write("### Intention: \n\n")
    f.write("### Primary Channels\n- \n- \n- \n\n")
    f.write("### Benchmarks\n- \n- \n- \n\n")
    f.write("### Habits\n- \n- \n- \n\n")
    f.write("### Things to Avoid\n- \n- \n- \n\n")
  print("Focus Page generated")
  

goodBadUgly(gbuPath, year)
generateYear(year)
yp.pageBuilder(year)
yearOutline(year)
yearFocuses()