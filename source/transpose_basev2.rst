transpose_base
==============

.. code-block:: python

	def transpose_base(liste,key,table)

_________________________________________________________________

**Algorithm**
-------------

A method to transpose an integer list to the corresponding key's base index
=> The result will be a succession of transposed values from differents integers to differents base

=============== ========== ============================================
**Parameters**   **Type**   **Description**
**liste**       *list*        the integer converted since ASCII list
**key**         *list*        The Base index list as key
**table**       *list*        The full Base Table recursively builded
=============== ========== ============================================

:Returns: **str list** : The crypted list as String list

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	res = []
	if(len(liste)!=len(key)):
		return []
	else :
		for i in range (0,len(liste)):
			if(key[i]==10):
				res.append(liste[i])
			else:
				res.append(table[key[i]-2][liste[i]])
	return res
