import datetime
import math

def TAI(UTC):
    #UTC TO TAI
    #convert to julian
    julian_datetime = 367 * UTC[0] - int((7 * (UTC[0] + int((UTC[1] + 9) / 12.0))) / 4.0) + int((275 * UTC[1]) / 9.0) + UTC[2] + 1721013.5 + (UTC[3]+10 / math.pow(60,2)) / 24.0 - 0.5 * math.copysign(1, 100 * UTC[0] + UTC[1] - 190002.5) + 0.5
    return julian_datetime

print(TAI(UTC))

def GPST(UTC):
    #UTC TO GPST
    #convert to julian
    julian_datetime = 367 * UTC[0] - int((7 * (UTC[0] + int((UTC[1] + 9) / 12.0))) / 4.0) + int((275 * UTC[1]) / 9.0) + UTC[2] + 1721013.5 + (UTC[3]-9 / math.pow(60,2)) / 24.0 - 0.5 * math.copysign(1, 100 * UTC[0] + UTC[1] - 190002.5) + 0.5
    return julian_datetime

print(GPST(UTC))

def TT(UTC):
    #UTC TO TT
    #convert to julian
    julian_datetime = 367 * UTC[0] - int((7 * (UTC[0] + int((UTC[1] + 9) / 12.0))) / 4.0) + int((275 * UTC[1]) / 9.0) + UTC[2] + 1721013.5 + (UTC[3]+32194 / math.pow(60,2)) / 24.0 - 0.5 * math.copysign(1, 100 * UTC[0] + UTC[1] - 190002.5) + 0.5
    return julian_datetime

print(TT(UTC))
