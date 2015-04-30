'''
Class standard_data

Public methods: __init__, get_movies

This class contains the default movie data.  By cloning this class and changing the data stored in the dict objects you can change what movies will appear in the web page.

DO NOT ACCESS CLASS VARIABLES DIRECTLY!!  ONLY USE THE DEFINED METHODS TO GUARANTEE THAT ANY INCLUDED ERROR CHECKING OR FORMATTING OCCURS.
'''


class standard_data():

    DN = {'title': "Dr. No",
            'poster': "img/Dr._No_-_UK_cinema_poster.jpg",
            'rating': "7.3/10",
            'URL': "https://www.youtube.com/watch?v=pw61uyA0F8A"
    }

    GF = {'title': "Goldfinger",
            'poster': "img/Goldfinger_-_UK_cinema_poster.jpg",
            'rating': "7.8/10",
            'URL': "https://www.youtube.com/watch?v=MA65V-oLKa8"

    }

    TB = {'title': "Thunderball",
            'poster': "img/Thunderball.jpg",
            'rating': "7.0/10",
            'URL': "https://www.youtube.com/watch?v=ElyENM6i0xg"

    }

    RFL = {'title':"From Russia with Love",
            'poster': "img/From_Russia_with_Love.jpg",
            'rating': "7.5/10",
            'URL': "https://www.youtube.com/watch?v=VqAOf66o1Wg"

    }

    HMSS = {'title': "On Her Majesty's Secret Service",
            'poster': "img/On_Her_Majestys_Secret_Service-UK-poster.jpg",
            'rating': "6.8/10",
            'URL': "https://www.youtube.com/watch?v=DVP2n_GcdlQ"

    }

    CR = {'title': "Casino Royale",
            'poster': "img/Casino_Royale_poster.jpg",
            'rating': "5.2/10",
            'URL': "https://www.youtube.com/watch?v=0px9QxojVjU"

    }

    # Constructor that loads the dict objects defined above into a list
    def __init__(self, test_flag = False):

        self.movie_list = None

        try:
            if test_flag == False:
                '''if this fails to instantiate variable, following test should
                fail '''
                self.movie_list = [self.DN,
                                    self.GF,
                                    self.TB,
                                    self.RFL,
                                    self.HMSS,
                                    self.CR]

            if self.movie_list == None:
                raise TypeError('TypeError', 'None',
                'standard_data was not created')

        #catch expected failure
        except TypeError as type_error:
            raise type_error

        #catch any unexpected failure
        except Exception as e:
            raise e

    # The public method used to retrieve the list of movie data
    def get_movies(self):
        return self.movie_list
