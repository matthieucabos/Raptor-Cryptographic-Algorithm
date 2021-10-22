split_number
============

.. code-block:: python	

	def split_number(num)

_________________________________________________________________

**Algorithm**
-------------

Integer splitter using the inverse Horner scheme and get it as a list of digits.

=============== ========== =============================
**Parameters**   **Type**   **Description**
**num**         *int*        The integer to be splitted
=============== ========== =============================

:Returns: **list** : The splitted integer as list

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python	

	res=[]
	while(num>0):
		res.append(num % 10)
		num=int(num/10)
	return reverse(res)