import random, os, datetime
# TODO add in backlinks to qualities and reverse qualities
# TODO Fix the backlin tags for runes and ogham

date = datetime.date.today()
year = date.year

planets = {
    1: "[[Book of Shadows/MOD/Astrology/Planets/Sun|Sun]]",
    2: "[[Book of Shadows/MOD/Astrology/Planets/Moon|Moon]]",
    3: "[[Book of Shadows/MOD/Astrology/Planets/Jupiter|Jupiter]]",
    4: "[[Book of Shadows/MOD/Astrology/Planets/Uranus|Uranus]]",
    5: "[[Book of Shadows/MOD/Astrology/Planets/Mercury|Mercury]]",
    6: "[[Book of Shadows/MOD/Astrology/Planets/Venus|Venus]]",
    8: "[[Book of Shadows/MOD/Astrology/Planets/Saturn|Saturn]]",
    9: "[[Book of Shadows/MOD/Astrology/Planets/Mars|Mars]]",
    7: "[[Book of Shadows/MOD/Astrology/Planets/Neptune|Neptune]]",
    0: "[[Book of Shadows/MOD/Astrology/Planets/Pluto|Pluto]]"
}

zodiac = {
    0: "[[Book of Shadows/MOD/Astrology/Zodiac/Aries|Aries]]",
    1: "[[Book of Shadows/MOD/Astrology/Zodiac/Taurus|Taurus]]",
    2: "[[Book of Shadows/MOD/Astrology/Zodiac/Gemini|Gemini]]",
    3: "[[Book of Shadows/MOD/Astrology/Zodiac/Cancer|Cancer]]",
    4: "[[Book of Shadows/MOD/Astrology/Zodiac/Leo|Leo]]",
    5: "[[Book of Shadows/MOD/Astrology/Zodiac/Virgo|Virgo]]",
    6: "[[Book of Shadows/MOD/Astrology/Zodiac/Libra|Libra]]",
    7: "[[Book of Shadows/MOD/Astrology/Zodiac/Scorpio|Scorpio]]",
    8: "[[Book of Shadows/MOD/Astrology/Zodiac/Sagittarius|Sagittarius]]",
    9: "[[Book of Shadows/MOD/Astrology/Zodiac/Capricorn|Capricorn]]",
    10: "[[Book of Shadows/MOD/Astrology/Zodiac/Aquarius|Aquarius]]",
    11: "[[Book of Shadows/MOD/Astrology/Zodiac/Pisces|Pisces]]"
}

runes = {
    1: "[[Fehu]]",
    2: "[[Uruz]]",
    3: "[[Thurisaz]]",
    4: "[[Ansuz]]",
    5: "[[Raidho]]",
    6: "[[Kenaz]]",
    7: "[[Gebo]]",
    8: "[[Wunjo]]",
    9: "[[Haglaz]]",
    10: "[[Naudhiz]]",
    11: "[[Isa]]",
    12: "[[Jera]]",
    13: "[[Eihwaz]]",
    14: "[[Pertho]]",
    15: "[[Algiz]]",
    16: "[[Sowilo]]",
    17: "[[Tiwaz]]",
    18: "[[Berkano]]",
    19: "[[Ehwaz]]",
    20: "[[Mannaz]]",
    21: "[[Laguz]]",
    22: "[[Ingwaz]]",
    23: "[[Othala]]",
    24: "[[Dagaz]]",
    0: "[[Blank]]",
}

ogham = {
    1: "[[B Beith]]",
    2: "[[L Luis]]",
    3: "[[F Fearn]]",
    4: "[[S Saille]]",
    5: "[[N Nion]]",
    6: "[[H Uath]]",
    7: "[[D Dair]]",
    8: "[[T Tinne]]",
    9: "[[C Coll]]",
    10: "[[Q Quert]]",
    11: "[[M Muin]]",
    12: "[[G Gort]]",
    13: "[[NG Ngeatal]]",
    14: "[[Z Straif]]",
    15: "[[R Ruis]]",
    16: "[[A Ailm]]",
    17: "[[O Ohn]]",
    18: "[[U Ur]]",
    19: "[[E Eadhadh]]",
    20: "[[I Iodhadh]]",
    21: "[[EA Koad]]",
    22: "[[OI Or]]",
    23: "[[UI Uilleand]]",
    24: "[[IO Phagos]]",
    25: "[[AE Mor]]",
    26: "[[P Peith]]",
    27: "[[Start]]",
    0: "[[Space]]",
    28: "[[End]]",
}

