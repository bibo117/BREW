#!/usr/bin/env python3
from datetime import timedelta, datetime
from nptime import nptime
import os
#Updates: txt to csv + notes.txt##
###############
#bl()
#cp()
#cc()

#nf()
#pp()
#pc()
###############

#initiate the main output file. 
def id (coupleID):
  print("*********** START *********************************")
  print("ID:" + str(coupleID))

  #change: header  
  header = ['id','name','dateStart','dateEnd', 'blStart','blEnd','cpStart','cpEnd','ccStart','ccEnd','nfStart','nfEnd','ppStart','ppEnd','pcStart','pcEnd','notes']
  f1 = open ('output.txt','a+')
  for i in header:
    f1.write(i+'\t')

  #output ID/name/dates
  f1.write('\n'+ str(coupleID)+'\t')
  f1.write('BiBo'+'\t')
  currentDT = datetime.now()
  for i in range (2):
    f1.write(str(currentDT.strftime('%m/%d/%Y'))+'\t')

  #initiate note.txt
  f2 = open("notes.txt", "a+")
  f2.write("ID: " + str(coupleID)+os.linesep)
  f1.close()

#output notes 
def output(start, expEnd, end, type): 
  if ((end - expEnd).seconds <= 2):
    return 
  f2 = open("notes.txt", "a+")
  note = type + ": should've ended at " + str(expEnd) + ", but experimenter knocked on door at " + str(end) + ", extra time =" + str((end - expEnd).seconds) +"s.| "
  f2.write(note)
  if type == 'PosConvo':
    for i in range (2):
      f2.write(os.linesep)
  f2.close()
  
#output notes func for bl/nf
def outputFilm(start, expEnd, end, type):
  if ((end - expEnd).seconds <= 2):
    return 
  f2 = open('notes.txt', 'a+')
  note = type + ": should've ended at " + str(expEnd) + ", but film actually ended at " + str(end) + ", extra time =" + str((end - expEnd).seconds) +"s.| "
  f2.write(note)
  f2.close() 
 
#output to txt file. 
def outputTXT(start,expEnd):
  f1 = open("output.txt", "a+")
  f1.write(str(start)+'\t')
  f1.write(str(expEnd)+'\t')
  f1.close()

#txt to csv
def csv():
  os.rename("output.txt", "output.csv")


# 1. Baseline 
def bl(startMin, startSec, endMin, endSec):
  blStart= nptime(minute =startMin, second = startSec)
  blExpEnd= nptime.from_time(blStart + timedelta(minutes = 5, seconds=3))
  print ("Baseline Start=", blStart)
  print ("Baseline End=", blExpEnd)
  blEnd= nptime(minute =endMin, second = endSec) 
  print()
  #print ("Baseline: expected endtime =",  blExpEnd, ", actual endtime (door-knock) =", blEnd, ", extra time =", (blEnd - blExpEnd).seconds, "s.")
  
  outputFilm(blStart, blExpEnd, blEnd, "Baseline")
  outputTXT(blStart,blExpEnd)
  return 

# 2. Conflict Prep
def cp(startMin, startSec, endMin, endSec):
  startHour = 0;
  endHour=0;
  if startMin > 59:
    startHour = 1;
    startMin -= 60;
  if endMin >59:
    endHour = 1
    endMin -=60
  cpStart= nptime(hour = startHour, minute =startMin, second = startSec)
  cpExpEnd= nptime.from_time(cpStart + timedelta(seconds=90))
  print ("ConPrep Start=", cpStart)
  print ("ConPrep End=", cpExpEnd)
  cpEnd= nptime(hour = endHour, minute =endMin, second = endSec) 
  print()

  output(cpStart, cpExpEnd, cpEnd, "ConPrep")
  outputTXT(cpStart,cpExpEnd)
  return 


# 3. Conflict Convo
def cc(startMin, startSec, endMin, endSec):
  ccStart= nptime(minute =startMin, second = startSec)
  ccExpEnd= nptime.from_time(ccStart + timedelta(minutes=7))
  print ("ConConvo Start=", ccStart)
  print ("ConConvo End=", ccExpEnd)
  ccEnd= nptime(minute =endMin, second = endSec) 
  print()
  
  output(ccStart, ccExpEnd, ccEnd, "ConConvo")
  outputTXT(ccStart,ccExpEnd)
  return 

# 4. Neutral Film
def nf(startMin, startSec, endMin, endSec):
  startHour = 0;
  endHour=0;
  if startMin > 59:
    startHour = 1;
    startMin -= 60;
  if endMin >59:
    endHour = 1
    endMin -=60

  nfStart= nptime(hour = startHour, minute =startMin, second = startSec)
  nfExpEnd= nptime.from_time(nfStart + timedelta(minutes = 2, seconds=1))
  print ("Neutral Film Start=", nfStart)
  print ("Neutral Film End=", nfExpEnd)
  nfEnd= nptime(hour = endHour, minute =endMin, second = endSec) 
  print()

  outputFilm(nfStart, nfExpEnd, nfEnd, "Neutral Film")
  outputTXT(nfStart,nfExpEnd)
  return 


# 5. Positive prep
def pp(startMin, startSec, endMin, endSec):
  startHour = 0;
  endHour=0;
  if startMin > 59:
    startHour = 1;
    startMin -= 60;
  if endMin >59:
    endHour = 1
    endMin -=60

  ppStart= nptime(hour= startHour, minute =startMin, second = startSec)
  ppExpEnd= nptime.from_time(ppStart + timedelta(seconds=90))
  print ("PosPrep Start=", ppStart)
  print ("PosPrep End=", ppExpEnd)
  ppEnd= nptime(hour=endHour, minute =endMin, second = endSec) 
  print()
  
  output(ppStart, ppExpEnd, ppEnd, "PosPrep")
  outputTXT(ppStart,ppExpEnd)
  return 

#6. Positive Convo
def pc(startMin, startSec, endMin, endSec):
  startHour = 0;
  endHour=0;
  if startMin > 59:
    startHour = 1
    startMin -= 60
  if endMin >59:
    endHour = 1
    endMin -=60

  pcStart= nptime(hour=startHour, minute =startMin, second = startSec)
  pcExpEnd= nptime.from_time(pcStart + timedelta(minutes=7))
  print ("PosConvo Start=", pcStart)
  print ("PosConvo End=", pcExpEnd)
  pcEnd= nptime(hour=endHour, minute =endMin, second = endSec) 
  print()
  
  output(pcStart, pcExpEnd, pcEnd, "PosConvo")
  outputTXT(pcStart,pcExpEnd)

  #txt to csv
  csv()

  print("*********** END *********************************")
  return 

print ("Yay! New data entry!")