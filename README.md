# Econoday RESTful - Get Modified events.

This is a "Get Modified events" Python script on how to talk to the Econoday
system with RESTful calls.

# To Configure Python Script:
The only configuration that is needed will be to replace the variable TOKEN with
your token key that was purchased from Econoday.

# To Run:
`python3 getmodevents.py`

The python script will perform two API calls. The first will get all the events
in the Econoday system that you have access, that have been modified on the
current date. A list of events that were modified as of the current date will
be listed. You can enter the number of the event and at this point another
RESTful API is performed to get the details of he event.

# RESTful API Documentation:

The HTML or OpenAPI/Swagger file relating to the RESTful API calls can be found here:

https://api.econoday.com/api/api.html

https://api.econoday.com/api/api.yaml

# Contact US
If you have any questions, comments or suggestions you can email us at support@econoday.com

# About Us
Econoday Inc.
3736 Mt. Diablo Boulevard, Suite #205
Lafayette, CA 94549 United States
+1 (925) 299-5355
+1 (800) 988-3332
info@econoday.com

Econoday launched in 1990 when a trading floor economist, an institutional
salesperson and a desktop publishing expert decided to teach investors how
economic events move markets and influence trading decisions. 
