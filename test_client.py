
import requests_mock
from client import return_results
import json


def test_client_sends_json_and_params():
    # When we specify a requests_mock object, it will intercept
    # all calls to requests.get, requests.put, requests.post, etc.
    with requests_mock.mock() as mock_requests:
        # First, we set up the mock: We know our code is supposed to call
        # put_results end point.  Here we specify the response that
        # should occur: {} with a status code of 200.  The mock
        mock_requests.put('http://localhost/put_results', text='{}')

        # Now we make a call to the function we want to test using
        # known data
        data = {'data': {
                    'id': 'EPA-HQ-OECA-2004-0024-0048',
                    'type': 'comments'
                    }
               }
        return_results(42, 15, data)

        # the mock_requests object will only respond to the call
        # we specified above, so this tests that our code made the
        # right call
        assert mock_requests.called
        assert mock_requests.call_count == 1

        # The object saved information about the request that our code
        # made.
        request = mock_requests.request_history[0]
        assert request.method == 'PUT'

        # The client id should be in the query string of the request
        # request mocks saves this as a dict in the history
        # NOTE: requests-mock used urllib.parse to parse the query
        # parameters.  This method puts the values in a list!
        # (https://docs.python.org/3/library/urllib.parse.html#urllib.parse.parse_qs)
        assert request.qs['client_id'] == ['42']

        # The client should send the data as the body of the message
        # The .json() method returns the data as a string
        saved_data = json.loads(request.json())
        assert saved_data['job_id'] == 15
        assert saved_data['results']['data']['id'] == 'EPA-HQ-OECA-2004-0024-0048'

