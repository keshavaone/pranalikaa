 ##Company Organization details are needed and Employee flow times need to code and have to save on the daily basis and also 
#add code to include payroll on daily basis.

############################################## Import Libraries Begin ###############################################
import numpy as np, tkinter as tk,getpass,time,datetime,pickle,sys

user_choice = 'BubbleeTree 1.0'
############################################## Import Libraries  Done ###############################################
#Used Library Lists
    #1. numpy
    #2. tkinter
    #3. getpass
    #4. datetime
    #5. pickle
    #6. keyboard
    #7. os
    #8. time
    #9. sys
############################################## Saving and Loading Files Begin #######################################
def save(net): #Function: Saving the Updated Values
    with open(user_choice,"wb") as save_file: 
    #File Open/Create a File
        pickle.dump(net,save_file) 
        #input dumping

def load(name = "noname"):
    #Function: Loading the Recently Updated Values.
    with open(user_choice,"rb") as load_file: 
    #Opens the loaded file
        return pickle.load(load_file) 
        #returns the loaded file

    ############################################## Saving and Loading Files Done  #######################################

    ############################################## File Check Begin #####################################################

# def AutoCOVIDingExcel():
#     ## Covid Excel Sheet Import program helps dialy statistics,Analysis and Predictions.
#     #used keyboard library, for installing, ---> pip install keyboard.Thats it.
#     print('Alert: Please Dont Touch the Keyboard until Confirmation of Completion.') #Warning. during this function process.
#     #During this process, continuous operations are being held out. 
#     #better not touch the keyboard... until the function executes "Done".
#     import os,time
#     try: #Python not pre installed with keyboard library. its better to avoid exception.
#     #Hence the Try Form is There.
#         import keyboard
#         os.startfile('C:\\Users\\Home\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Anaconda Powershell Prompt (AnacondaNewandManualInstallation)')
#         # if executing from another computer, Changing the Destination Folder is Mandatory.
#         # Please Make Sure Directory Path is Changed According to User Requirements.
#         time.sleep(4) 
#         # Time Taking for Loading to certain Directory and then, writing on the Command Helps Process Better.
#         keyboard.write('cd \'C:\\Users\\Home\\Downloads\\Keshav Files\\Keshav\\Codes\\COVID-19\'') #Program Directory Path
#         ##Series of Process Running the Program and Executing back to Normal Work(alt+tab) Automatically.
#         keyboard.press_and_release('enter')
#         #presses the enter key
#         keyboard.write('python COVID-19.py')
#         #enters this command
#         #this is changeable according to user preferences. name is a variant here.
        
#         time.sleep(3)
#         #waits for 3 seconds, for not creating any errors.
#         keyboard.press_and_release('enter')
#         #presses to enter the program
#         keyboard.write('n')
#         #Means: No
#         keyboard.press_and_release('enter')
#         #Decision Given to Program 
#         keyboard.write('n')
#         #Means: No
#         keyboard.press_and_release('enter')
#         #Decision Given to Program
#         keyboard.write('n')
#         #Means: No
#         keyboard.press_and_release('enter')
#         #Decision Given to Program
#         keyboard.write('n')
#         #Means: No
#         keyboard.press_and_release('enter')
#         #Decision Given to Program
#         keyboard.write('y')
#         #Means: Yes
#         keyboard.press_and_release('enter')
#         #Decision Given to Program        
#         time.sleep(2)
#         #waits for 2 Seconds to enter into Full Screen Mode
#         keyboard.press_and_release('F11') #Full Screen Mode
#         keyboard.press_and_release('alt+tab')
#         #to get back to currently operating program by user.
#         print('\nDone\n\n') #Function Execution Completion Result.
#     except: 
#         #Notifying All Possible Errors.
#         print('Probable Errors:\n\t1.Cant Execute the Program. please install keyboard library - pip install keyboard\n\t2.Please Update the Application Program Location in the program or input the shortcut key in the program.\n\t3.Update the Press Keys.')

dw = ['yes','y'] #just to verify the user input as yes or no
count56 = 0 #variable assigning
start_hours,start_minutes,start_seconds,end_hours,end_minutess,end_seconds = 23,59,59,23,59,59 #default time settings.
dw, Date_Current,count_check = str(dw),datetime.datetime.now(),False
global plan,task1,task3,today_mins_left,today_mins_over,task2,t1,t2,t3,t10,t4,t5,count # global declaration of variables
remainder,timerun,describe,time2,t1,t2,t3,t4,t5,t6,stupid,status1,t10,tasks_over  = [],[],[],[],True,True,True,True,True,True,False,False,True,False #list inits
#Defualt Remainder is set according to user requested time formats.
Default_Remainders = ['09:00','13:30','18:30','21:00']
#ExcelProgram Time init.
task31 = '21:45'
#count is a parameter for the first task as a default one.
count = 1 #default inits
new_remminder,final_remainder = [],[] #list initialization for reminders.
new_remmind_int = 16 #1440/90 #reminder for every 90 mins
for i in range(16):
    new_remminder.append(90*i) #minutes count for every 90 mins.
reminder_time_half = [( str(int(new_remminder[i] / 60)) + ' : 30') for i in range(len(new_remminder)) if str(new_remminder[i] / 60 ).split('.')[1] == '5'] #reminder list values.
 #list values divided by 60 in hours side and filtered for .5 on minutes side and convert it to strings and add ':30' at the end.
 #Assigned those values to reminder_time_half.

reminder_time = [( str(int(new_remminder[i] / 60)) + ' : 00') for i in range(len(new_remminder)) if str(new_remminder[i] / 60 ).split('.')[1] == '0']
#list values divided by 60 in hours side and filtered for .0 on minutes side and convert it to strings and add ':00' at the end.

half_an_hour_remainders = [list((reminder_time_half[i],reminder_time[i])) for i in range(int(len(new_remminder)/2))]
#half an hour reminders .., :00 are collected, :30 reminders are collected and formed a tuple and assigned the nested loops of tuples
#tuples are nested by list forms.

[((final_remainder.append(half_an_hour_remainders[i][1])), final_remainder.append(half_an_hour_remainders[i][0])) for i in range(len(half_an_hour_remainders))][0][0]     
#final remainder is the list of all values in remainders that are converting the tuples into individual values.
#all the individual values are considered as individual counts and inserted as a list.

final_remainder1 = []
for i in range(len(final_remainder)):
    if len(final_remainder[i].split(':')[0].split(' ')[0]) == 1:
        final_remainder1.append('0' + final_remainder[i])
        #splitting the values of a string.
        #concatenating 0 in prefix side if the value < 10.
    else:
        final_remainder1.append(final_remainder[i])
        #if the hours side has a length > 1, direct addition of values into list form.
task3 = (int(task31.split(':')[0]) * 60) + int(task31.split(':')[1]) # splits hours side value and multiply by 60.
#Add Miutes side value to the result to get the exact form of output.
#Current Hours is given to check_hrs to check for wishes.
check_hrs = int(datetime.datetime.now().strftime('%H'))
if check_hrs < 12: #if it is Morning Hours
    wishes,wishes1 = 'Good Morning','Good Morning'
