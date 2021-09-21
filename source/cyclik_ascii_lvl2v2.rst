cyclik_ascii_lvl2
=================

.. code-block:: python

	def cyclik_ascii_lvl2(current)

_________________________________________________________________

**Algorithm**
-------------

Compute a cyclik ascii separators into ponctuation signs.
Get a second cyclic ascii set modulo length

============== =========== ===================================
**Parameters**   **Type**   **Description**
**current**     *str*        The current poncuation separator 
============== =========== ===================================

:Returns: **str** : The following separator from the defined 'sep' Set.

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	sep=[":",";","<","=",">","?","@"]
	tmp=((sep.index(current)+1)%6)
	res =sep[tmp]
	return res
