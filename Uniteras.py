# Uniteras v10.4  (c) Adi Andrei / Radu Andrei / Technosophics Ltd 1992 - 2022

#  *TERAASH0.01 *  
def teraasho():
    answer = "undefined"
    if X <= 50 and Y <= 30 and Z <= 15 and LL <= 100 and IP <= 6 and IG == 0:
        answer = "*** soil class AASHO :a-1-a ***"
    if X <= 100 and Y <= 50 and Z <= 25 and LL <= 100 and IP <= 6 and IG == 0:
        answer = "*** soil class AASHO :a-1-b ***"
    if X <= 100 and Y >= 51 and Z <= 10 and LL <= 100 and IP == 0 and IG == 0:
        answer = "*** soil class AASHO :a-3 ***"
    if X <= 100 and Y <= 100 and Z <= 35 and LL <= 40 and IP <= 10 and IG == 0:
        answer = "*** *soil class AASHO:a-2-4 ***"
    if X <= 100 and Y <= 100 and Z <= 35 and LL >= 41 and IP <= 10 and IG == 0:
        answer = "*** soil class AASHO:a-2-5 ***"
    if X <= 100 and Y <= 100 and Z <= 35 and LL <= 40 and IP >= 11 and IG == 0:
        answer = "*** soil class AASHO :a-2-6 ***"
    if X <= 100 and Y <= 100 and Z <= 35 and LL >= 41 and IP >= 11 and IG <= 4:
        answer = "*** soil class AASHO:a-2-7 ***"
    if X <= 100 and Y <= 100 and Z >= 36 and LL <= 40 and IP <= 10 and IG <= 6:
        answer = "*** soil class AASHO :a-4 ***"
    if X <= 100 and Y <= 100 and Z >= 36 and LL >= 41 and IP <= 10 and IG <= 12:
        answer = "*** soil class AASHO:a-5 ***"
    if X <= 100 and Y <= 100 and Z >= 36 and LL <= 40 and IP >= 11 and IG <= 16:
        answer = "*** soil class AASHO :a-6 ***"
    if X <= 100 and Y <= 100 and Z >= 36 and LL >= 41 and IP >= 11 and IP <= (LL - 30) and IG <= 20:
        answer = "*** soil class AASHO: a-7-5 **It II 5 **It II"
    if X <= 100 and Y <= 100 and Z >= 36 and LL >= 41 and IP >= 11 and IP >= (LL - 30) and IG <= 20:
        answer = "*** soil class AASHO :a-7-6 ***"
    return (answer)


