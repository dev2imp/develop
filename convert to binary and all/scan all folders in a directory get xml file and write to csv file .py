import csv
import xml.etree.ElementTree as ET
import os
import shutil
import subprocess
from pathlib import WindowsPath
import filecmp

class get_permission():
    
    def featur(features):
        with open('Allfeatur.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                features.append(row)
#the featur named function contains 328 kind of permissions on an android file
#those permissions are in the csv file that is in same directory with py file.

                
                
    def start(features):
        arrayoffolder=[]
        subdirs = WindowsPath(r'C:\\APKTOOL\\decompile by python\\1 decompiles all apk file in the same directory')
        numberofapps=0
        for f in subdirs.iterdir():
            if f.is_dir():
                numberofapps=numberofapps+1
                arrayoffolder.append(f)
                #all folders of the apps are appened to array later we willneed when extract
                #permission from androidmanifest xml file.
        i=0#to count apps in same directory
        while i!=numberofapps:
            for fl in arrayoffolder[i].iterdir():
                k=('%s\AndroidManifest.xml'%arrayoffolder[i])
                print(fl)
                if filecmp.cmp(fl, k):                    
#to find androidmanifest file on the folder. compreing returns true when dir are same
                    root = ET.parse(fl).getroot()
                    permissions = root.findall("uses-permission")
                    permission_in_checking_app=[]
#array to save all 1 s and 0 s to  write a file
                    for perm in permissions:
                        for att in perm.attrib:
                            permission_in_checking_app.append([perm.attrib[att]])
                    #line above add all permmissions to an array.                                                    
                        data=[]
#data array will have 0's and 1's of apps if they have perm.1 if doesnt have 0 for present perm.
                        for f in range(328):#totally we have 328 permis. we need to scan all perms to decide
                                            #if we put 0 or 1 to data array.
                            for r in range(len(permission_in_checking_app)):
                                if (features[f])==(permission_in_checking_app[r]):
                                            #permission_in_checking_app contain permissions of the app that
                                            #we are going to check. it may contain 2 or 10 or 328 etc.
                                    data.append('1')#if contain the permission 1 will be added to data
                                else:
                                    data.append('0')#if doesnt contain the permission 0 will be added to data
                    with open('train_test.csv','r') as csvinput:
                        with open('handler_of_train_test_data.csv', 'w') as csvoutput:
                            writer = csv.writer(csvoutput, lineterminator='\n')
                            reader = csv.reader(csvinput)
                            all = []#we need another array that is named all it saves all data of a single app
                            #that will be writen on a a row.
                            row = next(reader)
                            row.append('1')#first row is type: malware or bening
                            all.append(row)
                            n=0
                            for row in reader:
                                row.append(data[n])
                                all.append(row)
                                n=n+1
                            writer.writerows(all)
                            csvinput.close()
                            csvoutput.close()
                    with open('handler_of_train_test_data.csv','r') as csvinput:
                        with open('train_test.csv', 'w') as csvoutput:
                            writer = csv.writer(csvoutput, lineterminator='\n')
                            reader = csv.reader(csvinput)
                            writer.writerows(reader)
                            csvinput.close()
                            csvoutput.close()
            i=i+1
    features=[]
    featur(features)    
    start(features)
        
               
get_permission()



        
    
