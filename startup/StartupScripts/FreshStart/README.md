# Custumized Startup Settings

## Notes

The functions of this addons are in reality obsolete; custom changes for startup regarding scene and settings can be saved as a startup file, using File > Defaults > Save Startup File.

The purpose of this project is for creating understanding of working with Blender API and Python, interacting with properties using code, and setting requirements for when changes are to be applied.


## INSTALLATION
Gå till Preferences > Add-ons, välj installera. Lägg till ZIP-filen.


## INSTÄLLNINGAR - Hur du gör egna anpassningar av detta add-on
Du kan göra egna justeringar i FreshStart_ini.txt för ett antal förinställda anpassningar.
Du kan slå av och på eller justera anpassningar genom att ändra värden i FreshStart_ini.txt.
Numeriska alternativ för inställningar anges till höger.

### I enkelhet:
För att göra ändringar, byt ut ett värde mot ett annat.
OBS. Ange värden i heltal.
0-1 alternativ slår av eller på en inställning.
Övriga återger värden i jämna intervall enligt angivelse.


### ÄNDRINGAR I FILEN
Se till att ändringarna är sparade i den komprimerade filen.
Ditt Windows eller ditt komprimeringsverktyg löser antagligen detta.

I annat fall kan du öppna den komprimerade mappen, flytta ut filen, gör ändringarna och flytta tillbaka den.
Se då till att ZIP-filen innehåller:
- FreshStart.py
- FreshStart_ini.txt
- README.md


### FÖRTYDLIGANDE AV INSTÄLLNINGAR
- remove_cube:1
  0: av, 1: på och tar då alltså bort kuben
- remove_light:1
  0: av, 1: på
- add_sun:1
  0: av, 1: på. Om den är satt till 0 finns ingen sol och övriga inställningar för "Sol" saknar betydelse.
- sun_strength:4
  Jämna steg 0-9, motsvarar direkt ljusstyrkan. Med 0 så lyser den dock inte alls.
  4-5 är en bra utgångspunkt.
- sun_inclination:3
  Jämna steg 0-9, motsvarar 0-90 grader. 0 innebär att solen lyser rakt ned, 9 så lyser den parallellt med marken.
  3-6 är en bra utgångspunkt för dagsljus.
- sun_direction:1
  Jämna steg 0-9, varje steg är 36 grader i medsols rotation. 
  Förutsatt att solen har en lutning (sun_inclination över 0): 
  Med 0 lyser solen framåt (+y-riktning), 5 bakåt (-y-riktning).
  Med vyn/kameran i +y-riktning: 1-2 lyser framåt åt höger, 8-9 från vänster.
  

### Format: 
Function:value       Element, förklaring (värden i heltal) (effekt)
Function: vilken funktion
value: värdet som påverkar funktionen, DEN ENDA DU SKA ÄNDRA PÅ.
Element: om flera inställningar påverkar samma objekt eller kategori så har de samma namn här.


