import subprocess
from datetime import datetime
from time import sleep




#Checks the time taken to upload a new project to DDS, using the GCB client
#At present references a file in my personal desktop, but should probably be modified to
#include a test file in the GCB client's download files
def checkuploadtime():
    start=datetime.now()
    subprocess.run('ddsclient upload -p Test C:\\Users\\lwpul\Desktop\TestFolder', shell=True)
    return datetime.now()-start
#Checks the time taken to delete a project from DDS, using the GCB client
def checkdeletetime():
    start=datetime.now()
    subprocess.run('ddsclient delete -p Test --force', shell=True)
    return datetime.now()-start

#Uses the parameter testnumber for the number of tests to be done
#Checks both upload and deletion times and returns the average for each
#in the form upload, download
#note: these returned values are datetime objects
def getAverageTimes(testnumber):
    subprocess.run('pip install --upgrade DukeDSClient')
    uptimes = datetime.now() - datetime.now();
    deletetimes = datetime.now() - datetime.now();
    for i in range(testnumber):
        print('Test Number ' + str(i + 1))
        uptimes += checkuploadtime()
        deletetimes += checkdeletetime()
    #print("\n\n\n\n " + str(testtime) + "  Trials: \nThe average upload time is: " + str(uptimes/testtime) + "\nThe average delete time is: " + str(deletetimes/testtime))
    return uptimes / testnumber, deletetimes / testnumber

#startval parameter defines the number of trials in the initial establishment of the average time
#tests upload and deletion times every ten seconds
#keeps rolling average -- if the rolling average ever becomes greater than twice the initial avg
#returns and prints error statement
def testPerformance(up, delete):
    upavg, deleteavg = up, delete
    initup = upavg
    initdelete = deleteavg
    #Below weights the average so that the most recent test is half of the average
    upavg = (checkuploadtime() + upavg) / 2
    #Same for deleteavg
    deleteavg = (checkdeletetime() + deleteavg) / 2
    print("Average Upload Time: " +str(upavg))
    print("Average Deletion Time: " +str(deleteavg))
    if upavg > 2 * initup:
        print("DANGER: UPLOAD TIME COMPROMISED")
        print(str(((upavg / initup) - 1) * 100) + "% greater than expected")
        print("The average upload time is " + str(upavg) + " and the initial average is " + str(initup))
        return False
    elif deleteavg > 2 * initdelete:
        print("DANGER: DELETE TIME COMPROMISED")
        print(str(((deleteavg / initdelete) - 1) * 100) + "% greater than expected")
        print("The average delete time is " + str(deleteavg) + " and the initial average is " + str(initdelete))
        return False
    else:
        return True

def runTest(startval):
    up, delete = getAverageTimes(startval)
    while True:
        if testPerformance(up, delete):
            print("Test Passed")
        else:
            print("Test Failed")
        if input("Enter y to conduct another test:") == 'y':
            continue
        else:
            break
