'''
Class:  data_manager

Public methods: __init__, get_movies

 This class manages retrieving the movie data and then populating instances of the data_object class.  It is the interface for the calling program needs to invoke.  It handles loading the appropriate DataInitiator class.

    NOTE:  DO NOT DIRECTLY ACCESS THE CLASS VARIABLES.  ALWAYS USE THE get_ and
    set_ methods!!!!

    Directly accessing class variables bypasses error checking.

'''

from DataObject.DataInitiator import data_initiator as di
# Change this to reflect changes to html_base
from  DataObject.StandardDataObject import standard_data_object as sdo

class data_manager():

    def __init__(self, test_flag = False):

        try:
            #set the variable to fail test
            self.data_initiator = None
            if test_flag == False:
                #if this fails to instantiate variable, following test should
                #fail
                self.data_initiator = di()

            if self.data_initiator == None:
                raise TypeError('TypeError', 'None',
                'data_initiator was not created')

        #catch expected failure
        except TypeError as type_error:
            raise type_error
        except Exception as e:
            raise e

    '''
    This method gets the defined movie data from data_initiator.  This method should only be used by get_movies and should not be invoked outside of the class
    '''
    def get_movie_data(self, test_flag = False):

        movies = None

        if test_flag == False:
            # Retrieve data from data_initiator
            movies = self.data_initiator.get_movies()

        try:
            if type(movies) != list:
                raise TypeError('TypeError',
                                type(movies),
                                "get_movie_data did not receive correct data.")

        except TypeError as type_error:
            raise type_error
        except Exception as e:
            raise e

        return movies

    '''
    This method takes the data from get_movie_data and creates an instance of the standard_data_object class (or whatever class replaces it) for each entry defined.
    '''
    def get_movies(self, test_flag = False):

        movie_data = self.get_movie_data()
        movie_list = []

        try:
            if test_flag == False:
                for movie in movie_data:

                    '''
                    Create an instance of the standard_data_object class or whatever class replaces it to match the change to html_base
                    '''
                    movie_entry = sdo(movie['title'], movie['poster'], movie['URL'])
                    if movie_entry == None:
                        raise TypeError('TypeError',
                                        type(movie_entry),                                            "could not create sdo object.")

                    '''
                    Append the newly created movie_entry to the movie_list class
                    '''
                    movie_list.append(movie_entry)

            else:
                #test_flag overwritten to force an error in testing
                raise TypeError('TypeError',
                                'None',                                            "could not create sdo object.")

        except TypeError as type_error:
                raise type_error

        return movie_list
