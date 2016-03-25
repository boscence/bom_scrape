# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 22:55:35 2016

@author: ab
"""

bom = requests.get('http://www.bom.gov.au/vic/forecasts/melton.shtml')
tree = html.fromstring(bom.content)

fdate = tree.xpath('//h2/text()')
max = tree.xpath('//em[@class="max"]/text()')
min = tree.xpath('//em[@class="min"]/text()')
rain = tree.xpath('//em[@class="rain"]/text()')
frain = tree.xpath('//dd[@class="rain"]/text()')


print(fdate,max,min,rain,frain)