elif check_hrs < 16 and check_hrs >= 12: #if it is in Afternoon Hours
    wishes1, wishes = 'Good Afternoon','Good Afternoon'
elif check_hrs >= 16: #if it is in Evening Hours
    wishes, wishes1 = 'Good Evening','Good Evening'
elif check_hrs >= 19: #if it is night hours
    wishes1 = 'Good Night'
username = input('UserName: ') #username input
password = getpass.getpass() #password input

if username == 'Keshav' and password == 'Pranalikaa': #username and password is a case-sensitive and checks the input values
#if username and password is correct, it enter the if loop otherwise, it wont.
    #result/status printing.
    print('Password: Correct\nLogin Status: Success\n\n\n\t\t\t\t\t\t\t\t{} {}'.format(wishes, username)) #success output printing.
    #Line Helps in printing the Current Time and wishing from Current Program to User.
    print('\n\n\n\n\n\n\t\t\t\t\t\t\t    Welcome to Day Plan Program\t\t\t\t{}\n\n\n'.format(Date_Current.strftime("%b %d %Y - %A - %H:%M:%S")))
    time.sleep(2.5) #waited to see the Name, Wishing.
    
    ################################### Function: Updated Score(Preparing the last updated scores and use it to Update current)
    
    #Single Rule is, This Program intentionally allots the user to book any 2/3 tasks in a day.
    #All the Other Tasks are in the form of Plans.
    #if you are loyal to this program in scoring your performances on dialy basis. this will ensures you the exact productivity score.
    #This is the Function That takes care of the program in scoring the user finished timely tasks.
    def UpdatedScore(pLan): #function def for Updated Scores
        if pLan == '1': #input check for the First task
            CHECK_STAGE11 = float(input('Rate your Satisfaction(0(Poor) - 5(Excellent)): ')) #Level of your Acceptance, Asks the user to enter the score.
            if CHECK_STAGE11 == 0.0: #Which Means youyr productivity consideration at level : 0
                print('you have wasted your day') #Ofcourse, this will discourage you. but you made yourself come into this loop.
                #Please Make sure you are using your time on productive basis.
                #worst case scenario
            print('Entered Score:',CHECK_STAGE11) #To Make sure that the input is Taken.
            #Score Output
            #Below Line is loading the encoded values by decoding from Binary Format into their exact variables.
            [count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3,task_name1,task_name2,task_name3,start_year,start_month,start_date,end_year,end_month,end_date] = load(user_choice) #Loading Previous Scores
            #adds to the previously saved variable.
            #adds the saved variable to the current variable.
            CHECK_STAGE1 += (CHECK_STAGE11)
            #Adding it to Current Scores
            #rounding the currently operated variable to the current variable.
            CHECK_STAGE1 = round(CHECK_STAGE1,3)
            #rounding it to 3 
            #Takes the decimal value to check the level.
            if np.ceil(CHECK_STAGE11) == 1:
                #printing the current value level.
                print('Productivity Status: Poor\n\tFind Sometime and Improve the Scores and learning rate for the Best Results.\n\tPlan Accordingly.')
            #rounding it to 3 
            #Takes the decimal value to check the level.
            elif np.ceil(CHECK_STAGE11) == 2:
                #printing the current value level.
                print('Productivity Status: Below Avearge')
            
            #rounding it to 3 
            #Takes the decimal value to check the level.
            elif np.ceil(CHECK_STAGE11) == 3:
                #printing the current value level.
                print('Productivity Status: Average')
            #rounding it to 3 
            #Takes the decimal value to check the level.
            elif np.ceil(CHECK_STAGE11) == 4:
                #printing the current value level.
                print('Productivity Status: Above Average')
            #rounding it to 3 
            #Takes the decimal value to check the level.
            elif np.ceil(CHECK_STAGE11) == 5:
                #printing the current value level.
                print('Productivity Status: Excellent')
            else:
                #pass
                pass
            #printing the final value output.
            print('Score Submitted!\nNewly Updated Score for ',task_name1,' is',round(CHECK_STAGE1,3),'\nSaved\n') #submitting the scores
            #setting back the values.
            final_count = [count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3,task_name1,task_name2,task_name3,start_year,start_month,start_date,end_year,end_month,end_date] #load into a variable
            save(final_count) #saving the file (user_choice)
    
        elif pLan == '2':  #input check for the second task.
            #program asks the user to take the value, and inserts the data into CHECK_STAGE22
            CHECK_STAGE22 = float(input('Rate your Satisfaction(0(Poor) - 5(Excellent)): ')) #Level of your Acceptance for the range
            if CHECK_STAGE22 == 0.0: #worst case scenario
                print('\n\n\t\tInkeppudu raa, nuvvu baagupadedhi') #worst case scenario output for the bad usage of your time
            print('Entered Score:',CHECK_STAGE22)  #Score Output lets us know the input is given and it has taken successfully.
            [count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3,task_name1,task_name2,task_name3,start_year,start_month,start_date,end_year,end_month,end_date] = load(user_choice) #Loading Previous Scores that are stored
            #This actually ensures the code being in upto date by taking the previous values and outputs
            #operates the current format.
            CHECK_STAGE2 += CHECK_STAGE22 #Adding the values with current scores
            CHECK_STAGE2 = round(CHECK_STAGE2,3) #rounding it to 3 decimal points. 
            #takes the integer value to verify the fact of time usage and outputs the value.
            if np.ceil(CHECK_STAGE22) == 1:
                #if the value is 1, time usage level is at poor state.
                print('Productivity Status: Poor')    
            #takes the integer value to verify the fact of time usage and outputs the value.
            elif np.ceil(CHECK_STAGE22) == 2:
                #if the value is 2, time usage level is at below average state.
                print('Productivity Status: Below Avearge')
            #takes the integer value to verify the fact of time usage and outputs the value.
            elif np.ceil(CHECK_STAGE22) == 3:
                #if the value is 3, time usage level is at average state.
                print('Productivity Status: Average')
            #takes the integer value to verify the fact of time usage and outputs the value.
            elif np.ceil(CHECK_STAGE22) == 4:
                #if the value is 4,time usage level is at above average state.
                print('Productivity Status: Above Average')
            #takes the integer value to verify the fact to time usage and outputs the value.
            elif np.ceil(CHECK_STAGE22) == 5:
                #if the value is 5, time usage level is at Excellent Stage
                print('Productivity Status: Excellent')
            
            #if the user did not passes any value, the user current state automatically takes it as a zero.
            #But no output generates.
            else:    
                pass
            #gives an output that the value has been taken and gives the updated score after adding the value with the previous values.
            print('Score Submitted!\nNewly Updated Score for ',task_name2,' is',round(CHECK_STAGE2,3),'\nSaved\n') #submitting the scores            
            #reassigns the updated values to single variable in the form of list.
            final_count = [count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3,task_name1,task_name2,task_name3,start_year,start_month,start_date,end_year,end_month,end_date] #load into a variable
            #then saves the file.
            save(final_count) #saving the file (user_choice)    
        #if the task is 3
        elif pLan == '3': #if the task is 3...    
             #program asks the user to take the value, and inserts the data into CHECK_STAGE22
            CHECK_STAGE33 = float(input('Rate your Satisfaction(0(Poor) - 5(Excellent)): ')) #Level of your Acceptance
            if CHECK_STAGE33 == 0.0: #worst case scenario    
                print('\n\n\t\tInkeppudu raa, nuvvu baagupadedhi')#worst case scenario output for the bad usage of your time            
            #Score Output lets us know the input is given and it has taken successfully.
            print('Entered Score:',CHECK_STAGE33)  #Score Output            
            #This actually ensures the code being in upto date by taking the previous values and outputs
            [count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3,task_name1,task_name2,task_name3,start_year,start_month,start_date,end_year,end_month,end_date] = load(user_choice) #Loading Previous Scores    
            #operates the current format.
            CHECK_STAGE3 += (CHECK_STAGE33)  #Adding it to Current Scores    
            CHECK_STAGE3 = round(CHECK_STAGE3,3)  #rounding it to 3 
             #takes the integer value to verify the fact of time usage and outputs the value.
            if np.ceil(CHECK_STAGE33) == 1:
                #if the value is 1, time usage level is at poor state.
                print('Productivity Status: Poor')
            #takes the integer value to verify the fact of time usage and outputs the value.
            elif np.ceil(CHECK_STAGE33) == 2:
                #if the value is 2, time usage level is at below average state.
                print('Productivity Status: Below Avearge')
            #takes the integer value to verify the fact of time usage and outputs the value.
            elif np.ceil(CHECK_STAGE33) == 3:
                #if the value is 3, time usage level is at average state.
                print('Productivity Status: Average')
            #takes the integer value to verify the fact of time usage and outputs the value.
            elif np.ceil(CHECK_STAGE33) == 4:
                #if the value is 4,time usage level is at above average state.
                print('Productivity Status: Above Average')
            #if the value is 5, time usage level is at Excellent Stage
            elif np.ceil(CHECK_STAGE33) == 5:
                #if the value is 5, time usage level is at Excellent Stage
                print('Productivity Status: Excellent')
            
            #if the user did not passes any value, the user current state automatically takes it as a zero.
            #But no output generates.
            else:
                pass
            #gives an output that the value has been taken and gives the updated score after adding the value with the previous values.
            print('Score Submitted!\nNewly Updated Score for ',task_name3,' is',round(CHECK_STAGE3,3),'\nSaved\n') #submitting the scores
            #reassigns the updated values to single variable in the form of list.
            final_count = [count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3,task_name1,task_name2,task_name3,start_year,start_month,start_date,end_year,end_month,end_date] #load into a variable
            #then saves the file.
            save(final_count) #saving the file (user_choice)          
    
        else: #if not
            pass #pass
    
    

