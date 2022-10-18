import pygame
from sys import exit
from random import randint

def summ(x):
    accum = 0
    for valuu in x.values(): #summmmmm
        accum += int(valuu)
    return(accum)

def clicked(button): #checks to see if click happens inside location of button
    if button[0] <= mouse[0] <= button[0]+button[2] and button[1] <= mouse[1] <= button[1]+button[3]:
        return True
    else:
        return False

pygame.init()
active = True
screen = pygame.display.set_mode((870,640))
pygame.display.set_caption("Op calculator")
clock = pygame.time.Clock()
width = screen.get_width()
height = screen.get_height()
font1 = pygame.font.SysFont('Arial',35)
font2 = pygame.font.SysFont('Arial',15)
text = font1.render('calculate' , True , "black")

#"boxes", <name>b means its a button
calcb = [700,420,150,50] # location in x, location in y, size in x, size in y
outputbackground = [10,10,850,500]
opback = [10,520,850,75]

#"global variables"
gsubjects = []

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            exit()

    #checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if clicked(calcb):
                if active == False:
                    break
                active = False
                with open("op.txt", 'r') as wl: #
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
                
                    subjects2 = []
                    subnpoints = {}

                    print(subjects)
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
                    for subject, point in subnpoints.items():
                        print("{}: {} opintopisteitä".format(subject, point))
                        gsubjects.append("{}: {} opintopisteitä".format(subject, point))

                    print("_______________________")
                    print("You have a total of: ",summ(subnpoints),'"opintopisteitä"')
                    total = font1.render(f"Sinulla on: {summ(subnpoints)} opintopisteitä",True,"DarkTurquoise")
                    
    screen.fill((95,130,162))
    pygame.draw.rect(screen,"aliceblue",outputbackground)
    pygame.draw.rect(screen,"aquamarine",opback)
    credits = font2.render("OP calc v1.1, made by Rui", True, "Black")
    screen.blit(credits,(10, height-30))

    if active == True:
        msg = ["welcome! / tervetuloa!",
        "en:",
        "remember to paste the wilma-data into op.txt, which is read automatically by this program.",
        "(the op.txt file must be in the same folder as this program.)",
        "fi:",
        "muista liittää wilman kurssitarjoittimen datan op.txt:n sisälle, ohjelma lukee sen automaattisesti.",
        "(op.txt tiedosto on oltava samassa kansiossa kuin tämä ohjelma."]

        why = 20
        for line in msg: #i hate pygame
            message = pygame.font.SysFont('Arial',20).render(line,True,"Black")
            screen.blit(message,(15,why))
            why += 24

        mouse = pygame.mouse.get_pos()
    
        button = pygame.draw.rect(screen,"white",calcb) 
        pygame.draw.rect(screen,"orange",calcb, width=2)
      
        screen.blit(text, (calcb[0]+17,calcb[1]+4))

        # updates the frames of the game
        pygame.display.update()
        clock.tick(60)

    if active == False:
        pygame.draw.rect(screen,"azure1",opback)
        pygame.draw.rect(screen,"aquamarine",opback, width=5)
        blt = font2.render('below, are your subjects and OP seperated by a " : "',True,"black")
        blt2 = font2.render('alhaallasi on opinnot ja opintopisteet erotettu " : " lla',True,"black")
        screen.blit(blt,(20,20))
        screen.blit(blt2,(20,37))

        pygame.draw.rect(screen,(95,130,162),[10,60,850,3])

        y = 66
        y2 = 66
        for subject in gsubjects:
            if y > outputbackground[3]-20:
                screen.blit(font2.render(subject,True,"black"),(250,y2))
                y2 += 16
            else:
                screen.blit(font2.render(subject,True,"black"),(20,y))
                y += 16

        screen.blit(total,(20,opback[1]+10))
        screen.blit(font2.render("You have: "+str(len(gsubjects))+" subjects.",True,"black"),(720,480))
        pygame.display.update()
        clock.tick(60)
        
        
        
        
