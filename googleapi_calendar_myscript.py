from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime
import json
from time import sleep
import os,os.path,sys,subprocess
import inspect,sys, traceback



def auth_setup(eventKind):
    # Setup the Calendar API
    # FOLLOWING CODE ALONG WTH verify_creds IS MANDATORY TO CONNECT TO CALENDAR API, AUTHENTICATE, AUTHORIZE YOUR APP

    print ('\n\nIN FUNCTION RIGHT NOW:-',inspect.stack()[0][3])

    if eventKind.upper()=='ADD':

       print ('\n\n CALENDAR OPERATION SELECTED:-',eventKind.upper())
       SCOPES = 'https://www.googleapis.com/auth/calendar'
       json_data = file.Storage('credentials.json')
       service=verify_creds(SCOPES,json_data)
       return service

    elif eventKind.upper()=='VIEW':

       print ('\n\n CALENDAR OPERATION SELECTED:-',eventKind.upper())
       SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
       json_data = file.Storage('credentials.json')
       service=verify_creds(SCOPES,json_data)
       return service

    elif eventKind.upper()=='DELETE':
        print ('\n\n CALENDAR OPERATION SELECTED:-',eventKind.upper())
        SCOPES = 'https://www.googleapis.com/auth/calendar'
        json_data = file.Storage('credentials.json')
        service=verify_creds(SCOPES,json_data)
        return service


    elif eventKind.upper()=='LIST':
        print ('\n\n CALENDAR OPERATION SELECTED:-',eventKind.upper())
        SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
        json_data = file.Storage('credentials.json')
        service=verify_creds(SCOPES,json_data)
        return service

    elif eventKind.upper()=='ADD_DELETE':
        print ('\n\n CALENDAR OPERATION SELECTED:-',eventKind.upper())
        SCOPES = 'https://www.googleapis.com/auth/calendar'
        json_data = file.Storage('credentials.json')
        service=verify_creds(SCOPES,json_data)
        return service


    else:
       return ('INVALID OPERATION ENTERED. EXITING THE SCRIPT')



def verify_creds(SCOPES,json_data):
    print ('\n\nIN FUNCTION RIGHT NOW:-',inspect.stack()[0][3])
    print ('CREDS AND SCOPE:-',json_data,SCOPES)
    creds = json_data.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('/home/ary/PycharmProjects/Python_files_in_Ubuntu/client_secret.json', SCOPES)
        creds = tools.run_flow(flow, json_data)

    service = build('calendar', 'v3', http=creds.authorize(Http()))
    print ('SERVICE OBJECT RETURNED BY VERIFY_CREDS:-',service)
    return service


def add_event(service,cid):

    # 2] ADDING AN EVENT IN THE CALENDAR. FOR THIS YOU NEED TO CHANGE THE SCOPE TO
    # SCOPES = 'https://www.googleapis.com/auth/calendar' AND NOT readonly
    # Also delete the old credentials.json from the script.

    print ('\n\nIN FUNCTION RIGHT NOW:-',inspect.stack()[0][3])
    print ('ADDING A NEW EVENT IN CALENDAR AFTER SLEEPING FOR 5 SECONDS\n\n')
    sleep(5)
    myevent= {

        "description": "TENNIS PLAY",
        "creator": {
            "email": "aryan21710@gmail.com",
            "displayName": "aryan sharma"
        },


            "start": {
            "dateTime": "2018-05-13T06:00:00+05:30",
            "timeZone": "GMT+05:30"
            },
             "end":{
            "dateTime": "2018-05-13T08:00:30+05:30",
            "timeZone": "GMT+05:30"
             },

        "attendees": [
            {
                "email": "arysharma1209@gmail.com"


            }],


    }


    myevent2= {
        "kind": "calendar#events",
        "summary": "google_api_testing",
        "timeZone": "Asia/Calcutta",
        "defaultReminders": [
        ],
        "items": [
            {


                "kind": "calendar#event",
                "htmlLink": "https://www.google.com/calendar/event?eid=NDBtY2dhOG5vZzF0bGQ3dm52azUwN3V1azIgbWRvamxyZXRwMHM4YWhsb2J1Y3FpNWo2Z29AZw",
                "summary": "Mom's death Anniversary",
                "location": "Prestige Tranquility, Budigere Cross, Off Old Madras Road, Bengaluru, Karnataka 560049, India",

                "organizer": {
                    "email": "mdojlretp0s8ahlobucqi5j6go@group.calendar.google.com",
                    "displayName": "google_api_testing",
                },
                "start": {
                    "dateTime": "2018-05-13T09:00:00+05:30",
                    "timeZone": "GMT+05:30"


                },
                "end": {
                    "dateTime": "2018-05-14T11:00:00+05:30",
                    "timeZone": "GMT+05:30"

                },
                "attendees": [
                    {
                        "email": "seemasam1223@gmail.com",
                        "responseStatus": "needsAction"
                    }
                ],

            }
        ]
    }


    myevent3= { 'summary' : 'TITLE TEST EVENT', 'description' : 'TEST EVENT', 'location' : 'Prestige Tranquility Bangalore'
                 , 'start' : {'dateTime': '2018-05-15T09:00:00+05:30', 'timeZone' : 'GMT+05:30'}, 'end' : {'dateTime' : '2018-05-15T11:00:00+05:30', 'timeZone' : 'GMT+05:30'},
                'attendees': [ {'email' : 'aryan21710@gmail.com' }, {'email' : 'seemasam1223@gmail.com'}], }

    try:
       addrequest=service.events().insert(calendarId=cid,body=myevent3).execute()
       print ('CALENDAR EVENT ADDED:-\n\n',addrequest)
       servAndEventId=get_event_id(service,addrequest,cid)
       return servAndEventId
    except Exception as exc:
        e=sys.exc_info()[0]
        print ('INVALID INPUT', e, ':' ,exc)
        print ('TRACEBACK:-',traceback.format_exc())


        print ('ADDING AN EVENT FAILED... FAILING THE SCRIPT')
        return False


