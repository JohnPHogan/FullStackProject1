'''
Class:  standard_data_object

Public methods: __init__, get_title, get_poster, get_url

 This class contains the data structure used to populate the movie data stored in the web page.  It must stay in sync with the html_base class in order for the program to work.  If other data is wanted, you can create other copies of this class and use them in conjunction wtih updated html_base classes.  The ServePage class will need to be modified to import the correct version of this class.

    NOTE:  DO NOT DIRECTLY ACCESS THE CLASS VARIABLES.  ALWAYS USE THE get_ and
    set_ methods!!!!

'''
class standard_data_object:

    # default data items.  This can be overridden in other versions of the class
    title = ""
    poster = ""
    url = ""

    # constructor populates the defined data items
    def __init__(self, title, poster, url):
        self.title = title
        self.poster = poster
        self.url = url

    '''
    The following methods may be overriden in other versions of the class.  ServePage would have to changed to handle that change.
    '''

    # public method to return title
    def get_title(self):
        return self.title

    # public method to return poster
    def get_poster(self):
        return self.poster

    #public method to return url
    def get_url(self):
        return self.url
