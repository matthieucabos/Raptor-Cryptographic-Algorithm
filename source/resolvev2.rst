resolve
=======

.. code-block:: python

	def resolve(liste)

_________________________________________________________________

**Algorithm**
-------------

This method compute the chained 2nd order equations to solve the numeric suit.
It permit us to get the ASCII values as a list.
To solve the system you have to instance the solver with the square root of term 0.
Once theorem zero done, you will apply the equation solver with square root of the 0-term as b,
a as 1 and c as -following term.
The algorithm sort the roots and take only positives ones.

============== =========== ========================================
**Parameters**   **Type**   **Description**
**liste**       *int list*  The computed multiplied list to solve
============== =========== ========================================

:Returns: **int list** : A list containing solved terms. 

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	res = []
	x = 0
	tmp2 = 0
	res.append(int(m.sqrt(liste[0])))
	tmp=res[0]
	for i in range (1,len(liste)):
		tmp2 = equa_2_nd(1,-tmp,-liste[i])
		x=tmp2-tmp
		res.append(int(x))
		tmp=tmp2
	return res
