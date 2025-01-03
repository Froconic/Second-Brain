import random, math, os, datetime
#TODO Fix path of points outputs
# TODO add in to pairs outputting the houses
# TODO Seperate functions into files
# TODO Add houses data

date = datetime.date.today()
# year = date.year
puer = "[[Puer#Qualities|Puer]]"
puella = "[[Puella#Qualities|Puella]]"
fortunaMajor = "[[Fortuna Major#Qualities|Fortuna Major]]"
fortunaMinor = "[[Fortuna Minor#Qualities|Fortuna Minor]]"
caputDraconis = "[[Caput Draconis#Qualities|Caput Draconis]]"
caudaDraconis = "[[Cauda Draconis#Qualities|Cauda Draconis]]"
amissio = "[[Amissio#Qualities|Amissio]]"
aquisitio = "[[Aquisitio#Qualities|Aquisitio]]"
albus = "[[Albus#Qualities|Albus]]"
rubeus = "[[Rubeus#Qualities|Rubeus]]"
tristitia = "[[Tristitia#Qualities|Tristitia]]"
laetitia = "[[Laetitia#Qualities|Laetitia]]"
via = "[[Via#Qualities|Via]]"
carcer = "[[Carcer#Qualities|Carcer]]"
conjunctio = "[[Conjunctio#Qualities|Conjunctio]]"
populus = "[[Populus#Qualities|Populus]]"


def oddOrEven(bit):
  if (bit % 2) == 0:
    bit = 2
  else:
    bit = 1

def plexer():
  bit = random.randint(1,2)
  bit = math.ceil(bit)
  oddOrEven(bit)
  return bit

def figure():
  fire = plexer()
  air = plexer()
  water = plexer()
  earth = plexer()
  figure = [fire, air, water, earth]
  return figure

def figureCheck(figure):
  if figure == [1,1,2,1]:
    figure = puer
  if figure == [1,2,1,1]:
    figure = puella
  if figure == [2, 1, 2, 1]:
    figure = aquisitio
  if figure == [1,2,1,2]:
    figure = amissio
  if figure == [2, 2, 1, 1]:
    figure = fortunaMajor
  if figure == [1,1,2,2]:
    figure = fortunaMinor
  if figure == [1, 1, 1, 2]:
    figure = caudaDraconis
  if figure == [2, 1, 1, 1]:
    figure = caputDraconis
  if figure == [1,2,2,2]:
    figure = laetitia
  if figure == [2,2,2,1]:
    figure = tristitia
  if figure == [1, 1, 1, 1]:
    figure = via
  if figure == [2,2,2,2]:
    figure = populus
  if figure == [1,2,2,1]:
    figure = carcer
  if figure == [2, 1, 1, 2]:
    figure = conjunctio
  if figure == [2,2,1,2]:
    figure = albus
  if figure == [2, 1, 2, 2]:
    figure = rubeus
  return figure

def motherGenerator():
  mother = figure()
  return mother

def firstWave():
  mother1 = motherGenerator()
  # print(mother1)
  mother2 = motherGenerator()
  # print(mother2)
  mother3 = motherGenerator()
  # print(mother3)
  mother4 = motherGenerator()
  # print(mother4)
  daughter1 = [mother1[0], mother2[0], mother3[0], mother4[0]]
  # print(daughter1)
  daughter2 = [mother1[1], mother2[1], mother3[1], mother4[1]]
  # print(daughter2)
  daughter3 = [mother1[2], mother2[2], mother3[2], mother4[2]]
  # print(daughter3)
  daughter4 = [mother1[3], mother2[3], mother3[3], mother4[3]]
  # print(daughter4)
  return mother1, mother2, mother3, mother4, daughter1, daughter2, daughter3, daughter4

def mathCheck(figure):
  if figure[0] % 2 == 0:
    figure[0] = 2
  else:
    figure[0] = 1
    
  if figure[1] % 2 == 0:
      figure[1] = 2
  else:
    figure[1] = 1
  
  if figure[2] % 2 == 0:
    figure[2] = 2
  else:
    figure[2] = 1
    
  if figure[3] % 2 == 0:
      figure[3] = 2
  else:
    figure[3] = 1
  return figure

def secondWave():
  mother1, mother2, mother3, mother4, daughter1, daughter2, daughter3, daughter4 = firstWave()
  niece1 = [mother1[0] + mother2[0], mother1[1] + mother2[1], mother1[2] + mother2[2], mother1[3] + mother2[3]]
  # print(niece1)
  niece2 = [mother3[0] + mother4[0], mother3[1] + mother4[1], mother3[2] + mother4[2], mother3[3] + mother4[3]]
  # print(niece2)
  niece3 = [daughter1[0] + daughter2[0], daughter1[1] + daughter2[1], daughter1[2] + daughter2[2], daughter1[3] + daughter2[3]]
  # print(niece3)
  niece4 = [daughter3[0] + daughter4[0], daughter3[1] + daughter4[1], daughter3[2] + daughter4[2], daughter3[3] + daughter4[3]]
  # print(niece4)
  niece1 = mathCheck(niece1)
  # print(niece1)
  niece2 = mathCheck(niece2)
  # print(niece2)
  niece3 = mathCheck(niece3)
  # print(f"niece 3 = {niece3}")
  niece4 = mathCheck(niece4)
  # print(f"niece 4 = {niece4}")
  return mother1, mother2, mother3, mother4, daughter1, daughter2, daughter3, daughter4, niece1, niece2, niece3, niece4

def thirdWave():
  mother1, mother2, mother3, mother4, daughter1, daughter2, daughter3, daughter4, niece1, niece2, niece3, niece4 = secondWave()
  leftWitness = [niece4[0] + niece3[0], niece4[1] + niece3[1], niece4[2] + niece3[2], niece4[3] + niece3[3]]
  # print(f"left witness raw = {leftWitness}")
  rightWitness = [niece2[0] + niece1[0], niece2[1] + niece1[1], niece2[2] + niece1[2], niece2[3] + niece1[3]]
  # print(f"right witness raw = {rightWitness}")
  leftWitness = mathCheck(leftWitness)
  # print(f"left witness = {leftWitness}")
  rightWitness = mathCheck(rightWitness)
  # print(f"right witness = {rightWitness}")
  return mother1, mother2, mother3, mother4, daughter1, daughter2, daughter3, daughter4, niece1, niece2, niece3, niece4, leftWitness, rightWitness

def lastWave():
  mother1, mother2, mother3, mother4, daughter1, daughter2, daughter3, daughter4, niece1, niece2, niece3, niece4, leftWitness, rightWitness = thirdWave()
  judge = [leftWitness[0] + rightWitness[0], leftWitness[1] + rightWitness[1], leftWitness[2] + rightWitness[2], leftWitness[3] + rightWitness[3]]
  judge = mathCheck(judge)
  reconciler = [judge[0] + mother1[0], judge[1] + mother1[1], judge[2] + mother1[2], judge[3] + mother1[3]]
  reconciler = mathCheck(reconciler)
  return mother1, mother2, mother3, mother4, daughter1, daughter2, daughter3, daughter4, niece1, niece2, niece3, niece4, leftWitness, rightWitness, judge, reconciler

