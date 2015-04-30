'''
Class:  ServePage

Public methods:  get_html_data and open_movies_page

The front end of the progam to serve up the web page

    NOTE:  DO NOT DIRECTLY ACCESS THE CLASS VARIABLES.  ALWAYS USE THE get_ and
    set_ methods!!!!

    Directly accessing class variables bypasses error checking.

'''

from HTML.HTML import html_manager as hm
from Data.Data import data_manager as dm
import sys
import webbrowser
import os
import re


class serve_page():

    #Default constructor for the class
    def __init__(self, test_flag = False):

        '''
        initiates instance of html_manager and data_manager.  Raises error on failure
        '''
        self.my_html_manager = None
        self.my_data_manager = None
        try:
            if test_flag == False:
                self.my_html_manager = hm()
                self.my_data_manager = dm()

            if self.my_html_manager == None or self.my_data_manager == None:
                raise Exception('Exception', 'None',
                'HTML_manager or Data_manager object was not created')

        except Exception as e:
            raise e

    '''
    This is a method that is called by run and loads the html template data in html_manager.  It should not be called outside of the class.
    '''
    def get_source_html(self, test_flag = False):
        try:
            #If the test_flag is set to true, it's passed to method
            self.my_html_manager.get_html(test_flag)
        except Exception as e:
            raise e

    '''
    This is a method that is called as a parameter to the call to open_movies_page by run and gets the movie data from data_manager.  It should not be called outside of the class.
    '''
    def get_movies(self, test_flag = False):

        movies = []
        try:
            if test_flag == True:
                movies = None
            else:
                movies = self.my_data_manager.get_movies()


            if type(movies) != list or len(movies) < 1:
                raise TypeError("TypeError",
                                type(movies),
                                "ServePage unable to get movies list")

        except TypeError as type_error:
            raise type_error

        return movies
    '''
    This method is called by open_movies_page and should not be accessed directly outside of this class.  It processes the data and loads it into the variable portion of the html template.  It should not be called outside of the class.
    '''
    def create_movie_tiles_content(self, movies):
        # The HTML content for this section of the page
        content = ''
        variable = self.my_html_manager.get_variable()

        for movie_item in movies:

            # Extract the youtube ID from the url
            url = movie_item.get_url()

            youtube_id_match = re.search(r'(?<=v=)[^&#]+', url)
            youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', url)
            trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None


            youtube_id_match = re.search(r'(?<=v=)[^&#]+', url)
            youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+',url)
            youtube_id = youtube_id_match.group(0) if youtube_id_match else None

            # Append the tile for the movie with its content from data_object
            content += variable.format(movie_title=movie_item.get_title(), poster_image_url=movie_item.get_poster(), trailer_youtube_id=youtube_id)

        return content


    '''
    A  method called by run to load the movie data into the variable template, write the html output file and then open it with a browser.  It should not be called outside of the class.  
    '''
    def open_movies_page(self, movies):

        # Create or overwrite the output file
        output_file = open('bin/james_bond.html', 'w')

        # Replace the placeholder for the movie tiles with the actual dynamically generated content
        body = self.my_html_manager.get_body()
        head = self.my_html_manager.get_header()

        rendered_content =  body.format(movie_tiles = self.create_movie_tiles_content(movies))

        # Output the file
        output_file.write(head + rendered_content)
        output_file.close()

        # open the output file in the browser
        url = os.path.abspath(output_file.name)
        print url
        webbrowser.open('file://' + url, new=2) # open in a new tab, if possible

    '''
    The public method to the serve_page class and the one invoked to perform all actions needed to populate data, write the html page and open the page.
    '''
    def run(self):
        self.get_source_html()
        self.open_movies_page(self.get_movies())

if __name__ == '__main__':

    my_start = serve_page()
    my_start.run()
