# Raptor-Cryptographic-Algorithm Automation

**Author**  CABOS Matthieu

**Release Date** 21/09/2021

**Organisation** ICGM-CNRS

______________________________________________________________________________________________________

This script has been thinked to automate the Raptor Cryptographic Algorithm.
It allow to crypt much larger String as raw data band.

This Script must be used with this correct syntax :

**./Automate.sh** *1 String*

to automate the crypting process where :
  * **1** *define the mode (crypting)*
  * **String** *define the raw data entry*

It will produce two files *Crypted.txt* and *Key.txt* wich allow decrypting process

or

**./Automate.sh** *2*

To automate the decrypting process where **2** define the mode (decrypting).
It need the *Crypted.txt* and *Key.txt* files to decrypt the full content.
It will produce a res.txt file containing all raw decrypted contents.

Each independant Raptor Cryptographic Algorithm could be automated like that.

The final res.txt can be arranged using the **Clear_res.py** Script using the following syntax :

**python3 Clear_res.py** *res.txt*

Where res.txt is the raw content of the decrypting process.
 
# Support

For any support request, contact @ matthieu.cabos@umontpellier.fr
