from time import sleep

def summ(x):
    accum = 0
    for valuu in x.values(): #this function is meant for future expansion, but only used once currently.
        accum += int(valuu)
    return(accum)

banner = r"""
 ________  ________        ________  ________  ___       ________         
|\   __  \|\   __  \      |\   ____\|\   __  \|\  \     |\   ____\        
\ \  \|\  \ \  \|\  \     \ \  \___|\ \  \|\  \ \  \    \ \  \___|        
 \ \  \\\  \ \   ____\     \ \  \    \ \   __  \ \  \    \ \  \           
  \ \  \\\  \ \  \___|      \ \  \____\ \  \ \  \ \  \____\ \  \____  ___ 
   \ \_______\ \__\          \ \_______\ \__\ \__\ \_______\ \_______\\__\
    \|_______|\|__|           \|_______|\|__|\|__|\|_______|\|_______\|__|
"""

print(banner)
print("Welcome to opintopiste calculator!")
print("_______________________________________________________________________\n")

print("WARNING: please make sure that the data file is in the same folder as this program.")
print(
"""Please make sure that in VScode you select the right folder containing the datafile and program.\n
To select a folder, navigate to the upper left icon, hover over the icons and find explorer,
there you can choose the folder containing this program and the datafile.\n """)

debugging = input('do you wish to turn on debugging mode? for normal use please select "n" and press enter. y/n: ')
if debugging != "y":
    if debugging != "n":
        print("debugging input is wrong, quitting...")
        sleep(3) #i want to emphasize the misinput so ill add a small delay
        quit()


thefile = input("please write the filename containing your subjects and points\nwith file extension(.txt) and press enter: ")

with open(thefile, 'r') as wl:
    data = wl.readlines()
    dataf = []                  # this function opens up the file, splits the table and puts every 
    for subject in data:        # object into a list.
        subject = subject[:-2]
        dataf.append(subject.split("\t"))

    subjects = []

    for sub in dataf:
        if sub[0][3:8] == "jakso":
            sub = sub[3]
            print("found 'jakso' header in this subject: ",sub)
            subjects.append(sub)
        else:
            third = sub[2]
            subjects.append(third)
        
    if debugging == "y":
        print("these are the subjects that will be calculated:")
        print(subjects)

    subjects2 = []
    subnpoints = {}

    print("Calculating..........\n")

    # the line below will check to see if the subject has a special character, 
    # and then add a key value pair of "subject: op".
    # if the subject already exists in the dictionary as a special op amount,
    # it will override and nothing will happen. - thus disregarded.
    # however if it already exists in the dictionary as a normal subject
    # with op set to 2, it will run line 42, - thus disregarded.
    # if its completely new, it will set op to 2. - thus setting it as default value.

    for sub in subjects:
        if sub[-1] == ")":
            sub2 = sub[:-6]
            num = sub[-5:]
            point = num[1]
            if sub2 in subnpoints:
                print("CUSTOM SUB: "+sub+" HAS ALREADY BEEN ACCOUNTED FOR")
                subnpoints[sub2] = point
            else:
                subnpoints[sub2] = point

        else:
            if sub in subnpoints:
                print("hey, wait a minute, "+sub+" is already accounted for")
        
            else:
                subnpoints[sub] = 2

    print("below, are your subjects and OP seperated by a ':'.")
    if debugging == "y":
        print(subnpoints)

    for subject, point in subnpoints.items():
        print("{}: {} opintopisteitä".format(subject, point))

    print("_______________________")
    print("You have a total of: ",summ(subnpoints),'"opintopisteitä"')
