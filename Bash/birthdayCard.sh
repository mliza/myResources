#!/usr/local/bin/bash
figlet -f banner3 -w 100 -c 'Happy Birthday' > birthday.txt; 
#echo " " >> birthday.txt; 
jp2a koala.jpg --size=100x90 | sed 's/M/ /g' | sed 's/W/ /g' | sed 's/N/ /g' >> birthday.txt
echo " " >> birthday.txt; 
figlet -f banner3  -w 100 -c 'Danee' >> birthday.txt; 
cat birthday.txt
