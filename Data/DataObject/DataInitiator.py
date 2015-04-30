'''
Class data_initiator

Public methods: __init__, get_movies

This class is the wrapper class to the the standard_data class.  It is used by data_manager to get the html template data.  By changing the class data_initiator imports from, you can change the movie data loaded into the web page.

DO NOT ACCESS CLASS VARIABLES DIRECTLY!!  ONLY USE THE DEFINED METHODS TO GUARANTEE THAT ANY INCLUDED ERROR CHECKING OR FORMATTING OCCURS.
'''

class data_initiator():

    # Change the import to load a different set of movie data
    from StandardData import standard_data as sd

    def __init__(self, test_flag = False):
        self.my_data = None
        try:
            if test_flag == False:
                '''if this fails to instantiate variable, following test should
                fail '''
                self.my_data = self.sd()

            if self.my_data == None:
                raise TypeError('TypeError', 'None',
                'data_initiator was not created')

        #catch expected failure
        except TypeError as type_error:
            raise type_error

        #catch any unexpected failure
        except Exception as e:
            raise e

    # Public method that wraps the defined get_movies method of the imported 
    # movie data class
    def get_movies(self):

        return self.my_data.get_movies()
