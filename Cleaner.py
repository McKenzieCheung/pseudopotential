# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 00:11:43 2016

@author: McKenzie Cheung
"""

#Pseudopotential robot - Initialization of the robot
#Accepts no values - Main initialized function
def Pseudos():
    #Input ...
    #Initialization of the pseudos_data dictionary - It splits the user-inputted file at the "=" and it separates the information into key words (pseudos_data[key]) and their respective values
    pseudos_data = {}
    #elvalue = {}
    #elname = {}
    print("Hello, welcome to the Pseudo Potential generator.") 
    #User-inputted file - The file contains: Radii values for (S,P,D,(F?) ), the # of steps between each radius, the psueod_type, nlcc value, atom type, atomic coniguration, and dft value
    #User specifies the atom type, the atomic configuration, and the dft value especially
    userresponse = input('Do you have a file you could load in?: ')
    if userresponse is None:
        print('Please respond to the question.')
    elif userresponse == "Yes" or userresponse == "yes": 
      #This section below works to import and print a simple text file -- Imports the user-inputted file and opens it so it can be read
       userfile = input('Enter filename with .txt extension: ') 
       username = input('Enter your preferred username: ')
       print('\n')
       f1 = open(userfile,'r') 
       #This portion splits the file at the "=" and stores each piece into the pseudos_data dictionary
       #Each respective value can be called by the keyword - ie. pseudos_data['atom']
       for line in f1: 
           if "=" in line:
               newsplit1 = line.split("=") 
               #newsplit1 = line.split("=")
               #elname = newsplit1[0].strip()
               #elvalue = newsplit1[1].strip()
               #print(elname)
               #print(elvalue)
               #print(newsplit1[0].strip())
               #print(newsplit1[1].strip())
               pseudos_data[newsplit1[0].strip()] = newsplit1[1].strip() 
       
       #print(sorted(pseudos_data))
       
       #This for loop just reiterates the important user-specified values (Atom, Config, DFT value)
       for key in sorted(pseudos_data):
           if pseudos_data[key] == pseudos_data['atom']:
               print('The type of atom is:', pseudos_data['atom'])
               print('\n')
           elif pseudos_data[key] == pseudos_data['config']:
               print('The electron configuration is:', pseudos_data['config'])
               print('\n')
           elif pseudos_data[key] == pseudos_data['dft']:
               print('The density functional theory value is:', pseudos_data['dft'])  
               print('\n') 

    #This for loop loops through all the radii - Starts from the minimum value and works it up to the maximum value 
    #No way of actually knowing the right values - If a user begins to input a file, will use the covalent radii
    #WORKING - "for loop" to loop through the parameters - The radius size of the different orbitals being tested
    #Changed - my_data to pseudos_data
    s_delta = (float(pseudos_data['r_s_max']) - float(pseudos_data['r_s_min']))/(float(pseudos_data['r_s_steps']))
    #for i in range(0, int(my_data['r_s_steps'])):
    #if float(my_data['r_p_max']) >= float(my_data['r_p_min']):
    for i in range(0, int(pseudos_data['r_s_steps'])+1): 
        #if float(my_data['r_s_max']) < float(my_data['r_s_min']): 
        r_s = float(pseudos_data['r_s_min']) + s_delta * i 
        #print('The radius of the s-orbital is:',r_s)  
        #print("\n")
        p_delta = (float(pseudos_data['r_p_max']) - float(pseudos_data['r_p_min']))/(float(pseudos_data['r_p_steps'])) 
            #if float(my_data['r_p_max']) < float(my_data['r_p_min']):
        for i in range(0, int(pseudos_data['r_p_steps'])+1): 
            #if float(my_data['r_p_max']) >= float(my_data['r_p_min']):
            r_p = float(pseudos_data['r_p_min']) + p_delta * i 
            #print('The radius of the p-orbital is:',r_p)
            #print("\n")
            d_delta = (float(pseudos_data['r_d_max']) - float(pseudos_data['r_d_min']))/(float(pseudos_data['r_d_steps']))
                #if float(my_data['r_d_max']) < float(my_data['r_d_min']):
            for i in range(0, int(pseudos_data['r_d_steps'])+1):
                #if float(my_data['r_d_max']) >= float(my_data['r_d_min']):
                r_d = float(pseudos_data['r_d_min']) + d_delta * i 
                #print('The radius of the d-orbital is:',r_d) 
                #print("\n")  
    
    #writer(userfile, configlist, **pseudos_data)        
    parser(userfile, username, **pseudos_data) 

#This subfunction takes the input file and separatess and parses the line that contains the atomic configuration
#Accepts two values -- userfile and pseudos_data initiallized in Pseudos()
def parser(userfile, username, **pseudos_data): 
    configlist = []  
    #configlist = {} 
    #print(type(configlist)) 
    f1 = open(userfile,'r') 
    #Takes the atomic configuration and numbers the orbitals (second column in the displayed channels)
    for line in f1: 
        if pseudos_data['config'] in line: 
            configlist = pseudos_data['config'].split() 
            #print(pseudos_data['config'].split()) 
            #print(configlist[0].strip("'"))
            #print(configlist[1].strip("'"))
            j = 0
            for i in configlist: 
                configlist[j] = i.strip("'") 
                #print(configlist[j])
                j = j+1  
                #print(configlist)
    
    #return configlist
    
    config(userfile, configlist, username, **pseudos_data)      
    
    #writer(userfile, configlist, **pseudos_data)

#This function accepts three values: userfile and pseudos_data (Taken from Pseudos()); configlist (Taken from parser())
#The purpose of this function is to create the channels for each specified orbital in the atomic configuration
#The method behind this is to index into the needed values and concatenate everything needed into one long string
#These strings are then fed into writer() where they are written in a text format to the final output file
def config(userfile, configlist, username, **pseudos_data): 
    emptyString1 = '' 
    emptyString2 = ''
    emptyString3 = ''
    #emptyString4 = '' #For "f" orbital
    #emptyList = []  
    emptyList1 = []
    emptyList2 = []
    emptyList3 = []
    #emptyList4 = []

#    tempelement = configlist[0] 
#    #print(configlist)
#    configlist = list(configlist)
#    configlist.pop(0) 
#    print(configlist)
    
    #if isinstance(tempelement, str) is True: 
    #print(type(configlist))
    if len(configlist[0]) >= 4:  #is 4
        print("The elemental configuration will not be used.\n")
        #print(type(configlist))
        configlist = list(configlist)
        configlist.pop(0)
        #print(configlist) 
        #print(type(configlist))
        
    count = 0
    for elem in configlist:   
        count += 1
        if elem[2] is "-":
            elem2 = elem[2]
            elem2 = elem[3]
            #print(elem2) 
        else:
            elem2 = elem[2]
            #print(elem2)
            
        if len(configlist) <= 2:
#            emptyString += elem[0] + elem[1].upper() + " " + str(count) + " " + str(int(count-1)) + " " + elem[2] + ".00"
#            print(emptyString)
#            emptyList.append(emptyString) 
#            emptyString = ''  
            if elem[1] == "s":
                 emptyString1 += elem[0] + elem[1].upper() + " " + str(count) + " " + str(int(count-1)) + " " + elem2 + ".00" + " " + "0.00" + " " + pseudos_data['r_s_max'] + " " + pseudos_data['r_s_max'] + " " + "0.0"
                 #print(emptyString1)
                 emptyList1.append(emptyString1) 
                 #emptyString1 = ''  
            elif elem[1] == "p":
                emptyString2 += elem[0] + elem[1].upper() + " " + str(count) + " " + str(int(count-1)) + " " + elem2 + ".00" + " " + "0.00" + " " + pseudos_data['r_p_max'] + " " + pseudos_data['r_p_max'] + " " + "0.0"
                #print(emptyString2)
                emptyList2.append(emptyString2) 
                #emptyString2 = ''  
            elif elem[1] == "d": 
                emptyString3 += elem[0] + elem[1].upper() + " " + str(count) + " " + str(int(count-1)) + " " + elem2 + ".00" + " " + "0.00" + " " + pseudos_data['r_d_max'] + " " + pseudos_data['r_d_max'] + " " + "0.0"
                #print(emptyString3)
                emptyList3.append(emptyString3) 
                #emptyString3 = ''  
                 
        elif len(configlist) >= 3: 
#            emptyString += elem[0] + elem[1].upper() + " " + str(count) + " " + str(int(count-1)) + " " + elem[2] + ".00"
#            print(emptyString)
#            emptyList.append(emptyString) 
#            emptyString = ''
            if elem[1] == "s": 
                emptyString1 += elem[0] + elem[1].upper() + " " + str(count) + " " + str(int(count-1)) + " " + elem2 + ".00" + " " + "0.00" + " " + pseudos_data['r_s_max'] + " " + pseudos_data['r_s_max'] + " " + "0.0"
                #print(emptyString1)
                emptyList1.append(emptyString1) 
                 #emptyString1 = ''  
            elif elem[1] == "p":
                emptyString2 += elem[0] + elem[1].upper() + " " + str(count) + " " + str(int(count-1)) + " " + elem2 + ".00" + " " + "0.00" + " " + pseudos_data['r_p_max'] + " " + pseudos_data['r_p_max'] + " " + "0.0"
                #print(emptyString2)
                emptyList2.append(emptyString2) 
                #emptyString2 = ''  
            elif elem[1] == "d":
                emptyString3 += elem[0] + elem[1].upper() + " " + str(count) + " " + str(int(count-1)) + " " + elem2 + ".00" + " " + "0.00" + " " + pseudos_data['r_d_max'] + " " + pseudos_data['r_d_max'] + " " + "0.0"
                #print(emptyString3)
                emptyList3.append(emptyString3)  
                #emptyString3 = '' 

#        if str(int(count-1)) is 0: 
# Do within the file-writing function 

# Passing the strings down to writer() - Before the writing
# if lloc in that posiiton, just pass that string by, can save it and have a boolean saying the string was passed over
# Have the file write the index of the string passed over 
# Look @ last character of the name 
# String name dependent on lloc
# Make a dictionary where lloc is the kkey and the string is the value
# Keep a dummy variable that keeps track of the strings and which one was skipped over

    writer(userfile, configlist, emptyString1, emptyString2, emptyString3, count, username, **pseudos_data)
                
#Takes many values...
#Pseudos() - userfile, pseudos_data
#parser() - configlist
#config() - emptyString1, emptyString2, emptyString3
#this function writes all specified content to the output file that the user will then take and run through ld1
def writer(userfile, configlist, emptyString1, emptyString2, emptyString3, count, username, **pseudos_data): 
    #This is where you will write to the new file
    #Manipulate the dictionary how you want....
    print('Creating a new text file for the ld1 executable.')
    userld1 = input('Enter a file name with .txt extension: ')
    with open(userld1, "wt") as out_file:
    #Actual working section
        #&input section 
        out_file.write("&input\n")  
        out_file.write("  title=") 
        out_file.write(pseudos_data['atom'])
        out_file.write(",\n") 
        out_file.write("  dft=")
        out_file.write(pseudos_data['dft']) 
        out_file.write("\n")
        out_file.write("  zed=7.,\n")
        out_file.write("  rel=1,\n")
        out_file.write("  config=") 
        out_file.write(pseudos_data['config'])
        out_file.write("\n") 
        out_file.write("  iswitch=3,\n")  
        #out_file.write("  dft=")
        #out_file.write(pseudos_data['dft']) 
        out_file.write("  rlderiv=1.5,\n")
        out_file.write("  eminld=-4.0,\n")
        out_file.write("  emaxld=4.0,\n")
        out_file.write("  deld=0.005,\n")
        out_file.write("  nld=")
        out_file.write(str(count)) #Need to condition this - Number of unbounded channels
        out_file.write(",")
        out_file.write("\n")
        out_file.write("  verbosity='high'\n")
        out_file.write(" /\n")
        
        #&inputp section        
        out_file.write("&inputp\n") 
        out_file.write("  pseudotype=2,\n")
        
        if count is 2:
            eltitle1 = pseudos_data['atom'].strip("'")
            out_file.write("  file_pseudopw=")
            out_file.write("'")
            out_file.write(eltitle1)
            out_file.write(".pz-nc_KL111-")
            out_file.write(pseudos_data['r_p_max'])
            out_file.write("-")
            out_file.write(pseudos_data['r_s_max'])
            out_file.write(".UPF',")
            out_file.write("\n") 
        #elif count is 3:
            
#        f1 = open(userfile,'r')
#        for line in f1:
#            if pseudos_data['config']: 
#                if "1s" in line or "2s" in line: #Refine this portion with elements given by Prof.
#                    eltitle1 = pseudos_data['atom'].strip("'")
#                    out_file.write(" file_pseudopw=")
#                    out_file.write("'") 
#                    out_file.write(eltitle1)
#                    #out_file.write(".pbe-n-nc.UPF',")
#                    out_file.write(".pz-nc_KL111-")
#                    out_file.write(pseudos_data['r_s_max'])
#                    out_file.write("-")
#                    out_file.write(pseudos_data['r_s_min'])
#                    out_file.write(".UPF',")
#                    out_file.write("\n") 
#                   
#            elif pseudos_data['config']:
#                if "3d" in line or "6s" in line: #Refine this portion with elements given by Prof.
#                    eltitle2 = pseudos_data['atom'].strip("'")
#                    out_file.write(" file_pseudopw=") 
#                    out_file.write("'")
#                    out_file.write(eltitle2)
#                    out_file.write(".rel-pbe-n-nc.UPF',")
#                    out_file.write("\n")  
                 
        out_file.write("  author=")
        out_file.write("'")
        out_file.write(str(username))
        out_file.write("'")
        out_file.write(",\n")
        out_file.write("  lloc=0,\n")  
        #out_file.write("  nlcc=.true.") #If-statement this -- Seems to only be applicable for elements above a certain number of orbitals
        #out_file.write(",\n") 
        out_file.write("  tm=.true.,\n") 
        out_file.write("/\n") 
        out_file.write(str(count))
        out_file.write("\n")
        out_file.write(emptyString1) 
        out_file.write('\n')
        out_file.write(emptyString2)
        out_file.write('\n') 
        out_file.write(emptyString3)
    
    #Read a file 
    with open(userld1, "rt") as in_file:
    #with open("ld1input.txt", "rt") as in_file:
        text = in_file.read() 
   
    print(text) 

    #When you get to the config piece, make sure you call the config method....
    #It will return a list strings, that you can then write to the file by iterarting
    
Pseudos()