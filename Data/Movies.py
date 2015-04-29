class movies():

    def __init__(self, keys):

        self.values = {}
        try:
            #set the variable to fail test
            self.keys = keys

            if type(self.keys) != list:
                raise TypeError('TypeError', 'None',
                'movie object did not get list of keys')

        #catch expected failure
        except TypeError as type_error:
            raise type_error

        #catch any unexpected failure
        except Exception as e:
            raise e

    def load_data(self, data):

        self.movie_data = data
        try:
            if type(self.movie_data) == dict:

                self.values.update({k: v for k, v in data.iteritems()})

            else:
                raise TypeError('TypeError', 'type(data)',
                'movie.load_data did not receive dict')

        # Catch initial type error
        except TypeError as type_error:
            raise type_error
        except Exception as e:
            raise e