#  "rtr.02"
def rtr():
    answer = "undefined"
    F = Z;
    A = ALT;
    G = FK
    if DM > 0 and DM < 50 and F > 35 and IP > 0 and IP < 10:
        answer = "*** soil class RTR :A ;subclass: A1 ***"
    if DM > 0 and DM < 50 and F > 35 and IP > 10 and IP < 20:
        answer = " *** soil class RTR :A ;subclass:A2 ***"
    if DM > 0 and DM < 50 and F > 35 and IP > 20 and IP < 50:
        answer = " *** soil class RTR :A ;subclass: A3 ***"
    if DM > 0 and DM < 50 and F > 35 and IP > 0 and IP < 50:
        answer = "*** soil class RTR :A ;subclass: A4 ***"
    if DM > 0 and DM < 50 and F > 5 and F < 12 and FRG > 0 and FRG < 30 and EN > 35:
        answer = "*** soil class RTR :B ;subclass:B1 ***"
    if DM > 0 and DM < 50 and F > 5 and F < 12 and EN > 0 and EN < 35 and FRG > 0 and FRG < 30:
        answer = "*** soil class RTR :B ;subclass:B2 ***"
    if DM > 0 and DM < 50 and F > 5 and F < 12 and FRG > 30 and EN > 25:
        answer = "*** soil class RTR :B ;subclass:B3 ***"
    if DM > 0 and DM < 50 and F > 5 and F < 12 and FRG > 30 and EN > 0 and EN < 25:
        answer = "*** soil class RTR :B ;subclass:B4 ***"
    if DM > 0 and DM < 50 and F > 12 and F < 35 and IP > 0 and IP < 10:
        answer = " *** soil class RTR :B ;subclass:B5 ***"
    if DM > 0 and DM < 50 and F > 12 and F < 35 and IP > 10:
        answer = "*** soil class RTR :B ;subclass: B6 ***"
    if DM > 50 and F > 10 and F < 20:
        answer = "***soil class RTR :C ;subclass: C1 ***"
    if DM > 50 and DM < 250 and F > 10 and F < 20:
        answer = "***soil class RTR :C ;subclass: C2 ***"
    if DM > 250 and F > 10 and F < 20:
        answer = "*** soil class RTR :C ;subclass: C3 ***"
    if DM > 0 and DM < 50 and F > 0 and F < 5 and G > 0 and G < 30:
        answer = "*** soil class RTR :D ;subclass: D1 ***"
    if DM > 0 and DM < 50 and G > 30:
        answer = "*** soil class RTR :D ;subclass: D2 ***"
    if DM > 50 and DM < 250:
        answer = "*** soil class RTR :D ;subclass: D3 ***"
    if DM > 250:
        answer = "*** soil class RTR :D ;subclass:  D4 ***"
    if DU > 1.7:
        answer = "*** evolutive soil/dense chalk class RTR E, subclass: CR1 ***"
    if DU > 0 and DU < 1.5:
        answer = "*** evolutive soil/chalk class RTR E, subclass: CR3 ***"
    if FRG > 0 and FRG < 30:
        answer = "*** evolutive soil/marl class RTR E, subclass: MA1 ***"
    if FRG > 30 and A > 0 and A < 20:
        answer = "*** evolutive soil/marl class RTR E, subclass:MA2 ***"
    if FRG > 30 and A > 20 and A < 50:
        answer = "*** evolutive soil/marl class RTR E, subclass:MA3 ***"
    if FRG > 30 and A > 50:
        answer = "*** evolutive soil/marl, class RTR E, subclass: MA4 ***"
    if MO > 3 and MO < 10:
        answer = "*** soil class RTR F, subclass: MOM ***"
    if MO > 10:
        nswer = " soil class RTR F, subclass:MOR ***"
    return (answer)

    #  ##### ROMTERAS #1141#14


