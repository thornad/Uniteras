from decimal import Decimal
                             
def current_layer():
    C=0
    if WN>WO+1 and CBR<8 and CBR>0 and DM>0 and DM<50 and F>75 and IP<10 and IP>0 and IC+EN+A+G+DU+FRG==0 : C=1          
    if WN<WO+1 and WN>WO-2 and DM<50 and DM>0 and CBR<8 and CBR>0 and F>3 and IP<10 and IP>0 and IC+A+G+FRG+DU==0 : C=2        
    if WN<WO-2 and CBR>25 and DM<50 and DM>0 and F>30 and IP<10 and IP>0 and IC+EN+A+G+FRG+DU==0 : C=3            
    if WN>WO+2 and CBR<5 and CBR>0 and IC<1 and IC>0 and DM>50 and F>35 and IP<20 and IP>10 and EN+A+G+FRG+DU==0 : C=4        
    if WN<WO+2 and WN>WO-2 and CBR<15 and CBR >5 and IC<1.2 and IC>1 and DM<50 and DM>0 and F>75 and IP<20 and IP>10 and EN+A+G+FRG+DU==0 : C=5   
    if WN<WO-2 and CBR>15 and IC>1.2 and DM<50 and DM >0 and F>35 and IP>10 and EN+A+G+FRG+DU==0 : C=6           
    if WN>WO+4 and CBR<3 and CBR >0 and IC<.9 and IC>0 and DM<50 and DM >0 and F>35 and IP<50 and IP>20 and EN+A+G+FRG+DU==0 : C=7    
    if WN<WO+4 and WN>WO-4 and CBR<15 and CBR >3 and IC<1.7 and IC>.9 and DM<50 and DM>0 and F>35 and IP<50 and IP>20 and EN+A+G+FRG+DU==O : C=8   
    if WN<WO-4 and CBR> 15 and IC>1.3 and DM<50 and DM >0 and F>35 and IP<50 and IP>20 and EN+A+G+FRG+DU==0 : C=9        
    if DM<50 and DM >0 and F>35 and IP>50 and CBR+IC+EN+A+G+FRG+DU==0 : C=10                 
    if DM<50 and DM>0 and F<12 and F>5 and EN>35 and G<30 and G>0 and IC+CBR+A+IP+FRG+DU==0 : C=11            
    if WN>WO+2 and CBR<8 and CBR>0 and DM<50 and DM>0 and F>5 and F<12 and EN<35 and EN>0 and IC+A+G+IP+FRG+DU==0 : C=12        
    if WN<WO+2 and WN>WO+1 and CBR>8 and DM<50 and DM>0 and F>5 and F<12 and EN<35 and EN >0 and G<30 and G>0 and IC+A+IP+FRG+DU==0 : C=13
    if WN<WO-1 and DM<50 and DM >0 and F>5 and F< 12 and EN< 35 and EN>0 and G<30 and G>0 and CBR+IC+A+IP+FRG+DU==0 : C=14     
    if WN<WO-1 and DM<50 and DM >0 and F>5 and F<12 and EN<35 and G>30 and CBR+IC+A+IP+FRG+DU==0 : C=15
    if WN>WO+2 and CBR<8 and CBR>0 and DM<50 and DM>0 and F<12 and F>5 and EN<25 and EN>0 and G>30 and IC+A+IP+FRG+DU==0 : C=16
    if WN<WO+2 and WN >WO-1 and CBR>8 and DM<50 and DM>0 and F>5 and F<12 and EN<25 and EN>0 and G>30 and IC+A+IP+FRG+DU==0 : C=17     
    if WN<WO-1 and DM<50 and DM >0 and F>5 and F<12 and EN<25 and EN>0 and G>30 and CBR+IC+A+IP+FRG+DU==0 : C=18
    if WN<WO+1 and DM<50 and DM>0 and F>5 and F< 12 and EN<25 and EN>0 and G>30 and IC+A+IP+FRG+DU==0 : C=19
    if WN>WO+1 and CBR<8 and CBR>0 and DM<50 and DM >0 and F>12 and F<35 and IP<10 and IC+EN+A+G+FRG+DU==0 : C=20         
    if WN<WO+1 and WN>WO-2 and CBR<25 and CBR>8 and DM<50 and DM>0 and F>12 and F<35 and IP<10 and IP>0 and IC+EN+A+G+FRG+DU==0 : C=21      
    if WN<WO-2 and CBR>25 and DM<50 and DM >0 and F>12 and F<35 and IP<10 and IP>0 and IC+EN+A+G+FRG+DU==0 : C=22         
    if WN>WO+2 and CBR>8 and IC<1 and IC>0 and DM<50 and DM>0 and F>12 and F<35 and IP>10 and EN+A+G+FRG+DU==0 : C=23        
    if WN<WO+2 and WN>WO-2 and CBR>8 and IC<1.2 and IC>1 and DM<50 and DM>0 and F>12 and F<35 and IP>10 and EN+A+G+FRG+DU==0 : C=24      
    if WN<WO-2 and IC>1.2 and DM<50 and DM>0 and F>12 and F<35 and IP>10 and CBR+EN+A+G+FRG+DU==0 : C=25
    if WN>WO+4 and CBR<3 and CBR>0 and DM<50 and DM>0 and F>10 and F<20 and IC+EN+A+G+IP+FRG+DU==0 : C=26            
    if WN<WO+4 and WN>WO-2 and CBR<15 and CBR>3 and DM>50 and F>10 and F<20 and IC+EN+A+G+IP+FRG+DU==0 : C=27
    if WN<WO-2 and CBR<15 and CBR>0 and DM>50 and F>10 and F<20 and IC+EN+A+G+IP+FRG+DU==0 : C=28              
    if DM<250 and DM>50 and F>5 and F<10 and IC<1 and CBR+EN+A+G+IP+FRG+DU==0 : C=29                
    if DM<250 and DM>50 and F>5 and F<10 and IC>1 and IC<1.2 and CBR+EN+A+IP+FRG+DU==0 : C=30              
    if DM<250 and DM>50 and F>5 and F<10 and IC>1.2 and CBR+EN+A+G+IP+FRG+DU==0 : C=31                
    if DM>250 and F>5 and F<10 and IC<1 and IC>0 and CBR+EN+A+G+IP+FRG+DU==0 : C=32                
    if DM>250 and F>5 and F<10 and IC>1.2 and CBR+EN+A+G+IP+FRG+DU==0 : C=33                  
    if DM>250 and F>5 and F<10 and IC<1.2 and IC>0 and CBR+EN+A+G+IP+FRG+DU==0 : C=34                
    if DM<50 and DM>0 and F<5 and F>0 and G<30 and IC+EN+A+IP+FRG+DU==0 : C=35               
    if DM<50 and DM >0 and F<5 and F>0 and G>30 and CBR+IC+EN+A+IP+FRG+DU==0 : C=36               
    if DM>50 and DM<250 and F<5 and F>0 and CBR+IC+EN+A+G+IP+FRG+DU==0 : C=37                  
    if DM>250 and F<5 and F>0 and CBR+IC+EN+A+G+IP+FRG+DU==0 : C=38                    
    if WN>23 and DU>1.5 and DU<1.7 and CBR+IC+DM+F+EN+A+G+IP+FRG==0 : C=39                    
    if WN<23 and WN>0 and DU>1.5 and DU<1.7 and CBR+IC+DM+F+EN+A+G+IP+FRG==0 : C=40                  
    if DU>1.7 and WN+CBR+IC+DM+F+EN+A+G+IP+FRG==0 : C=41                        
    if WN<20 and WN>0 and DU<1.5 and DU>0 and CBR+IC+DM+F+EN+A+G+IP+FRG==0 : C=42
    if WN>25 and DU<1.5 and CBR+IC+DM+F+EN+A+G+IP+FRG==0 : C=43                      
    if WN>30 and DU< 1.5 and CBR+IC+DM+F+EN+A+G+IP+FRG==0 : C=44                     
    if DM>300 and WN+CBR+IC+F+EN+A+G+IP+FRG+DU==0 : C=45                        
    if FRG>30 and WN+CBR+IC+DM+F+EN+A+G+IP+DU==0 : C=46                        
    if A<20 and A>0 and FRG<30 and FRG>0 and WN+CBR+IC+DM+F+EN+IP+DU==0 : C=-47                  
    if A>20 and A<50 and F<30 and F>0 and WN+CBR+IC+DM+EN+G+IP+FRG+DU==0 : C=48                  
    if A>50 and FRG<30 and FRG>0 and WN+CBR+IC+DM+F+EN+G+IP+DU==0 : C=49                    
    if WN+CBR+IC+DM+F+EN+A+G+IP+FRG+DU==0 : C=50                          
    return C                           
                             
                             
