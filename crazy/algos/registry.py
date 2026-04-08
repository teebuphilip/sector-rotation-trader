from .tsa import TSAAlgo
from .cardboard import CardboardAlgo
from .craigslist import CraigslistAlgo
from .glassdoor import GlassdoorAlgo
from .calls311 import Calls311Algo
from .liquor import LiquorAlgo
from .linkedin import LinkedInAlgo
from .congress import CongressAlgo
from .biscotti import BiscottiAlgo
from .bailey import BaileyAlgo


def get_crazy_algos():
    return [
        TSAAlgo(),
        CardboardAlgo(),
        CraigslistAlgo(),
        GlassdoorAlgo(),
        Calls311Algo(),
        LiquorAlgo(),
        LinkedInAlgo(),
        CongressAlgo(),
        BiscottiAlgo(),
        BaileyAlgo(),
    ]
