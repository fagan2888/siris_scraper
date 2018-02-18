# encoding: utf-8
"""Tests for making queries to the api."""
from unittest import TestCase

from siris.scraper import SirisScraper

class TestSirisQuerying(TestCase):

    def setUp(self):
        self.scraper = SirisScraper()

    def test_basic_query(self):
        # This test depends on the content of the site
        dataset = self.scraper.items.get_by_label(u"Öppen förskola")\
                              .items.get_by_label("Kostnader per kommun")
        res = dataset.fetch({"period": "2016"})
        assert len(res) == 290

        res = dataset.fetch({"period": ["2015", "2016"]})
        assert len(res) == 290 * 2

    def test_query_grundskolan(self):
        dataset = self.scraper.items.get_by_label(u"Grundskolan")\
                              .items["177"]
        res = dataset.fetch()
        assert len(res) > 0
