# -*- coding:utf-8 -*-
import requests, datetime
from lxml import html, etree


class MyParse(object):

#update parse file if we need
    @staticmethod
    def updateparse(filename, url, freq):
        if datetime.datetime.now().hour % freq == 0:
            MyParse.lets_parse(filename, url)

#parse from url to file
    @staticmethod
    def lets_parse(filename, url):
        r = requests.get(url)
        with open(filename, 'w') as output_file:
            output_file.write(r.text.encode('utf-8'))

#red file and return all info from
    @staticmethod
    def read_file(filename):
        with open(filename) as input_file:
            text = input_file.read()
        return text

#return info from xpath
    @staticmethod
    def parse_user_datafile_bs(filename, xpath):
        text = MyParse.read_file(filename)
        tree = html.fromstring(text)
        valuefromparse = tree.xpath(xpath)
        return valuefromparse

if __name__ == "__main__":
    pass