################################################### Actual Program Begins ###########################################################################
    try: #check side
        f = open(user_choice) #opens file and gets the details of all stored formats.
        #loads into their respective variable
        count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3,task_name1,task_name2,task_name3,start_year,start_month,start_date,end_year,end_month,end_date = load('user_choice')
        #all the received variables are saved and given into single variable in the form of list.
        final_count = [count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3,task_name1,task_name2,task_name3,start_year,start_month,start_date,end_year,end_month,end_date]  # set it to final_count        
        #all the saved variables are printed out to show the program is taken the variables.
        index2 = '\n{} STATUS SCORE -->{}.\n{} STATUS SCORE -->{}.\n{} STATUS SCORE -->{}.\n\nRate of Learning {} Score is-->{}.\nRate of {} Completion Score is-->{}.\nRate of {} Score is -->{}'.format(task_name1,count1,task_name2,count2,task_name3,count3,task_name1,CHECK_STAGE1,task_name2,CHECK_STAGE2,task_name3,CHECK_STAGE3) #Score Loading
        f.close() #program closes the file    
    #Exception Occured if there is a File Exists (IOError).
    except IOError:              
        time.sleep(2)                                              
        print("File not Exist\nCreating File...",end='\r') #Output the Failed Execution Reason.        
        #all the default values are used and given it to final_count.
        count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3,task_name1,task_name2,task_name3,start_year,start_month,start_date,end_year,end_month,end_date, =  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 #load into a variable        
        final_count = [count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3,task_name1,task_name2,task_name3,start_year,start_month,start_date,end_year,end_month,end_date]
        #final_count list values are saved into the file.
        f = save(final_count) #saving the value        
        index2 = '\n{} STATUS SCORE = {}.\n{} STATUS SCORE = {}.\n{} STATUS SCORE = {}.\n\nRate of Learning {} Score is = {}.\nRate of {} Completion Score is = {}.\nRate of {} Score is = {}'.format(task_name1,count1,task_name2,count2,task_name3,count3,task_name1,CHECK_STAGE1,task_name2,CHECK_STAGE2,task_name3,CHECK_STAGE3) #Score Loading
        #prints the output value of current progress.
        time.sleep(2)
        print('count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3 are newly Assigned\nNew File({}) Created,Values are',count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3,user_choice,end = '\r') #printing the progress
    finally: #finally statement (Default Print)        
        #reopens the file 
        f = open(user_choice)    
        print('\nSaving, Updated Scores...',end='\r') #Saving the Updated Files
        time.sleep(2)
        print('Program is Ready to RUN.',end = '\r')
        time.sleep(2)
        print('Opened File is Closing..',end = '\r')
        time.sleep(2)
        f.close() #closing the file
        print('Displaying Results init.',end = '\r') #printing the progress

    ############################################## File Check Done #####################################################
    print(index2,'\nAll Required Inputs are Retrieved and alloted to its Respective Variables.')
    print('\n\t\t\t\tMake Sure you Meditated for Today. Its Very Much Essential Ingredient for your Life.\n\n\n\n')
    theme = input('\nEnter the Theme for your Day: ') #Theme Input like proverb or quotation.
    print('\n\n\t\t\t\t\t\tTHEME: ',theme,'\n\n')# Theme Taken print.
    #all available tasks.
    #you can change or update them in admin block side.
    #Admin Credentials needed.
    Output_Plan,Plan = '\nAvailable LEARNINGs/Tasks: \n1 : {}\n2 : {} \n3 : {}'.format(task_name1,task_name2,task_name3),{'1': task_name1, '2':task_name2, '3':task_name3} #options available
   
    #remaining days.
    Updated_days = (datetime.datetime(end_year,end_month,end_date,end_hours,end_minutess,end_seconds) - datetime.datetime.today()).days
    days_left = Updated_days #days over
    #finished days.
    #count value
    DAY_COUNT = int((datetime.datetime.today() - datetime.datetime(start_year,start_month,start_date,start_hours,start_minutes,start_seconds)).days) + 1
    #print format of values that are got.
    print('Days Over: {}\nDays Left: {}\n{}\n\n'.format(DAY_COUNT,days_left,Output_Plan)) #printing the days over
    #if the day length is 1, then the value is converted into string
    #then adds 0 the prefix.
    #saves the value to the DAY_COUNT1
    if len(str(DAY_COUNT)) == 1:
        DAY_COUNT1 = '0' + str(DAY_COUNT)
   
    #Otherwise the values are same.
    else:
        DAY_COUNT1 = DAY_COUNT
        pass
    #Asks the user to take any 2 plans for the day.        
    plan = str(input('\n\t\t\t\t\tDay Plan\n\n\nChoose from above three plans for your day: ')) #Input for the plan name   
    #checks for the plan values by dividing
    try:
        if plan[0] and plan[1] in Plan: # checking the input   
            print('\n\t\t\t\t\tTasks for Today is:\n\n\t\t\t\t\t\t1.', Plan[plan[0]],'\n\t\t\t\t\t\t2.',Plan[plan[1]]) #format style type printing
            for i in range(2): #checking and adding 1 to the respective user_choice variable           
                if plan[i] == '1': #check value            
                    count1 += 1 #adding  value by 1 for task 1
                    print(Plan[plan[i]],'Score:',count1) #count value output
                elif plan[i] == '2': #check value 
                    count2 += 1 #adding  value by 1 for task 2
                    print(Plan[plan[i]],'Score:',count2) #count value output
                elif plan[i] == '3': #check value 
                    count3 += 1 #adding  value by 1 for task 3
                    print(Plan[plan[i]],'Score:',count3)  #count value output
        else: #if nothing is given
            print('You have entered a wrong input') #printing the error message
            stupid = True
            pass #pass
    except: #exception occured because of the input length is one
        #Error message is given as an index error.
        print('Error: ',str(sys.exc_info()).split('\'')[1].split('>')[0],'\nWrong inputs Given.')
        stupid = True #boolean assigning.
    #saving inputted values by assigning them into default variable final_count.
    final_count = [count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3,task_name1,task_name2,task_name3,start_year,start_month,start_date,end_year,end_month,end_date] #load into a variable
    save(final_count) #saves with updated file 
    if stupid == True:
        check_time = 'n'
    else:
        #asks the user to input each task time 
        check_time = input('Do you want to add a custom end time for each task: (y/n): ').lower() #end-time request
   
    if check_time in dw: 
    #if user inputs yes
        task1 = str(input('Task 1 End Time (HH:MM): ')) #inputs the task1 end time   
        task1 = (int(task1.split(':')[0]) * 60) + int(task1.split(':')[1]) # splits to convert to minutes
   
        task2 = str(input('Task 2 End Time (HH:MM): ')) # inputs the task2 end time
        task2 = (int(task2.split(':')[0]) * 60) + int(task2.split(':')[1]) # splits to convert to minutes
   
        print('Task 1 and Task 2 Schedules are Saved Successfully') # output Success output
    else: #if  not        
        if stupid == True: #if boolen value is True, no tasks given as an input, hence it should be true.            
            task1,task2 = 0,0 # tasks 1 and 2 are set to zero.
            print('No Tasks are Scheduled.')
        else: #if the tasks are given, then it comes into this loop as the boolean value(stupid) is False.
            print('\nSetting it into Default Time.\nTask 1 end time: 16:30\nTask 2 end time: 17:30') #Default Print Output to 960 minutes(16:00) and 1420 minutes(23:40)         
            task2 = 1050 #default time value
            task1 = 990
            count = 1
    
    task2_half = np.ceil((task2 -  task1)/2 + task1) #task is halved for remainder info.
    #Remainder list.
    remainder = ['Breakfast Time','Lunch Time','Dinner Time','Resource Checklist Time']    
    #Remainder Description.
    describe = ['Normal Breakfast Time','Normal Lunch Time','Normal Dinner Time','Gather all your Resources Now and Help your Next Day.']
    #Default Remainders are given according to user style of day format.
    time2 = [Default_Remainders[0], Default_Remainders[1], Default_Remainders[2],Default_Remainders[3]]
    #for loop actually converts the string form that the user gave into minutes format
    #that program can operate on efficient basis.
    for i in range(len(time2)): #loop for the total time length.
        time1 = str(time2[i]) #takes i th position from time2
        time1 = (int(time1.split(':')[0]) * 60) + int(time1.split(':')[1]) # splits to convert it to minutes.
        timerun.append(time1) #appends to list.
        count56 += 1#its just a count parameter.               
    print('---\nBreakfast.\nLunch.\nDinner.\nResource Checklist. \n---Status---->On Default Remainders.')
    check = input('Any Other Plans(y/n): ').lower() #asking the user weather the user sets any other plans or not.
    if check in dw: #if user says says yes.
        g = int(input('No of Extra Plans for Today: '))#Total No of Plans
        #counting starts and asks the user plans
        #Reqmnts:#Name of the Plan
                 #Any Notes for the Plan to describe in detail
                 #Reminding Time
                 #Update Acknowledgement.
        for k in range(g):# 
            remainder1 = input('Enter the name of the Remainder-{}: '.format(k+1))
            remainder.append(remainder1) #Remainder1 is stacked into remainder list.
            describe1 = input('Description: ')
            describe.append(describe1)#describe1 is stacked into describe list.
            time1 = str(input('Reminding Time at (HH:MM): ')) #inputs the task1 end time
            time2.append(time1)#time1 is stacked into time2 list
            #converts the user set time into mins
            #appends the minutes time in timerun list.
            time1 = (int(time1.split(':')[0]) * 60) + int(time1.split(':')[1]) # splits according to requirements
            timerun.append(time1) #time1 is stacked into list.
            count56 += 1 #count parameter.
            print('Updated')
    else: #if user is not having plans, it will be No.
        pass
    print('All 1.5 Hr Remainder Timings are Set and they are : ')
    custom_time_final = '22:15' ##program end time 

    #loops into the list of half_an_hour_remainders and prints each one in the stack.
    #The half_an_hour_remainders has list of tuples.
    #These Tuples are divided into items.
    #this moves the program to show the user the list of remainders in ordered format
    [((print('\t',half_an_hour_remainders[i][1])), print('\t',half_an_hour_remainders[i][0])) for i in range(len(half_an_hour_remainders))][0][0]
    time_final_check = input('\n\t\tProgram ends at {} ,\n Do you want to end the Program in a Different Time (y/n): '.format(custom_time_final))
    
    if time_final_check in dw: #program termination request
    #if the user wants to enter the different time  , it asks in custom_time_final    
        custom_time_final = input('Enter the End Time(HH:MM): ')
    #after taking the input, the value is converted into minutes.
    #converted minutes value is assigned to time_final
        time_final = (int(custom_time_final.split(':')[0]) * 60) + int(custom_time_final.split(':')[1]) # splits according to requirements                   
    # if the user is not willing to change the termination time.
    #sets the time to default that is 22:15 PM. IST
    else:
        print('Registering Program Termination Clock time at: {}'.format(custom_time_final))    
        time_final = time_final = (int(custom_time_final.split(':')[0]) * 60) + int(custom_time_final.split(':')[1]) # splits according to requirements
    #asking the user to change the default excel time
    # excel_final_check =  input('\n\n\n\tExcelImport Start Time at {}.\nDo you want to update its time (y/n): '.format(task31))
    # #if the user is interested to change the time.
    # if excel_final_check in dw:
    #     #if the user said 'yes', then the Excel import Time is Changed in the next output.
    #     task31 = input('Enter the Time(HH:MM): ')
    #     print('Registering ExcelImport Start Time at {}\n\n'.format(task31))
    #     #converting the time from user format to minutes format to get the program requirements.
    #     task3 = (int(task31.split(':')[0]) * 60) + int(task31.split(':')[1]) # splits to convert it to minutes.

    
    # else:
    # #if not interested , then it comes to this loop.
    #     print('Ok')
    #     print('Registering ExcelImport Start Time at {}\n\n'.format(task31))
    #prints all the Remiander list.
    print('\n\t\tRemainder List:')
    
    for k in range(count56):#counts with the count parameter.
        #prints all the available remainders in the remainder list along with the time.
        print('\t\t\t',remainder[k],'-->',time2[k])
    #subtracts the End date to start date.
    sce = str(datetime.datetime(end_year,end_month,end_date,end_hours,end_minutess,end_seconds) - datetime.datetime.now()) #value between the task1 start and end time
    try: # try check error input
        # day status in days.    
        day_status = int(sce[0:2]) #day status inits    
    except: # error outputs
    #day count in days.
        day_status = int(sce[0:1]) # day status inits
    #sleep for a second.
    time.sleep(1)
    #if the length of the day is 1
    if len(str(days_left)) == 1:
    # concatenate 0 to the prefix.
        days_left1 = '0' + str(days_left)
    else:
        days_left1 = days_left
        pass
    # So, Preprocessing for the program requirements are done.
    # Now its time to run.

