#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
testing flux functions
Created on Thu Jul 22 2019

@author: jkulpa
"""

import sys

sys.path.append("..")

#import OnOff.flux
#import OnOff.misc
#import OnOff.yFactor
import OnOff
import datetime
import pickle

#onFileName = '/home/jkulpa/Desktop/onoff_20190125_1548375694_rf10000.00_n16_casa_on_001_ant_2f_10000.00_obsid2871.pkl'
#offFileName = '/home/jkulpa/Desktop/onoff_20190125_1548375641_rf10000.00_n16_casa_off_000_ant_2f_10000.00_obsid2871.pkl'

onFileName = '/home/jkulpa/Desktop/onoff_20190125_1548378095_rf1000.00_n16_casa_on_000_ant_1a_1000.00_obsid2872.pkl'
offFileName = '/home/jkulpa/Desktop/onoff_20190125_1548378147_rf1000.00_n16_casa_off_000_ant_1a_1000.00_obsid2872.pkl'

onDict = pickle.load( open( onFileName, "rb" )  )
offDict = pickle.load( open( offFileName, "rb" ) )


freq=offDict['rfc']
freqtest=onDict['rfc']

assert freq == freqtest, "file mismatch"

ant = onDict['ant'];
meastime = int(onDict['auto0_timestamp'][0])
datetime_stamp = datetime.datetime.utcfromtimestamp(meastime)
source= onDict['source']

TsysX,TsysstdX = OnOff.calcSingleAnt(source, freq, datetime_stamp, onDict['auto0'], offDict['auto0'])
TsysY,TsysstdY = OnOff.calcSingleAnt(source, freq, datetime_stamp, onDict['auto1'], offDict['auto1'])

print('TsysX = %f +- %f K',TsysX, TsysstdX)
print('TsysY = %f +- %f K',TsysY, TsysstdY)