'''
Class html_initiator

Inherits from class html_base
Public methods: __init__, header, body, var

This class is the wrapper class to the html_base class and is the class used by html_manager to get the html template data.  By changing the class html_initiator inherits from, you can change the html template contents.

DO NOT ACCESS CLASS VARIABLES DIRECTLY!!  ONLY USE THE DEFINED METHODS TO GUARANTEE THAT ANY INCLUDED ERROR CHECKING OR FORMATTING OCCURS.
'''

# change the import to change the html template loaded
from HTMLBase import html_base as hb

class html_initiator(hb):


    def __init__(self, test_flag = False):

        try:

            if test_flag == True:
                raise TypeError('TypeError',
                                'None',
                                'html_initiator could not initiate')
            else:
                '''this will generate it's own exception if created in it's
                __init__ method.  It does not need to inherit test_flag.
                '''
                hb.__init__(self)


        except TypeError as type_error:
            raise TypeError
        except Exception as e:
            raise e


    # Calls the parent class header method
    def header(self):
        return hb.header(self)

    # Calls the parent class body method
    def body(self):
        return hb.body(self)

    # Calls the parent class var method
    def var(self):
        return hb.var(self)
