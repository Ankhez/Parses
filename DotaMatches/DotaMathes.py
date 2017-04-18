from Weather.BasicParse import MyParse
import http

class Matches(MyParse):

    @staticmethod
    def nowgames():
        the_main_box = Matches.parse_user_datafile_bs('dotamatches.html', './/*[@id="matches"]/div[1]//tr')
        for item in the_main_box:
            commands_vs = item.xpath('.//*[@class = "mlink"]/@title')[0]
            bet_for_first_command = item.xpath('.//*[@class="bet-percentage bet1"]/text()')[0]
            bet_for_second_command = item.xpath('.//*[@class="bet-percentage bet2"]/text()')
            #the_data_time = item.xpath('.//*[@id="matches"]/div[1]//*[@class="live-in"]')[1]
            print bet_for_first_command
        #items_the_main_box = the_main_box.xpath('.//*[@id="matches"]/div[1]//tr')




if __name__ == '__main__':
    pass
#Matches.lets_parse('dotamatches.html', 'http://game-tournaments.com/dota-2')
Matches.nowgames()