############################################## Auto Program Works Now ##########################################################

    print('\nAll Scores, Schedules, Plans are saved Successfully.\n\nTime to go...\n') #Progress Report
    #format printing.
    #-----------------------
    #|Days Over: Day_COUNT1|
    #|Days Left: days_left1|
    #-----------------------
    print('\t\t-----------------') #format printing
    
    print('\t\t|Days Over: ',DAY_COUNT1,'|') #printing the days over
    
    print('\t\t|Days Left: ',days_left1,'|')#printing the days remaining
    
    print('\t\t-----------------')#format printing
    
    try:    
        #index111 --> Task 1
        index111 = '\n\n\n\t\t\t\t\t\tTODAY:{}\n\n\n\t\t\t\t\t\t\t\t M.I.T: {}\n\t\t\t\t\t\t\t\t Plan Time has Started (Only 1440)\n\n\n\n\nMinutes Over Today:\tTotal Time Left:\tMinutes left for today:       Total % Minutes Over:     Total % Minutes Left:\t    Task Countdown:'.format(theme,Plan[plan[0]])#init format output    
        #index112 --> Task 2
        index112 = '\n\n\n\t\t\t\t\t\tTODAY:{}\n\n\n\t\t\t\t\t\t\t\t M.I.T: {}\n\t\t\t\t\t\t\t\t Plan Time has Started (Only 1440)\n\n\n\n\nMinutes Over Today:\tTotal Time Left:\tMinutes left for today:       Total % Minutes Over:     Total % Minutes Left:\t    Task Countdown:'.format(theme,Plan[plan[1]]) #init format output
    except:    
        pass
    #index --> No Task is Scheduled.
    index = '\n\n\n\t\t\t\t\t\tTODAY:{}\n\n\n\t\t\t\t\t\t\t\t M.I.T: No M.I.T\n\t\t\t\t\t\t\t\t Plan Time has Started (Only 1440)\n\n\n\n\nMinutes Over Today:\tTotal Time Left:\tMinutes left for today:        Total % Minutes Over:     Total % Minutes Left:\t    Task Countdown:'.format(theme)#init format output
    
    try:#try
    #prints for the first task
        print(index111) #printing the output
    #if error rose during this process.
    except:
    #prints default print index form
        print(index)    
    try:
        #Total Days Completed, hours_completed, minutes completed, seconds completed till now
        day_counting,hours_counting,minutes_counting, secs_counting = int(str(sce.split(' ')[0])) * 24 * 60 * 60, int(sce.split(',')[1].split(':')[0]) * 60 * 60 ,int(str(sce.split(',')[1]).split(':')[1]) * 60,int(str(sce.split(',')[1]).split(':')[2].split('.')[0])    
    except:
        #Total Days Completed, hours_completed, minutes completed, seconds completed till now
        day_counting,hours_counting,minutes_counting,secs_counting = 0,int(str(sce.split(',')[0].split(':')[0])) * 60 * 60,int(str(sce.split(',')[0]).split(':')[1]) * 60,int(str(sce.split(',')[0]).split(':')[2].split('.')[0])
    # secs = days couting in seconds + total hours completed in seconds + total miutes completed in seconds + total seconds completed
    secs = day_counting + hours_counting + minutes_counting + secs_counting# convert it to seconds ( data preprocessing) #current seconds output
    #only today seconds completed
    todaysecs = int(str(datetime.datetime.now()).split(' ')[1].split(':')[0]) * 60 * 60 + int(str(datetime.datetime.now()).split(' ')[1].split(':')[1]) * 60 + int(str(datetime.datetime.now()).split(' ')[1].split(':')[2].split('.')[0])
    exact_secs = secs # Difference between total plan seconds to current seconds(for time format printing)
    #task boolean value initialization for task movement.    
    t1,t2,t3,t1,t2,t3,t4,t5,count = 0,0,0,True,True,True,True,True,0#inits