def amissioPairs(chart):
  amissioCount = 0
  if figureCheck(chart[0]) == amissio:
    amissioCount += 1
  if figureCheck(chart[1]) == amissio:
    amissioCount += 1
  if figureCheck(chart[2]) == amissio:
    amissioCount += 1
  if figureCheck(chart[3]) == amissio:
    amissioCount += 1
  if figureCheck(chart[4]) == amissio:
    amissioCount += 1
  if figureCheck(chart[5]) == amissio:
    amissioCount += 1
  if figureCheck(chart[6]) == amissio:
    amissioCount += 1
  if figureCheck(chart[7]) == amissio:
    amissioCount += 1
  if figureCheck(chart[8]) == amissio:
    amissioCount += 1
  if figureCheck(chart[9]) == amissio:
    amissioCount += 1
  if figureCheck(chart[10]) == amissio:
    amissioCount += 1
  if figureCheck(chart[11]) == amissio:
    amissioCount += 1
  if amissioCount > 1:
    temp = f"Amissio: {amissioCount}"
    # print(f"Amissio: {amissioCount}")
    return temp

def aquisitioPairs(chart):
  aquisitioCount = 0
  if figureCheck(chart[0]) == aquisitio:
    aquisitioCount += 1
  if figureCheck(chart[1]) == aquisitio:
    aquisitioCount += 1
  if figureCheck(chart[2]) == aquisitio:
    aquisitioCount += 1
  if figureCheck(chart[3]) == aquisitio:
    aquisitioCount += 1
  if figureCheck(chart[4]) == aquisitio:
    aquisitioCount += 1
  if figureCheck(chart[5]) == aquisitio:
    aquisitioCount += 1
  if figureCheck(chart[6]) == aquisitio:
    aquisitioCount += 1
  if figureCheck(chart[7]) == aquisitio:
    aquisitioCount += 1
  if figureCheck(chart[8]) == aquisitio:
    aquisitioCount += 1
  if figureCheck(chart[9]) == aquisitio:
    aquisitioCount += 1
  if figureCheck(chart[10]) == aquisitio:
    aquisitioCount += 1
  if figureCheck(chart[11]) == aquisitio:
    aquisitioCount += 1
  if aquisitioCount > 1:
    temp = f"Aquisitio: {aquisitioCount}"
    # print(f"Aquisitio: {aquisitioCount}")
    return temp

def puerPairs(chart):
  puerCount = 0
  if figureCheck(chart[0]) == puer:
    puerCount += 1
  if figureCheck(chart[1]) == puer:
    puerCount += 1
  if figureCheck(chart[2]) == puer:
    puerCount += 1
  if figureCheck(chart[3]) == puer:
    puerCount += 1
  if figureCheck(chart[4]) == puer:
    puerCount += 1
  if figureCheck(chart[5]) == puer:
    puerCount += 1
  if figureCheck(chart[6]) == puer:
    puerCount += 1
  if figureCheck(chart[7]) == puer:
    puerCount += 1
  if figureCheck(chart[8]) == puer:
    puerCount += 1
  if figureCheck(chart[9]) == puer:
    puerCount += 1
  if figureCheck(chart[10]) == puer:
    puerCount += 1
  if figureCheck(chart[11]) == puer:
    puerCount += 1
  if puerCount > 1:
    temp = f"Puer: {puerCount}"
    # print(f"Puer: {puerCount}")
    return temp

def puellaPairs(chart):
  puellaCount = 0
  if figureCheck(chart[0]) == puella:
    puellaCount += 1
  if figureCheck(chart[1]) == puella:
    puellaCount += 1
  if figureCheck(chart[2]) == puella:
    puellaCount += 1
  if figureCheck(chart[3]) == puella:
    puellaCount += 1
  if figureCheck(chart[4]) == puella:
    puellaCount += 1
  if figureCheck(chart[5]) == puella:
    puellaCount += 1
  if figureCheck(chart[6]) == puella:
    puellaCount += 1
  if figureCheck(chart[7]) == puella:
    puellaCount += 1
  if figureCheck(chart[8]) == puella:
    puellaCount += 1
  if figureCheck(chart[9]) == puella:
    puellaCount += 1
  if figureCheck(chart[10]) == puella:
    puellaCount += 1
  if figureCheck(chart[11]) == puella:
    puellaCount += 1
  if puellaCount > 1:
    temp = f"Puella: {puellaCount}"
    # print(f"Puella: {puellaCount}")
    return temp

def majorPairs(chart):
  majorCount = 0
  if figureCheck(chart[0]) == fortunaMajor:
    majorCount += 1
  if figureCheck(chart[1]) == fortunaMajor:
    majorCount += 1
  if figureCheck(chart[2]) == fortunaMajor:
    majorCount += 1
  if figureCheck(chart[3]) == fortunaMajor:
    majorCount += 1
  if figureCheck(chart[4]) == fortunaMajor:
    majorCount += 1
  if figureCheck(chart[5]) == fortunaMajor:
    majorCount += 1
  if figureCheck(chart[6]) == fortunaMajor:
    majorCount += 1
  if figureCheck(chart[7]) == fortunaMajor:
    majorCount += 1
  if figureCheck(chart[8]) == fortunaMajor:
    majorCount += 1
  if figureCheck(chart[9]) == fortunaMajor:
    majorCount += 1
  if figureCheck(chart[10]) == fortunaMajor:
    majorCount += 1
  if figureCheck(chart[11]) == fortunaMajor:
    majorCount += 1
  if majorCount > 1:
    temp = f"Fortuna Major: {majorCount}"
    # print(f"Fortuna Major: {majorCount}")
    return temp

def minorPairs(chart):
  minorCount = 0
  if figureCheck(chart[0]) == fortunaMinor:
    minorCount += 1
  if figureCheck(chart[1]) == fortunaMinor:
    minorCount += 1
  if figureCheck(chart[2]) == fortunaMinor:
    minorCount += 1
  if figureCheck(chart[3]) == fortunaMinor:
    minorCount += 1
  if figureCheck(chart[4]) == fortunaMinor:
    minorCount += 1
  if figureCheck(chart[5]) == fortunaMinor:
    minorCount += 1
  if figureCheck(chart[6]) == fortunaMinor:
    minorCount += 1
  if figureCheck(chart[7]) == fortunaMinor:
    minorCount += 1
  if figureCheck(chart[8]) == fortunaMinor:
    minorCount += 1
  if figureCheck(chart[9]) == fortunaMinor:
    minorCount += 1
  if figureCheck(chart[10]) == fortunaMinor:
    minorCount += 1
  if figureCheck(chart[11]) == fortunaMinor:
    minorCount += 1
  if minorCount > 1:
    temp = f"Fortuna Minor: {minorCount}"
    # print(f"Fortuna Minor: {minorCount}")
    return temp

def caudaPairs(chart):
  caudaCount = 0
  if figureCheck(chart[0]) == caudaDraconis:
    caudaCount += 1
  if figureCheck(chart[1]) == caudaDraconis:
    caudaCount += 1
  if figureCheck(chart[2]) == caudaDraconis:
    caudaCount += 1
  if figureCheck(chart[3]) == caudaDraconis:
    caudaCount += 1
  if figureCheck(chart[4]) == caudaDraconis:
    caudaCount += 1
  if figureCheck(chart[5]) == caudaDraconis:
    caudaCount += 1
  if figureCheck(chart[6]) == caudaDraconis:
    caudaCount += 1
  if figureCheck(chart[7]) == caudaDraconis:
    caudaCount += 1
  if figureCheck(chart[8]) == caudaDraconis:
    caudaCount += 1
  if figureCheck(chart[9]) == caudaDraconis:
    caudaCount += 1
  if figureCheck(chart[10]) == caudaDraconis:
    caudaCount += 1
  if figureCheck(chart[11]) == caudaDraconis:
    caudaCount += 1
  if caudaCount > 1:
    temp = f"Cauda Draconis: {caudaCount}"
    # print(f"Cauda Draconis: {caudaCount}")
    return temp

