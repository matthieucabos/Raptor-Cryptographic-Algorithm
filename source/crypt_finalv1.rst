crypt_final
===========

.. code-block:: python

	def crypt_final(tuple)

_________________________________________________________________

**Algorithm**
-------------

The layout procedure to organise crypting results.

=============== ========== ===================================================================
**Parameters**   **Type**   **Description**
**tuple**        *tuple*     List couple representing the crypted strin and the associated key
=============== ========== ===================================================================

:Returns: **str** : The crypted list as a string with correct separators

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	res = ''
	sep = '!'
	crypt=tuple[0]
	key=tuple[1]
	for i in range (0,len(crypt)):
		res+=sep+str(crypt[i])
		sep=cyclik_ascii(sep)
	return res
