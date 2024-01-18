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
    mov r5,0x5A-1
    ldr r1,[r0] @en r1 va a estar el nombre menor
    rev r1,r1 
    add r0, #4
menor:
    ldr r2, [r0] @ en r2 esta el nombre sujeto a comparacion
    rev r2,r2 
    add r0,#4
    cmp r1,r2 @compara si r1 es en verdad menor
    bmi men 
    mov r1,r2  @ se guarda en r1 el nombre menor si en r1 habia un nombre mayor
men:
    subs r5,#1
    bne menor
    bx lr