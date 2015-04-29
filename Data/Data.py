from DataObject.DataInitiator import data_initiator as di
from Movies import movies as mov

class data_manager():

    def __init__(self, test_flag = False, alt_flag = False):

        try:
            #set the variable to fail test
            self.data_initiator = None
            if test_flag == False:
                #if this fails to instantiate variable, following test should
                #fail
                self.data_initiator = di(alt_flag)

            if self.data_initiator == None:
                raise TypeError('TypeError', 'None',
                'data_initiator was not created')

        #catch expected failure
        except TypeError as type_error:
            raise type_error
        except Exception as e:
            raise e

    def get_data_object(self, test_flag = False):

        if test_flag == True:
            self.data_object = None
        else:
            self.data_object = self.data_initiator.get_data_object()

        try:
            if type(self.data_object) != list:
                raise TypeError('TypeError',
                                type(self.data_object),
                                "get_data_object did not receive correct data.")

        except TypeError as type_error:
            raise type_error
        except Exception as e:
            raise e

    def build_movie_list(self):

        #populate the data_object
        self.get_data_object()

        data_keys = self.data_initiator.get_keys()
        movie_list = []
        for data in self.data_object:
            #instantiate a new movie object
            movie_data = mov(data_keys)
            #load the data into the object
            movie_data.load_data(data)
            #add it to the movie_list
            movie_list.append(movie_data)

        return movie_list

    def get_movies(self):

        return self.build_movie_list()

    def get_keys(self):
        return self.data_initiator.get_keys()
