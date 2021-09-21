base_key
========

.. code-block:: python	

	def base_key(int_chaine)

_________________________________________________________________

**Algorithm**
-------------

This is the key builder.

=============== =========== ===================================================
**Parameters**   **Type**   **Description**
**int_chaine**  *int list*   The base index list as a starting builder for key
=============== =========== ===================================================

:Returns: **int list** : the builded key from index base list.

_________________________________________________________________

**Source Code**
---------------
 
.. code-block:: python

	res=[]
	for i in range (0,len(int_chaine)):
		tmp=((int_chaine[i]*int_chaine[len(int_chaine)-i-1]+10)%36)
		if(tmp<10):
			tmp+=10
		res.append(tmp)
	return res 