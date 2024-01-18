
.data
.balign 4
db_sour:   @ 1       2      3      4      5      6      7      8      9      0 
.ascii "LULU","LUCY","GEOO","LEON","AGUS","MAXI","MAJO","ALEX","TINA","ANDY" 
.ascii "GINA","LUPE","LINA","PATY","TONY","TONI","LISA","LOLA","LALO","ANIS" 
.ascii "ARON","EDDY","GUSS","IVAN","JAIR","ZACK","MAGY","RAFA","RAUL","RICO" 
.ascii "SAMY","FAVY","ISIS","VIKY","JUAN","MARY","CECI","GABY","LILI","DANI"
.ascii "NICO","CUCA","VERO","BERE","RENE","ROSA","SARA","SAUL","LUZZ","TEOO "  
.ascii "FLOR","PAME","LUIS","SUSY","TERE","JOSE","RAFA","POLO","PAZZ","PACO" 
.ascii "YOLA","ALMA","ROSY","ROSA","FANY","ELIA","ELII","BLAS","ANAA","SONY" 
.ascii "JENY","ERIC","ARES","EROS","ZEUS","IRIS","PEPE","KINO","BONI","ALDO" 
.ascii "LISA","DOLY","NORA","DORA","CRIS","CARO","REYY","IVON","BENI","ARAA" 

.balign 4
db_dest:   @ 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 
.word 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 
.word 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 
.word 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

.text
.global main

main:
    ldr r0,=db_sour
    ldr r1, =db_dest
    mov r5,0x5A

copy:
    ldr r2,[r0]
    str r2, [r1]
    add r0, #4
    add r1 ,#4
    subs r5,#1
    bne copy
    bx lr
