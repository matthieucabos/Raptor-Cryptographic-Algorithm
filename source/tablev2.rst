table
=====

.. code-block:: python

	def table()

_________________________________________________________________

**Algorithm**
-------------

Base table recursive builder. 
The generated Base table array is defined via :

	* **base** : Define the base to begin the table
	* **debut** : Define the first value of Base table 
	* **fin** : Define the last value of Base table
	* **inc** : Define the incrementation step

=============== =========== =================================================
**Parameters**   **Type**   **Description**
**base**         *int*       The first base of the table
**debut**        *int*       The first value of the table in the given base
**fin**          *int*       The last value of the table in the given base
**inc**          *int*       The value of incrementation step
=============== =========== =================================================

:Returns: **Str** : A string containing all the base generated representing the array (see conversion later)

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python	

	represent=''
	letter='a'
	powIndex=0
	count=0
	if(fin>10*base):
		fin=10*base
	for i in range(debut,fin):
		current=i
		if(i<base):
			if(i<10):
				represent+=str(i)
			else:				
				represent+=letter
				letter=chr(ord(letter)+1)
			if(i==base-1):
				letter='a'
		else:
			tmp=''
			while(current/base!=0):
				count=powIndex*10*base
				if(not current%(10*base)):
							powIndex+=1
				if(base<10):
					tmp+=str(current%base)
				else:					
					if(current%base<10):
						tmp+=str(current%base)
					else:
						tmp+=letter										
						if(count==0):
							letter=chr(ord(letter)+1)
						else:
							count-=1						
						if(current%base==base-1):
							letter='a'				
				current=int(current/base)
			represent+=reverse(tmp)
		represent+="\n"
	return represent