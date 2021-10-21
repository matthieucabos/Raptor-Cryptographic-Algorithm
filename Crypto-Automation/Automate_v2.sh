#!/bin/bash

# Author : CABOS Matthieu
# Date : 01/10/2021

function Usage (){
	echo " This Script must be used with this correct syntax :

	./Automate.sh 1 1 16 String 

	to automate the crypting process where :
		* 1 define the mode (crypting)
		* 1 define the algorithm to use
		* 16 define the size of the data slice
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

if [ "$1" == '-h' ] || [ "$1" == '--help' ]
then
	Usage
	exit
fi

if [ $3 -lt 2 ] && [ $3 -gt 28 ]
then
	echo "Slice size must be included in [2,28]"
	exit 
fi

mode=$1
algo=$2
slice_size=$3
raw_data=$4 
raw_data=`echo $raw_data | tr ' ' '_'`

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
		1) ./expect_script.exp "$splitted"  >> crypted.txt;;
		2) ./expect_script2.exp "$splitted" >> crypted.txt;;
		3) ./expect_script3.exp "$splitted" >> crypted.txt;;
		4) ./expect_script4.exp "$splitted" >> crypted.txt;; # Here
		5) ./expect_script5.exp "$splitted" >> crypted.txt;; # Here
	esac
	case $algo in
		1 | 2 | 3 ) cat crypted.txt | grep "^[!\"#$%&()*+,./:;<=>?@][0-9a-z]" >> Crypted.txt   
					cat crypted.txt | grep "^[0-9]" >> Key.txt 
					rm crypted.txt;;
		4 | 5 ) cat crypted.txt | grep "^([0-9a-z]{4,6}[!\"#$%&()*+,.\/:;<=>?@])+" >> Crypted.txt
				cat crypted.txt | grep "^([0-9]{1,3}[-!\"#$%&()*+,./:;<=>?@])*" >> Key.txt 
				rm crypted.txt;;
	esac
else
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
	# splitted=`cat tmp`
	splitted= eval cat tmp

	case $algo in
		1) ./expectD_script.exp "$splitted" >> uncrypted.txt;;
		2) ./expectD_script2.exp "$splitted" >> uncrypted.txt;;
		3) ./expectD_script3.exp "$splitted" >> uncrypted.txt;;
		4) ./expectD_script4.exp "$splitted" >> uncrypted.txt;;  # Here
		5) ./expectD_script5.exp "$splitted" >> uncrypted.txt;;  # Here
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
