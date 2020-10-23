import glob, os
from os.path import expanduser
import subprocess
import socket 
  
# Function to display hostname and IP address.
def getHostNameIP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname: ",host_name) 
        print("IP: ",host_ip) 
    except: 
        print("Unable to get Hostname and IP") 

home = expanduser("~")

owd = os.getcwd()
os.chdir("txts")
nameArr = []
countArr = []
for file in glob.glob("*.txt"):
    file = open(file, "rt")
    data = file.read()
    nameArr.append(file.name)
    words = data.split()
    countArr.append(len(words))

biggest = 0
bigFileName = ""
grandTotal = 0
for i in range(len(countArr)):
    grandTotal += countArr[i]
    if countArr[i] > biggest:
        biggest = countArr[i]
        bigFileName = nameArr[i]

textDir = os.listdir()
os.chdir(owd + "/output")
print("Winner: ", bigFileName, ", with the following word count: ", biggest)
print("Grand total word count: ", grandTotal)
print("List of all text files here: ", textDir)
getHostNameIP()

newText = open("result.txt","w+")

outputText = "Winner: " + str(bigFileName) + "\n with the following word count: " + str(biggest) + "\n Grand total word count: " + str(grandTotal) + "\n List of all text files here: " + str(textDir)

newText.write(outputText)
newText.close()
print('Created a text "result.txt": ', os.listdir())