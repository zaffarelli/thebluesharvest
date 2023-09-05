import sys
from frontdoor.utils.mechanics import populate_gallery

class ProdPrep:
    def __init__(self):
        print("Initializing!")

    def perform(self):
        print("Perform")
        populate_gallery('pictures/dates/');


ProdPrep().perform()