def caputPairs(chart):
  caputCount = 0
  if figureCheck(chart[0]) == caputDraconis:
    caputCount += 1
  if figureCheck(chart[1]) == caputDraconis:
    caputCount += 1
  if figureCheck(chart[2]) == caputDraconis:
    caputCount += 1
  if figureCheck(chart[3]) == caputDraconis:
    caputCount += 1
  if figureCheck(chart[4]) == caputDraconis:
    caputCount += 1
  if figureCheck(chart[5]) == caputDraconis:
    caputCount += 1
  if figureCheck(chart[6]) == caputDraconis:
    caputCount += 1
  if figureCheck(chart[7]) == caputDraconis:
    caputCount += 1
  if figureCheck(chart[8]) == caputDraconis:
    caputCount += 1
  if figureCheck(chart[9]) == caputDraconis:
    caputCount += 1
  if figureCheck(chart[10]) == caputDraconis:
    caputCount += 1
  if figureCheck(chart[11]) == caputDraconis:
    caputCount += 1
  if caputCount > 1:
    temp = f"Caput Draconis: {caputCount}"
    # print(f"Caput Draconis: {caputCount}")
    return temp

def viaPairs(chart):
  viaCount = 0
  if figureCheck(chart[0]) == via:
    viaCount += 1
  if figureCheck(chart[1]) == via:
    viaCount += 1
  if figureCheck(chart[2]) == via:
    viaCount += 1
  if figureCheck(chart[3]) == via:
    viaCount += 1
  if figureCheck(chart[4]) == via:
    viaCount += 1
  if figureCheck(chart[5]) == via:
    viaCount += 1
  if figureCheck(chart[6]) == via:
    viaCount += 1
  if figureCheck(chart[7]) == via:
    viaCount += 1
  if figureCheck(chart[8]) == via:
    viaCount += 1
  if figureCheck(chart[9]) == via:
    viaCount += 1
  if figureCheck(chart[10]) == via:
    viaCount += 1
  if figureCheck(chart[11]) == via:
    viaCount += 1
  if viaCount > 1:
    temp = f"Via: {viaCount}"
    # print(f"Via: {viaCount}")
    return temp

def populusPairs(chart):
  populusCount = 0
  if figureCheck(chart[0]) == populus:
    populusCount += 1
  if figureCheck(chart[1]) == populus:
    populusCount += 1
  if figureCheck(chart[2]) == populus:
    populusCount += 1
  if figureCheck(chart[3]) == populus:
    populusCount += 1
  if figureCheck(chart[4]) == populus:
    populusCount += 1
  if figureCheck(chart[5]) == populus:
    populusCount += 1
  if figureCheck(chart[6]) == populus:
    populusCount += 1
  if figureCheck(chart[7]) == populus:
    populusCount += 1
  if figureCheck(chart[8]) == populus:
    populusCount += 1
  if figureCheck(chart[9]) == populus:
    populusCount += 1
  if figureCheck(chart[10]) == populus:
    populusCount += 1
  if figureCheck(chart[11]) == populus:
    populusCount += 1
  if populusCount > 1:
    temp = f"Populus: {populusCount}"
    # print(f"Populus: {populusCount}")
    return temp

def conjunctioPairs(chart):
  conjunctioCount = 0
  if figureCheck(chart[0]) == conjunctio:
    conjunctioCount += 1
  if figureCheck(chart[1]) == conjunctio:
    conjunctioCount += 1
  if figureCheck(chart[2]) == conjunctio:
    conjunctioCount += 1
  if figureCheck(chart[3]) == conjunctio:
    conjunctioCount += 1
  if figureCheck(chart[4]) == conjunctio:
    conjunctioCount += 1
  if figureCheck(chart[5]) == conjunctio:
    conjunctioCount += 1
  if figureCheck(chart[6]) == conjunctio:
    conjunctioCount += 1
  if figureCheck(chart[7]) == conjunctio:
    conjunctioCount += 1
  if figureCheck(chart[8]) == conjunctio:
    conjunctioCount += 1
  if figureCheck(chart[9]) == conjunctio:
    conjunctioCount += 1
  if figureCheck(chart[10]) == conjunctio:
    conjunctioCount += 1
  if figureCheck(chart[11]) == conjunctio:
    conjunctioCount += 1
  if conjunctioCount > 1:
    temp = f"Conjunctio: {conjunctioCount}"
    # print(f"Conjunctio: {conjunctioCount}")
    return temp

def carcerPairs(chart):
  carcerCount = 0
  if figureCheck(chart[0]) == carcer:
    carcerCount += 1
  if figureCheck(chart[1]) == carcer:
    carcerCount += 1
  if figureCheck(chart[2]) == carcer:
    carcerCount += 1
  if figureCheck(chart[3]) == carcer:
    carcerCount += 1
  if figureCheck(chart[4]) == carcer:
    carcerCount += 1
  if figureCheck(chart[5]) == carcer:
    carcerCount += 1
  if figureCheck(chart[6]) == carcer:
    carcerCount += 1
  if figureCheck(chart[7]) == carcer:
    carcerCount += 1
  if figureCheck(chart[8]) == carcer:
    carcerCount += 1
  if figureCheck(chart[9]) == carcer:
    carcerCount += 1
  if figureCheck(chart[10]) == carcer:
    carcerCount += 1
  if figureCheck(chart[11]) == carcer:
    carcerCount += 1
  if carcerCount > 1:
    temp = f"Carcer: {carcerCount}"
    # print(f"Carcer: {carcerCount}")
    return temp

def albusPairs(chart):
  albusCount = 0
  if figureCheck(chart[0]) == albus:
    albusCount += 1
  if figureCheck(chart[1]) == albus:
    albusCount += 1
  if figureCheck(chart[2]) == albus:
    albusCount += 1
  if figureCheck(chart[3]) == albus:
    albusCount += 1
  if figureCheck(chart[4]) == albus:
    albusCount += 1
  if figureCheck(chart[5]) == albus:
    albusCount += 1
  if figureCheck(chart[6]) == albus:
    albusCount += 1
  if figureCheck(chart[7]) == albus:
    albusCount += 1
  if figureCheck(chart[8]) == albus:
    albusCount += 1
  if figureCheck(chart[9]) == albus:
    albusCount += 1
  if figureCheck(chart[10]) == albus:
    albusCount += 1
  if figureCheck(chart[11]) == albus:
    albusCount += 1
  if albusCount > 1:
    temp = f"Albus: {albusCount}"
    # print(f"Albus: {albusCount}")
    return temp

def rubeusPairs(chart):
  rubeusCount = 0
  if figureCheck(chart[0]) == rubeus:
    rubeusCount += 1
  if figureCheck(chart[1]) == rubeus:
    rubeusCount += 1
  if figureCheck(chart[2]) == rubeus:
    rubeusCount += 1
  if figureCheck(chart[3]) == rubeus:
    rubeusCount += 1
  if figureCheck(chart[4]) == rubeus:
    rubeusCount += 1
  if figureCheck(chart[5]) == rubeus:
    rubeusCount += 1
  if figureCheck(chart[6]) == rubeus:
    rubeusCount += 1
  if figureCheck(chart[7]) == rubeus:
    rubeusCount += 1
  if figureCheck(chart[8]) == rubeus:
    rubeusCount += 1
  if figureCheck(chart[9]) == rubeus:
    rubeusCount += 1
  if figureCheck(chart[10]) == rubeus:
    rubeusCount += 1
  if figureCheck(chart[11]) == rubeus:
    rubeusCount += 1
  if rubeusCount > 1:
    temp = f"Rubeus: {rubeusCount}"
    # print(f"Rubeus: {rubeusCount}")
    return temp

