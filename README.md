# FullStackProject1
Project 1 for the full stack nanodegree class

This program will load default data and default html templates to build an interactive web page to show movie posters, names, 
and allow the user to click on the poster and run a youtube movie trailer.  The program can be run by typing:

python ServePage.py 

in the root directory of the system.  

Dependencies:

This application was developed using python 2.7.9.  It is unknown if it is supported in python 3.x  

This program was tested on Mac OSX (Mavericks) and Ubuntu Linux 15.04.  Safari 8.0.5 and Firefox 37.0.2 were the respective 
browsers tested.

Testing:

The file TestCases.py contain the unit tests used to test development.  It can be run by typing:

python TestCase.py

NOTE:  The testing sequence will create the web page and open it in a browser upon successful completion.

Source Tree:

.gitignore
README.md
ServePage.py
TestCase.py
            -->bin
            JamesBond.html (not included in base, but written by the application)
                          -->img
                          Casino_Royale_poster.jpg
                          Dr._No_-_UK_cinema_poster.jpg
                          From_Russia_with_Love.jpg
                          Goldfinger_-_UK_cinema_poster.jpg
                          On_Her_Majestys_Secret_Service_UK_poster.jpg
                          Thunderball.jpg
            -->Data
            __init__.py
            Data.py
                  -->DataObject
                  __init__.py
                  DataInitiator.py
                  StandardData.py
                  StandardDataObject.py
            -->HTML
            __init__.py
            HTML.py
                  -->Source
                  __init__.py
                  HTMLBase.py
                  HTMLInitiator.py
        
Installation:

The project can be checked out from github.  Once installed, no further configuration should be needed.  

NOTES:

Comments in the source code explain how the initial program could be overridden to accept different movie data or different
html template data.  The movie posters in img would need to be updated or the poster data item would need to point to web URLs
for any new movies included in the system.
