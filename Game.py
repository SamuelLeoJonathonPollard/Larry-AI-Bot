import random
import os

os.system("color a")

WA1_1=random.randint(-100,100)/100
WA1_2=random.randint(-100,100)/100
WA1_3=random.randint(-100,100)/100
WA1_4=random.randint(-100,100)/100
WA1_5=random.randint(-100,100)/100
WA2_1=random.randint(-100,100)/100
WA2_2=random.randint(-100,100)/100
WA2_3=random.randint(-100,100)/100
WA2_4=random.randint(-100,100)/100
WA2_5=random.randint(-100,100)/100
WA3_1=random.randint(-100,100)/100
WA3_2=random.randint(-100,100)/100
WA3_3=random.randint(-100,100)/100
WA3_4=random.randint(-100,100)/100
WA3_5=random.randint(-100,100)/100
WA4_1=random.randint(-100,100)/100
WA4_2=random.randint(-100,100)/100
WA4_3=random.randint(-100,100)/100
WA4_4=random.randint(-100,100)/100
WA4_5=random.randint(-100,100)/100
WA5_1=random.randint(-100,100)/100
WA5_2=random.randint(-100,100)/100
WA5_3=random.randint(-100,100)/100
WA5_4=random.randint(-100,100)/100
WA5_5=random.randint(-100,100)/100
WOut1=random.randint(-100,100)/100
WOut2=random.randint(-100,100)/100
WOut3=random.randint(-100,100)/100
WOut4=random.randint(-100,100)/100
WOut5=random.randint(-100,100)/100

e=2.71828

I1=1
I2=0
I3=0
I4=0
I5=0

X=2
Y=8
HEAD=1

for x in range(0, 300):
    os.system("cls")
    A1=((I1*WA1_1)+(I2*WA1_2)+(I3*WA1_3)+(I4*WA1_4)+(I5*WA1_5))
    A2=((I1*WA2_1)+(I2*WA2_2)+(I3*WA2_3)+(I4*WA2_4)+(I5*WA2_5))
    A3=((I1*WA3_1)+(I2*WA3_2)+(I3*WA3_3)+(I4*WA3_4)+(I5*WA3_5))
    A4=((I1*WA4_1)+(I2*WA4_2)+(I3*WA4_3)+(I4*WA4_4)+(I5*WA4_5))
    A5=((I1*WA5_1)+(I2*WA5_2)+(I3*WA5_3)+(I4*WA5_4)+(I5*WA5_5))
    Out = 1/(1+e**-((A1*WOut1)+(A2*WOut2)+(A3*WOut3)+(A4*WOut4)+(A5*WOut5)))
    if(Out < 0.001):
        Out=0
    PrevHead=HEAD
    if(Out >= -1): #1=U 2=R 3=D 4=L
        HEAD=PrevHead-1
    if(Out >= -0.333333333):
        HEAD=PrevHead
    if(Out >= 0.333333333):
        HEAD=PrevHead+1

    if(HEAD == 0):
        HEAD=4
    if(HEAD == 5):
        HEAD=1
    AA=AB=AC=AD=AE=AF=AG=AH=AI=AJ="#"
    BA=BB=BC=BD=BE=BF=BG=BH=BI=BJ="#"
    CA=CB=CC=CD=CE=CF=CG=CH=CI=CJ="#"
    DA=DB=DC=DD=DE=DF=DG=DH=DI=DJ="#"
    EA=EB=EC=ED=EE=EF=EG=EH=EI=EJ="#"
    FA=FB=FC=FD=FE=FF=FG=FH=FI=FJ="#"
    GA=GB=GC=GD=GE=GF=GG=GH=GI=GJ="#"
    HA=HB=HC=HD=HE=HF=HG=HH=HI=HJ="#"
    IA=IB=IC=ID=IE=IF=IG=IH=II=IJ="#"
    JA=JB=JC=JD=JE=JF=JG=JH=JI=JJ="#"
    
    BB=BC=BD=BE=BF=BG=BH=BI=CB=CC=CD=CE=CF=CG=CH=CI=DB=DC=DD=DE=DF=DG=DH=DI=IB=IC=ID=IE=IF=IG=IH=II=HB=HC=HD=HE=HF=HG=HH=HI=GB=GC=GD=GE=GF=GG=GH=GI=EB=EC=ED=EI=EH=EG=FB=FC=FD=FI=FH=FG=str(" ")
    if(HEAD == 1):
        Y=Y-1
    if(HEAD == 2):
        X=X+1
    if(HEAD == 3):
        Y=Y+1
    if(HEAD == 4):
        X=X-1

    if(X>=0):
        R="A"
        if(X>=1):
            R="B"
            if(X>=2):
                R="C"
                if(X>=3):
                    R="D"
                    if(X>=4):
                        R="E"
                        if(X>=5):
                            R="F"
                            if(X>=6):
                                R="G"
                                if(X>=7):
                                    R="H"
                                    if(X>=8):
                                        R="I"
                                        if(X>=9):
                                            R="J"
    if(Y>=0):
        S="A"
        if(Y>=1):
            S="B"
            if(Y>=2):
                S="C"
                if(Y>=3):
                    S="D"
                    if(Y>=4):
                        S="E"
                        if(Y>=5):
                            S="F"
                            if(Y>=6):
                                S="G"
                                if(Y>=7):
                                    S="H"
                                    if(Y>=8):
                                         S="I"
                                         if(Y>=9):
                                            S="J"
    NUN=(S + R)
    Pixel=str(NUN)
    vars = {}
    
    if(HEAD == 1):
        vars[Pixel] = "^"
    if(HEAD == 2):
        vars[Pixel] = ">"
    if(HEAD == 3):
        vars[Pixel] = "V"
    if(HEAD == 4):
        vars[Pixel] = "<"
    
    print(AA + AB + AC + AD + AE + AF + AG + AH + AI + AJ)
    print(BA + BB + BC + BD + BE + BF + BG + BH + BI + BJ)
    print(CA + CB + CC + CD + CE + CF + CG + CH + CI + CJ)
    print(DA + DB + DC + DD + DE + DF + DG + DH + DI + DJ)
    print(EA + EB + EC + ED + EE + EF + EG + EH + EI + EJ)
    print(FA + FB + FC + FD + FE + FF + FG + FH + FI + FJ)
    print(GA + GB + GC + GD + GE + GF + GG + GH + GI + GJ)
    print(HA + HB + HC + HD + HE + HF + HG + HH + HI + HJ)
    print(IA + IB + IC + ID + IE + IF + IG + IH + II + IJ)
    print(JA + JB + JC + JD + JE + JF + JG + JH + JI + JJ)

    os.system("pause")

