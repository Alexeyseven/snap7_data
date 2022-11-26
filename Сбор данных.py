import snap7
from snap7.util import *
import time
import datetime
#import pyautogui as gui
import sqlite3
import logging

i = 0
j = 1

plc1 = snap7.client.Client()
plc2 = snap7.client.Client()
plc3 = snap7.client.Client()
plc4 = snap7.client.Client()
plc5 = snap7.client.Client()

plc1.connect('172.16.34.30',0,2)
plc2.connect('172.16.34.81',0,2)
plc3.connect('172.16.34.20',0,2)
plc4.connect('172.16.34.90',0,2)
plc5.connect('172.16.37.68',0,2)

logger = logging.getLogger('logger')


with sqlite3.connect('database.db') as db:
   cursor1 = db.cursor()
   query1 = """CREATE TABLE IF NOT EXISTS Paster_PET_4(id INTEGER, date TEXT, time TEXT, flow TEXT, PU TEXT, temp_past TEXT, temp_cool TEXT, press_past TEXT)"""
   cursor1.execute(query1)

   cursor2 = db.cursor()
   query2 = """CREATE TABLE IF NOT EXISTS Valves_PET_4(id INTEGER,
          date TEXT, time TEXT, V01 TEXT,
          V02 TEXT, V03 TEXT, V04 TEXT, V05 TEXT, V06 TEXT, V07 TEXT,
          V08 TEXT, V13 TEXT, V16 TEXT, V30 TEXT, V31 TEXT, V32 TEXT,
          V33 TEXT, V34 TEXT, V35 TEXT, V36 TEXT, V38 TEXT, V39 TEXT,
          V40 TEXT)"""
   cursor2.execute(query2)

   cursor3 = db.cursor()
   query3 = """CREATE TABLE IF NOT EXISTS Paster_Glass_6(id INTEGER, date TEXT, time TEXT, flow TEXT, PU TEXT, temp_past TEXT, temp_cool TEXT, press_past TEXT)"""
   cursor3.execute(query3)

   cursor4 = db.cursor()
   query4 = """CREATE TABLE IF NOT EXISTS Valves_Glass_6(id INTEGER,
          date TEXT, time TEXT, V01 TEXT,
          V02 TEXT, V03 TEXT, V04 TEXT, V05 TEXT, V06 TEXT, V07 TEXT,
          V08 TEXT, V09 TEXT, V10 TEXT, V11 TEXT, V12 TEXT, V13 TEXT,
          V14 TEXT, V15 TEXT, V16 TEXT, V17 TEXT, V18 TEXT, V19 TEXT,
          V20 TEXT, V21 TEXT, V22 TEXT, V23 TEXT, V24 TEXT, V25 TEXT,
          V60 TEXT, V61 TEXT, V62 TEXT, V70 TEXT)"""
   cursor4.execute(query4)

   cursor5 = db.cursor()
   query5 = """CREATE TABLE IF NOT EXISTS Paster_Keg(id INTEGER, date TEXT, time TEXT, flow TEXT, PU TEXT, temp_past TEXT, temp_cool TEXT, press_past TEXT)"""
   cursor5.execute(query5)

   cursor6 = db.cursor()
   query6 = """CREATE TABLE IF NOT EXISTS Valves_Keg(id INTEGER,
          date TEXT, time TEXT, V01 TEXT,
          V02 TEXT, V03 TEXT, V04 TEXT, V05 TEXT, V07 TEXT,
          V30 TEXT, V31 TEXT, V32 TEXT, V33 TEXT, V34 TEXT, V35 TEXT,
          V36 TEXT, V37 TEXT, V38 TEXT, V39 TEXT, V40 TEXT, V41 TEXT,
          V42 TEXT, V43 TEXT)"""
   cursor6.execute(query6)

   cursor7 = db.cursor()
   query7 = """CREATE TABLE IF NOT EXISTS Paster_PET_2(id INTEGER, date TEXT, time TEXT, flow TEXT, PU TEXT, temp_past TEXT, temp_cool TEXT, press_past TEXT)"""
   cursor7.execute(query7)

   cursor8 = db.cursor()
   query8 = """CREATE TABLE IF NOT EXISTS Valves_PET_2(id INTEGER,
          date TEXT, time TEXT, V01 TEXT,
          V02 TEXT, V03 TEXT, V04 TEXT, V05 TEXT, V06 TEXT, V07 TEXT,
          V08 TEXT, V21 TEXT, V23 TEXT, V30 TEXT, V31 TEXT, V32 TEXT,
          V33 TEXT, V34 TEXT, V35 TEXT, V36 TEXT, V38 TEXT, V39 TEXT,
          V40 TEXT, V41 TEXT, V42 TEXT, V43 TEXT, V44 TEXT, V45 TEXT,
          V46 TEXT)"""
   cursor8.execute(query8)

   cursor9 = db.cursor()
   query9 = """CREATE TABLE IF NOT EXISTS Paster_PET_Keg(id INTEGER, date TEXT, time TEXT, flow TEXT, PU TEXT, temp_past TEXT, temp_cool TEXT, press_past TEXT)"""
   cursor9.execute(query9)

   cursor10 = db.cursor()
   query10 = """CREATE TABLE IF NOT EXISTS Valves_PET_Keg(id INTEGER,
          date TEXT, time TEXT, V01_05 TEXT, V01_07 TEXT, V01_08 TEXT,
          V01_09 TEXT, V01_10 TEXT, V01_11 TEXT, V01_12 TEXT, V01_51 TEXT,
          V01_57 TEXT, V02_01 TEXT, V02_02 TEXT, V02_04 TEXT, V02_05 TEXT,
          V02_08 TEXT, V02_09 TEXT, V60, V61, V80
          )"""
   cursor10.execute(query10)

