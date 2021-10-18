#!/bin/bash

# Author : CABOS Matthieu
# Date : 01/10/2021

function Usage (){
	echo " This Script must be used with this correct syntax :

	./Automate.sh 1 1 String 

	to automate the crypting process where :
		* 1 define the mode (crypting)
		* 1 define the algorithm to use
		* String define the raw data entry

		
	It will produce two files Crypted.txt and Key.txt wich allow decrypting process

	or

	./Automate.sh 2 1


	to automate the decrypting process where :
		* 2 define the mode (decrypting).
		* 1 define the algorithm to use

	It need the Crypted.txt and Key.txt files to decrypt the full content.
	It will produce a res.txt file containing all raw decrypted contents.

	Each algorithm could be automated like that.
	"
}

mode=$1
raw_data=$3
raw_data=`echo $raw_data | tr ' ' '_'`
algo=$2

if [ $mode -eq 1 ]
then
	splitted=""
	count=0
	while [ -n "${raw_data:count:16}" ]
	do
		splitted=$splitted" ""${raw_data:count:16}"
		count=$((count + 16))
	done
	case $algo in
		1) ./expect_script.exp "$splitted" >> crypted.txt;;
		2) ./expect_script2.exp "$splitted" >> crypted.txt;;
	esac
	
	cat crypted.txt | grep "^[!\"#$%&()*+,./:;<=>?@][0-9a-z]" >> Crypted.txt   
	cat crypted.txt | grep "^[0-9]" >> Key.txt 
	rm crypted.txt
	tr '\n' '_' < Crypted.txt
	tr '\n' '_' < Key.txt
else
	tr '_' '\n' < Crypted.txt
	tr '_' '\n' < Key.txt
	splitted=""
	raw_crypted=`cat Crypted.txt`
	raw_key=`cat Key.txt`
	count_line=`wc -l Crypted.txt | cut -d " " -f1`
	count=1
	tmp=""
	line=""
	while [ $count -le $count_line  ]
	do
		tmp=""
		key=""
		tmp=`cat Crypted.txt | head -$count | tail -1`
		key=`cat Key.txt | head -$count | tail -1`
		echo $tmp >> tmp
		echo $key >> tmp
		count=$(( count + 1 ))
	done
	splitted=`cat tmp`
	case $algo in
		1) ./expectD_script.exp "$splitted" >> uncrypted.txt;;
		2) ./expectD_script2.exp "$splitted" >> uncrypted.txt;;
	esac
	count=10
	nb_line=`wc -l uncrypted.txt | cut -d ' ' -f1`
	while [ $count -le $nb_line ]
	do
		cat uncrypted.txt | head -$count | tail -1 >> res.txt
		count=$(( count + 9 ))
	done
	python3 Clear_res.py
	rm tmp
	rm uncrypted.txt
fi
