# Crypto-Automator

*******************************************

**Author** : *CABOS Matthieu*

**Date** : *27/10/2021*

**Organisation** : *ICGM-CNRS*

*******************************************

## Usage

As you can see, there is 4 Automate files in this folder, called :
* **Automate_v0.sh** : This is the Zero-version of the automate
* **Automate.sh** : This is the v1 of the automate
* **Automate_v2.sh** : This is the v2 of the automate
* **Automate.py** : This is the Python-version of the automate

I will explain for each of them the differents commands to use.

## Requirements

All these shell Script need the expect command, which can be founded with

```bash
sudo apt install expect
```

The Python Script also use an expect command line, which can be found with

```bash
pip3 install pexpect
```

*******************************************

## Automate.py


*******************************************

The Automate.py is a simple copy of the shell Automate algorithm.

This Script must be used with this correct syntax :

### Crypting Process

The Automate.py use the Raptor Algorithms Comiled as bin.
It could be called via :

```bash
python3 Automate.py 1 1 16 String

python3 Automate.py <mode> <algorithm> <slice size> <String>
```

Where:
* **mode** define the way to act between
  * *1* : Crypting Mode
  * *0* : Uncrypting Mode
* **algorithm** define the algorithm to use (between 1 & 2 for the moment, should be extended to [1,2,3,4,5] set)
* **slice_size** define the size of the differents slices of the raw String (which will be splitted from slice size)
* **String** represent the data to cryupt as string values.

It will produce a single Crypted.txt file representing the ful crypted data.

### Uncrypting Process

It could be called via :

```bash
python3 Automate.py 0 1 16

python3 Automate.py <mode> <algorithm> <slice size>
```

Where:
* **mode** define the way to act between
  * *1* : Crypting Mode
  * *0* : Uncrypting Mode
* **algorithm** define the algorithm to use (between 1 & 2 for the moment, should be extended to [1,2,3,4,5] set)
* **slice_size** define the size of the differents slices of the raw String (which will be splitted from slice size)

The uncrypting process need the unique Crypted.txt file produced from the same Automate.
It will produce an Uncrypted.txt file containing the preserved raw data vector as string.

*******************************************

## Automate_v0.sh


*******************************************

The Automate_v0 only use the first Raptor Comiled Algorithm as bin.
This Script must be used with this correct syntax :

### Crypting Process

```bash
./Automate_v0.sh 1 <String> 

./Automate_v0.sh <mode> <String> 
```

To automate the crypting process where :
* **1** define the **mode** (crypting)
* **String** define the raw data entry
		
It will produce two files Crypted.txt and Key.txt wich allow decrypting process

### Uncrypting Process

```bash
./Automate_v0.sh 2 

./Automate_v0.sh <mode>
```

To automate the decrypting process where:
* **2** define the **mode** (uncrypting)

It need the Crypted.txt and Key.txt files to decrypt the full content.
It will produce a res.txt file containing all raw decrypted contents.
Each algorithm could be automated like that.

*******************************************

## Automate.sh


*******************************************

The Automate.sh use the v1 & v2 of the Raptor Compiled Algorithm.

This Script must be used with this correct syntax :

### Crypting Process

```bash
./Automate.sh 1 1 <String> 

./Automate.sh <mode> <algorithm> <String> 
```

To automate the crypting process where :
* **1** define the **mode** (crypting)
* **1** define the **algorithm** to use (between 1 and 2)
* **String** define the raw data entry
		
It will produce two files Crypted.txt and Key.txt wich allow decrypting process

### Uncrypting Process

```bash
./Automate.sh 2 1
./Automate.sh <mode> <algorithm> 
```

To automate the decrypting process where :
* **2** define the **mode** (decrypting).
* **1** define the **algorithm** to use

It need the Crypted.txt and Key.txt files to decrypt the full content.
It will produce a res.txt file containing all raw decrypted contents.

Each algorithm could be automated like that.


*******************************************

## Automate_v2.sh


*******************************************

The Automate.sh use each of the Raptor Compiled Algorithm.

This Script must be used with this correct syntax :

### Crypting Process

```bash
./Automate_v2.sh 1 1 16 String

./Automate_v2.sh <mode> <algorithm> <slice size> <String> 
```

To automate the crypting process where :
* **1** define the **mode** (crypting)
* **1** define the **algorithm** to use (between 1,2,3,4 & 5 representing respectively the v1, v2, v3, va1 & va2 versions of the Raptor)
* **16** define the **slice size** of the data (must be contained in [4,24]
* **String** define the raw data entry
		
It will produce two files Crypted.txt and Key.txt wich allow decrypting process

### Uncrypting Process

```bash
./Automate_v2.sh 2 1
./Automate_v2.sh <mode> <algorithm> 
```

To automate the decrypting process where :
* **2** define the **mode** (decrypting).
* **1** define the **algorithm** to use

It need the Crypted.txt and Key.txt files to decrypt the full content.
It will produce a res.txt file containing all raw decrypted contents.

Each algorithm could be automated like that.


*******************************************

## Support

For any support request, please to mail @ matthieu.cabos@uontpellier.fr
