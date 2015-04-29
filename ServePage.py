'''
Class:  ServePage

Purpose: The front end of the progam to serve up

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
    def __init__(self, test_flag = False, alt_flag = False):

        # initiates instance of html_manager.  Raises error on failure
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


    def get_source_html(self, test_flag = False):

        try:
            #If the test_flag is set to true, it's passed to method
            self.my_html_manager.get_html(test_flag)
        except Exception as e:
            raise e


    def get_movies(self, test_flag = False):

        movies = []
        try:
            if test_flag == True:
                movies = None
            else:
                movies = self.my_data_manager.get_movies()


            if type(movies) != list and len(movies) < 1:
                raise TypeError("TypeError",
                                type(self.movies),
                                "ServePage unable to get movies list")

        except TypeError as type_error:
            raise type_error

        return movies

    def create_movie_tiles_content(self, movies):
        # The HTML content for this section of the page
        content = ''
        keys = self.my_data_manager.get_keys()
        movie = {}
        variable = self.my_html_manager.get_variable()


        for movie_item in movies:

            # Extract the youtube ID from the url

            for key in movie.keys():
                print key
                
            print type(movie)
            url = movie.get_value(keys[2])

            youtube_id_match = re.search(r'(?<=v=)[^&#]+', url)
            youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+',url)
            trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

            # Append the tile for the movie with its content filled in
            content += variable.format(
                movie_title=movie[keys[0]].value,
                poster_image_url=[keys[1]],
                trailer_youtube_id=trailer_youtube_id)
        return content

    def open_movies_page(self, movies):


        # Create or overwrite the output file
        output_file = open('fresh_tomatoes.html', 'w')

        # Replace the placeholder for the movie tiles with the actual dynamically generated content
        body = self.my_html_manager.get_body()
        head = self.my_html_manager.get_header()

        rendered_content =  body.format(variable = self.create_movie_tiles_content(movies))

        # Output the file
        output_file.write(head + rendered_content)
        output_file.close()

        # open the output file in the browser
        url = os.path.abspath(output_file.name)
        webbrowser.open('file://' + url, new=2) # open in a new tab, if possible


    def run(self):
        self.get_source_html()
        movies = self.get_movies()
        self.open_movies_page(self.get_movies())

if __name__ == '__main__':

    if len(sys.argv) > 2:
        print "Invalid arguments passed"
    elif len(sys.argv) == 2:
        if sys.argv[1] == "oldies":
            my_start = serve_page(False, True)
            my_start.run()
        else:
            print "The only accepted argument is 'oldies'"
    else:
        my_start = serve_page()
        my_start.run()
