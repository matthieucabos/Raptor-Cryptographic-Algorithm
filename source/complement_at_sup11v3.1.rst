complement_at_sup11
===================

.. code-block:: python	

	def complement_at_sup11(x,table,base=11)

_________________________________________________________________

**Algorithm**
-------------

This function is used to compute the complement value from the original one in his own base.
I use a temporary variable to store the numeric value of the compement and restitute it in his own base.

=============== =============== ===================================================
**Parameters**   **Type**       **Description**
**x**            *str*           A string representation of my base converted value
**table**        *list of list*  The full Base Table array
**base**         *int*           The base index of the current value
=============== =============== ===================================================

:Returns: **str** : The complmented value in his own Base.

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	nb_char=len(x)
	local_max=0
	for i in range(0,nb_char):
		local_max+=(base-1)*base**i
	num_value=local_max-get_value(x,table,base)
	return table[base][num_value]