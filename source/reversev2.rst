reverse
=======

.. code-block:: python

	def reverse(s)

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

	str= ""
	for i in s:
		str=i+str
	return str
		
