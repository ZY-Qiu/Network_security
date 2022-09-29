import subprocess
import os
import time


status,output = subprocess.getstatusoutput('adb devices')
print(status)
print(output)

PATH = "E://apk/"
apk_list = os.listdir(PATH)


for i in apk_list:
    
    status,output = subprocess.getstatusoutput('adb install -g ' + PATH + '\"' + i + '\"')
    print(status)
    print(output)
    print("----------------\n")
    
    status,output = subprocess.getstatusoutput('adb shell pm list packages -3')
    print(status)
    print(output)
    print("----------------\n")
    app_name = output.split()[0].split(':')[1]
    
    with open("./apk_list.txt", "a") as f:
        f.write(app_name + '\n')
    '''
    status,output = subprocess.getstatusoutput('adb shell monkey -p ' + app_name + ' -v 500')
    print(status)
    print(output)
    print("----------------\n")
    '''
    status,output = subprocess.getstatusoutput('adb shell pm uninstall '+app_name)
    print(status)
    print(output)
    print("----------------\n")
    
    status,output = subprocess.getstatusoutput('adb shell am start -a android.intent.action.VIEW -d http://1.neverssl.com')
    print(status)
    print(output)
    print("******************************\n")

    time.sleep(10)