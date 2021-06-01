# Requirements
# https://www.lambdatest.com/blog/generating-xml-and-html-report-in-pyunit-for-test-automation/
# Fetch first 20 builds which have status as completed, error, timeout
# Once the details are out, change the Build Title of the build_id 12024

# Refer https://www.lambdatest.com/support/docs/api-doc/#/Build/builds for more information
import requests
import json

# Equivalent Python code from https://curl.trillworks.com/
headers = {
    'accept': 'application/json',
    'Authorization': 'Basic aGltYW5zaHUuc2hldGhAZ21haWGI0T2x1OVI4bHdCc1hXVFNhSU9lYlhuNHg5',
}

params = (
    ('limit', '20'),
    ('status', 'completed,error,timeout'),
)

# Updated build information for build 12024
headers_updated_build = {
    'accept': 'application/json',
    'Authorization': 'Basic aGltYW5zaHUuc2hldGhAZ21haWGI0T2x1OVI4bHdCc1hXVFNhSU9lYlhuNHg5',
    'Content-Type': 'application/json',
}

data_updated_build = '{"name":"Updated build details for PyUnit test from prompt"}'

response = requests.get('https://api.lambdatest.com/automation/api/v1/builds', headers=headers, params=params)

print(response)

json_arr = response.json()

# Print the build_id matching our requirements and Change build title of build_id 12024

for loop_var in range(20):
    build_id = ((json_arr['data'][loop_var])['build_id'])
    test_status = ((json_arr['data'][loop_var])['status_ind'])

    if build_id == 12024:
        response_updated_build = requests.patch('https://api.lambdatest.com/automation/api/v1/builds/12024', headers=headers_updated_build, data=data_updated_build)
        print(response_updated_build)

    print ((build_id), (test_status))