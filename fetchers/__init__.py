"""
公司新聞爬蟲
"""

from .base import CompanyFetcher, CompanyDocument

from .aidc import AidcFetcher
from .bae import BaeFetcher
from .elbit import ElbitFetcher
from .general_dynamics import GeneralDynamicsFetcher
from .hanwha_aero import HanwhaAeroFetcher
from .kratos import KratosFetcher
from .l3harris import L3harrisFetcher
from .leonardo import LeonardoFetcher
from .lockheed import LockheedFetcher
from .northrop import NorthropFetcher
from .palantir import PalantirFetcher
from .rheinmetall import RheinmetallFetcher
from .rtx import RtxFetcher
from .saab import SaabFetcher
from .thales import ThalesFetcher

FETCHERS = {
    "aidc": AidcFetcher,
    "bae": BaeFetcher,
    "elbit": ElbitFetcher,
    "general_dynamics": GeneralDynamicsFetcher,
    "hanwha_aero": HanwhaAeroFetcher,
    "kratos": KratosFetcher,
    "l3harris": L3harrisFetcher,
    "leonardo": LeonardoFetcher,
    "lockheed": LockheedFetcher,
    "northrop": NorthropFetcher,
    "palantir": PalantirFetcher,
    "rheinmetall": RheinmetallFetcher,
    "rtx": RtxFetcher,
    "saab": SaabFetcher,
    "thales": ThalesFetcher,
}