def romteras():
    answer = "undefined"
    F1 = FA;
    F2 = FC;
    F3 = FD;
    F4 = FE;
    F5 = FG;
    F6 = FI;
    F7 = FJ;
    WC = LL;
    F8 = FK
    CC = CPS;
    A = ARG
    if CP == 1 and F8 > 50 and F7 > 50 and A < 1 and AP < 10 and APN < 20 and UN > 5 and SID == 1:
        answer = "***  coarse non cohesive soil (blocks), class 1, subclass 1-a, mark :FB/very good ***"
    if CP == 0 and F8 > 50 and A < 1 and AP < 10 and APN < 20 and UN > 5 and F6 > 50 and SID == 1:
        answer = "***  coarse non cohesive soil (boulder), class 1, subclass 1-a, mark :FB/very good ***"
    if CP == 0 and F8 > 50 and F5 > 50 and A < 1 and AP < 10 and APN < 20 and UN > 5 and SID == 1:
        answer = "*** coarse non cohesive soil (gravel), class 1, subclass 1-a, mark :FB/very good ***"
    if CP == 0 and F8 > 50 and F7 > 50 and A < 1 and AP < 10 and APN < 20 and UN <= 5 and SID == 1:
        answer = "*** coarse non cohesive soil (blocks), class 1, subclass 1-b, mark :FB/very good ***"
    if CP == 0 and F8 > 50 and F6 > 50 and A < 1 and AP < 10 and APN < 20 and UN <= 5 and SID == 1:
        answer = "*** coarse non cohesive soil (boulder), class 1, subclass 1-b, mark :FB/very good ***"
    if CP == 0 and F8 > 50 and F5 > 50 and A < 1 and AP < 10 and APN < 20 and UN <= 5 and SID == 1:
        answer = "***coarse non cohesive soil ( coarse gravel), class 1, subclass 1-b, mark :FB/very good ***"
    if CP == 0 and F8 < 50 and SID == 2 and A < 6 and AP < 20 and APN < 40 and UN > 5 and IP <= 10 and F4 > 50:
        answer = "*** coarse non cohesive soil (fine  gravel), class 2, subclass 2-a, mark :FB/very good ***"
    if CP == 0 and F8 < 50 and SID == 2 and F3 > 50 and A < 6 and AP < 20 and APN < 40 and UN > 5 and IP <= 10:
        answer = "*** coarse non cohesive soil (coarse sand), class 2, subclass 2-b, mark :FB/very good ***"
    if CP == 0 and F8 < 50 and SID == 2 and F2 > 50 and A < 6 and AP < 20 and APN < 40 and UN > 5 and IP <= 10:
        answer = "*** coarse non cohesive soil (medium size  sand), class 2, subclass 2-a, mark :FB/very good ***"
    if CP == 0 and F8 < 50 and SID == 2 and F1 > 50 and A < 6 and AP < 20 and APN < 40 and UN < 5 and IP <= 10:
        answer = "*** fine non cohesive soil (fine sand), class 2, subclass 2-a, mark :FB/very good ***"
    if CP == 0 and F8 < 50 and SID == 2 and F4 > 50 and A < 6 and AP < 20 and APN < 40 and UN <= 5 and IP <= 10:
        answer = "***  coarse non cohesive soil (coarse gravel), class 2, subclass 2-b, mark :FB/very good ***"
    if CP == 0 and F8 < 50 and SID == 2 and F3 > 50 and A < 6 and AP < 20 and APN < 40 and UN <= 5 and IP <= 10:
        answer = "***coarse non cohesive soil (coarse sand), class 2, subclass 2-b, mark :FB/very good ***"
    if CP == 0 and F8 < 50 and SID == 2 and F2 > 50 and A < 6 and AP < 20 and APN < 40 and UN <= 5 and IP <= 10:
        answer = "*** coarse non cohesive soil (medium size sand), class 2, subclass 2-b, mark :FB/very good ***"
    if CP == 0 and F8 < 50 and SID == 2 and F1 > 50 and A < 6 and AP < 20 and APN < 40 and UN <= 5 and IP <= 10:
        answer = "***  fine  non cohesive soil (fine  sand), class 2, subclass 2-b, mark :FB/very good ***"
    if CP == 0 and F8 < 50 and SID == 3 and F4 > 50 and A >= 6 and AP >= 20 and APN >= 40 and IP > 10 and UL <= 40:
        answer = "*** Non cohesive soil ( silty or clayey  gravel, class 3, subclass 3-a, mark : M/ mediocre  ***"
    if CP == 0 and F8 < 50 and SID == 3 and F3 > 50 and A >= 6 and AP >= 20 and APN >= 40 and IP > 10 and UL <= 40:
        answer = "*** Non cohesive soil ( silty or clayey coarse sand , class 3, subclass 3-a, mark : M/ mediocre  ***"
    if CP == 0 and F8 < 50 and SID == 3 and F2 > 50 and A >= 6 and AP >= 20 and APN >= 40 and IP < 10 and UL <= 40:
        answer = "*** Non cohesive soil ( silty or clayey medium size  sand , class 3, subclass 3-a, mark : M/ mediocre  ***"
    if CP == 0 and F8 < 50 and SID == 3 and F1 > 50 and A >= 6 and AP >= 20 and APN >= 40 and IP < 10 and UL <= 40:
        answer = "*** Non cohesive soil ( silty or clayey fine sand, class 3, subclass 3-a, mark : M/ mediocre  ***"
    if CP == 0 and F8 > 50 and SID == 3 and F4 > 50 and A >= 6 and AP >= 20 and APN >= 40 and IP > 10 and UL < 40:
        answer = "*** Non cohesive soil ( silty or clayey  fine gravel, class 3, subclass 3-b, mark : M/ mediocre  ***"
    if CP == 0 and F8 < 50 and SID == 3 and F3 > 50 and A >= 6 and AP >= 20 and APN >= 40 and IP > 10 and UL < 40:
        answer = "*** Non cohesive soil ( silty or clayey  coarse sand, class 3, subclass 3-b, mark : M/ mediocre  ***"
    if CP == 0 and F8 < 50 and SID == 3 and F2 > 50 and A >= 6 and AP >= 20 and APN >= 40 and IP > 10 and UL < 40:
        answer = "*** Non cohesive soil ( silty or clayey medium size sand, class 3, subclass 3-b, mark : M/ mediocre  ***"
    if CP == 0 and F8 < 50 and SID == 3 and F1 > 50 and A >= 6 and AP >= 20 and APN >= 40 and IP > 10 and UL > 40:
        answer = "*** Non cohesive soil ( silty or clayey fine sand , class 3, subclass 3-b, mark : M/ mediocre  ***"
    if IP > 35 and A > 60 and CC == 3 and UL > 70 and SID == 2:
        answer = "*** cohesive soil, loam clay, class 4, subclass 4-d,mark : B/ bad ***"
    if IP > 25 and IP < 50 and A > 35 and A < 60 and N < 30 and UL < 70 and CC == 2 and SID == 3:
        answer = "*** cohesive soil, clay, class 4, subclass 4-b ,mark : M/ mediocre *** "
    if IP > 15 and IP < 35 and A > 30 and A < 60 and P < A and N > 30 and CC == 2 and UL < 70 and SID == 3:
        answer = "*** cohesive soil, clayey sand, class 4, subclass 4-b ,mark : M/ mediocre ***"
    if IP > 15 and IP < 25 and A > 30 and A < 35 and P > A and N > 30 and UL < 70 and CC == 2 and SID == 3:
        answer = "*** cohesive soil, silty sandy clay , class 4, subclass 4-b ,mark : M/ mediocre ***"
    if IP > 10 and IP < 25 and A > 15 and A < 30 and P > N and N < 30 and CC == 2 and UL < 70 and SID == 3:
        answer = "*** cohesive soil, clayey silt , class 4, subclass 4-b ,mark : M/ mediocre ***"
    if IP > 5 and IP < 10 and A > 15 and A < 30 and P > N and N > 30 and CC == 1 and UL < 40 and SID == 2:
        answer = "*** cohesive soil, sandy clayey silt, class 4, subclass 4-a ,mark : M/ mediocre ***"
    if IP > 5 and IP < 15 and A > 0 and A < 15 and P > A and N < 30 and CC == 1 and UL < 40 and SID == 2:
        answer = "*** cohesive soil,silt, class 4, subclass 4-a ,mark : M/ mediocre ***"
    if IP > 0 and IP < 10 and A > 0 and A < 15 and P > N and N > 30 and CC == 1 and UL < 40 and SID == 2:
        answer = "*** cohesive soil, sandy silt, class 4, subclass 4-a ,mark : M/ mediocre ***"
    if IP > 5 and IP < 20 and A > 15 and A < 30 and P < N and CC == 2 and UL < 40 and SID == 2:
        answer = "*** cohesive soil, clayey sand , class 4,subclass 4-a ,mark : M/ mediocre ***"
    if IP > 5 and IP < 20 and A > 15 and A < 30 and P < N and CC == 2 and UL < 70 and SID == 3:
        answer = "*** cohesive soil, clayey, class 4, subclass 4-b ,mark : M/ mediocre ***"
    if IP >= 0 and IP < 10 and A > 0 and A < 15 and P < N and CC == 2 and UL < 40 and SID == 2:
        answer = "*** cohesive soil, silty sand, class 4, subclass 4-a,mark : M/ mediocre ***"
    if IP > 5 and IP <= 10 and A > 15 and A < 30 and P > N and N > 30 and MO > 5 and CC == 1 and UL < 40 and SID == 2:
        answer = "*** cohesive soil,sandy clayey silt with  organic matter, class 4, subclass 4-c ,mark : M/ mediocre ***"
    if IP > 5 and IP <= 10 and A > 0 and A <= 15 and P > A and N < 30 and MO > 5 and CC == 1 and SID == 2 and UL < 40:
        answer = "***cohesive soil,silt  with organic matter , class 4, subclass 4-c ,mark : M/ mediocre ***"
    if IP > 0 and IP <= 10 and A > 0 and A < 15 and P > N and N > 30 and MO > 5 and CC == 1 and UL < 40 and SID == 2:
        answer = "*** cohesive soil, sandy silt with organic matter, class 4, subclass 4-c ,mark : M/ mediocre ***"
    if IP > 5 and IP <= 10 and A > 15 and A < 30 and P < N and MO > 5 and CC == 1 and UL < 40 and SID == 2:
        answer = "*** cohesive soil, clayey sand with organic mater, class 4, subclass 4-c ,mark : M/ mediocre ***"
    if IP > 0 and IP <= 10 and A > 0 and A < 15 and P < N and MO > 5 and CC == 1 and UL < 40 and CC == 1 and UL < 40 and SID == 2:
        answer = "***  cohesive soil, silty sand , class 4, subclass 4-c ,mark : M/ mediocre ***"
    if IP > 25 and IP < 35 and A > 35 and A < 60 and P < A and N < 30 and MO > 5 and CC == 2 and UL < 75 and SID == 3:
        answer = "***  cohesive soil, clay with organic matter, class 4, subclass 4-e ,mark : B/bad ***"
    if IP > 15 and IP < 35 and A > 30 and A < 50 and P > A and N < P and MO > 5 and UL < 75 and SID == 3:
        answer = "*** cohesive soil, silty  clay, class 4, subclass 4-e ,mark : B/bad ***"
    if IP > 15 and IP < 35 and A > 30 and A < 60 and P < A and N > 30 and MO > 5 and CC == 2 and UL < 75 and SID == 3:
        answer = "*** cohesive soil, sandy clay, class 4, subclass 4-e ,mark : B/bad ***"
    if IP > 15 and IP < 25 and A > 30 and A < 35 and P > A and N > 30 and MO > 5 and CC == 2 and UL < 75 and SID == 3:
        answer = "*** cohesive soil, silty sandy  clay, class 4, subclass 4-e ,mark : B/bad ***"
    if IP > 10 and IP < 25 and A > 15 and A < 30 and P < N and N < 30 and MO > 5 and CC == 2 and UL < 75 and SID == 3:
        answer = "***cohesive soil, clayey dust, class 4, subclass 4-e ,mark : B/bad ***"
    if IP > 5 and IP < 20 and A > 15 and A < 30 and MO > 5 and CC == 2 and UN < 75 and P > N and N > 30 and SID == 3:
        answer = "*** cohesive soil, sandy clayey silt  with organic matter, class 4, subclass 4-e ,mark : B/bad ***"
    if IP > 5 and IP < 15 and A > 0 and A < 15 and P > A and N < 30 and MO > 5 and CC == 2 and UL < 75 and SID == 3:
        answer = "*** cohesive soil, silt with organic matter , class 4, subclass 4-e ,mark : B/bad ***"
    if IP > 0 and IP < 10 and A > 0 and A < 15 and P > N and N > 30 and MO > 5 and CC == 2 and UL < 75 and SID == 3:
        answer = "*** cohesive soil, clayey sand with organic matter , class 4, subclass 4-e ,mark : B/bad ***"
    if IP > 0 and IP < 10 and A > 0 and A <= 15 and P < N and MO > 5 and CC == 2 and UL < 75 and SID == 3:
        answer = "*** cohesive soil, silty sand with organic matter  , class 4, subclass 4-e ,mark : B/bad ***"
    if IP > 35 and A > 60 and MO > 5 and CC == 3 and UL > 40 and SID == 3:
        answer = "*** cohesive soil, clay with organic matter  , class 4, subclass 4-f ,mark : VB/ very bad ***"
    if IP > 25 and IP < 50 and A > 35 and A < 60 and P < A and N < 30 and MO > 5 and CC == 3 and UL > 40 and SID == 3:
        answer = "*** cohesive soil, clay  with organic matter  , class 4, subclass 4-f ,mark : VB/ very bad ***"
    if IP > 15 and IP < 35 and A > 30 and A < 50 and P > A and N < P and MO > 5 and CC == 3 and UL > 40 and SID == 3:
        answer = "*** cohesive soil, silty clay with organic matter  , class 4, subclass 4-f ,mark : VB/very bad ***"
    if IP > 15 and IP < 35 and A > 30 and A < 60 and P < A and N > 30 and MO > 5 and CC == 3 and UL > 40 and SID == 3:
        answer = "*** cohesive soil, sandy clay with organic matter  , class 4, subclass 4-f ,mark : VB/very bad ***"
    if IP > 15 and IP < 25 and A > 30 and A < 35 and MO > 5 and CC == 3 and UL > 40 and SID == 3:
        answer = "*** cohesive soil, silty  sandy clay  with organic matter  , class 4, subclass 4-f ,mark : VB/very bad ***"
    if IP > 10 and IP < 25 and A > 15 and A < 30 and P > N and N < 30 and MO > 5 and CC == 3 and UL > 40 and SID == 3:
        answer = "*** cohesive soil, clayey silt with organic matter  , class 4, subclass 4-f ,mark : VB/very bad ***"
    if IP > 10 and IP < 25 and A > 15 and A < 30 and P > N and N > 30 and MO > 5 and CC == 3 and UL > 40 and SID == 3:
        answer = "*** cohesive soil, clayey sandy silt with organic matter  , class 4, subclass 4-f ,mark : VB/very bad ***"
    if IP > 5 and IP < 15 and A >= 0 and A < 15 and P > A and N < 30 and MO > 5 and CC == 3 and UL > 40 and SID == 3:
        answer = "*** cohesive soil, silt  with organic matter  , class 4, subclass 4-f ,mark : VB/very bad ***"
    if IP >= 0 and IP <= 10 and A >= 15 and A <= 30 and P < N and MO > 5 and CC == 3 and UL > 40 and SID == 3:
        answer = "*** cohesive soil, sandy silt  with organic matter  , class 4, subclass 4-f ,mark : VB/very bad ***"
    if IP > 5 and IP < 20 and A > 15 and A < 30 and P < N and MO > 5 and CC == 3 and UL > 40 and SID == 3:
        answer = "*** cohesive soil, clayey  sand with organic matter  , class 4, subclass 4-f ,mark : VB/very bad ***"
    if IP >= 0 and IP < 10 and A >= 0 and A <= 15 and P < N and MO > 5 and CC == 3 and UL > 40 and SID == 3:
        answer = "*** cohesive soil, silty sand with organic matter  , class 4, subclass 4-f ,mark : VB/very bad ***"
    return (answer)


