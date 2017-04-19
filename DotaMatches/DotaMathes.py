# -*- coding:utf-8 -*-
from Weather.BasicParse import MyParse

class Matches(MyParse):



    @staticmethod
    def except_for_empty_values(path, error):
        try:
            name = path[0]
        except error:
            name = ''
        return name





    @staticmethod
    def nowgames():
        results = []

        the_main_box = Matches.parse_user_datafile_bs('dotamatches.html', './/*[@id="matches"]/div[1]//tr')
        for item in the_main_box:

            commands_vs = item.xpath('.//*[@class = "mlink"]/@title')[0]
            bet_for_first_command = Matches.except_for_empty_values(item.xpath('.//*[@class="bet-percentage bet1"]/text()'), IndexError)
            bet_for_second_command = Matches.except_for_empty_values(item.xpath('.//*[@class="bet-percentage bet2"]/text()'), IndexError)
            the_data_time = Matches.except_for_empty_values(item.xpath('.//td[3]/span[2]/span/text()'), IndexError)
            name_of_tournament = item.xpath('.//*[@class="ta odtip"]/@title')[0]

            results.append({

                'commands': commands_vs,
                'bet': bet_for_first_command+bet_for_second_command,
                'data_time': the_data_time,
                'tour_name': name_of_tournament
            })
        for element in results:
            print element.get('commands') + u'    /Стаки на команды: ' + element.get('bet') + u'  / Время: '+ element.get('data_time')\
                  + u' /Название турнира: ' + element.get('tour_name')
        #items_the_main_box = the_main_box.xpath('.//*[@id="matches"]/div[1]//tr')




if __name__ == '__main__':
    pass
Matches.lets_parse('dotamatches.html', 'http://game-tournaments.com/dota-2')
Matches.nowgames()

