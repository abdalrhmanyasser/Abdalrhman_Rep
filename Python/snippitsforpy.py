#*******************#
#timing user input  #
#time lib needed    #
#*******************#
import time
#*****************************#
#rounding for 2 decimal points#
#*****************************#
def rnd2(n):
  return int(n * 100) / 100
#*******************************************#
#returns an int that is rounded off 2 places#
#*******************************************#

#************************#
#Taking the starting time#
#************************#

start_time = time.time()

#**********************#
#Taking the ending time#
#**********************#

input("Press Enter to stop")
end_time = time.time()

#********************************************#
#Calculating the min and sec from time passed#
#********************************************#

time_lapsed = end_time - start_time
s = rnd2((time_lapsed) % 60)
m = int((time_lapsed / 60))
print(str(m) + " Mins " + str(s) + " Sec ")


#---------------------------------------------#


#*******************#
#also needs time lib#
#Count Down Timer   #
#*******************#
for b in range(15):
    print("{0} sec left...".format(15 -b))
    time.sleep(1)
#*******************#


#---------------------------------------------#

#*******************#
#reverses the number#
#no lib needed !    #
#*******************#

#********************#
def reverse_numb(st):
    sr = str(st)
    return int(sr[::-1])
#********************#


#---------------------------------------------#

#***************#
#opening a file #
#no lib needed !#
#***************#

#***********************#
try:
    file = open("path", "rt")
except:
    file = open("path", "x")
    file.close()
    file = open("path", "rt")

content = file.read()
#***********************#


#---------------------------------------------#

#**********************************#
from openpyxl import load_workbook #
from openpyxl import Workbook      #
#**********************************#
#needs two components from openpyxl#
#**********************************#

#***********************************************#
wb = Workbook()#this is used for initialization #
ws = wb.active #and object for later usage      #
#***********************************************#

#****************************************************************************************#
#functions can be used for gathering data                                                #
ws.append([input(), "second column"])            #appending a row to the excel sheet     #
ws.append(["second row"])                        #this is another row                    #
wb.save("file_name.xlsx")                        #used for submiting thee file and saving#
#****************************************************************************************#


#---------------------------------------------#