##################################### exact_secs time loop running starts ########################################################
#This Program actually executes the time loop that helps in counting down, current time displaying, total minutes remaining
#Percentge of total minuntes left and percentage of total minutes over and all.
#Remainder Clocks, Task Completion Notifications and its Operations.
#ExcelImport Program, that actually helps in every day COVID data that spreads around the world.
#AutoTermination Program is enabled that helps autoterminate the loop but only on exact time.
    while exact_secs: #While check
    #exact_secs is enabled with the total count as total seconds left for the entire time period.
        if count1 != 0 and count2 !=0 and count3 != 0:
    #if the total days over = 0, then this loop not begins as it reaches to ZeroDivisionError.
            SCORE1 = round(CHECK_STAGE1 / count1,3) #Learning Performance Score inits 1
    #learning performances of each task is divided by total no of days over, this helps in asses the performance of the program.
            SCORE2 = round(CHECK_STAGE2 / count2,3) #Learning Performance Score inits 2
            SCORE3 = round(CHECK_STAGE3 / count3,3) #Learning Performance Score inits 3
        else:# if the Days over =0
        #All the predefined errors shows there is no mean value calculation.
            SCORE1,SCORE2,SCORE3 = 'SCORES HAVE NOT UPDATED YET','SCORES HAVE NOT UPDATED YET', 'SCORES HAVE NOT UPDATED YET'
    #process_input = Total Days Left  - Total Days Over.
        process_input = str(datetime.datetime(end_year,end_month,end_date,end_hours,end_minutess,end_seconds) - datetime.datetime.now()) #days b/w planned date to current date
    #Total Minutes = Total Minutes Left - Total Minutes Over
    #now_mins =  Total Seconds left in seconds is converted into minutes.
        total_mins,now_mins = ((datetime.datetime(end_year,end_month,end_date,end_hours,end_minutess,end_seconds) - datetime.datetime(start_year,start_month,start_date,start_hours,start_minutes,start_seconds)).days + 1) * 24 * 60, exact_secs/60 #total's time in minutes
    #percentage minutes over = ((Total Minutes - Total Minutes Remaining) / Total Minutes Left ) * 100
        perce_mins_over = ((total_mins - now_mins) / total_mins) * 100 #Current Minutes/Total planned minutes * 100
    #total percentage minutes left = 100 - total percentage minutes over.
        total_percent_mins_left = 100 - perce_mins_over  #100 - Total Percentage minutes left
    #total minutes over = current hours in minutes + current minutes.  
        today_mins_over = int(str(datetime.datetime.now())[11:13]) * 60 + int(str(datetime.datetime.now())[14:16]) #todays minutes over
    #today mins left = total minutes in a day (1440) - today minutes over.
        today_mins_left = 1440 - today_mins_over #todays minutes left
    #second_Set = 59 - Current seconds. (helps in counting down the time)
        second_Set = 59 - int(str(datetime.datetime.now().strftime("%S")))
    #if the length of the second is = 1, 
    #convert the value from int to string.
    #then, add 0 to the prefix. 
        if len(str(second_Set)) == 1:
            second_Set = '0' + str(second_Set)
        else:
            pass
    
    #logical value to update the value to minutes and seconds is using divmod --> division value, modulus value.
    #This division value is a value of minutes.
    #modulus value is seconds count after the operation with 60.
        mins, secs = divmod(exact_secs, 60) #logic for printing the time
    #timeformat is a value that needs to print the in the output section.
        timeformat = '{:02d}:{:02d}'.format(mins,int(str(int(second_Set)- 1).replace('-1','59'))) #format printing
    #task countdown for each task by subtracting with today mins over.       
        count_task1,count_task2 = task1 - today_mins_over,task2 - today_mins_over #user_choice task 1 in minutes
    #current task countdown format print in the output section.
        current_task = '{:02d}:{}'.format(count_task1,int(str(int(second_Set)- 1).replace('-1','59'))) #default inits
    #hours, minutes logical operation to get the time for the current task ant it is countdown.
        hrs1,mins1 = divmod(today_mins_over,60)#Current Time Logic
    #secs2 is get the total secs from the countdown list is to set to go up.
        secs2 = 59-secs #for counting to go up rather than down...
    #timformat1 is to get the time of current time.
        timeformat1 = '{:02d}:{:02d}{}'.format(hrs1, mins1,datetime.datetime.now().strftime(":%S"))#Current Logic Time Format
    #timeformat2 is to get the time for total time left in a day.
        timeformat2 = '{:02d}:{:02d}:{:02d}'.format(23 - hrs1, 59 - mins1,int(str(int(second_Set)- 1).replace('-1','59')))#Current Logic Time Format
    #current_Secs _count is the secs of the total time running now.
        current_secs_count = hrs1 * 60 * 60 + mins1 * 60 + secs2
    #count task1  loop is to check the current task running by time. 
        if count_task1 < 0 and stupid == False: #check for the current task running
            second_Set = int(second_Set) - 1
            if len(str(second_Set)) == 1:
                second_Set = '0' + str(second_Set)
            else:
                pass
        #if the current task is running then the format to print in the output section is calculated in current_task.
            current_task ='{}:{}'.format(str(count_task2-1).replace('-',''),str(second_Set).replace('-1','59')) # inits if true
        #count parameter for the count of current task
            count = 2 #set to second task
        #status1 is to help the program to run only once into this loop.
            status1 = True
        #if count_task2 < 0, it  will check the loop with whether it entering into this loop for the first time or not.
        #the verification of the first time check can be made by boolean value.
        elif count_task1 > 0 and stupid == False: #check for the current task running
            second_Set = int(second_Set) - 1
            if len(str(second_Set)) == 1:
                second_Set = '0' + str(second_Set)
            else:
                pass
        #if the curr
            current_task = '{}:{}'.format(count_task1-1,str(second_Set).replace('-1','59')) # inits if true
            #the count parameter sets the task value to show at 1
            count  = 1 #set to first task
            #this boolean expression helps the value to false by setting the value to false for furthur movement.
            status1 = False
        #if the stupid boolean sets to true, which means there are no tasks to set a timer.
        elif stupid == True: #No Task
            #then the count parameter sets to 0 task.
            count = 0 #No Task,Task = 0
            #current task count down as 'No Task'
            current_task = 'No Task' #No Time Prints    
        else:
            pass #pass

