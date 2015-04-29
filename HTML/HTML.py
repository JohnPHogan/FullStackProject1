'''
Class:  html_manager

Purpose: The class that manages retrieving the HTML templates.  This class is the interface level that the calling program needs to invoke.  It handles loading the appropriate HTMLInitiator class.

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
    This method will load the 3 different parts of the HTML page trying to be
    created.  test_flag can be set to true to force a failure in testing.
    '''
    def get_html(self, test_flag = False):

        #set variable to fail test unless correctly updated
        self.header = None
        self.body = None
        self.variable = None

        try:
            if test_flag == False:
                self.header = self.my_html_initiator.header()
                self.body = self.my_html_initiator.body()
                self.variable = self.my_html_initiator.variable()

            if type(self.header) == str and type(self.body) == str and type(self.variable) == str:
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

    def get_header(self):
        return self.header

    def get_body(self):
        return self.body

    def get_variable(self):
        return self.variable
