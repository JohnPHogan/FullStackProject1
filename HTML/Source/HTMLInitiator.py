from HTMLBase import html_base as hb

class html_initiator(hb):


    def __init__(self, test_flag = False):

        self.HTML_TYPES = None

        try:

            if test_flag == True:
                raise TypeError('TypeError',
                                'None',
                                'html_initiator could not initiate')
            else:
                '''this will generate it's own exception if created in it's
                __init__ method.  It does not need to inherit test_flag.
                '''
                hb.__init__(self)

                self.HTML_TYPES = {0: 'header', 1: 'body', 2:'variable'}

            # If assignment fails, throw eception
            if self.HTML_TYPES == None:
                raise TypeError('TypeError',
                                'None',
                                'html_initiator could not initiate')
        except TypeError as type_error:
            raise TypeError
        except Exception as e:
            raise e

    def get_all(self, test_fail = False):

        if test_fail == True:
            return None

        return self.HTML_TYPES

    def header(self):
        return hb.header(self)

    def body(self):
        return hb.body(self)

    def variable(self):
        return hb.variable(self)
