'''
TestCases package.  This will house all the tests for the project.  Each class will have its own test class.
'''

import unittest

class test_html_base(unittest.TestCase):

    '''importing the class and instatiating an instance of the class serve as
    unit tests to prove that they exist in the base.
    '''
    from HTML.Source.HTMLBase import  html_base as hb
    my_html_base = hb()

    # Test that html_base __init__ accept test_flag
    def test_html_base_test_flag(self):
        my_html_base = self.hb(False)

    # Test that __init__ can catch and throw a TypeError
    def test_html_base_exception(self):
        self.assertRaises(TypeError, self.hb, True)

    #Test that the header method exists
    def test_html_base_header(self):
        self.my_html_base.header()

    #Test that the header method returns a type string
    def test_html_base_header_result(self):
        self.assertIsInstance(self.my_html_base.header(), str)

    #Test that the body method exists
    def test_html_base_body(self):
        self.my_html_base.body()

    #Test that the body method returns a string
    def test_html_base_body_result(self):
        self.assertIsInstance(self.my_html_base.body(), str)

    #Test that the variable method exists
    def test_html_base_variable(self):
        self.my_html_base.variable()

    #Test that the variable method returns a string
    def test_html_base_variable_result(self):
        self.assertIsInstance(self.my_html_base.variable(), str)

class test_html_initiator(unittest.TestCase):

    #Test that the class exists and can be instantiated
    from HTML.Source.HTMLInitiator import html_initiator as hi
    my_html_initiator = hi()

    #Test that __init__ can accept a test_flag parameter
    def test_init_flag(self):
        test_html_initator = self.hi(False)

    #Test that __init__ can catch and throw an TypeError exception
    def test_html_initiator_exception(self):
        self.assertRaises(TypeError, self.hi, True)

    #Test that get_all exists
    def test_get_all(self):
        self.my_html_initiator.get_all()

    #Test that get_all returns a dict
    def test_get_all(self):
        self.assertIsInstance(self.my_html_initiator.get_all(), dict)

    #Test that get_all support test_flag parameter
    def test_get_all_test_flag(self):
        self.my_html_initiator.get_all(False)

    #Test that get_all can return None
    def test_get_all_fail(self):
        self.assertIsNone(self.my_html_initiator.get_all(True))

    #Test that the header method exists
    def test_header(self):
        self.my_html_initiator.header()

    #Test that the header method returns a string
    def test_html_initiator_header_result(self):
        self.assertIsInstance(self.my_html_initiator.header(), str)

    #Test that the body method exists
    def test_body(self):
        self.my_html_initiator.body()

    #Test that the body method returns a string
    def test_html_initiator_body_result(self):
        self.assertIsInstance(self.my_html_initiator.body(), str)


    #Test that that variable method exists
    def test_variable(self):
        self.my_html_initiator.variable()

    #Test that the variable method returns a string
    def test_html_initiator_variable_result(self):
        self.assertIsInstance(self.my_html_initiator.variable(), str)

class test_html(unittest.TestCase):

    #Test that html_manager exists and can be instantiated
    from HTML.HTML import html_manager as hm
    my_html_manager = hm()

    #Test to see if the _init__ can accept a test_flag parameter
    def test_init_test_flag(self):
        test_html_manager = self.hm(False)

    #Test to see if __init__ can catch and throw a TypeError exception
    def test_init_throws_TypeError(self):
        self.assertRaises(TypeError, self.hm, True)

    # Test that the get_html method exists
    def test_get_html(self):
        self.my_html_manager.get_html()

    #Test to see if get_html can accept a test_flag parameter
    def test_get_html_test_flag(self):
        self.my_html_manager.get_html(False)

    #Test that get_html can catch and throw a TypeError exception
    def test_get_html_Raises_TypeError(self):
        self.assertRaises(TypeError, self.my_html_manager.get_html, True)

class Test_Standard_Data(unittest.TestCase):
    #Test that the class exists and can be instantiated
    from Data.DataObject.StandardData import standard_data as sd
    my_standard_data = sd()

    # Test that the __init__ method can accept test_flag parameter
    def test_init_test_flag(self):
        test_standard_data = self.sd(False)

    #Test that __init__ can catch and throw a TypeError exception
    def test_init_Raises_TypeError(self):
        self.assertRaises(TypeError, self.sd, True)

    #Test that get_keys exits
    def test_get_keys(self):
        self.my_standard_data.get_keys()

    #Test that the variable method returns a list
    def test_get_keys_result(self):
        self.assertIsInstance(self.my_standard_data.get_keys(), list)

    #Test that the get_movies method exists
    def test_get_movies(self):
        self.my_standard_data.get_movies()

    #Test that the get_movies method exists
    def test_get_movies_result(self):
        self.assertIsInstance(self.my_standard_data.get_movies(), list)

