"""
Main bioeq code
"""

import polars as pl

def asdf():
    """
    asdf
    """

    print("kshjfoweifjoi")


def sdfg():
    """
    asdf
    """

    print("asdfasdfrtherg")


class BioEq:
    """
    Main BioEq class
    """

    def __init__(self, number):
        self.number = number

        url = 'https://raw.githubusercontent.com/shaunporwal/bioeq/refs/heads/main/simdata/bioeq_simdata_1.csv'
        self.simdata1 = pl.read_csv(url)
