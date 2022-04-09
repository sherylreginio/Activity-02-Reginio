import random

Ptype = str(input("Pokemon Type: "))
Stype = str(input("Skill Type: "))
Clevel = int(input("Charizard Level: "))
SpAttack = int(input("Special Attack: "))
Pwr = int(input("Power: "))

('\n')

EneType = str(input("Enemy Type: "))
FeLevel = int(input("Feraligatr's Level: "))
SpDef = int(input("Special Defense: "))
Gen = int(input("Generation: "))
Trgt = int(input("Target: "))
Wthr = str(input("Weather: "))

def modifier (Trgt, Wthr, Gen, Ptype, Stype, EneType):

#target

    if Trgt == 1:
        Trgt = 1
    else:
        Trgt = .5

#weather
    if Wthr == "beneficial":
        Wthr = 1.5
    if Wthr == "against":
        Wthr = .5
    if Wthr == "otherwise":
        Wthr = 1

#badge
    if Gen == "2":
        Gen = 1.25
    else:
        Gen = 1
    
#critical
    Critical = [1 , 2]
    Critic = random.choice(Critical)
    if Critic == 2:
        print("\n CRITICAL HIT")
    else: 
        print("HIT")

#random
    Randm = [0.85,1]
    Rndm = random.choice(Randm)

#stab
    if Ptype == "fire" and Stype == "fire":
        effect1 = 1.5
    else:
        effect1 = 1

#type
    if Stype =="fire" and EneType == "water":
        effective = .5
    if Stype =="fire" and EneType == "flying":
        effective = 1
    
    type = effective

    if type <=.5:
        print ("NOT EFFECTIVE!")
    if type >=2:
        print("SUPER EFFECTIVE!")
    else:
        type == 1
        
#other
    Other = 1

#burn
    Burned = [.5 , 1]
    Burn = random.choice(Burned)
    if Burn == .5:
        print("\n The Attacker is BURNED!")

#calculation for modifier
    mod = Trgt * Wthr * Gen * Critic * Rndm * effect1 * type * Other * Burn
    return mod
    
#calculation for damage
dmge = ((((((2*Clevel)/5)+2)* Pwr * SpAttack/SpDef)/50)+2) * modifier(Trgt, Wthr, Gen, Ptype, Stype, EneType)
print("CHARIZARDS DAMAGE TO FERALIGATR: ", dmge)