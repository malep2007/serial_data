import random
import serial
import config
import time
import requests


def check_port_is_available():
    try:
        ser = serial.Serial(config.SERIAL_PORT, config.BAUD_RATE, timeout=config.PORT_READ_TIMEOUT)
        ser.close()
        return True
    except serial.serialutil.SerialException:
        return False


def listen_process():
    serial_port = serial.Serial(config.SERIAL_PORT, config.BAUD_RATE, timeout=config.PORT_READ_TIMEOUT)
    # log_id = 1
    while True:
        data_read = serial_port.readline()

        if data_read:
            received_data = data_read.decode("utf-8")
            received_data = received_data.strip()
            print "Received: {}".format(received_data)

            # time_stamp = time.asctime(time.localtime(time.time()))  # time.time() for epoch

            log_message = received_data
            # print("log_message: {}".format(log_message))
            datafile = open("logs.csv", 'a')
            datafile.write(log_message + "\n")
            datafile.close()

            # log_id += 1