def get_event_id(service,addrequest,cid):

    print ('\n\n IN FUNCTION RIGHT NOW...',inspect.stack()[0][3])
    servAndEventId=[]
    servAndEventId.append(service)
    for key,value in addrequest.items():
        print ('KEY ...',key)
        if key=='id':
            print ('EVENT ID:-',addrequest['id'])
            servAndEventId.append(addrequest['id'])
            return servAndEventId
        else:
            print ('EVENTID NOT FOUND....')




def view_calendarId(service,cid):
    # 1] CALENDAR ID WILL BE AVAILABLE AT FOLLOWING LINK WHICH IS A MANDATORY ARGUMENT.
    # 'https://calendar.google.com/calendar/r/settings/calendar/bWRvamxyZXRwMHM4YWhsb2J1Y3FpNWo2Z29AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ'

    print ('\n\nIN FUNCTION RIGHT NOW:-',inspect.stack()[0][3])
    print ('SERVICE OBJECT RETURNED IN view_calendarId:-',service)
    try:
        request=service.calendarList().get(calendarId=cid)
        output=request.execute()
        print ('\nTHE NEW CALENDAR CREDENTIALS ARE AS FOLLOWS:-',output)
        print ('\nTHE CALENDAR CREDENTIALS IN PYTHON DICTIONARY FORMAT...')
        print (output)

        for key,value in output.items():
            #print ('key :-',key)
            if key=='summary':
                print ('\n\nTHE CALENDAR NAME IS....',output['summary'])
    except:
        print ('SERVICE OBJECT NOT RETURNED BY VERIFY_CREDS...FAILING THE SCRIPT')



def delete_event(service,myeventId,cid):
    print ('\n\nIN FUNCTION RIGHT NOW...',inspect.stack()[0][3])
    print ('SERVICE OBJECT RETURNED IN delete_event:-',service)
    print ('EVENTID RETURNED IN delete_event...',myeventId)

    delReq=service.events().delete(calendarId=cid,eventId=myeventId).execute()

    #resp=delReq.execute()
    print ('DELETE OPERATION RESULT...',delReq)


def get_events_list(service,cid):
    print ('\n\nIN FUNCTION RIGHT NOW...',inspect.stack()[0][3])
    print ('SERVICE OBJECT RETURNED IN delete_event:-',service)
    lstEvents=service.events().list(calendarId=cid).execute()
    print ('\nLIST OF EVENTS ...',lstEvents)
    evntIdList=[]
    for key,value in lstEvents.items():
        if key=='items':
            out=lstEvents['items']
            print (len(out))
            if len(out) > 1:
                for i in out:
                    print ('LIST ENTRIES OF OUT:-',i)
                    for k,v in i.items():
                        if k=='description':
                            name=i[k]
                            #print ('EVENT NAME :-',name)
                        elif k=='start':
                            for k1,v1 in i[k].items():
                                startTime=i[k][k1]
                                #print ('START TIME:-',startTime)
                                print ('\n\n\nTHE EVENT DETAILS ARE ...',name,' ON ',startTime)

                        elif k=='id':
                            print ('\n\nEVENT ID:-',i[k])
                            evntIdList.append(i[k])

    print ('LIST OF EVENT-ID...',evntIdList)
    return evntIdList


if os.path.isfile('credentials.json') and os.path.getsize('credentials.json') > 0:
    delFile=subprocess.check_output(['rm','-rf','credentials.json'])
    print ('DELETED THE OLD CREDENTIALS.JSON FILE... SLEEPING FOR 5sec\n\n')
    sleep(5)

cid='mdojlretp0s8ahlobucqi5j6go@group.calendar.google.com'
print('ENTER WHAT KIND OF OPERATION TO PERFROM ON YOUR CALENDAR')
print ('ADD to add an event, DELETE to delete an event, VIEW to view an event, \
       ADD_DELETE to add and event first and delete the same event later, LIST to see the list of events')
operation=raw_input('ENTER NOW:- ')
pwd=os.getcwd()
print ('\n\nSCRIPT RUNNING IN FOLLOWING DIR...',pwd)

service=auth_setup(operation)

print ('\n\n SERVICE OBJECT RETURNED IN MAIN PROGRAM:-',service)

if operation.upper()=='ADD':
    add_event(service,cid)

elif operation.upper()=='ADD_DELETE':
    print ('\n\nLETS ADD AN EVENT FIRST TO PERFORM THE DELETE OPERATION')
    servAndEventId=add_event(service,cid)
    if len(servAndEventId) > 1:
       delete_event(servAndEventId[0],servAndEventId[1],cid)

elif operation.upper()=='VIEW':
    view_calendarId(service,cid)

elif operation.upper()=='LIST':
    evntIdList=get_events_list(service,cid)

elif operation.upper()=='DELETE':
    delete_event(service,myeventId,cid)



