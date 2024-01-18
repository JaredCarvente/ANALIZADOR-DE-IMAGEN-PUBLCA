.data
.balign 4
db_sour:
  .ascii "LULU","LUCY","GEO ","LEON","AGUS","MAX ","MAJO","ALEX","TINA","ANDY"
  .ascii "GINA","LUPE","LINA","PATY","TONY","TOÑO","LISA","LOLA","LALO","ANIS"
  .ascii "ARON","EDDY","GUS ","IVAN","JAIR","ZACK","MAGY","RAFA","RAUL","RICO"
  .ascii "SAMY","FAVY","ISIS","VIKY","JUAN","MARY","CECI","GABY","LILI","DANI"
  .ascii "NICO","CUCA","VERO","BERE","RENE","ROSA","SARA","SAUL","LUZ ","TEO "    
  .ascii "FLOR","PAME","LUIS","SUSY","TERE","JOSE","RAFA","POLO","PAZ ","PACO"
  .ascii "YOLA","ALMA","ROSY","ROSA","FANY","ELIA","ELI ","BLAS","ANA ","SONY"
  .ascii "JENY","ERIC","ARES","EROS","ZEUS","IRIS","PEPE","KINO","BONI","ALDO"
  .ascii "LISA","DOLY","NORA","DORA","CRIS","CARO","REY ","IVON","BENI","ARA "  
.balign 4
db_dest:   @ 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 
.word 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 
.word 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 
.word 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

.text
.balign 4
.global main
main:

	ldr r0,=db_sour
	ldr r1,=db_dest
	MOV R5,#0x5A
	
copy:
	LDM R0!,{R2}
	STM R1!,{R2}
	subs r5,#1
	bne copy
	bx lr
.end