class test_movies(unittest.TestCase):
    from Data.Movies import movies
    standard_keys = ['Title',
                    'Rating',
                    'Poster',
                    'URL']

    standard_dict = {'Title': "Test Movie",
                    'Rating': "Rating",
                    'Poster': "Test Poster",
                    'URL': "Test URL"}

    my_movies = movies(standard_keys)

    #test to make sure an exception is caught an thrown if a list is not passed
    def test_init_rejects_invalid_keys(self):

        self.assertRaises(TypeError,self.movies,'test string')

    def test_load_data_exists(self):
        self.my_movies.load_data(self.standard_dict)

    def test_load_data_throws_type_error(self):
        self.assertRaises(TypeError,
                        self.my_movies.load_data,
                        'this is an error')

class Test_Data_Initiator(unittest.TestCase):
    #Test that the class exists and can be instantiated
    from Data.DataObject.DataInitiator import data_initiator as di
    my_data_initiator = di()

    # Test that the __init__ method can accept test_flag parameter
    def test_init_test_flag(self):
        test_data_initiator = self.di(False)

    #Test that __init__ method can accept alt_flag parameter
    def test_init_handles_type_flag(self):
        test_data_initiator = self.di(False, False)

    #Test that __init__ can catch and throw a TypeError exception
    def test_init_Raises_TypeError(self):
        self.assertRaises(TypeError, self.di, True)

    #Test that get_data_object exists
    def test_data_get_object_exists(self):
        self.my_data_initiator.get_data_object()

    #Test that get_data_object returns a list
    def test_data_get_data_object_results(self):
        self.assertIsInstance(self.my_data_initiator.get_data_object(), list)


class Test_Data_Manager(unittest.TestCase):
    #Test that the class exists and can be instantiated
    from Data.Data import data_manager as dm
    my_data_manager = dm()

    # Test that the __init__ method can accept test_flag parameter
    def test_init_test_flag(self):
        test_data_manager = self.dm(False)

    #Test that get_html can catch and throw a TypeError exception
    def test_init_Raises_TypeError(self):
        self.assertRaises(TypeError, self.dm, True)

    #Test that data_manager can accept a third argument
    def test_init_alt(self):
        test_data_manager = self.dm(False, False)

    #Test to see if get_data_object exists
    def test_get_data_object(self):
        self.my_data_manager.get_data_object()

    #Test to see if get_data_object accepts test_flag as a parameter
    def test_get_data_object_flag(self):
        self.my_data_manager.get_data_object(False)

    #Test to see if get_data_object can throw a type error
    def test_get_data_object_exception(self):
        self.assertRaises(TypeError, self.my_data_manager.get_data_object, True)

    #Test to see if build_movies exists
    def test_build_movie_list_exists(self):
        self.my_data_manager.build_movie_list()

    #Test to see that build_movie_list returns a list
    def check_build_movie_list_return(self):
        self.assertIsInstance(self.my_data_manager.build_movie_list(), list)

    #Test to see if get_movies exists
    def test_get_movies_exists(self):
        self.my_data_manager.get_movies()

    #Test to see that build_movie_list returns a list
    def check_get_movies_list_return(self):
        self.assertIsInstance(self.my_data_manager.get_movies(), list)


class test_serve_page(unittest.TestCase):

    '''the implied unit test for modules/classes existing is that the import
    function will fail until you create the necessary directories/files.
    '''
    from ServePage import serve_page as sp
    my_ServePage = sp()

    def test_init_test_flag(self):
        test_ServePage = self.sp(False)

    def test_init_exception(self):
        self.assertRaises(Exception, self.sp, True)

    def test_init_alternate(self):
        test_ServerPage = self.sp(False, False)

    def test_get_source_html(self):
        self.my_ServePage.get_source_html()

    def test_get_source_html_false(self):
        self.my_ServePage.get_source_html(False)

    def test_get_source_html_exception(self):
        self.assertRaises(TypeError, self.my_ServePage.get_source_html, True)

    def test_init_command_line_argument(self):
        test_ServePage = self.sp(False, False)

    #Test to see if movies method exists
    def test_movies(self):
        self.my_ServePage.get_movies()

    #Test to see if movies accepts test_flag parameter
    def test_movies_flag(self):
        self.my_ServePage.get_movies(False)

    #Test to see if method can throw an TypeError
    def test_get_movies_exception(self):
        self.assertRaises(TypeError, self.my_ServePage.get_movies, True)

    #Test to see that method returns a list
    def test_get_movies_returns_list(self):
        #self.my_ServePage.get_movies()
        self.assertIsInstance(self.my_ServePage.get_movies(), list)

    #Test to see that method is available
    def test_build_variable_data(self):
        test = []
        self.my_ServePage.create_movie_tiles_content(test)


if __name__ == '__main__':
    unittest.main()
