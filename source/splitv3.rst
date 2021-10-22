split
=====

.. code-block:: python	

	def split(chaine,seuil)

_________________________________________________________________

**Algorithm**
-------------

Split the given string argument 'chaine' into slices from threshold size 'seuil'.
Each of this slices are allowed into the cryptographic algorithm.

============== ========== ============================================
**Parameters**   **Type**   **Description**
**chaine**     *str*        The full string to treat
**seuil**      *int*        Define the threshold size of the slices
============== ========== ============================================

:Returns: **str list** : The slices list as result	

_________________________________________________________________

**Source Code**
---------------
 
.. code-block:: python

	res = []
	tmp = ''
	index = 0
	div=int(len(chaine)/seuil)
	for i in range(0,div):
		tmp=''
		for j in range(index,(index+seuil)):
			tmp+=chaine[j]
			if(j==(index+seuil-1)):
				index=j+1
		res.append(tmp)
	if((index-1)<len(chaine)):
		tmp=chaine[index:]
		res.append(tmp)
	return res