ascii_to_int
============

.. code-block:: python

	def ascii_to_int(chaine)

_________________________________________________________________

**Algorithm**
-------------

Utils method : ascii to integer converter.

=============== ========== =======================
**Parameters**   **Type**   **Description**
**chaine**       *str*      The string to convert
=============== ========== =======================

:Returns: **list** : A list containing all integers values since ASCII. 

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	res = []
	for letter in chaine:
		res.append(ord(letter))
	return res