def laetitiaPairs(chart):
  laetitiaCount = 0
  if figureCheck(chart[0]) == laetitia:
    laetitiaCount += 1
  if figureCheck(chart[1]) == laetitia:
    laetitiaCount += 1
  if figureCheck(chart[2]) == laetitia:
    laetitiaCount += 1
  if figureCheck(chart[3]) == laetitia:
    laetitiaCount += 1
  if figureCheck(chart[4]) == laetitia:
    laetitiaCount += 1
  if figureCheck(chart[5]) == laetitia:
    laetitiaCount += 1
  if figureCheck(chart[6]) == laetitia:
    laetitiaCount += 1
  if figureCheck(chart[7]) == laetitia:
    laetitiaCount += 1
  if figureCheck(chart[8]) == laetitia:
    laetitiaCount += 1
  if figureCheck(chart[9]) == laetitia:
    laetitiaCount += 1
  if figureCheck(chart[10]) == laetitia:
    laetitiaCount += 1
  if figureCheck(chart[11]) == laetitia:
    laetitiaCount += 1
  if laetitiaCount > 1:
    temp = f"Laetitia: {laetitiaCount}"
    # print(f"Laetitia: {laetitiaCount}")
    return temp

def tristitiaPairs(chart):
  tristitiaCount = 0
  if figureCheck(chart[0]) == tristitia:
    tristitiaCount += 1
  if figureCheck(chart[1]) == tristitia:
    tristitiaCount += 1
  if figureCheck(chart[2]) == tristitia:
    tristitiaCount += 1
  if figureCheck(chart[3]) == tristitia:
    tristitiaCount += 1
  if figureCheck(chart[4]) == tristitia:
    tristitiaCount += 1
  if figureCheck(chart[5]) == tristitia:
    tristitiaCount += 1
  if figureCheck(chart[6]) == tristitia:
    tristitiaCount += 1
  if figureCheck(chart[7]) == tristitia:
    tristitiaCount += 1
  if figureCheck(chart[8]) == tristitia:
    tristitiaCount += 1
  if figureCheck(chart[9]) == tristitia:
    tristitiaCount += 1
  if figureCheck(chart[10]) == tristitia:
    tristitiaCount += 1
  if figureCheck(chart[11]) == tristitia:
    tristitiaCount += 1
  if tristitiaCount > 1:
    temp = f"Tristitia: {tristitiaCount}"
    # print(f"Tristitia: {tristitiaCount}")
    return temp

def pairCheck(chart):
  puerTemp = puerPairs(chart)
  puellaTemp = puellaPairs(chart)
  aquisitioTemp = aquisitioPairs(chart)
  amissioTemp = amissioPairs(chart)
  majorTemp = majorPairs(chart)
  minorTemp = minorPairs(chart)
  viaTemp = viaPairs(chart)
  populusTemp = populusPairs(chart)
  conjunctioTemp = conjunctioPairs(chart)
  carcerTemp = carcerPairs(chart)
  albusTemp = albusPairs(chart)
  rubeusTemp = rubeusPairs(chart)
  laetitiaTemp = laetitiaPairs(chart)
  tristitiaTemp = tristitiaPairs(chart)
  caudaTemp = caudaPairs(chart)
  caputTemp = caputPairs(chart)
  return puellaTemp, puerTemp, amissioTemp, aquisitioTemp, caudaTemp, caputTemp, viaTemp, populusTemp, conjunctioTemp, majorTemp, minorTemp, carcerTemp, albusTemp, rubeusTemp, laetitiaTemp, tristitiaTemp

def pathOfPoints(chart):
  path = []
  t = ''
  if chart[12][0] == chart[14][0]:
    path.append("J, L")
    
  if chart[12][0] == chart[14][0] & chart[11][0] == chart[12][0]:
    path.append("12")
    
  if chart[12][0] == chart[14][0] & chart[11][0] == chart[12][0] & chart[7][0] == chart[11][0]:
    path.append("8")
    
  if chart[12][0] == chart[14][0] & chart[11][0] == chart[12][0] & chart[6][0] == chart[11][0]:
    path.append("7")
    
  if chart[12][0] == chart[14][0] & chart[10][0] == chart[12][0]:
    path.append("11")
    
  if chart[12][0] == chart[14][0] & chart[10][0] == chart[12][0] & chart[5][0] == chart[10][0]:
    path.append("6")
    
  if chart[12][0] == chart[14][0] & chart[10][0] == chart[12][0] & chart[4][0] == chart[10][0]:
    path.append("5")
    
  if chart[13][0] == chart[14][0]:
    path.append("J, R")
    
  if chart[13][0] == chart[14][0] & chart[9][0] == chart[13][0]:
    path.append("10")
    
  if chart[13][0] == chart[14][0] & chart[9][0] == chart[13][0] & chart[3][0] == chart[9][0]:
    path.append("4")
  
  if chart[13][0] == chart[14][0] & chart[9][0] == chart[13][0] & chart[2][0] == chart[9][0]:
    path.append("3")
  
  if chart[13][0] == chart[14][0] & chart[8][0] == chart[13][0]:
    path.append("9")
  
  if chart[13][0] == chart[14][0] & chart[8][0] == chart[13][0] & chart[0][0] == chart[13][0]:
    path.append("2")
  
  if chart[13][0] == chart[14][0] & chart[8][0] == chart[13][0] & chart[0][0] == chart[13][0]:
    path.append("1")
  
  if path == []:
    temp = f"Path of points: No Path"
    # print("No Path")
  else:
    c = ''
    for i in range(len(path)):
      t = path[i]
      c += ', ' + t
    # t = path.pop()
    # temp = f"Path of points: {t}"
    temp = f"Path of points: {c})"
    # print(f"Path of points: {c} ")
  return temp

def projectionAndFortune(chart):
  single = 0
  double = 0
  total = 0
  for figure in chart:
    for bit in figure:
      if bit == 1:
        single+=1
      if bit == 2:
        double+=2
  # print(f"Single Points: {single}")
  single = single % 12
  if single == 0:
    keyToSuccess = f"House {single+12} {figureCheck(chart[single-1])}"
    # print(f"Projection of Points:  house {single+12} {figureCheck(chart[single-1])}")
  else:
    keyToSuccess = f"House {single} {figureCheck(chart[single-1])}"
    # print(f"Projection of Points:  house {single} {figureCheck(chart[single-1])}")
  total = single + double
  # print(f"Total Points: {total}")
  total = total % 12
  if total == 0:
    keyToFortune = f"House 12 {figureCheck(chart[total+11])}"
    # print(f"Part of Fortune: house {total+12} {figureCheck(chart[total-1])}")
  else:
    keyToFortune = f"House {total} {figureCheck(chart[total-1])}"
    # print(f"Part of Fortune: house {total} {figureCheck(chart[total-1])}")
  return keyToSuccess, keyToFortune