def BtS(valve):
    if valve:
        return('Открыт')
    else:
        return ('Закрыт')
 
while(True):
    try:
        flow_4 = plc1.db_read(177,44,4)
        flow_real_4 = snap7.util.get_real(flow_4,0)
        flow_format_4 = int(flow_real_4*10)/10

        flow_6 = plc2.db_read(180,4,2)
        flow_real_6 = snap7.util.get_int(flow_6,0)
        flow_format_6 = int(flow_real_6)

        flow_keg = plc3.db_read(1,44,4)
        flow_real_keg = snap7.util.get_real(flow_keg,0)
        flow_format_keg = int(flow_real_keg*10)/10

        flow_2 = plc4.db_read(176,10,4)
        flow_real_2 = snap7.util.get_real(flow_2,0)
        flow_format_2 = int(flow_real_2)/10

        flow_PET_Keg = plc5.db_read(77,4,2)
        flow_real_PET_Keg = snap7.util.get_int(flow_PET_Keg,0)
        flow_format_PET_Keg = int(flow_real_PET_Keg)/100
    
        PU_4 = plc1.db_read(177,48,4)
        PU_real_4 = snap7.util.get_real(PU_4,0)
        PU_format_4 = int(PU_real_4*10)/10

        PU_6 = plc2.db_read(180,2,2)
        PU_real_6 = snap7.util.get_int(PU_6,0)
        PU_format_6 = int(PU_real_6)/10

        PU_keg = plc3.db_read(1,48,4)
        PU_real_keg = snap7.util.get_real(PU_keg,0)
        PU_format_keg = int(PU_real_keg*10)/10

        PU_2 = plc4.db_read(176,34,2)
        PU_real_2 = snap7.util.get_int(PU_2,0)
        PU_format_2 = int(PU_real_2*10)/10

        PU_PET_Keg = plc5.db_read(77,2,2)
        PU_real_PET_Keg = snap7.util.get_int(PU_PET_Keg,0)
        PU_format_PET_Keg = int(PU_real_PET_Keg*10)/10
    
        temp_past_4 = plc1.db_read(177,52,4)
        temp_past_real_4 = snap7.util.get_real(temp_past_4,0)
        temp_past_format_4 = int(temp_past_real_4*10)/10

        temp_past_6 = plc2.db_read(180,6,2)
        temp_past_real_6 = snap7.util.get_int(temp_past_6,0)
        temp_past_format_6 = int(temp_past_real_6)/100

        temp_past_keg = plc3.db_read(1,52,4)
        temp_past_real_keg = snap7.util.get_real(temp_past_keg,0)
        temp_past_format_keg = int(temp_past_real_keg*10)/10

        temp_past_2 = plc4.db_read(176,18,4)
        temp_past_real_2 = snap7.util.get_real(temp_past_2,0)
        temp_past_format_2 = int(temp_past_real_2)/10

        temp_past_PET_Keg = plc5.db_read(77,6,2)
        temp_past_real_PET_Keg = snap7.util.get_int(temp_past_PET_Keg,0)
        temp_past_format_PET_Keg = int(temp_past_real_PET_Keg)/100
    
        temp_cool_4 = plc1.db_read(177,56,4)
        temp_cool_real_4 = snap7.util.get_real(temp_cool_4,0)
        temp_cool_format_4 = int(temp_cool_real_4*10)/10

        temp_cool_6 = plc2.db_read(180,8,2)
        temp_cool_real_6 = snap7.util.get_int(temp_cool_6,0)
        temp_cool_format_6 = int(temp_cool_real_6)/100

        temp_cool_keg = plc3.db_read(1,56,4)
        temp_cool_real_keg = snap7.util.get_real(temp_cool_keg,0)
        temp_cool_format_keg = int(temp_cool_real_keg*10)/10

        temp_cool_2 = plc4.db_read(176,22,4)
        temp_cool_real_2 = snap7.util.get_real(temp_cool_2,0)
        temp_cool_format_2 = int(temp_cool_real_2)/10

        temp_cool_PET_Keg = plc5.db_read(77,8,2)
        temp_cool_real_PET_Keg = snap7.util.get_int(temp_cool_PET_Keg,0)
        temp_cool_format_PET_Keg = int(temp_cool_real_PET_Keg)/100
    
        press_past_4 = plc1.db_read(177,60,4)
        press_past_real_4 = snap7.util.get_real(press_past_4,0)
        press_past_format_4 = int(press_past_real_4*10)/10

        press_past_6 = plc2.db_read(180,10,2)
        press_past_real_6 = snap7.util.get_int(press_past_6,0)
        press_past_format_6 = int(press_past_real_6)/10

        press_past_keg = plc3.db_read(1,60,4)
        press_past_real_keg = snap7.util.get_real(press_past_keg,0)
        press_past_format_keg = int(press_past_real_keg*10)/10

        press_past_2 = plc4.db_read(176,26,4)
        press_past_real_2 = snap7.util.get_real(press_past_2,0)
        press_past_format_2 = int(press_past_real_2)/10

        press_past_PET_Keg = plc5.db_read(77,10,2)
        press_past_real_PET_Keg = snap7.util.get_int(press_past_PET_Keg,0)
        press_past_format_PET_Keg = int(press_past_real_PET_Keg)/10
    
        V_byte_1_4 = plc1.read_area(0x82,0,8,1)
        V01_4 = get_bool(V_byte_1_4,0,0)
        V02_4 = get_bool(V_byte_1_4,0,1)
        V03_4 = get_bool(V_byte_1_4,0,2)
        V04_4 = get_bool(V_byte_1_4,0,3)
        V05_4 = get_bool(V_byte_1_4,0,4)
        V06_4 = get_bool(V_byte_1_4,0,5)
        V07_4 = get_bool(V_byte_1_4,0,6)
        V08_4 = get_bool(V_byte_1_4,0,7)

        V_byte_2_4 = plc1.read_area(0x82,0,9,1)
        V13_4 = get_bool(V_byte_2_4,0,0)
        V16_4 = get_bool(V_byte_2_4,0,1)
        V30_4 = get_bool(V_byte_2_4,0,2)
        V31_4 = get_bool(V_byte_2_4,0,3)
        V32_4 = get_bool(V_byte_2_4,0,4)
        V33_4 = get_bool(V_byte_2_4,0,5)
        V34_4 = get_bool(V_byte_2_4,0,6)
        V35_4 = get_bool(V_byte_2_4,0,7)

        V_byte_3_4 = plc1.read_area(0x82,0,10,1)
        V36_4 = get_bool(V_byte_3_4,0,0)
        V38_4 = get_bool(V_byte_3_4,0,1)
        V39_4 = get_bool(V_byte_3_4,0,2)
        V40_4 = get_bool(V_byte_3_4,0,3)

        V_byte_1_6 = plc2.read_area(0x82,0,10,1)
        V01_6 = get_bool(V_byte_1_6,0,1)
        V02_6 = get_bool(V_byte_1_6,0,0)
        V03_6 = get_bool(V_byte_1_6,0,3)
        V04_6 = get_bool(V_byte_1_6,0,5)
        V05_6 = get_bool(V_byte_1_6,0,4)
        V06_6 = get_bool(V_byte_1_6,0,6)
        V07_6 = get_bool(V_byte_1_6,0,2)
        V08_6 = get_bool(V_byte_1_6,0,7)

        V_byte_2_6 = plc2.read_area(0x82,0,11,1)
        V09_6 = get_bool(V_byte_2_6,0,3)
        V10_6 = get_bool(V_byte_2_6,0,5)
        V11_6 = get_bool(V_byte_2_6,0,4)
        V12_6 = get_bool(V_byte_2_6,0,7)
        V19_6 = get_bool(V_byte_2_6,0,6)
        V21_6 = get_bool(V_byte_2_6,0,1)
        V22_6 = get_bool(V_byte_2_6,0,0)
        V23_6 = get_bool(V_byte_2_6,0,2)
    
        V_byte_3_6 = plc2.read_area(0x82,0,12,1)
        V13_6 = get_bool(V_byte_3_6,0,1)
        V14_6 = get_bool(V_byte_3_6,0,0)
        V15_6 = get_bool(V_byte_3_6,0,3)
        V16_6 = get_bool(V_byte_3_6,0,2)
        V17_6 = get_bool(V_byte_3_6,0,7)
        V18_6 = get_bool(V_byte_3_6,0,5)
        V20_6 = get_bool(V_byte_3_6,0,4)

        V_byte_4_6 = plc2.read_area(0x82,0,25,1)
        V24_6 = get_bool(V_byte_4_6,0,0)
        V25_6 = get_bool(V_byte_4_6,0,1)

        V_byte_5_6 = plc2.read_area(0x82,0,0,1)
        V60_6 = get_bool(V_byte_5_6,0,0)
        V61_6 = get_bool(V_byte_5_6,0,1)
        V62_6 = get_bool(V_byte_5_6,0,2)
        V70_6 = get_bool(V_byte_5_6,0,3)

        V_byte_1_keg = plc3.read_area(0x82,0,21,1)
        V01_keg = get_bool(V_byte_1_keg,0,0)
        V02_keg = get_bool(V_byte_1_keg,0,1)
        V03_keg = get_bool(V_byte_1_keg,0,2)
        V04_keg = get_bool(V_byte_1_keg,0,3)
        V05_keg = get_bool(V_byte_1_keg,0,4)
        V30_keg = get_bool(V_byte_1_keg,0,5)
        V07_keg = get_bool(V_byte_1_keg,0,6)
        V31_keg = get_bool(V_byte_1_keg,0,7)

        V_byte_2_keg = plc3.read_area(0x82,0,22,1)
        V32_keg = get_bool(V_byte_2_keg,0,0)
        V33_keg = get_bool(V_byte_2_keg,0,1)
        V34_keg = get_bool(V_byte_2_keg,0,2)
        V35_keg = get_bool(V_byte_2_keg,0,3)
        V36_keg = get_bool(V_byte_2_keg,0,4)
        V37_keg = get_bool(V_byte_2_keg,0,5)
        V38_keg = get_bool(V_byte_2_keg,0,6)
        V39_keg = get_bool(V_byte_2_keg,0,7)

        V_byte_3_keg = plc3.read_area(0x82,0,26,1)
        V40_keg = get_bool(V_byte_3_keg,0,2)
        V41_keg = get_bool(V_byte_3_keg,0,3)
        V42_keg = get_bool(V_byte_3_keg,0,4)
        V43_keg = get_bool(V_byte_3_keg,0,5)

        V_byte_1_2 = plc4.read_area(0x82,0,8,1)
        V01_2 = get_bool(V_byte_1_2,0,1)
        V02_2 = get_bool(V_byte_1_2,0,2)
        V03_2 = get_bool(V_byte_1_2,0,3)
        V08_2 = get_bool(V_byte_1_2,0,4)
        V43_2 = get_bool(V_byte_1_2,0,5)

        V_byte_2_2 = plc4.read_area(0x82,0,9,1)
        V04_2 = get_bool(V_byte_2_2,0,0)
        V05_2 = get_bool(V_byte_2_2,0,1)
        V06_2 = get_bool(V_byte_2_2,0,2)
        V07_2 = get_bool(V_byte_2_2,0,3)
        V21_2 = get_bool(V_byte_2_2,0,4)
        V23_2 = get_bool(V_byte_2_2,0,5)

        V_byte_3_2 = plc4.read_area(0x82,0,10,1)
        V30_2 = get_bool(V_byte_3_2,0,0)
        V31_2 = get_bool(V_byte_3_2,0,1)
        V32_2 = get_bool(V_byte_3_2,0,2)
        V39_2 = get_bool(V_byte_3_2,0,3)
        V42_2 = get_bool(V_byte_3_2,0,4)
        V44_2 = get_bool(V_byte_3_2,0,5)
        V45_2 = get_bool(V_byte_3_2,0,6)
        V46_2 = get_bool(V_byte_3_2,0,7)

        V_byte_4_2 = plc4.read_area(0x82,0,11,1)
        V33_2 = get_bool(V_byte_3_2,0,0)
        V34_2 = get_bool(V_byte_3_2,0,1)
        V35_2 = get_bool(V_byte_3_2,0,2)
        V36_2 = get_bool(V_byte_3_2,0,3)
        V38_2 = get_bool(V_byte_3_2,0,5)
        V40_2 = get_bool(V_byte_3_2,0,6)
        V41_2 = get_bool(V_byte_3_2,0,7)

        V_byte_1_PET_Keg = plc5.read_area(0x82,0,32,1)
        V60_PET_Keg = get_bool(V_byte_1_PET_Keg,0,5)
        V61_PET_Keg = get_bool(V_byte_1_PET_Keg,0,6)
        V01_05 = get_bool(V_byte_1_PET_Keg,0,7)

        V_byte_2_PET_Keg = plc5.read_area(0x82,0,33,1)
        V01_07 = get_bool(V_byte_2_PET_Keg,0,0)
        V02_01 = get_bool(V_byte_2_PET_Keg,0,1)
        V02_02 = get_bool(V_byte_2_PET_Keg,0,2)
        V01_11 = get_bool(V_byte_2_PET_Keg,0,5)
        V80_PET_Keg = get_bool(V_byte_2_PET_Keg,0,6)

        V_byte_3_PET_Keg = plc5.read_area(0x82,0,40,1)
        V01_09 = get_bool(V_byte_3_PET_Keg,0,3)
        V01_10 = get_bool(V_byte_3_PET_Keg,0,4)
        V01_12 = get_bool(V_byte_3_PET_Keg,0,5)
        V01_51 = get_bool(V_byte_3_PET_Keg,0,7)

        V_byte_4_PET_Keg = plc5.read_area(0x82,0,41,1)
        V01_57 = get_bool(V_byte_4_PET_Keg,0,0)
        V02_04 = get_bool(V_byte_4_PET_Keg,0,1)
        V02_05 = get_bool(V_byte_4_PET_Keg,0,2)
        V01_08 = get_bool(V_byte_4_PET_Keg,0,4)
        V02_08 = get_bool(V_byte_4_PET_Keg,0,5)
        V02_09 = get_bool(V_byte_4_PET_Keg,0,6)

        time.sleep(5)
    
        date = datetime.datetime.now()
        if date.minute < 10:
            minute = '0'+str(date.minute)
        else:
            minute = date.minute
        if date.hour < 10:
            hour = '0'+str(date.hour)
        else:
            hour = date.hour

        day = str(date.month) + '/' + str(date.day) + '/' + str(date.year).replace('20', '')
        time_recvd = str(hour)+':'+str(minute)+':'+str(date.second)

        insert_values_4 = [
        (j, day, time_recvd, str(flow_format_4), str(PU_format_4), str(temp_past_format_4), str(temp_cool_format_4), str(press_past_format_4)),
        ]

        insert_valves_4 = [
        (j, day, time_recvd, BtS(V01_4), BtS(V02_4), BtS(V03_4), BtS(V04_4), BtS(V05_4), BtS(V06_4), BtS(V07_4),
         BtS(V08_4), BtS(V13_4), BtS(V16_4), BtS(V30_4), BtS(V31_4), BtS(V32_4), BtS(V33_4), BtS(V34_4),
         BtS(V35_4), BtS(V36_4), BtS(V38_4), BtS(V39_4), BtS(V40_4))
        ]

        insert_values_6 = [
        (j, day, time_recvd, str(flow_format_6), str(PU_format_6), str(temp_past_format_6), str(temp_cool_format_6), str(press_past_format_6)),
        ]

        insert_valves_6 = [
        (j, day, time_recvd, BtS(V01_6), BtS(V02_6), BtS(V03_6), BtS(V04_6), BtS(V05_6), BtS(V06_6), BtS(V07_6),
         BtS(V08_6), BtS(V09_6), BtS(V10_6), BtS(V11_6), BtS(V12_6), BtS(V13_6), BtS(V14_6), BtS(V14_6),
         BtS(V15_6), BtS(V16_6), BtS(V17_6), BtS(V18_6), BtS(V19_6), BtS(V20_6), BtS(V21_6),
         BtS(V22_6), BtS(V23_6), BtS(V24_6), BtS(V25_6), BtS(V60_6), BtS(V61_6), BtS(V70_6))
        ]

        insert_values_keg = [
        (j, day, time_recvd, str(flow_format_keg), str(PU_format_keg), str(temp_past_format_keg), str(temp_cool_format_keg), str(press_past_format_keg)),
        ]

        insert_valves_keg = [
        (j, day, time_recvd, BtS(V01_keg), BtS(V02_keg), BtS(V03_keg), BtS(V04_keg), BtS(V05_keg), BtS(V07_keg),
         BtS(V30_keg), BtS(V31_keg), BtS(V32_keg), BtS(V33_keg), BtS(V34_keg), BtS(V35_keg), BtS(V36_keg), BtS(V37_keg),
         BtS(V38_keg), BtS(V39_keg), BtS(V40_keg), BtS(V41_keg), BtS(V42_keg), BtS(V43_keg))
        ]

        insert_values_2 = [
        (j, day, time_recvd, str(flow_format_2), str(PU_format_2), str(temp_past_format_2), str(temp_cool_format_2), str(press_past_format_2)),
        ]

        insert_valves_2 = [
        (j, day, time_recvd, BtS(V01_2), BtS(V02_2), BtS(V03_2), BtS(V04_2), BtS(V05_2), BtS(V06_2),
         BtS(V07_keg), BtS(V08_2), BtS(V21_2), BtS(V23_2), BtS(V30_2), BtS(V31_2), BtS(V32_2),
         BtS(V33_2), BtS(V34_2), BtS(V35_2), BtS(V36_2), BtS(V38_2), BtS(V39_2),    
         BtS(V40_2), BtS(V41_2), BtS(V42_2), BtS(V43_2), BtS(V44_2), BtS(V45_2), BtS(V46_2))
        ]

        insert_values_PET_Keg = [
        (j, day, time_recvd, str(flow_format_PET_Keg), str(PU_format_PET_Keg), str(temp_past_format_PET_Keg), str(temp_cool_format_PET_Keg), str(press_past_format_PET_Keg)),
        ]

        insert_valves_PET_Keg = [
        (j, day, time_recvd, BtS(V01_05), BtS(V01_07), BtS(V01_08), BtS(V01_09),
         BtS(V01_10), BtS(V01_11), BtS(V01_12), BtS(V01_51), BtS(V01_57),
         BtS(V02_01), BtS(V02_02), BtS(V02_04), BtS(V02_05), BtS(V02_08), BtS(V02_09),
         BtS(V60_PET_Keg), BtS(V61_PET_Keg), BtS(V80_PET_Keg))
        ]
    
        with sqlite3.connect('database.db') as db:
        
            cursor1 = db.cursor()
            query1 = """INSERT INTO Paster_PET_4(id, date, time, flow, PU, temp_past, temp_cool, press_past)
                VALUES(?,?,?,?,?,?,?,?)"""
        
            cursor2 = db.cursor()
            query2 = """INSERT INTO Valves_PET_4(id, date, time, V01,
                V02, V03, V04, V05, V06, V07,
                V08, V13, V16, V30, V31, V32,
                V33, V34, V35, V36, V38, V39,
                V40)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""

            cursor3 = db.cursor()
            query3 = """INSERT INTO Paster_Glass_6(id, date, time, flow, PU, temp_past, temp_cool, press_past)
                VALUES(?,?,?,?,?,?,?,?)"""

            cursor4 = db.cursor()
            query4 = """INSERT INTO Valves_Glass_6(id, date, time, V01,
                V02, V03, V04, V05, V06, V07,
                V08, V09, V10, V11, V12, V13,
                V14, V15, V16, V17, V18, V19,
                V20, V21, V22, V23, V24, V25,
                V60, V61, V62, V70)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""

            cursor5 = db.cursor()
            query5 = """INSERT INTO Paster_Keg(id, date, time, flow, PU, temp_past, temp_cool, press_past)
                VALUES(?,?,?,?,?,?,?,?)"""

            cursor6 = db.cursor()
            query6 = """INSERT INTO Valves_Keg(id, date, time, V01,
                V02, V03, V04, V05, V07,
                V30, V31, V32, V33, V34, V35,
                V36, V37, V38, V39, V40, V41,
                V42, V43)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""

            cursor7 = db.cursor()
            query7 = """INSERT INTO Paster_PET_2(id, date, time, flow, PU, temp_past, temp_cool, press_past)
                VALUES(?,?,?,?,?,?,?,?)"""

            cursor8 = db.cursor()
            query8 = """INSERT INTO Valves_PET_2(id, date, time, V01,
              V02, V03, V04, V05, V06, V07,
              V08, V21, V23, V30, V31, V32,
              V33, V34, V35, V36, V38, V39,
              V40, V41, V42, V43, V44, V45,
              V46)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""

            cursor9 = db.cursor()
            query9 = """INSERT INTO Paster_PET_Keg(id, date, time, flow, PU, temp_past, temp_cool, press_past)
                VALUES(?,?,?,?,?,?,?,?)"""

            cursor10 = db.cursor()
            query10 = """INSERT INTO Valves_PET_Keg(id, date, time, V01_05,
              V01_07, V01_08, V01_09, V01_10, V01_11, V01_12, V01_51, V01_57,
              V02_01, V02_02, V02_04, V02_05, V02_08, V02_09, V60, V61, V80)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        
        cursor1.executemany(query1, insert_values_4)
        cursor2.executemany(query2, insert_valves_4)
        cursor3.executemany(query3, insert_values_6)
        cursor4.executemany(query4, insert_valves_6)
        cursor5.executemany(query5, insert_values_keg)
        cursor6.executemany(query6, insert_valves_keg)
        cursor7.executemany(query7, insert_values_2)
        cursor8.executemany(query8, insert_valves_2)
        cursor9.executemany(query9, insert_values_PET_Keg)
        cursor10.executemany(query10, insert_valves_PET_Keg)
        db.commit()

        j+=1

    except:
        logger.warning('NO connection')
        time.sleep(5)
