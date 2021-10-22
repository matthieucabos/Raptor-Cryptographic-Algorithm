miam
====

.. code-block:: python	

	def miam(key)

_________________________________________________________________

**Algorithm**
-------------

Key builder from the half key as integer list. It rebuild the missing half with a mirror copy of the first one.

=============== ========== ==========================
**Parameters**   **Type**   **Description**
**key**         *int list*   The half key as int list
=============== ========== ==========================

:Returns: **int list** : The full key rebuilded from the half key

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	tmp=''
	count=1
	res=[]
	for this in key:
		# print("this = "+str(this))
		# print("tmp = "+str(tmp))
		if(count%2==0):
			tmp+=str(this)
			count=1
			# print("tmp = "+str(tmp))
			res.append(tmp)
			tmp=''
		else:
			tmp=str(this)
			count+=1
	for i in range(0,len(res)):
		res[i]=int(res[i])
	return res