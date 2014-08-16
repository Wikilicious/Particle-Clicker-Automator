__author__ = 'Thomaz Lago Santana'
__date__ = "August 14, 2014"


'''
Play CERN Particle Clicker Game like a boss! Automatically click as fast as your CPU can process.
You can still do upgrades, research, and hire HR as the code is automatically clicking.
To get the best results get the +4, +12, and +42 data per click upgrades first. Then get the
three x3 data per click upgrades so you get 1,593 data per click ((1+4+12+42)*3*3*3)
Rough estimate: I'm getting 8.7 clicks per second @ 1.6k data = 50M data per hr.
Game URL: http://particle-clicker.web.cern.ch/particle-clicker/
Need Firefox, Python, and Selenium.
'''


from selenium import webdriver
import time


url = 'http://particle-clicker.web.cern.ch/particle-clicker/'
br = webdriver.Firefox()
br.get(url)
time.sleep(2)

for i in range(99999999):
    for i in range(1000):
        br.find_element_by_id('detector-events').click()
    print '5s pause'
    time.sleep(5)