def companySimple(chart):
  if chart[0] == chart[1]:
    firstCompany = f"Simple 1st {figureCheck(chart[0])} and 2nd House {figureCheck(chart[1])}\n- \n\n"
    return firstCompany
    # print(f"Simple First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}")
  if chart[2] == chart[3]:
    secondCompany = f"Simple 3rd {figureCheck(chart[2])} and 4th House {figureCheck(chart[3])}\n- \n\n"
    return secondCompany
    # print(f"Simple Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}")
  if chart[4] == chart[5]:
    thirdCompany = f"Simple 5th {figureCheck(chart[4])} and 6th House {figureCheck(chart[5])}\n- \n\n"
    return thirdCompany
    # print(f"Simple Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}")
  if chart[6] == chart[7]:
    fourthCompany = f"Simple 7th {figureCheck(chart[6])} and 8th House {figureCheck(chart[7])}\n- \n\n"
    return fourthCompany
    # print(f"Simple Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}")
  if chart[8] == chart[9]:
    fifthCompany = f"Simple 9th {figureCheck(chart[8])} and 10th House {figureCheck(chart[9])}\n- \n\n"
    return fifthCompany
    # print(f"Simple Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}")
  if chart[10] == chart[11]:
    sixthCompany = f"Simple 11th {figureCheck(chart[10])} and 12th House {figureCheck(chart[11])}\n- \n\n"
    return sixthCompany
    # print(f"Simple Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}")

def sunCheck(chart):
  if figureCheck(chart[0]) == fortunaMajor and figureCheck(chart[1]) == fortunaMinor:
    temp = f"Company Demi Simple First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
    return temp
  if figureCheck(chart[2]) == fortunaMajor and figureCheck(chart[3]) == fortunaMinor:
    temp = f"Company Demi Simple First {figureCheck(chart[2])} and Second House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == fortunaMajor and figureCheck(chart[5]) == fortunaMinor:
    temp = f"Company Demi Simple First {figureCheck(chart[4])} and Second House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == fortunaMajor and figureCheck(chart[7]) == fortunaMinor:
    temp = f"Company Demi Simple First {figureCheck(chart[6])} and Second House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == fortunaMajor and figureCheck(chart[9]) == fortunaMinor:
    temp = f"Company Demi Simple First {figureCheck(chart[8])} and Second House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == fortunaMajor and figureCheck(chart[11]) == fortunaMinor:
    temp = f"Company Demi Simple First {figureCheck(chart[10])} and Second House {figureCheck(chart[11])}\n- \n\n"
    return temp


  if figureCheck(chart[0]) == fortunaMinor and figureCheck(chart[1]) == fortunaMajor:
      temp = f"Company Demi Simple First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
      return temp
  if figureCheck(chart[2]) == fortunaMinor and figureCheck(chart[3]) == fortunaMajor:
    temp = f"Company Demi Simple First {figureCheck(chart[2])} and Second House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == fortunaMinor and figureCheck(chart[5]) == fortunaMajor:
    temp = f"Company Demi Simple First {figureCheck(chart[4])} and Second House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == fortunaMinor and figureCheck(chart[7]) == fortunaMajor:
    temp = f"Company Demi Simple First {figureCheck(chart[6])} and Second House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == fortunaMinor and figureCheck(chart[9]) == fortunaMajor:
    temp = f"Company Demi Simple First {figureCheck(chart[8])} and Second House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == fortunaMinor and figureCheck(chart[11]) == fortunaMajor:
    temp = f"Company Demi Simple First {figureCheck(chart[10])} and Second House {figureCheck(chart[11])}\n- \n\n"
    return temp

def moonCheck(chart):
  if figureCheck(chart[0]) == via and figureCheck(chart[1]) == populus:
    temp = f"Company Demi Simple First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
    return temp
  if figureCheck(chart[2]) == via and figureCheck(chart[3]) == populus:
    temp = f"Company Demi Simple Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == via and figureCheck(chart[5]) == populus:
    temp = f"Company Demi Simple Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == via and figureCheck(chart[7]) == populus:
    temp = f"Company Demi Simple Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == via and figureCheck(chart[9]) == populus:
    temp = f"Company Demi Simple Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == via and figureCheck(chart[11]) == populus:
    temp = f"Company Demi Simple Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp

  if figureCheck(chart[0]) == populus and figureCheck(chart[1]) == via:
      temp = f"Company Demi Simple First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
      return temp
  if figureCheck(chart[2]) == populus and figureCheck(chart[3]) == via:
    temp = f"Company Demi Simple Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == populus and figureCheck(chart[5]) == via:
    temp = f"Company Demi Simple Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == populus and figureCheck(chart[7]) == via:
    temp = f"Company Demi Simple Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == populus and figureCheck(chart[9]) == via:
    temp = f"Company Demi Simple Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == populus and figureCheck(chart[11]) == via:
    temp = f"Company Demi Simple Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp

def marsCheck(chart):
  if figureCheck(chart[0]) == rubeus and figureCheck(chart[1]) == puer:
    temp = f"Company Demi Simple First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
    return temp
  if figureCheck(chart[2]) == rubeus and figureCheck(chart[3]) == puer:
    temp = f"Company Demi Simple Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == rubeus and figureCheck(chart[5]) == puer:
    temp = f"Company Demi Simple Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == rubeus and figureCheck(chart[7]) == puer:
    temp = f"Company Demi Simple Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == rubeus and figureCheck(chart[9]) == puer:
    temp = f"Company Demi Simple Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == rubeus and figureCheck(chart[11]) == puer:
    temp = f"Company Demi Simple Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp


  if figureCheck(chart[0]) == puer and figureCheck(chart[1]) == rubeus:
      temp = f"Company Demi Simple First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
      return temp
  if figureCheck(chart[2]) == puer and figureCheck(chart[3]) == rubeus:
    temp = f"Company Demi Simple Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == puer and figureCheck(chart[5]) == rubeus:
    temp = f"Company Demi Simple Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == puer and figureCheck(chart[7]) == rubeus:
    temp = f"Company Demi Simple Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == puer and figureCheck(chart[9]) == rubeus:
    temp = f"Company Demi Simple Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == puer and figureCheck(chart[11]) == rubeus:
    temp = f"Company Demi Simple Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp

def mercuryCheck(chart):
  if figureCheck(chart[0]) == albus and figureCheck(chart[1]) == conjunctio:
    temp = f"Company Demi Simple First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
    return temp
  if figureCheck(chart[2]) == albus and figureCheck(chart[3]) == conjunctio:
    temp = f"Company Demi Simple Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == albus and figureCheck(chart[5]) == conjunctio:
    temp = f"Company Demi Simple Fifth {figureCheck(chart[4])} and Second Sixth {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == albus and figureCheck(chart[7]) == conjunctio:
    temp = f"Company Demi Simple Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == albus and figureCheck(chart[9]) == conjunctio:
    temp = f"Company Demi Simple Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == albus and figureCheck(chart[11]) == conjunctio:
    temp = f"Company Demi Simple Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp


  if figureCheck(chart[0]) == conjunctio and figureCheck(chart[1]) == albus:
      temp = f"Company Demi Simple First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
      return temp
  if figureCheck(chart[2]) == conjunctio and figureCheck(chart[3]) == albus:
    temp = f"Company Demi Simple Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == conjunctio and figureCheck(chart[5]) == albus:
    temp = f"Company Demi Simple Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == conjunctio and figureCheck(chart[7]) == albus:
    temp = f"Company Demi Simple Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == conjunctio and figureCheck(chart[9]) == albus:
    temp = f"Company Demi Simple Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == conjunctio and figureCheck(chart[11]) == albus:
    temp = f"Company Demi Simple Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp

