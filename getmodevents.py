#!/usr/bin/env python3

import json
import os
import requests
import datetime

# for documentation from go here
# https://api.econoday.com/api/api.html
# This code will query all new modified events that happen on the current day.
# please note this code does not query by "released on dates" but rather when
# the # event was last touched. So an event that is released on this day may not
# appear in the list found if it has not been updated yet.

TOKEN = "12345678901234567890123456789012"

SITE_NAME = "https://api.econoday.com"
BASE_PATH_LASTMOD = "/api/v1/geteventsbylastmod?token="+TOKEN
BASE_PATH_DETAILS = "/api/v1/geteventdetails?token="+TOKEN

BASE_PATH_LASTMOD = BASE_PATH_LASTMOD+"&startd="+(datetime.datetime.today().strftime('%m-%d-%Y'))


def mid(s, offset, amount):
    return s[offset-1:offset+amount-1]

try:
    r = requests.get(SITE_NAME+BASE_PATH_LASTMOD, verify=True)
    if (r.status_code == 200):
        os.system('clear')
        parsed_json = r.json()

        # Uncomment to see the JSON return by the unit
        # print (parsed_json)

        iStatusCode = int(parsed_json['status']['code'])
        cszStatusCode = parsed_json['status']['text']

        if (iStatusCode != 0):
            print(cszStatusCode)
            exit(3)

        count = int(parsed_json['count'])
        cszTimeStamp = parsed_json['timestamp']

        x = datetime.datetime(int(mid(cszTimeStamp, 1, 4)), int(mid(cszTimeStamp, 5, 2)), int(mid(cszTimeStamp, 7, 2)), int(mid(cszTimeStamp, 9, 2)), int(mid(cszTimeStamp, 11, 2)))
        print(datetime.datetime.isoformat(x))

        print("Last mod events for %s are:" % (x.strftime('%m-%d-%Y')))
        print("----------------------")
        print("count %d" % (count))
        print("Range lastmod return from %s to %s" % (parsed_json['SDRANGE'], parsed_json['EDRANGE']))

        uid = []

        if (int(iStatusCode) == 0):
            iTotalEvents = 0
            for node in parsed_json['events']:
                eventname = parsed_json['events'][iTotalEvents]['NAME']

                releasedongmt = parsed_json['events'][iTotalEvents]['RELEASED_ON_GMT']
                # print("RELEASED_ON_GMT = "+releasedongmt)
                uid.append(int(parsed_json['events'][iTotalEvents]['UID']))
                # print("UID = "+str(uid[iTotalEvents]))
                iAttribute = int(parsed_json['events'][iTotalEvents]['ATTRIBUTE'])
                # print("ATTRIBUTE = "+iAttribute)

                attributestring = ""
                if ((iAttribute & 1) == 1):
                    attributestring += "one "
                if ((iAttribute & 2) == 2):
                    attributestring += "two "
                if ((iAttribute & 4) == 4):
                    attributestring += "four "
                if ((iAttribute & 8) == 8):
                    attributestring += "eight "
                if ((iAttribute & 16) == 16):
                    attributestring += "sixteen "
                if ((iAttribute & 32) == 32):
                    attributestring += "thirtytwo "
                if ((iAttribute & 64) == 64):
                    attributestring += "sixtyfour "
                if ((iAttribute & 128) == 128):
                    attributestring += "onetwentyeight "
                if ((iAttribute & 256) == 256):
                    attributestring += "twofiftysix "
                if ((iAttribute & 512) == 512):
                    attributestring += "fivetwelve "
                # print("attributestring = %s" % (attributestring))

                frequency = int(parsed_json['events'][iTotalEvents]['FREQUENCY'])
                # print("frequency = %d\n" % (frequency))

                lastmod = parsed_json['events'][iTotalEvents]['MODIFYDATE']
                releasedongmt = parsed_json['events'][iTotalEvents]['RELEASED_ON_GMT']
                # print("%d) %s" % (iTotalEvents+1, eventname))
                print("{:2} {:30} lastmod: {}, releasedon: {}".format(iTotalEvents+1, eventname, lastmod, releasedongmt))

                iTotalEvents += 1

            tempdata = input("Enter event number: ")
            if (len(tempdata) > 0):
                if ((int(tempdata)) <= 0):
                    print("Invalid choice to small.")
                    exit(1)

                if ((int(tempdata)) > iTotalEvents):
                    print("Invalid choice to large.")
                    exit(2)

                cszTemp = ("&format=json&uid=%d&values=1&text=1" % (uid[(int(tempdata) - 1)]))

                r = requests.get(SITE_NAME+BASE_PATH_DETAILS+cszTemp, verify=True)
                if (r.status_code == 200):
                    # parsed_json = r.json()

                    print (parsed_json)
                    # print(parsed_json['events'][0]['FREQUENCY'])
                    # print(parsed_json['events'][0]['VALUES'][0]['VALUE_NAME'])
    else:
        print(r.status_code)

except requests.exceptions.RequestException as e:  # This is the correct syntax
    print (e)
