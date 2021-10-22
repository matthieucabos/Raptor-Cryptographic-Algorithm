tablebase
=========

.. code-block:: python	

	def tablebase(base)

_________________________________________________________________

**Algorithm**
-------------
This method allow to build the first step Numeric Base Transposition Table.
I use the Horner's scheme procedure to build the correct table independantly of the base index.
I can build Base from 1->a to 1->z, mean Base11 to Base36.
	
=============== ========== ===========================
**Parameters**   **Type**   **Description**
**base**        *int*        The base index to build
=============== ========== ===========================

:Returns: **list** : The builded first step base table.

_________________________________________________________________

**Source Code**
---------------
.. code-block:: python	

	res = []
	letter = 'a'
	letterbis = 'A'

	for i in range(0,base):
		if(i<10 or (i<=10 and base <=10)):
			res.append(str(i))
		if(i>=10 and base >10 and base<37):
			res.append(letter)
			letter=chr(ord(letter)+1)

	return res
