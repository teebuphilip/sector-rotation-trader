from .faber import FaberMomentumAlgo
from .dmsr import DMSRAlgo
from .simple_monthly import SimpleMonthlyAlgo
from .biscotti import BiscottiAlgo
from .bailey import BaileyAlgo


def get_normal_algos():
    return [
        FaberMomentumAlgo(),
        DMSRAlgo(),
        SimpleMonthlyAlgo(),
        BiscottiAlgo(),
        BaileyAlgo(),
    ]