def jupiterCheck(chart):
  if figureCheck(chart[0]) == laetitia and figureCheck(chart[1]) == aquisitio:
    temp = f"Company Demi Simple First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
    return temp
  if figureCheck(chart[2]) == laetitia and figureCheck(chart[3]) == aquisitio:
    temp = f"Company Demi Simple Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == laetitia and figureCheck(chart[5]) == aquisitio:
    temp = f"Company Demi Simple Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == laetitia and figureCheck(chart[7]) == aquisitio:
    temp = f"Company Demi Simple Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == laetitia and figureCheck(chart[9]) == aquisitio:
    temp = f"Company Demi Simple Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == laetitia and figureCheck(chart[11]) == aquisitio:
    temp = f"Company Demi Simple Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp


  if figureCheck(chart[0]) == aquisitio and figureCheck(chart[1]) == laetitia:
      temp = f"Company Demi Simple First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
      return temp
  if figureCheck(chart[2]) == aquisitio and figureCheck(chart[3]) == laetitia:
    temp = f"Company Demi Simple Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == aquisitio and figureCheck(chart[5]) == laetitia:
    temp = f"Company Demi Simple Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == aquisitio and figureCheck(chart[7]) == laetitia:
    temp = f"Company Demi Simple Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == aquisitio and figureCheck(chart[9]) == laetitia:
    temp = f"Company Demi Simple Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == aquisitio and figureCheck(chart[11]) == laetitia:
    temp = f"Company Demi Simple Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp

def venusCheck(chart):
  if figureCheck(chart[0]) == puella and figureCheck(chart[1]) == amissio:
    temp = f"Company Demi Simple First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
    return temp
  if figureCheck(chart[2]) == puella and figureCheck(chart[3]) == amissio:
    temp = f"Company Demi Simple Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == puella and figureCheck(chart[5]) == amissio:
    temp = f"Company Demi Simple Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == puella and figureCheck(chart[7]) == amissio:
    temp = f"Company Demi Simple Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == puella and figureCheck(chart[9]) == amissio:
    temp = f"Company Demi Simple Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == puella and figureCheck(chart[11]) == amissio:
    temp = f"Company Demi Simple Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp


  if figureCheck(chart[0]) == amissio and figureCheck(chart[1]) == puella:
      temp = f"Company Demi Simple First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
      return temp
  if figureCheck(chart[2]) == amissio and figureCheck(chart[3]) == puella:
    temp = f"Company Demi Simple Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == amissio and figureCheck(chart[5]) == puella:
    temp = f"Company Demi Simple Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == amissio and figureCheck(chart[7]) == puella:
    temp = f"Company Demi Simple Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == amissio and figureCheck(chart[9]) == puella:
    temp = f"Company Demi Simple Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == amissio and figureCheck(chart[11]) == puella:
    temp = f"Company Demi Simple Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp

def saturnCheck(chart):
  if figureCheck(chart[0]) == carcer and figureCheck(chart[1]) == tristitia:
    temp = f"Company Demi Simple First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
    return temp
  if figureCheck(chart[2]) == carcer and figureCheck(chart[3]) == tristitia:
    temp = f"Company Demi Simple Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == carcer and figureCheck(chart[5]) == tristitia:
    temp = f"Company Demi Simple Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == carcer and figureCheck(chart[7]) == tristitia:
    temp = f"Company Demi Simple Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == carcer and figureCheck(chart[9]) == tristitia:
    temp = f"Company Demi Simple Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == carcer and figureCheck(chart[11]) == tristitia:
    temp = f"Company Demi Simple Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp


  if figureCheck(chart[0]) == tristitia and figureCheck(chart[1]) == carcer:
      temp = f"Company Demi Simple First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
      return temp
  if figureCheck(chart[2]) == tristitia and figureCheck(chart[3]) == carcer:
    temp = f"Company Demi Simple Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == tristitia and figureCheck(chart[5]) == carcer:
    temp = f"Company Demi Simple Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == tristitia and figureCheck(chart[7]) == carcer:
    temp = f"Company Demi Simple Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == tristitia and figureCheck(chart[9]) == carcer:
    temp = f"Company Demi Simple Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == tristitia and figureCheck(chart[11]) == carcer:
    temp = f"Company Demi Simple Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp

def companyDemiSimple(chart):
  sunCheck(chart)
  moonCheck(chart)
  marsCheck(chart)
  mercuryCheck(chart)
  jupiterCheck(chart)
  venusCheck(chart)
  saturnCheck(chart)


