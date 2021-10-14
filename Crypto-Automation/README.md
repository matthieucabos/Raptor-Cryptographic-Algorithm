# Raptor-Cryptographic-Algorithm Automation

**Author**  CABOS Matthieu

**Release Date** 21/09/2021

This script has been thinked to automate the Raptor Cryptographic Algorithm.
It allow to crypt much larger String as raw data band.

This Script must be used with this correct syntax :

**./Automate.sh** *1 String*

to automate the crypting process where :
  * **1** define the mode (crypting)
  * **String** define the raw data entry

It will produce two files *Crypted.txt* and *Key.txt* wich allow decrypting process

or

**./Automate.sh** *2*

To automate the decrypting process where **2** define the mode (decrypting).
It need the *Crypted.txt* and *Key.txt* files to decrypt the full content.
It will produce a res.txt file containing all raw decrypted contents.

Each independant Raptor Cryptographic Algorithm could be automated like that.
