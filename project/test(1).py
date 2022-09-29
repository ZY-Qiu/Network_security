import subprocess
import os
import time


status,output = subprocess.getstatusoutput('adb devices')
print(status)
print(output)

PATH = "E://apk/"
apk_list = os.listdir(PATH)

index = 1
for i in apk_list:
    print(index)
    print(i)
    status,output = subprocess.getstatusoutput('adb install -g -r '+ PATH + '\"' + i + '\"')
    if(status == 1):
        continue
    with open("./apk_list.txt", "a") as f:
        f.write(i.replace(".apk", "").replace("_apk-dl.com", "") + "\n")
    status,output = subprocess.getstatusoutput('adb shell pm list packages -3')
    if(output == '' or output == None):
        continue
    app_name = output.split()[0].split(':')[1]
    print(app_name)
    
    status,output = subprocess.getstatusoutput('adb shell monkey -p ' + app_name + ' --pct-touch 100 --throttle 1000 30')
    
    status,output = subprocess.getstatusoutput('adb shell pm uninstall '+app_name)
    
    status,output = subprocess.getstatusoutput('adb shell am start -a android.intent.action.VIEW -d http://'+ str(index) +'.neverssl.com')
    
    status,output = subprocess.getstatusoutput('adb shell am force-stop com.android.chrome')

    time.sleep(10)
    index += 1
