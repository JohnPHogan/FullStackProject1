class data_initiator():

    from StandardData import standard_data as sd


    def __init__(self, test_flag = False, alt_flag = False):
        self.my_data_object = None
        try:
            if test_flag == False:
                '''if this fails to instantiate variable, following test should
                fail '''

                if alt_flag == False:
                    self.my_data_object = self.sd()

            if self.my_data_object == None:
                raise TypeError('TypeError', 'None',
                'data_initiator was not created')

        #catch expected failure
        except TypeError as type_error:
            raise type_error

        #catch any unexpected failure
        except Exception as e:
            raise e

    def get_keys(self):
        return self.my_data_object.get_keys()

    def get_data_object(self):
        return self.my_data_object.get_movies()