def base_layer():
    K=0
    if C==1 and CP==1 and SA==1 and RU==1 : K=1                    
    if C==1 and CP==1 and SA==0 and RU==1 : K=2                    
    if C==1 and CP==1 and SA==0 and RU==0 : K=3
    if C==1 and CP==0 and SA==0 and RU==0 : K=4                    
    if C==2 and CP==1 and SA==1 and RU==1 : K=5                    
    if C==2 and CP==1 and SA==0 and RU==1 : K=6                    
    if C==2 and CP==1 and SA==0 and RU==0 : K=7                    
    if C==2 and CP==0 and SA==0 and RU==0 : K=8                    
    if C==3 and CP==1 and SA==1 and RU==1 : K=9                    
    if C==3 and CP==1 and SA==0 and RU==1 : K=10
    if C==3 and CP==1 and SA==0 and RU==0 : K=11                    
    if C==3 and CP==0 and SA==0 and RU==0 : K=12                    
    if C==4 and CP==1 and SA==1 and RU==1 : K=17                    
    if C==4 and CP==1 and SA==0 and RU==1 : K=14                    
    if C==4 and CP==1 and SA==0 and RU==0 : K=15                    
    if C==4 and CP==0 and SA==0 and RU==0 : K=16                    
    if C==5 and CP==1 and SA==1 and RU==1 : K=17                    
    if C==5 and CP==1 and SA==0 and RU==1 : K=18                    
    if C==5 and CP==1 and SA==0 and RU==0 : K=19                    
    if C==5 and CP==0 and SA==0 and RU==0 : K=20                    
    if C==6 and CP==1 and SA==1 and RU==1 : K=21                    
    if C==6 and CP==1 and SA==0 and RU==1 : K=22                    
    if C==6 and CP==1 and SA==0 and RU==0 : K=23                    
    if C==6 and CP==0 and SA==0 and RU==0 : K=24                    
    if C==11 and CP==1 and SA==1 and RU==1 : K=25                    
    if C==35 and CP==1 and SA==1 and RU==1 : K=25                    
    if C==11 and CP==1 and SA==0 and RU==1 : K=26                    
    if C==35 and CP==1 and SA==0 and RU==1 : K=26                    
    if C==11 and CP==1 and SA==0 and RU==0 : K=27                    
    if C==35 and CP==1 and SA==0 and RU==0 : K=27                    
    if C==11 and CP==0 and SA==0 and RU==0 : K=28                    
    if C==35 and CP==0 and SA==0 and RU==0 : K=28                    
    if (C==12 or C==13 or C==14 or C==16 or C==17 or C==18 or C==19 or C==23 or C==24 or C==25) and CP==1 and SA==1 and RU==1 : K=29  
    if (C==12 or C==13 or C==14 or C==16 or C==17 or C==18 or C==19 or C==23 or C==24 or C==25) and CP==1 and SA==0 and (RU==1 or RU==0) : K=30
    if (C==12 or C==13 or C==14 or C==16 or C==17 or C==18 or C==19 or C==23 or C==24 or C==25) and CP==0 and SA==0 and RU==0 : K=31  
    if C==15 or C==36 and CP==1 and SA==1 and RU==1 : K=32                  
    if C==15 or C==36 and CP==1 and SA==0 and RU==1 : K=33                  
    if C==15 or C==36 and CP==1 and SA==0 and RU==0 : K=34                  
    if C==15 or C==36 and CP==0 and SA==0 and RU==0 : K=35
    if C==37 and CP==1 and SA==1 and RU==1 : K=36                    
    if C==37 and (CP==1 or CP==0) and (SA==0 or SA==1) and (RU==0 or RU ==1) : K=37             
    if C==30 or C==31 and CP==1 and SA==0 and RU==1 : K=38                  
    if C==41 and CP==1 and SA==0 and RU==1 : K=39                    
    if C==41 and CP==1 and SA==0 and RU==0 : K=40
    if C==41 and CP==0 and (SA==1 or SA==0) and (RU==1 or RU==0) : K=41                
    return K