################################## This is the Main Print where all the operations that are happened can be Seen. ###################################################################################
        #template format printing to the user side.
        print(' ',today_mins_over,'(',timeformat1,')','  ', timeformat,'( Hrs:',int(mins/60),')       ',today_mins_left,'(',timeformat2,')\t\t    ',str(round(perce_mins_over,2)),'%\t\t      ',str(round(total_percent_mins_left,2)),'%           ',current_task,'( task:',count,')', end = '\r')

################################## Main Print Option End. This print displays for every second by replacing the old outputs. ########################################################################

        time.sleep(1) #wait for the next loop by 1 second.
#waits for a second to move to another loop.

        #setting the value by minus 1 for the next loop.
        #This helps in updating the values and loop entering if any remainders and alerts arose.
        exact_secs -= 1

        for i in range(count56): #Remainder count loop.
            if timerun[i] * 60 == current_secs_count: #Remainder list in minutes.so, each value is multiplied by 60 to match the current_secs_count
            #after converting to seconds. its time to check the current time with remainder time. enters if both times match result is true.
                #new window display initiation.
                root = tk.Tk() #initiating for tkinter
                #title of the new remainder. 
                root.title('Remainder')
                #format or the text that need to print in the window when opened.
                formattype = "Time: {}\nRemainder: {}\nDescription: {}".format(timeformat1,remainder[i],describe[i])
                #labelling on the window with position and height of the window that should be displayed.
                tk.Label(root, text = formattype,height = 1000,width = 1000,bg = 'white').pack()
                #when the time comes, remainder notification aroses with window from the mainloop function.
                root.mainloop()
                #Remainder and its Description will give output in the terminal side.
                print('\n\n\tRemainder:',remainder[i])
                print('\tDescription: ',describe[i])

                #tries the index112 (task2 clock)
                try:
                    print('\n\n\n',index112)
                #if error occured, index111 (task1 clock)
                except:
                    try:
                        print('\n\n\n',index111)
                    #if this error also occurs, then index (defualt time clock).
                    except:
                        print('\n\n\n',index)
            #if noting else found, it escapes the loop (which means there is a error in program.)
            else:
                pass
            #t6 boolean form helps the program enters the loop only once.
            t6 = True
        #if the time in new_reminder and it enters only if it enter the list
        for i in range(len(new_remminder)):  
        #Reminder loop for the total one and hald reminders.
            if current_secs_count == new_remminder[i] * 60:
            #if any of the reminder matches with the current_secs_count.
            #then a new window will open
                root = tk.Tk()
                #tkinter initiation.
                root.title('Remainder')
                #format type for the printing the text on the new window.
                formattype = 'Time: {}\nRemainder: {}\nDescription: {}'.format(timeformat1,'Refresh for 5 Mins','Have Something or Drink Some Water.')
                #labelling on the window, height and width positioning and also setting backgroud to white.
                tk.Label(root,text = formattype,height = 1000,width = 1000,bg = 'white').pack()
                #initiates the code to run when the loop sets true.
                root.mainloop()
                #printing teh value of status in the terminal.
                print('\n\n\n\n\n\n\n\n\t\t\tRemainder: Refresh for 5 mins')
                #description of what reminder could be...
                print('\t\t\tDescription: Have Something or Drink Some Water.')
                #telling when the next reminder could be...
                print('\t\t\tNext Refresh Remainder - ',final_remainder1[i+1])
                if count == 1:
                    print('\n\n\n',index111)
                elif count == 2:
                    print('\n\n\n',index112)
                #if stupid == True:
                else:
                    print('\n\n\n',index)


        if today_mins_over == time_final: #checks if the termination time of program reaches or not..
           
            print('\nyour Progress Rate for TASK: {}: {}/5'.format(task_name1,SCORE1)) #Learning Performance Output Score 1 (Task 1)

            print('your Progress Rate for TASK: {} : {}/5'.format(task_name2,SCORE2)) #Learning Performance Output Score 2 (Task 2)

            print('your Progress Rate for TASK: {}: {}/5'.format(task_name3,SCORE3)) #Learning Performance Output Score 3 (Task 3)

            
            if today_mins_over > task2:# If loop is moved into the termination clock , asks user to end time or continue the program.

                end_ask = input('All Tasks are Over.\nDo you want to end the program (y/n): ')

                
                if end_ask in dw: #if user agrees to end the program

                    exact_secs = 0 #logic to end the program. So, Loop exits.
                    if check_hrs < 12: #if it is Morning Hours
                        wishes1 = 'Good Morning'
                    elif check_hrs < 16 and check_hrs >= 12: #if it is in Afternoon Hours
                        wishes1 = 'Good Afternoon'
                    elif check_hrs >= 16: #if it is in Evening Hours
                        wishes1 = 'Good Evening'
                    elif check_hrs >= 19: #if it is night hours
                        wishes1 = 'Good Night'
                    print('{}, {}'.format(wishes1,username))
                
                else: #if user disagrees to end the program, runs

                    time_final = 0

                    print(index)

                    pass

        else:

            pass

        if today_mins_over == task1/2 and t1 == True: #if total task 1 time is finished by half

            print('\n\n\n\tPre-Remainder: One Half Time for your first Task is Over, Task must be Completed On Time.!') #outputs the remainder

            t1 = False #to not let into come into this loop again after a second

            try:

                print('\n\n',index111) #time format outputs

            except:

                pass

        elif today_mins_over == task1 and t2 == True: #if task1 time is over

            try:

                print('\n\n\n\tRemainder: First Task is Over, Task Completed On Time.!------------>M I T:{}'.format(Plan[plan[0]])) #Remainder Output for task1 complete

            except:

                pass

            plan1 = plan[0] #task1 is set to plan1

            root = tk.Tk()

            root.title('Alert Message')

            formattype = 'Time: {}\nRemainder: {}\nDescription: {}'.format(timeformat1,'First Task Over','Please Update your Scores.')

            tk.Label(root,text = formattype,height = 1000,width = 1000,bg = 'white').pack()

            root.mainloop()

            print('\n\n\n\n\n\n\n\n\t\t\tRemainder:First Task is Over, Task Completed On Time.!------------>M I T:{}'.format(Plan[plan[0]]))

            print('\t\t\tDescription: Please Update the Scores')

            UpdatedScore(plan1) #prints the updated score for plan1


            t2 = False #to not let into come into this loop again after a second

            try:

                print('\n\n',index112) #time format outputs

            except:

                pass

        elif today_mins_over == task2_half and t1 == True: #checks if total task2 time is finished by half

            print('\n\n\n\tPre-Remainder: One Half Time for your second M I T is Over, Task must be Completed On Time.!') #outputs the remainder

            t1 = False #to not let into come into this loop again after a second

            try:

                print('\n\n',index112) #time format outputs

            except:

                pass

        elif today_mins_over == task2  and t3 == True:#if task2 time is over

            try:

                print('\n\n\n\tRemainder: Second Task is Over,Task Competed on Time------------>Task Name:{}'.format(Plan[plan[1]])) #Remainder Output for task1 complete

            except:

                pass

            t3 = False  #to not let into come into this loop again after a second

            stupid = True

            plan2 = plan[-1] #task1 is set to plan2

            root = tk.Tk()

            root.title('Alert Message')

            formattype = 'Time: {}\nRemainder: {}\nDescription: {}'.format(timeformat1,'Second Task Over','Please Update your Scores.')

            tk.Label(root,text = formattype,height = 1000,width = 1000,bg = 'white').pack()

            root.mainloop()

            print('\n\n\n\n\n\n\n\n\t\t\tRemainder:Second Task is Over, Task Completed On Time.!------------>M I T:{}'.format(Plan[plan[1]]))

            print('\t\t\tDescription: Please Update the Scores')

            UpdatedScore(plan2) #prints the updated score for plan1

            print('\n\n',index)#time format outputs

            tasks_over = True

        # elif today_mins_over >= task3 and t10 == True:

        #     print('\n\nAuto Excel import Program is initiating...')

        #     AutoCOVIDingExcel()

        #     print('COVID-19 Excel Import Request Initiated and it is Running Successfully in the BackGround.')

        #     t10 = False

        #     print('\n\n',index)

        else:#if not

            pass #pass

    print('Done(Time is Over)!!!') #final Output as Time is Over 

    ############################################### Actual Program Done ###############################################