def companyCompound(chart):
  # Draconis
  if figureCheck(chart[0]) == caudaDraconis and figureCheck(chart[1]) == caputDraconis:
    temp = f"Company Compound First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
    return temp
  if figureCheck(chart[2]) == caudaDraconis and figureCheck(chart[3]) == caputDraconis:
    temp = f"Company Compound Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == caudaDraconis and figureCheck(chart[5]) == caputDraconis:
    temp = f"Company Compound Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == caudaDraconis and figureCheck(chart[7]) == caputDraconis:
    temp = f"Company Compound Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == caudaDraconis and figureCheck(chart[9]) == caputDraconis:
    temp = f"Company Compound Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == caudaDraconis and figureCheck(chart[11]) == caputDraconis:
    temp = f"Company Compound Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp

  if figureCheck(chart[0]) == caputDraconis and figureCheck(chart[1]) == caudaDraconis:
      temp = f"Company Compound First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
      return temp
  if figureCheck(chart[2]) == caputDraconis and figureCheck(chart[3]) == caudaDraconis:
    temp = f"Company Compound Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == caputDraconis and figureCheck(chart[5]) == caudaDraconis:
    temp = f"Company Compound Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == caputDraconis and figureCheck(chart[7]) == caudaDraconis:
    temp = f"Company Compound Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == caputDraconis and figureCheck(chart[9]) == caudaDraconis:
    temp = f"Company Compound Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == caputDraconis and figureCheck(chart[11]) == caudaDraconis:
    temp = f"Company Compound Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp
    # Draconis end
    # Puer Puella
  if figureCheck(chart[0]) == puer and figureCheck(chart[1]) == puella:
    temp = f"Company Compound First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
    return temp
  if figureCheck(chart[2]) == puer and figureCheck(chart[3]) == puella:
    temp = f"Company Compound Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == puer and figureCheck(chart[5]) == puella:
    temp = f"Company Compound Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == puer and figureCheck(chart[7]) == puella:
    temp = f"Company Compound Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == puer and figureCheck(chart[9]) == puella:
    temp = f"Company Compound Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == puer and figureCheck(chart[11]) == puella:
    temp = f"Company Compound Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp

  if figureCheck(chart[0]) == puella and figureCheck(chart[1]) == puer:
      temp = f"Company Compound First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
      return temp
  if figureCheck(chart[2]) == puer and figureCheck(chart[3]) == puella:
    temp = f"Company Compound Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == puer and figureCheck(chart[5]) == puella:
    temp = f"Company Compound Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == puer and figureCheck(chart[7]) == puella:
    temp = f"Company Compound Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == puer and figureCheck(chart[9]) == puella:
    temp = f"Company Compound Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == puer and figureCheck(chart[11]) == puella:
    temp = f"Company Compound Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp
    # End Puer Puella
    # Fortuna
  if figureCheck(chart[0]) == fortunaMajor and figureCheck(chart[1]) == fortunaMinor:
    temp = f"Company Compound First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
    return temp
  if figureCheck(chart[2]) == fortunaMajor and figureCheck(chart[3]) == fortunaMinor:
    temp = f"Company Compound Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == fortunaMajor and figureCheck(chart[5]) == fortunaMinor:
    temp = f"Company Compound Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == fortunaMajor and figureCheck(chart[7]) == fortunaMinor:
    temp = f"Company Compound Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == fortunaMajor and figureCheck(chart[9]) == fortunaMinor:
    temp = f"Company Compound Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == fortunaMajor and figureCheck(chart[11]) == fortunaMinor:
    temp = f"Company Compound Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp

  if figureCheck(chart[0]) == fortunaMinor and figureCheck(chart[1]) == fortunaMajor:
      temp = f"Company Compound First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
      return temp
  if figureCheck(chart[2]) == fortunaMinor and figureCheck(chart[3]) == fortunaMajor:
    temp = f"Company Compound Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == fortunaMinor and figureCheck(chart[5]) == fortunaMajor:
    temp = f"Company Compound Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == fortunaMinor and figureCheck(chart[7]) == fortunaMajor:
    temp = f"Company Compound Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == fortunaMinor and figureCheck(chart[9]) == fortunaMajor:
    temp = f"Company Compound Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == fortunaMinor and figureCheck(chart[11]) == fortunaMajor:
    temp = f"Company Compound Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp
    # End Fortuna
    # Laetitita Tristitia
  if figureCheck(chart[0]) == laetitia and figureCheck(chart[1]) == tristitia:
    temp = f"Company Compound First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
    return temp
  if figureCheck(chart[2]) == laetitia and figureCheck(chart[3]) == tristitia:
    temp = f"Company Compound Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == laetitia and figureCheck(chart[5]) == tristitia:
    temp = f"Company Compound Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == laetitia and figureCheck(chart[7]) == tristitia:
    temp = f"Company Compound Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == laetitia and figureCheck(chart[9]) == tristitia:
    temp = f"Company Compound Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == laetitia and figureCheck(chart[11]) == tristitia:
    temp = f"Company Compound Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp

  if figureCheck(chart[0]) == tristitia and figureCheck(chart[1]) == laetitia:
      temp = f"Company Compound First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
      return temp
  if figureCheck(chart[2]) == tristitia and figureCheck(chart[3]) == laetitia:
    temp = f"Company Compound Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == tristitia and figureCheck(chart[5]) == laetitia:
    temp = f"Company Compound Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == tristitia and figureCheck(chart[7]) == laetitia:
    temp = f"Company Compound Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == tristitia and figureCheck(chart[9]) == laetitia:
    temp = f"Company Compound Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == tristitia and figureCheck(chart[11]) == laetitia:
    temp = f"Company Compound Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp
    # End L & T
    # Via Populus
  if figureCheck(chart[0]) == via and figureCheck(chart[1]) == populus:
    temp = f"Company Compound First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
    return temp
  if figureCheck(chart[2]) == via and figureCheck(chart[3]) == populus:
    temp = f"Company Compound Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == via and figureCheck(chart[5]) == populus:
    temp = f"Company Compound Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == via and figureCheck(chart[7]) == populus:
    temp = f"Company Compound Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == via and figureCheck(chart[9]) == populus:
    temp = f"Company Compound Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == via and figureCheck(chart[11]) == populus:
    temp = f"Company Compound Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp

  if figureCheck(chart[0]) == populus and figureCheck(chart[1]) == via:
      temp = f"Company Compound First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
      return temp
  if figureCheck(chart[2]) == populus and figureCheck(chart[3]) == via:
    temp = f"Company Compound Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == populus and figureCheck(chart[5]) == via:
    temp = f"Company Compound Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == populus and figureCheck(chart[7]) == via:
    temp = f"Company Compound Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == populus and figureCheck(chart[9]) == via:
    temp = f"Company Compound Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == populus and figureCheck(chart[11]) == via:
    temp = f"Company Compound Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp
    # End V & P
    # Carcer Conjunctio
  if figureCheck(chart[0]) == conjunctio and figureCheck(chart[1]) == carcer:
    temp = f"Company Compound First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
    return temp
  if figureCheck(chart[2]) == conjunctio and figureCheck(chart[3]) == carcer:
    temp = f"Company Compound Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == conjunctio and figureCheck(chart[5]) == carcer:
    temp = f"Company Compound Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == conjunctio and figureCheck(chart[7]) == carcer:
    temp = f"Company Compound Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == conjunctio and figureCheck(chart[9]) == carcer:
    temp = f"Company Compound Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == conjunctio and figureCheck(chart[11]) == carcer:
    temp = f"Company Compound Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp

  if figureCheck(chart[0]) == carcer and figureCheck(chart[1]) == conjunctio:
      temp = f"Company Compound First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
      return temp
  if figureCheck(chart[2]) == carcer and figureCheck(chart[3]) == conjunctio:
    temp = f"Company Compound Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == carcer and figureCheck(chart[5]) == conjunctio:
    temp = f"Company Compound Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == carcer and figureCheck(chart[7]) == conjunctio:
    temp = f"Company Compound Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == carcer and figureCheck(chart[9]) == conjunctio:
    temp = f"Company Compound Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == carcer and figureCheck(chart[11]) == conjunctio:
    temp = f"Company Compound Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp
    # End C & C
    # Albus Rubeus
  if figureCheck(chart[0]) == albus and figureCheck(chart[1]) == rubeus:
    temp = f"Company Compound First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
    return temp
  if figureCheck(chart[2]) == albus and figureCheck(chart[3]) == rubeus:
    temp = f"Company Compound Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == albus and figureCheck(chart[5]) == rubeus:
    temp = f"Company Compound Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == albus and figureCheck(chart[7]) == rubeus:
    temp = f"Company Compound Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == albus and figureCheck(chart[9]) == rubeus:
    temp = f"Company Compound Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == albus and figureCheck(chart[11]) == rubeus:
    temp = f"Company Compound Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp

  if figureCheck(chart[0]) == rubeus and figureCheck(chart[1]) == albus:
      temp = f"Company Compound First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
      return temp
  if figureCheck(chart[2]) == rubeus and figureCheck(chart[3]) == albus:
    temp = f"Company Compound Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == rubeus and figureCheck(chart[5]) == albus:
    temp = f"Company Compound Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == rubeus and figureCheck(chart[7]) == albus:
    temp = f"Company Compound Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == rubeus and figureCheck(chart[9]) == albus:
    temp = f"Company Compound Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == rubeus and figureCheck(chart[11]) == albus:
    temp = f"Company Compound Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp
    # End A R
    # Albus Rubeus
  if figureCheck(chart[0]) == amissio and figureCheck(chart[1]) == aquisitio:
    temp = f"Company Compound First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
    return temp
  if figureCheck(chart[2]) == amissio and figureCheck(chart[3]) == aquisitio:
    temp = f"Company Compound Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == amissio and figureCheck(chart[5]) == aquisitio:
    temp = f"Company Compound Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == amissio and figureCheck(chart[7]) == aquisitio:
    temp = f"Company Compound Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == amissio and figureCheck(chart[9]) == aquisitio:
    temp = f"Company Compound Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == amissio and figureCheck(chart[11]) == aquisitio:
    temp = f"Company Compound Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp

  if figureCheck(chart[0]) == aquisitio and figureCheck(chart[1]) == amissio:
      temp = f"Company Compound First {figureCheck(chart[0])} and Second House {figureCheck(chart[1])}\n- \n\n"
      return temp
  if figureCheck(chart[2]) == aquisitio and figureCheck(chart[3]) == amissio:
    temp = f"Company Compound Third {figureCheck(chart[2])} and Fourth House {figureCheck(chart[3])}\n- \n\n"
    return temp
  if figureCheck(chart[4]) == aquisitio and figureCheck(chart[5]) == amissio:
    temp = f"Company Compound Fifth {figureCheck(chart[4])} and Sixth House {figureCheck(chart[5])}\n- \n\n"
    return temp
  if figureCheck(chart[6]) == aquisitio and figureCheck(chart[7]) == amissio:
    temp = f"Company Compound Seventh {figureCheck(chart[6])} and Eighth House {figureCheck(chart[7])}\n- \n\n"
    return temp
  if figureCheck(chart[8]) == aquisitio and figureCheck(chart[9]) == amissio:
    temp = f"Company Compound Ninth {figureCheck(chart[8])} and Tenth House {figureCheck(chart[9])}\n- \n\n"
    return temp
  if figureCheck(chart[10]) == aquisitio and figureCheck(chart[11]) == amissio:
    temp = f"Company Compound Eleventh {figureCheck(chart[10])} and Twelfth House {figureCheck(chart[11])}\n- \n\n"
    return temp
    # End A R


