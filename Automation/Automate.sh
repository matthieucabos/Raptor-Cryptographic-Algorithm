#!/bin/bash

# Author : CABOS Matthieu
# Date : 01/10/2021

function Usage (){
	echo " This Script must be used with this correct syntax :

	./Automate.sh 1 String   

	to automate the crypting process where :
		* 1 define the mode (crypting)
		* String define the raw data entry

	or

	./Automate.sh 2 

	to automate the decrypting process where 2 define the mode (decrypting).

	Each algorithm could be automated like that.
	"
}

mode=$1
raw_data=$2

if [ $mode -eq 1 ]
then
	splitted=""
	count=0
	while [ -n "${raw_data:count:16}" ]
	do
		splitted=$splitted" ""${raw_data:count:16}"
		count=$((count + 16))
	done

# Automate via sub shell to make it faster.
	for item in $splitted
	do
		echo "c" ; echo $item | ./basetestrecursivev2 >> crypted.txt
	done

	Crypted_data=`cat crypted.txt | grep "^!"`
	Crypted_key=`cat crypted.txt | grep "^[0-9][0-9]*$"`

	echo $Crypted_data >> Crypted.txt  # length 101 / slice
	echo $Crypted_key  >> Key.txt      # length 16  / slice
	rm crypted.txt
else
	splitted=""
	splitted_key=""

	raw_crypted=`cat Crypted.txt`
	raw_key=`cat Key.txt`
	count=1
	while [ `echo $raw_crypted | cut -d " " -f$count` != '' ]
	do
		splitted=$splitted" "`echo $raw_crypted | cut -d " " -f$count`
		splitted=$splitted" "`echo $raw_key | cut -d " " -f$count`
		count=$((count + 1))
	done
	count=1

# Automate via sub shell to make it faster.	
	for item in $splitted 
	do
		set -- $item
		count=$((count + 1))
		if [ $((count % 2 )) -eq 0 ]
		then
			txt=$1
		else
			key=$1
			echo "c" | ./basetestrecursivev2_solveur.bin $txt $key >> uncrypted.txt
		fi
	done
fi