elif username == 'Keshav' and password == 'AdminPranalikaa':

    import pickle,getpass,time

    print('Password: Correct\nLogin Status: Success\n\n\n\t\t\t\t\t\t\t\t{} {}'.format(wishes, username))

    print('\n\n\n\n\n\n\t\t\t\t\t\t\tWelcome to Day Plan Admin Block\t\t\t\t{}\n\n\n'.format(Date_Current.strftime("%b %d %Y - %A - %H:%M:%S")))

    time.sleep(2.5)

    """

    this is a Admin Block to give access to Date Modifications, Task Scores, Task Names.

    This Helps Users, Not to Enter the Program Manually.

    """

    try: #check side

        f = open(user_choice) #open file

        [count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3,task_name1,task_name2,task_name3,start_year,start_month,start_date,end_year,end_month,end_date] = load('user_choice') #load into a variable

        final_count = [count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3,task_name1,task_name2,task_name3,start_year,start_month,start_date, end_year,end_month,end_date]# set it to final_count

        index2 = '\n{} STATUS SCORE -->{}.\n{} STATUS SCORE -->{}.\n{} STATUS SCORE -->{}.\n\nRate of Learning {} Score is-->{}.\nRate of {} Completion Score is-->{}.\nRate of {} Score is -->{}'.format(task_name1,load(final_count)[0],task_name2,load()[1],task_name3,load('user_choice')[2],task_name1,load(final_count)[3],task_name2,load(final_count)[4],task_name3,load(final_count)[5]) #Score Loading

        print('Status: Connected to Encryped File.you can work here.')

    except IOError:

        print("File not Exist\nCreating File...") #Outputting the Failed Execution Reason

        [count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3,task_name1,task_name2,task_name3,start_year,start_month,start_date,end_year,end_month,end_date] = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 #load into a variable

        final_count = [count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3,task_name1,task_name2,task_name3,start_year,start_month,start_date,end_year,end_month,end_date]

        f = save(final_count) #saving the value

        index2 = '\n{} STATUS SCORE -->{}.\n{} STATUS SCORE -->{}.\n{} STATUS SCORE -->{}.\n\nRate of Learning {} Score is-->{}.\nRate of {} Completion Score is-->{}.\nRate of {} Score is -->{}'.format(task_name1,load(final_count)[0],task_name2,load()[1],task_name3,load('user_choice')[2],task_name1,load(final_count)[3],task_name2,load(final_count)[4],task_name3,load(final_count)[5]) #Score Loading

        print('count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3 are newly Assigned\nNew File(user_choice) Created,Values are',final_count) #printing the progress

    finally: #finally statement (Default Print)

        f = open(user_choice) #opens the file

        print('\n\nAvailable Scores are:\n',index2,'\nAll Required Inputs are Retrieved and alloted to its Respective Variables.')

        f.close() #closing the file

        print('Closed...',end = '') #printing the progress
        time.sleep(1.5)

        print('Ok\n\n\n\n\nOperation Access : Running')   

    task_name1 = 'Data Science(SAS)'

    task_name2 = 'Read Audio Book / Physical Book Library'

    task_name3 = 'Java Script Learning'

    [count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3,task_name1,task_name2,task_name3,start_year,start_month,start_date,end_year,end_month,end_date] = load('user_choice') #load into a variable

    print('\nDates are \n\n\tStart Date: {}/{}/{}\n\tEnd Date: {}/{}/{}\n\n\n'.format(start_date,start_month,start_year, end_date, end_month, end_year))

    print('\n\n1. Task1 count:',count1,'\n2. Task2 count:',count2,'\n3. Task3 count:',count3,'\n4. Satisfaction Value for Task1: ',CHECK_STAGE1,'\n5. Satisfaction Value for Task2:',CHECK_STAGE2,'\n6. Satisfaction Value for Task3: ',CHECK_STAGE3)

    req = int(input('Choose from the above Options: '))

    print('Remember: if you wanna add, input the value with +1 or subtract,input the value with -1')

    change = float(input('How much you wanna Update: '))

    if req == 1:

        count1 = round(count1 + change,3)

    elif req == 2:

        count2 = round(count2 + change,3)

    elif req == 3:

        count3 = round(count3 + change,3)

    elif req == 4:

        CHECK_STAGE1 = round(CHECK_STAGE1 + change,3)

    elif req == 5:

        CHECK_STAGE2 = round(CHECK_STAGE2 + change,3)

    elif req == 6:

        CHECK_STAGE3 = round(CHECK_STAGE3 + change,3)

    else:

        print('Wrong Input')

    final_count = [count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3,task_name1, task_name2, task_name3, start_year,start_month,start_date,end_year,end_month,end_date] # adding the updated values to final_count variable

    save(final_count) #saves with updated file 

    print('Updated')

    print('\n\n\nStart Date: {}/{}/{}\nEnd Date: {}/{}/{}\n\n\n'.format(start_date,start_month,start_year, end_date, end_month, end_year))


    print('1. Task - 1 Name : {}\n2. Task - 2 Name : {}\n3. Task - 3 Name : {}\n\n4. Start Date: {}/{}/{}\n5. End Date: {}/{}/{}'.format(task_name1,task_name2,task_name3,start_date,start_month,start_year,end_date,end_month,end_year))

    check_ask = input('Do you want to update any of the existing data above(y/n): ').lower()

    while check_ask in dw:

        print('Available options are:\n\n1. Task - 1 Name : {}\n2. Task - 2 Name : {}\n3. Task - 3 Name : {}\n\n4. Start Date: {}/{}/{}\n5. End Date: {}/{}/{}'.format(task_name1,task_name2,task_name3,start_date,start_month,start_year,end_date,end_month,end_year))

        update_ask = input('Choose from Above: ')

        if update_ask == '1':

            task_name1 = input('Enter the Task - 1 Name: ')

        elif update_ask == '2':

            task_name2 = input('Enter the Task - 2 Name: ')

        elif update_ask == '3':

            task_name3 = input('Enter the Task - 3 Name: ')

        elif update_ask == '4':

            date1 = input('Enter the Start Date: (\'DD/MM/YYYY\'): ')

            start_date = int(date1.split('/')[0])

            start_month = int(date1.split('/')[1])

            start_year = int(date1.split('/')[2])

        elif update_ask == '5':

            date = input('Enter the End Date: (\'DD/MM/YYYY\'): ')

            end_date = int(date.split('/')[0])

            end_month = int(date.split('/')[1])

            end_year = int(date.split('/')[2])

        else:

            print('\nwrong input')

            pass

        check_ask = input('Do you want to update any other existing data(y/n): ').lower()

        final_count = [count1,count2,count3,CHECK_STAGE1,CHECK_STAGE2,CHECK_STAGE3,task_name1, task_name2, task_name3, start_year,start_month,start_date,end_year,end_month,end_date] # adding the updated values to final_count variable

        save(final_count) #saves with updated file 

        print('Saved\n\n\n')

        print(len(final_count),' variables are saved\n\n')

        f.close()

        print('Saved Values/Scores are:\n\t{}:{}\n\t{}:{}\n\t{}:{}\n\tSum of Scores of {}:{}\n\tSum of Scores of {}:{}\n\tSum of Scores of {}:{}'.format(task_name1,count1,task_name2,count2,task_name3,count3,task_name1,CHECK_STAGE1,task_name2,CHECK_STAGE2,task_name3,CHECK_STAGE3))

        print('\nSaved Dates are \n\n\tStart Date: {}/{}/{}\n\tEnd Date: {}/{}/{}\n\n\n'.format(start_date,start_month,start_year, end_date, end_month, end_year))

        print('Connection Disconnected')

    print('Operation Access: Disconnected')

else:

    print('Password: Incorrect\nLogin Status: Failed\n\n')