def uscs():
    #  "*** USCS.01 -Program  for identification of  soils"
    answer = "undefined"
    if FP > 50 and Z > 0 and Z < 5 and UN > 4 and CC >= 1 and CC <= 3:
        answer = "*** coarse soil with gravel or ballast with good grading and less fine fraction, class  GW ***"
    if FP > 50 and Z > 0 and Z < 5 and UN < +4 and CC < 1 and CC > 3:
        answer = "*** coarse soil with gravel or ballast with  mediocre grading and less fine fraction, class  GP ***"
    if FP > 50 and Z >= 5 and Z <= 12 and UN > 4 and CC >= 1 and CC <= 3 and (
            (LL > 20 and IP < .73 * (LL - 20)) or (LL > 0 and LL < 20 and IP >= 0 and IP < 4)):
        answer = "*** coarse soil with gravel or ballast with good grading , with silty binder, class  GW - GM ***"
    if FP > 50 and Z >= 5 and Z <= 12 and UN > 4 and CC >= 1 and CC <= 3 and (
            (LL > 29 and IP > .73 * (LL - 20)) or (LL > 0 and LL < 29 and IP > 7)):
        answer = "*** coarse soil with gravel or ballast with good grading  with clayey  binder, class  GW- GC ***"
    if FP > 50 and Z >= 5 and Z <= 12 and UN <= 4 and CC < 1 and CC > 3 and (
            (LL > 20 and IP < .73 * (LL - 20)) or (LL >= 0 and LL < 20 and IP < 4)):
        answer = "*** coarse soil with gravel or ballast with mediocre grading, with silty binder, class  GW-GM ***"
    if FP > 50 and Z >= 5 and Z <= 12 and UN <= 4 and CC < 1 and CC > 3 and (
            (LL > 29 and IP > .73 * (LL - 20)) or (LL >= 0 and LL < 29 and IP > 7)):
        answer = "*** coarse soil with gravel or ballast with mediocre  grading , with clayey binder, class  GP-GC ***"
    if FP > 50 and Z > 12 and ((LL > 20 and IP < .73 * (LL - 20)) or (LL >= 0 and LL < 20 and IP < 4)):
        answer = "*** coarse soil with gravel or ballast with silty binder, class  GM ***"
    if FP > 50 and Z > 12 and IP >= 4 and IP <= 7:
        answer = "*** coarse soil with gravel or ballast with silty-clayey binder , class  GM-GC ***"
    if FP > 50 and Z > 12 and IP >= 4 and IP <= 7:
        answer = "*** coarse soil with gravel or ballast with silty-clayey  binder, class  GM-GC ***"
    if FP > 0 and FP < 50 and Z > 0 and Z < 5 and UN > 6 and CC >= 1 and CC <= 3:
        answer = "*** coarse soil , sand, with good grading, class  SW ***"
    if FP > 0 and FP < 50 and Z > 0 and Z < 5 and UN < 6 and CC < 1 and CC > 3:
        answer = "*** coarse soil , sand, with mediocre  grading, class  SP ***"
    if FP > 0 and FP < 50 and Z >= 5 and Z <= 12 and UN > 6 and CC >= 1 and CC <= 3 and (
            (LL > 20 and IP < .73 * (LL - 20)) or (LL >= 0 and LL < 20 and IP >= 0 and IP < 4)):
        answer = "*** coarse soil , sand, with good grading, with silty binder, class  SW-SM  ***"
    if FP > 0 and FP < 50 and Z >= 5 and Z <= 12 and UN > 6 and CC >= 1 and CC <= 3 and (
            (LL > 29 and IP > .73 * (LL - 20)) or (LL >= 0 and LL < 29 and IP > 7)):
        answer = "***   coarse soil , sand, with good  grading, with clayey binder,  class  SW-SC ***"
    if FP > 0 and FP < 50 and Z >= 5 and Z <= 12 and UN <= 6 and CC < 1 and CC > 3 and (
            (LL > 0 and IP < .73 * (LL - 20)) or (LL >= 0 and LL < 20 and IP >= 0 and IP < 4)):
        answer = "*** coarse soil , sand, with mediocre  grading, with silty binder, class  SP-SM ***"
    if FP > 0 and FP < 50 and Z < 5 and Z > 12 and UN <= 6 and CC < 1 and CC > 3 and (
            (LL > 29 and IP >= .73 * (LL - 20)) or (LL > 0 and LL < 29 and IP > 7)):
        answer = "*** coarse soil , sand, with mediocre  grading,with clayey binder, class  SP-SC ***"
    if FP > 0 and FP < 50 and Z > 12 and (
            (LL > 20 and IP < .73 * (LL - 20)) or (LL >= 0 and LL < 20 and IP >= 0 and IP < 4)):
        answer = "*** coarse soil , sand, with silty binder, class  SM ***"
    if FP > 0 and FP < 50 and Z > 12 and ((LL > 29 and IP > .73 * (LL - 20)) or (LL > 0 and LL < 29 and IP >= 7)):
        answer = "*** coarse soil , sand, with clayey binder, class  SC ***"
    if Z > 50 and LL < 50 and ((LL > 20 and IP < .73 * (LL - 20)) or (LL < 20 and IP >= 0 and IP < 4)):
        answer = "*** fine soil , silt with or without  organic matter, class  OL , or  respectively ML ***"
    if Z > 50 and LL > 0 and LL < 50 and ((LL > 29 and IP > .73 * (LL - 20)) or (LL < 29 and IP > 7)):
        answer = "*** fine soil,clayey- silty, class ML-CL***"
    if Z > 50 and LL > 0 and LL < 50 and ((LL > 29 and IP > .73 * (LL - 20)) or (LL < 29 and IP > 7)):
        answer = "*** fine soil,clayey, class CL ***"
    if Z > 50 and IP < .73 * (LL - 20):
        answer = "***  fine soil, silty, with or without organic matter, class OM, and respectively MH ***"
    if Z > 50 and LL > 50 and IP > .73 * (LL - 20):
        answer = "***  fine clayey  soil , class  CH ***"
    if Z > 50 and IP > .73 * (LL - 20):
        answer = "***  fine cagey soil, class CH ***"
    return (answer)


