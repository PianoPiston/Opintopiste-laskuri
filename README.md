# Opintopiste-laskuri
wilman opintopistelaskuri, tämä ohjelma laskee opintopisteesi automaattisesti kurssitarjottimen avulla.
https://yvkoulut.inschool.fi/trays

**info**:

Tässä projektissa on kolme ohjelmaa:

opcalc.zip -  normaalin käytön ladattava tiedosto (käytä windowsilla)

opcalc-en.py -  command-line interface python ohjelma (älä lataa, paitsi jos oot linuxil tai osaat vscodia)

opcalcgui-v1.py - opcalc.zip:in source tiedosto, tätä tiedostoa muutin pyinstallerin apuna exe tiedostoon, joka on zip:in sisällä.(älä lataa)

**käyttö**

lataa ja unzippaa opcalc.zip, sitten 
kopio kaikki opintopisteesi:

<img src="https://i.imgur.com/8SGAbVB.png" height="80%" width="80%" >
kopioi... kopioi... kopioi... 
<img src="https://i.imgur.com/0Z3cofj.png" height="80%" width="80%" >
vedä vielä alemmas kunnes tulet loppuun.
<img src="https://i.imgur.com/4i2CRbe.png" height="80%" width="80%" >

liitä kopioitu opintopisteet op.txt tiedostoon joka on unzippattun tiedoston sisällä, ja tupla-klikkaa opcalc-vx,x.exe tiedostoa. (x,x = versio)

esimerkki:

<img src="https://i.imgur.com/JYssfv3.png" height="80%" width="80%" >

saa tuloksen:

<img src="https://i.imgur.com/DeQ4R7j.png" height="80%" width="80%" >


**issues and faq:**

1.
due to the unknown nature of pyinstaller, its commonly known to raise false positives on antivirus software, if you are concerned about downloading the exe file,
compile the cli version (use vscode) from source.

2.
wilma doesnt have an API i can use to get the data, in the future im planning on adding a webscraper with the collaboration of others