##### Main  Program #####
def main():
    print("Teras Construction Case   v3.0  (c) Adi Andrei / Radu Andrei / Technosophics Ltd 1992 - 2022")

    global  WN, WO, CBR, IC, DM, F, EN, A, G, IP, FRG, DU, C, K, CP, SA, RO, RU

    print("INTRODUCETI DATELE :")
    WN = Decimal(input("UMIDITATE NATURALA (WN)="))
    WO = Decimal(input("UMIDITATE OPTIMA  (WO)="))
    CBR = Decimal(input("CBR ="))
    IC = Decimal(input("INDICE CONSISTENTA (IC)="))
    DM = Decimal(input("DIMENSIUNE MAXIMA (DM)="))
    F = Decimal(input("FRACTIUNI FINE (F)="))
    EN = Decimal(input("ECHIVALENT NISIP  (EN)="))
    A = Decimal(input("ALTERABILITATE  (A)="))
    G = Decimal(input("TRACTIUNI GROSIERE (G)="))
    IP = Decimal(input("PLASTICITATE (IP)="))
    FRG = Decimal(input("FRAGMENTABILITATE (FRG)="))
    DU = Decimal(input("DENSITATE (DU)="))

    C = current_layer()

    if C == 0:
        print("*** CAZ NEIDENTifICAT. RECOMandAM INVESTISATII SUPLIIMENTARE")
    else:
        print("##### CAZUL DE CONSTRUCTIE (straturi curente) nr:", C)

    if input("DorITI IDENTifICAREA SI PENTRU STRATURILE DE ForMA?(D/N)") == 'D':
        CP = Decimal(input("CAPACITATE PorTANTA (CP)="))
        SA = Decimal(input("SENSIBILITAE LA ACTIUNEA APEI (SA)="))
        RO = Decimal(input("RISCUL DE UMEZIRE DIN APE SUBTERANE (RU)="))

        K = base_layer()
        if K == 0:
            print("*** CAZ NEIDENTifICAT. RECOMandAM INVESTISATII SUPLIIMENTARE")
        else:
            print("##### CAZUL DE CONSTRUCTIE (straturi baza) nr:", K)

if __name__ == "__main__":
    main()