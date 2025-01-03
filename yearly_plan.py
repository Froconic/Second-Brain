import yearly_forecast as yf
import monthly_plan as mp

year = input("Year: ")

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