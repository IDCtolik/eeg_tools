# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 21:28:10 2019

@author: Tolik
"""
#global variables in use of auxilary methods
trigger_list = []
camera_trigger = 0
main_camera_trigger = 0


#sets the camera trigger, calculates trigger times in video and saves it in a list
def set_triggers():
    triggers = input("insert triggers using the following format: 10,11,12 \n")
    triggers = list(map(int, triggers.split(",")))
    global main_camera_trigger
    global camera_trigger
    main_camera_trigger = int(input("enter camera trigger \n"))
    camera_trigger = main_camera_trigger
    global trigger_list
    trigger_list = []
    
    for i in triggers:
        #calculates the new triggers and sets the format: mm:ss, ssss
        trigger_list.append(str(int((i-camera_trigger)/60)) + ':' + str((i - camera_trigger)%60) + ',    ' + str(i - camera_trigger))
    print_triggers()
        
#prints the list of triggers for camera        
def print_triggers():
    global trigger_list
    print("\n")
    for i in trigger_list:
        print(i + "\n")

#set a different value for the camera trigger        
def set_camera_trigger():
    global camera_trigger
    global main_camera_trigger
    main_camera_trigger = camera_trigger
    camera_trigger = int(input("type new camera trigger \n"))

#reset the camera trigger to the current set of triggers (as set by set_triggers())
def reset_camera_trigger():
    global camera_trigger
    global main_camera_trigger
    camera_trigger = main_camera_trigger

#converts eeg time to video time    
def eeg_to_video(eeg_time):
    eeg_time = int(eeg_time)
    global camera_trigger
    print(str(int((eeg_time - camera_trigger)/60)) + ":" + str((eeg_time - camera_trigger)%60))

#converts video time to eeg   
def video_to_eeg(video_time):
    video_time = video_time.split(":")
    global camera_trigger
    print(int(video_time[0])*60 + int(video_time[1]) + camera_trigger)



   
while True:
    arg = input("enter command: exit|set triggers|set camera|reset camera|show triggers|mm:ss|ssss\n")
    if arg == "exit":
        break
    elif arg == "set triggers":
        set_triggers()
    elif arg == "set camera":
        set_camera_trigger()
    elif arg == "reset camera":
        reset_camera_trigger()
    elif arg == "show triggers":
        print_triggers()
    elif (':' in arg):
        video_to_eeg(arg)
    else:
        eeg_to_video(arg)

    

        