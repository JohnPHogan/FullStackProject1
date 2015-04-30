'''
Class html_base

Public methods: __init__, header, body, var

This class contains the default definitions of the html page to be rendered.  It must stay in sync with the contents of whatever form of the StandardDataOjbect class you wish to use.  If alternative versions of the page are created, they can be implemented as separate classes exposing the same methods and then accessed through the html_initiator.

DO NOT ACCESS CLASS VARIABLES DIRECTLY!!  ONLY USE THE DEFINED METHODS TO GUARANTEE THAT ANY INCLUDED ERROR CHECKING OR FORMATTING OCCURS.
'''

class html_base():

    '''
    The constructor that sets the class variables for the html template.  It assumes that the content will be divided into a header, body and variable section.  The variable section will need to conform to the data object built by the data_initiator class
    '''
    def __init__(self, test_flag = False):

        try:
            if test_flag == True:
                raise TypeError('TypeError',
                                'None',
                                'html_base could not initiate')
            else:

                self.main_page_head = '''
                <head>
                    <meta charset="utf-8">
                    <title>Bond. James Bond!</title>

                    <!-- Bootstrap 3 -->
                    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
                    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
                    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
                    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
                    <style type="text/css" media="screen">
                        body {
                            padding-top: 80px;
                        }
                        #trailer .modal-dialog {
                            margin-top: 200px;
                            width: 640px;
                            height: 480px;
                        }
                        .hanging-close {
                            position: absolute;
                            top: -12px;
                            right: -12px;
                            z-index: 9001;
                        }
                        #trailer-video {
                            width: 100%;
                            height: 100%;
                        }
                        .movie-tile {
                            margin-bottom: 20px;
                            padding-top: 20px;
                        }
                        .movie-tile:hover {
                            background-color: #EEE;
                            cursor: pointer;
                        }
                        .scale-media {
                            padding-bottom: 56.25%;
                            position: relative;
                        }
                        .scale-media iframe {
                            border: none;
                            height: 100%;
                            position: absolute;
                            width: 100%;
                            left: 0;
                            top: 0;
                            background-color: white;
                        }
                    </style>
                    <script type="text/javascript" charset="utf-8">
                        // Pause the video when the modal is closed
                        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
                            // Remove the src so the player itself gets removed, as this is the only
                            // reliable way to ensure the video stops playing in IE
                            $("#trailer-video-container").empty();
                        });
                        // Start playing the video whenever the trailer modal is opened
                        $(document).on('click', '.movie-tile', function (event) {
                            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
                            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
                            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
                              'id': 'trailer-video',
                              'type': 'text-html',
                              'src': sourceUrl,
                              'frameborder': 0
                            }));
                        });
                        // Animate in the movies when the page loads
                        $(document).ready(function () {
                          $('.movie-tile').hide().first().show("fast", function showNext() {
                            $(this).next("div").show("fast", showNext);
                          });
                        });
                    </script>
                </head>
                '''

                self.main_page_content = '''
                <!DOCTYPE html>
                <html lang="en">
                  <body>
                    <!-- Trailer Video Modal -->
                    <div class="modal" id="trailer">
                      <div class="modal-dialog">
                        <div class="modal-content">
                          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
                          </a>
                          <div class="scale-media" id="trailer-video-container">
                          </div>
                        </div>
                      </div>
                    </div>

                    <!-- Main Page Content -->
                    <div class="container">
                      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
                        <div class="container">
                          <div class="navbar-header">
                            <a class="navbar-brand" href="#">James Bond Movie Trailers</a>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="container">
                      {movie_tiles}
                    </div>
                  </body>
                </html>
                '''
                # A single movie entry html template
                self.movie_tile_content = '''
                <div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
                    <img src="{poster_image_url}" width="220" height="342">
                    <h2>{movie_title}</h2>
                </div>
                '''
        except TypeError as type_error:
            raise TypeError
        except Exception as e:
            raise e

    # The public method to return the html template header information
    def header(self):
        return self.main_page_head

    # The public method to return the html template body information
    def body(self):
        return self.main_page_content

    '''
    The public method to return the html template variable information that will be populated by the data object.
    '''
    def var(self):
        return self.movie_tile_content
