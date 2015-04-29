class standard_data():

    DN = {'title': "Dr. No",
            'Poster': "img/Dr._No_-_UK_cinema_poster.jpg",
            'Rating': "7.3/10",
            'URL': "https://www.youtube.com/watch?v=pw61uyA0F8A"
    }

    GF = {'title': "Goldfinger",
            'Poster': "img/Goldfinger_-_UK_cinema_poster.jpg",
            'Rating': "7.8/10",
            'URL': "https://www.youtube.com/watch?v=MA65V-oLKa8"

    }

    TB = {'title': "Thunderball",
            'Poster': "img/Thunderball.jpg",
            'Rating': "7.0/10",
            'URL': "https://www.youtube.com/watch?v=ElyENM6i0xg"

    }

    RFL = {'title':"From Russia with Love",
            'Poster': "img/From_Russia_with_Love.jpg",
            'Rating': "7.5/10",
            'URL': "https://www.youtube.com/watch?v=VqAOf66o1Wg"

    }

    HMSS = {'title': "On Her Majesty's Secret Service",
            'Poster': "img/On_Her_Majesty's_Secret_Service-UK-poster.jpg",
            'Rating': "6.8/10",
            'URL': "https://www.youtube.com/watch?v=DVP2n_GcdlQ"

    }

    CR = {'title': "Casino Royale",
            'Poster': "http://members.casema.nl/renem/JamesBond/Casino_Royale-1967/Casino_Royale-1967-front.jpg",
            'Rating': "5.2/10",
            'URL': "https://www.youtube.com/watch?v=0px9QxojVjU"

    }

    def __init__(self, test_flag = False):

        self.movie_list = None
        self.keys = None

        try:
            if test_flag == False:
                '''if this fails to instantiate variable, following test should
                fail '''
                self.name = 'Standard'
                self.keys = ['Title',
                'Rating',
                'Poster',
                'URL']

                self.movie_list = [self.DN,
                                    self.GF,
                                    self.TB,
                                    self.RFL,
                                    self.HMSS,
                                    self.CR]

            if self.keys == None or self.movie_list == None:
                raise TypeError('TypeError', 'None',
                'standard_data was not created')

        #catch expected failure
        except TypeError as type_error:
            raise type_error

        #catch any unexpected failure
        except Exception as e:
            raise e

    def get_keys(self):
        return self.keys

    def get_movies(self):
        return self.movie_list
