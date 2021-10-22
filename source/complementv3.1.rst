complement
==========

.. code-block:: python	

	def complement(x,table,base=2)

_________________________________________________________________

**Algorithm**
-------------

The complement function is the full algorithm combining the complement_at_sup11 and complement_at functions.
I specify the way to take between both of them using an if then else structure.

=============== =============== =====================================================
**Parameters**    **Type**       **Description**
**x**            *str*            A string representation of my base converted value
**table**        *list of list*   The full Base Table array
**base**         *int*            The base index of the current value
=============== =============== =====================================================

:Returns: **str** : The complmented value in his own Base.

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	final_res=0
	if(base<=10):
		splitted=split_number(int(x))
		for i in range(0,len(splitted)):
			splitted[i]=complement_at(splitted[i],base)
			final_res*=10
			final_res+=splitted[i]
		return final_res
	else:
		final_res=complement_at_sup11(x,table,base)
		return final_res