def chartBuilder():
  chart = lastWave()
  input("What is your query? ")
  print(f"Right Witness: {figureCheck(chart[13])}")
  print(f"Left Witness: {figureCheck(chart[12])}")
  print(f"Judge: {figureCheck(chart[14])}")
  print(f"Reconciler: {figureCheck(chart[15])}")
  print(f"1st House: {figureCheck(chart[0])}")
  print(f"2nd House: {figureCheck(chart[1])}")
  print(f"3rd House: {figureCheck(chart[2])}")
  print(f"4th House: {figureCheck(chart[3])}")
  print(f"5th House: {figureCheck(chart[4])}")
  print(f"6th House: {figureCheck(chart[5])}")
  print(f"7th House: {figureCheck(chart[6])}")
  print(f"8th House: {figureCheck(chart[7])}")
  print(f"9th House: {figureCheck(chart[8])}")
  print(f"10th House: {figureCheck(chart[9])}")
  print(f"11th House: {figureCheck(chart[10])}")
  print(f"12th House: {figureCheck(chart[11])}")
  pathOfPoints(chart)
  projectionAndFortune(chart)
  pairCheck(chart)
  companySimple(chart)
  companyDemiSimple(chart)
  companyCompound(chart)

def pageBuilder(weekNumber, pn,year):
  chart = lastWave()
  print("Weekly Forecast commence")
  file = weekNumber
  file
  print(file)
  # folder = "/home/akira/Documents/Synced Files/Daily-Journal/" + str(year) + "/Weekly/Forecasts"
  folder = "/home/rivre/Documents/Synced Files/Daily-Journal/" + str(year) + "/Weekly/Forecasts"
  # folder = "/home/rivre/Documents/Synced Files/Daily-Journal/" + str(year) + "/Weekly/Forecasts/Test"
  folder
  print(folder)
  path = os.path.join(folder,file)
  path = path + '.md'
  print(path)
  
  with open( path, 'w+') as f:
    f.write('[[#Key points]]\n')
    f.write(f'### PN: {pn}\n')
    f.write('---\n')
    f.write(f'Right witness: {figureCheck(chart[13])}\n- \n\n')
    f.write(f'Left witness: {figureCheck(chart[12])}\n- \n\n')
    f.write(f'Judge: {figureCheck(chart[14])}\n- \n\n')
    f.write(f'Reconciler: {figureCheck(chart[15])}\n- \n\n')
    f.write(f'1st House: {figureCheck(chart[0])}\n- \n\n')
    f.write(f'2nd House: {figureCheck(chart[1])}\n- \n\n')
    f.write(f'3rd House: {figureCheck(chart[2])}\n- \n\n')
    f.write(f'4th House: {figureCheck(chart[3])}\n- \n\n')
    f.write(f'5th House: {figureCheck(chart[4])}\n- \n\n')
    f.write(f'6th House: {figureCheck(chart[5])}\n- \n\n')
    f.write(f'7th House: {figureCheck(chart[6])}\n- \n\n')
    f.write(f'8th House: {figureCheck(chart[7])}\n- \n\n')
    f.write(f'9th House: {figureCheck(chart[8])}\n- \n\n')
    f.write(f'10th House: {figureCheck(chart[9])}\n- \n\n')
    f.write(f'11th House: {figureCheck(chart[10])}\n- \n\n')
    f.write(f'12th House: {figureCheck(chart[11])}\n- \n\n')
    
    pointsOfPath = pathOfPoints(chart)
    f.write(f"{pointsOfPath}\n- \n\n")
    
    keys = projectionAndFortune(chart)
    f.write(f"### Key to Success: {keys[0]}\n- \n\n")
    f.write(f"### Key to Fortune: {keys[1]}\n- \n\n")
    
    f.write("Pairs\n---\n")
    puerPair = puerPairs(chart)
    puellaPair = puellaPairs(chart)
    aquisitioPair = aquisitioPairs(chart)
    amissioPair = amissioPairs(chart)
    majorPair = majorPairs(chart)
    minorPair = minorPairs(chart)
    viaPair = viaPairs(chart)
    populusPair = populusPairs(chart)
    caudaPair = caudaPairs(chart)
    caputPair = caputPairs(chart)
    albusPair = albusPairs(chart)
    rubeusPair = rubeusPairs(chart)
    tristitiaPair = tristitiaPairs(chart)
    laetitiaPair = laetitiaPairs(chart)
    carcerPair = carcerPairs(chart)
    conjunctioPair = conjunctioPairs(chart)
    if puerPair != None:
      f.write(f"{puerPair}\n- \n\n")
    if puellaPair != None:
      f.write(f"{puellaPair}\n- \n\n")
    if albusPair != None:
      f.write(f"{albusPair}\n- \n\n")
    if rubeusPair != None:
      f.write(f"{rubeusPair}\n- \n\n")
    if caudaPair != None:
      f.write(f"{caudaPair}\n- \n\n")
    if caputPair != None:
      f.write(f"{caputPair}\n- \n\n")
    if majorPair != None:
      f.write(f"{majorPair}\n- \n\n")
    if minorPair != None:
      f.write(f"{minorPair}\n- \n\n")
    if laetitiaPair != None:
      f.write(f"{laetitiaPair}\n- \n\n")
    if tristitiaPair != None:
      f.write(f"{tristitiaPair}\n- \n\n")
    if carcerPair != None:
      f.write(f"{carcerPair}\n- \n\n")
    if conjunctioPair != None:
      f.write(f"{conjunctioPair}\n- \n\n")
    if viaPair != None:
      f.write(f"{viaPair}\n- \n\n")
    if populusPair != None:
      f.write(f"{populusPair}\n- \n\n")
    if aquisitioPair != None:
      f.write(f"{aquisitioPair}\n- \n\n")
    if amissioPair != None:
      f.write(f"{amissioPair}\n- \n\n")
    f.write("\n### Company:\n\n---\n\n")
    companies = companySimple(chart)
    # if companies[0] != None:
    #   f.write(f"{companies[0]}\n- \n\n")
    if companies != None:
      f.write(companies)
      # for company in companies:
      #   if company != None:
      #     f.write(f"{company}\n- \n\n")
    demiSun = sunCheck(chart)
    demiMoon = moonCheck(chart)
    demiMars = marsCheck(chart)
    demiMercury = mercuryCheck(chart)
    demiJupiter = jupiterCheck(chart)
    demiVenus = venusCheck(chart)
    demiSaturn = saturnCheck(chart)
    
    if demiSun != None:
      f.write(demiSun)
    if demiMoon != None:
      f.write(demiMoon)
    if demiMercury != None:
      f.write(demiMercury)
    if demiMars != None:
      f.write(demiMars)
    if demiJupiter != None:
      f.write(demiJupiter)
    if demiVenus != None:
      f.write(demiVenus)
    if demiSaturn != None:
      f.write(demiSaturn)
    
    f.write("Key Points \n---\n")
  print("Forecast generated and ready")
  print("moving on to outline")
  

# C:\Users\akira\Desktop\Stuff\Keep\Technomancy\DIVINATION

# chartBuilder()
# pageBuilder()