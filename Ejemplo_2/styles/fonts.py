from enum import Enum 

class Font(Enum):
    HERO="Playfair Display"
    BUTTON="Roboto"
    DESCRIPTION="Quicksand"
    LOGO="Poppins"
    SERVICES_TITLE="Oswald"
    SERVICES_BODY="Open Sans"
    CONTACT="Nunito"
    PROJECT="Merriweather"

class FontWeight(Enum):
    LIGHT="300"
    MEDIUM="500"
    BOLD="700"
    SEMIBOLD="600"
    REGULAR="400"