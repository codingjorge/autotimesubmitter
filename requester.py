import os
import pprint

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

baseUrl = os.environ.get('baseUrl')
username = os.environ.get('username')
password = os.environ.get('password')
projectName = os.environ.get('projectName')
projectActivityName = os.environ.get('projectActivityName')
employeeId = os.environ.get('employeeId')
timesheetId = os.environ.get('timesheetId')

validate_creds_url = f'{baseUrl}/auth/validateCredentials'

payload = {'txtUsername': username, 'txtPassword': password}

auth_res = requests.post(validate_creds_url, data=payload)

auth_cookies = auth_res.history[0].cookies

view_my_timesheet_res = requests.get(f'{baseUrl}/time/viewMyTimesheet',
                                     cookies=auth_cookies)

soup = BeautifulSoup(view_my_timesheet_res.text, 'html.parser')

csrf_token_element = soup.find(id='time__csrf_token')

csrf_token = csrf_token_element['value']

form_data = {
    '_csrf_token': f'{csrf_token}',
    'initialRows[0][projectName]': f'{projectName}',
    'initialRows[0][projectId]': '',
    'initialRows[0][projectActivityName]': f'{projectActivityName}',
    'initialRows[0][projectActivityId]': '',
    'initialRows[0][0]': '7.5',
    'initialRows[0][TimesheetItemId0]': '',
    'initialRows[0][1]': '7.5',
    'initialRows[0][TimesheetItemId1]': '',
    'initialRows[0][2]': '7.5',
    'initialRows[0][TimesheetItemId2]': '',
    'initialRows[0][3]': '7.5',
    'initialRows[0][TimesheetItemId3]': '',
    'initialRows[0][4]': '7.5',
    'initialRows[0][TimesheetItemId4]': '',
    'initialRows[0][5]': '',
    'initialRows[0][TimesheetItemId5]': '',
    'initialRows[0][6]': '',
    'initialRows[0][TimesheetItemId6]': '',
    'btnSave': 'Save'
}

pprint.pprint(form_data)

# save_timesheet_post_res = requests.post(f'{baseUrl}/time/editTimesheet?'
#                                         f'employeeId={employeeId}&timesheetId={timesheetId}&actionName=viewMyTimesheet',
#                                         data=form_data, cookies=auth_cookies)
#
# pprint.pprint(view_my_timesheet_res.text)
# todo GET TIMESHEET START DATE
# timesheet_start_date = ''
#
# submit_timesheet_post_res = requests.post(f'{baseUrl}/time/viewMyTimesheet?'
#                                           f'act=1&'
#                                           f'timesheetStartDate={timesheet_start_date}&'
#                                           f'employeeId={employeeId}&'
#                                           f'submitted=true&'
#                                           f'updateActionLog=true')
