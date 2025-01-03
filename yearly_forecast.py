import monthly_forecast as mf
import random, os

def yearlyForecast(year):
  path = "/home/rivre/Documents/Synced Files/Daily-Journal/2030/Monthly/Forecasts" + year + "/Monthly/Forecasts"
  january = mf.pageBuilder("1 January", year)
  february = mf.pageBuilder("2 February", year)
  march = mf.pageBuilder("3 March", year)
  april = mf.pageBuilder("4 April", year)
  may = mf.pageBuilder("5 May", year)
  june = mf.pageBuilder("6 June", year)
  july = mf.pageBuilder("7 July", year)
  august = mf.pageBuilder("8 August", year)
  september = mf.pageBuilder("9 September", year)
  october = mf.pageBuilder("10 October", year)
  november = mf.pageBuilder("11 November", year)
  december = mf.pageBuilder("12 December", year)
  
  print("Commencing monthly forecasts")
  print("Generating January")
  january
  print("January Created")
  print("Generating January")
  january
  print("January Created")
  print("Generating February")
  february
  print("February Created")
  print("Generating March")
  march
  print("March Created")
  print("Generating April")
  april
  print("April Created")
  print("Generating May")
  may
  print("May Created")
  print("Generating June")
  june
  print("June Created")
  print("Generating July")
  july
  print("July Created")
  print("Generating August")
  august
  print("August Created")
  print("Generating September")
  september
  print("September Created")
  print("Generating October")
  october
  print("October Created")
  print("Generating November")
  november
  print("November Created")
  print("Generating December")
  december
  print("December Created")
  