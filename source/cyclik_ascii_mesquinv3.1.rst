cyclik_ascii_mesquin
====================

.. code-block:: python	

	def cyclik_ascii_mesquin(current,int_chaine)

_________________________________________________________________

**Algorithm**
-------------

Compute a cyclik ascii separators into Upper letters from M to Z.
Get a third cyclic ascii set modulo length

============== =========== ===================================
**Parameters**   **Type**   **Description**
**current**     *str*        The current poncuation separator 
============== =========== ===================================

:Returns: **str** : The following separator from the defined 'sep' Set.

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	mesquin=['M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
	tmp=r.randint(0,11)
	res=mesquin[tmp]
	return res