def demo():
    global CP, FA, FC, FD, FE, FG, FI, FJ, X, Y, LL, IP, IG, WN, WO, CBR, IC, DM, Z, \
        EN, ALT, FRG, DU, MO, FP, CC, UN, ARG, P, N, UL, AP, APN, FK, CPS, SID
    CP = 0  # soil category ,cp
    FA = 0  # fraction 0.05-0.25,fa
    FC = 0  # fraction 0.25-0.5 ,fc
    FD = 0  # fraction 0.5 - 2 ifd
    FE = 0  # fraction 2 - 20 ife
    FG = 0  # fraction 20 - 70 ,fg
    FI = 0  # fraction 70 -200 ji
    FJ = 0  # fraction <200 fj
    X = 40  # fraction <2 (N.10),x
    Y = 30  # fraction <0.425 (N.40) y
    LL = 30  # liquid limit ,LL
    IP = 9  # plasticity index,IP
    IG = 5  # group index,IG
    WN = 0  # natural moisture content,wn
    WO = 0  # optimum moisture content  ,wo
    CBR = 0  # bearing capacity index,cbr
    IC = 0  # consistency index  ,ic
    DM = 0  # maximum  size ,dm
    Z = 40  # fine fraction  (<0.074 sau <0.080 mm) z
    EN = 0  # sand equivalent  ,en
    ALT = 0  # alterability ,alt= ")
    FRG = 0  # fragmentation  frg
    DU = 0  # dry density ,du
    MO = 0  # organic matter content  ,mo
    FP = 0  # fraction >4.75 (N.4)/p
    CC = 0  # curvature coefficient  ,cc
    UN = 0  # unevenness coefficient  ,un
    ARG = 0  # fraction <0.005 ,arg
    P = 0  # fraction silt (0.005<d<0.05),p
    N = 0  # fraction sand(0.05<d< 2) ,n
    UL = 0  # free inflation ,u1
    AP = 0  # fraction clay+silt(d<0.05),ap
    APN = 0  # fraction clay+silt+fine sand (d<0.25) apn
    FK = 0  # coarse fraction (>2mm) fk
    CPS = 0  # compressibility,cps
    SID = 0  # sensibility at though -freezing ,sid

    print("Uniteras v10.4  (c) Adi Andrei / Radu Andrei/ Technosophics Ltd 1992 - 2021")
    print("AASHO ....:", teraasho())
    print("RTR :", rtr())
    print("US :", uscs())
    print("ROMTERAS...:", romteras())


demo()
