# Raptor-Cryptographic-Algorithm

**Author**  CABOS Matthieu

**Release Date** 21/09/2021

**Raptor Cryptographic Algorithm Official Full Source Code and Documentation Distribution Repository**

This work project have been released under **Licence GNU General Public License v3.0** 

Project release @ **CNRS laboratory ICGM - Montpellier, FRANCE**         

Source Code release @ **CNRS laboratory INRAE/TSE - Toulouse, FRANCE**   

# Setup

Build the html Documentation from the **make html** command.

The full printable pdf is avaible inside the Repository.

See Full documents @ : https://raptor-cryptographic-algorithm.readthedocs.io/en/latest/


# Compilation
  
 Each algorithm can be indepedantly compiled via the command
  
 **python3 -m nuitka --follow-imports** *Algorithm_to_compile*
 
# Use

To use, you can test each algorithm individually. 

If you want to automate the process, use the Shell Script Automate.sh found in the Crypto-Automation Repertory.

The Shell Script must be use with the following syntax :


Crypting Process
----------------

**./Automate.sh** 1 *Data_as_string_to_crypt*
  
and will produce two file : Crypted.txt and Key.txt representing the crypted data.
  
Decrypting Process
------------------
  
**./Automate.sh 2**
  
 will read the Crypted.txt and Key.txt files and will produce a res.txt containing uncrypted string.
 
 Results are shown as line by line result, wich can be colmated removing '\n' instances.
  
 
# Support

For any support request, contact @ matthieu.cabos@umontpellier.fr
