mesqui
======

.. code-block:: python	

	def mesqui(txt,seuil)

_________________________________________________________________

**Algorithm**
-------------

This method is used to create a wrong path of decrypting method.
Using a similar Separators terms, I define a 'fake' terms list wich have absolutely no meanings for the rest of the algorithm.
Using it as the last step of algorithm, it doesn't allow any brute force attack to decrypt.
The threshold value 'seuil' will define the amount of distribution of fake separators.

=============== ========== ==========================================================
**Parameters**   **Type**   **Description**
**txt**          *str*       The raw string to treat
**seuil**        *int*       The threshold variable to assign the 'fake terms' length
=============== ========== ==========================================================

:Returns: **str** : The fully 'fake splitted' crypted string

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	mesquin=['M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	res=''
	sep='M'
	for i in range(0,len(txt)):
		res+=txt[i]
		if(i%int((seuil))==0):
			res+=sep 
			sep=cyclik_ascii_mesquin(sep,int_chaine)
	return res