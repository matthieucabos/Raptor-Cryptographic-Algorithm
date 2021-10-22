inv_transpose_base
==================

.. code-block:: python

	def inv_transpose_base(liste,key,table)

_________________________________________________________________

**Algorithm**
-------------

The inverse method to decrypt a str list of base transposed values

=============== ========== ===========================================
**Parameters**   **Type**   **Description**
**liste**       *str list*  The crypted list as String list
**key**         *int list*  The Base index list as key
**table**       *int list*  The full Base table recursively builded
=============== ========== ===========================================

:Returns: **int list** : The decrypted list as integers

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	res = []
	if(len(liste)!=len(key)):
		return []
	else:
		for i in range(0,len(liste)):
			if(key[i]==10):
				res.append(int(liste[i]))
			else:
				res.append(int(table[key[i]-2].index(liste[i])))
	return res