def chooser(system):
  length = len(system)
  choice = random.randint(0, length-1)
  # print(choice)
  return choice

def position():
  face = random.randint(1,2)
  if face == 2:
    return "Reverse"
  
def forceFigure():
  temp = chooser(planets)
  temp
  force = planets[temp]
  facing = position()
  facing
  if facing != None:
    force = force + ' ' + facing
    return force
  else:
    return force
  
def faceFigure():
  temp = chooser(zodiac)
  temp
  face = zodiac[temp]
  facing = position()
  facing
  if facing != None:
    face = face + ' ' + facing
    return face
  else:
    return face

def firstFigure():
  # TODO Duplicate for each week
  temp = chooser(runes)
  tempTwo = chooser(ogham)
  temp
  tempTwo
  figureOne = runes[temp]
  figureTwo = ogham[tempTwo]
  facing = position()
  facing
  if facing != None:
    figureOne = figureOne + ' ' + facing

  facing
  if facing != None:
    figureTwo = figureTwo + ' ' + facing
  return figureOne, figureTwo

def secondFigure():
  # TODO Duplicate for each week
  temp = chooser(runes)
  tempTwo = chooser(ogham)
  temp
  tempTwo
  figureOne = runes[temp]
  figureTwo = ogham[tempTwo]
  facing = position()
  facing
  if facing != None:
    figureOne = figureOne + ' ' + facing

  facing
  if facing != None:
    figureTwo = figureTwo + ' ' + facing
  return figureOne, figureTwo

def thirdFigure():
  # TODO Duplicate for each week
  temp = chooser(runes)
  tempTwo = chooser(ogham)
  temp
  tempTwo
  figureOne = runes[temp]
  figureTwo = ogham[tempTwo]
  facing = position()
  facing
  if facing != None:
    figureOne = figureOne + ' ' + facing

  facing
  if facing != None:
    figureTwo = figureTwo + ' ' + facing
  return figureOne, figureTwo

def fourthFigure():
  # TODO Duplicate for each week
  temp = chooser(runes)
  tempTwo = chooser(ogham)
  temp
  tempTwo
  figureOne = runes[temp]
  figureTwo = ogham[tempTwo]
  facing = position()
  facing
  if facing != None:
    figureOne = figureOne + ' ' + facing

  facing
  if facing != None:
    figureTwo = figureTwo + ' ' + facing
  return figureOne, figureTwo


def pageBuilder(month):
  file = month
  folder = "/home/akira/Documents/Synced-Files/Daily-Journal/" + str(year) + "/Monthly/Forecasts"
  # folder = "/home/rivre/Documents/Synced-Files/Daily-Journal/" + str(year) + "/Monthly/Forecasts"
  path = os.path.join(folder,file)
  path = path + '.md'
  file
  folder
  with open(path, 'w+') as f:
    firstWeek = []
    secondWeek = []
    thirdWeek = []
    fourthWeek = []
    
    f.write(f"[[#Key points]]\n\n")
    force = forceFigure()
    face = faceFigure()
    firstWeek = firstFigure()
    secondWeek = secondFigure()
    thirdWeek = thirdFigure()
    fourthWeek = fourthFigure()
    
    f.write(f"Force| {force}\n---\n\n\n")
    f.write(f"Face| {face}\n---\n\n\n")
    f.write(f"Week 1| {firstWeek[0]}\n---\n- \n\n")
    f.write(f"Underlying Force| {firstWeek[1]}\n---\n- \n\n")
    f.write(f"Week 2| {secondWeek[0]}\n---\n- \n\n")
    f.write(f"Underlying Force| {secondWeek[1]}\n---\n- \n\n")
    f.write(f"Week 3| {thirdWeek[0]}\n---\n- \n\n")
    f.write(f"Underlying Force| {thirdWeek[1]}\n---\n- \n\n")
    f.write(f"Week 4| {fourthWeek[0]}\n---\n- \n\n")
    f.write(f"Underlying Force| {fourthWeek[1]}\n---\n- \n\n")
    f.write(f"Key Points\n---\n\n")



# C:\Users\akira\Desktop\Stuff\Keep\Technomancy\DIVINATION

# pageBuilder()