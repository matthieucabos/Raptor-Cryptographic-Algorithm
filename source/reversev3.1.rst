reverse
=======

.. code-block:: python	

	def reverse(liste)

_________________________________________________________________

**Algorithm**
-------------

A function to reverse a string as argument.

============== ========== ========================
**Parameter**   **Type**   **Description**
**s**           *String*   The string to reverse
============== ========== ========================

:Returns: **str** : The reversed string

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python	

	res=[]
	for i in range(0,len(liste)):
		res.append(liste[len(liste)-i-1])
	return res