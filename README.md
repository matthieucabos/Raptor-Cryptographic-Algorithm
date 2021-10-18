# Raptor-Cryptographic-Algorithm

**Author**  CABOS Matthieu

**Release Date** 21/09/2021

**Raptor Cryptographic Algorithm Official Full Source Code and Documentation Distribution Repository**

______________________________________________________________________________________________________

This work project have been released under **Licence GNU General Public License v3.0** 

Project release @ **CNRS laboratory ICGM - Montpellier, FRANCE**         

Source Code release @ **CNRS laboratory INRAE/TSE - Toulouse, FRANCE**   

______________________________________________________________________________________________________

## Setup

Build the html Documentation from the **make html** command.

The full printable pdf is avaible inside the Repository.

See Full documents @ : https://raptor-cryptographic-algorithm.readthedocs.io/en/latest/


## Compilation
  
 Each algorithm can be indepedantly compiled via the command
 ```bash
 python3 -m nuitka --follow-imports Algorithm_to_compile
 ```
 This compilation need the nuitka module, avaible using the following command :
  ```bash
 pip install nuitka
  ```
 
## Use

To use, you can test each algorithm individually. 

If you want to automate the process, use the Shell Script Automate.sh found in the Crypto-Automation Repertory.

You can use the associated *Crypted.txt* and *Key.txt* file to get an example of decrypting process, wrote into res.txt using the decrypting process.

The Shell Script must be use with the following syntax :

***********************************************

### Crypting Process

 ```bash
./Automate.sh 1 1 Data_as_string_to_crypt

./Automate.sh <Mode> <Algorithm> <Data_as_string_to_crypt>
 ```  
and will produce two file : *Crypted.txt* and *Key.txt* representing the crypted data.

***********************************************

### Decrypting Process

  ```bash 
./Automate.sh 2 1

./Automate.sh <Mode> <Algorithm>
  ``` 
 will read the *Crypted.txt* and *Key.txt* files and will produce a res.txt containing uncrypted string.
 
 Results are shown as line by line result, wich can be colmated removing '\n' instances using the Clear_res.py Script.
 
 ```bash 
 python3 Clear_res.py
  ```
 It will give the clear text.
 
 ***********************************************
 
## Support

For any support request, contact @ matthieu.cabos@umontpellier.fr
