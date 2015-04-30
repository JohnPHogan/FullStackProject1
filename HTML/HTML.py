'''
Class:  html_manager

Public methods: __init__, get_header, get_body, get_variable

 This class manages retrieving the HTML templates.  It is the interface for the calling program needs to invoke.  It handles loading the appropriate HTMLInitiator class.

    NOTE:  DO NOT DIRECTLY ACCESS THE CLASS VARIABLES.  ALWAYS USE THE get_ and
    set_ methods!!!!

    Directly accessing class variables bypasses error checking.

'''

#import the sections that will make up the rendered page

from Source.HTMLInitiator import html_initiator as hi

class html_manager():

    '''
    Default constructor for the class.  test_flag is used to generate an error
    during testing.
    '''
    def __init__(self, test_flag = False):

        #Set variable so that test will fail if it is not correctly set
        self.my_html_initiator = None

        try:
            if test_flag == True:
                self.my_html_initiator = None
            else:
                '''if this fails to instantiate variable, following test should
                fail '''
                self.my_html_initiator = hi()

            if self.my_html_initiator == None:
                raise TypeError('TypeError', 'None',
                'HTMLInitiator object was not created')

        #catch expected failure
        except TypeError as type_error:
            raise type_error

        #catch any unexpected failure
        except Exception as e:
            raise e

    '''
    This method will load the 3 different parts of the HTML template.  It is a test method to ensure that strings exist for each of the expected html template variables.  test_flag can be set to true to force a failure in testing.
    '''
    def get_html(self, test_flag = False):

        #set variable to fail test unless correctly updated
        header = None
        body = None
        var = None

        try:
            if test_flag == False:
                header = self.my_html_initiator.header()
                body = self.my_html_initiator.body()
                var = self.my_html_initiator.var()

            #Test to make sure strings exist for all sections
            if type(header) == str and type(body) == str and type(var) == str:
                return True
            else:
                raise TypeError('TypeError',
                                'None',
                                'HTMLInitiator could not load HTML')

        # catch the excepted error
        except TypeError as type_error:
            raise type_error

        #catch any other error
        except Exception as e:
            raise e

    # The method that calls html_initiator's header method
    def get_header(self):
        return self.my_html_initiator.header()

    # The method that calls html_initiator's body method
    def get_body(self):
        return self.my_html_initiator.body()

    # The method that calls html_initiator's var method
    def get_variable(self):
        return self.my_html_initiator.var()
