
import requests
import json

url = 'http://localhost'


def return_results(client_id, job_id, job_results):
    """
    Return the results to the server.  This method should make an HTTP PUT
    call to the url with the following:
    
    * the client_id sent as a query parameter
    * The body of the message should contain
      * 'job_id'
      * 'results'
    """
    data = {'job_id': job_id,
            'results': job_results}

    params = {'client_id': client_id}
    endpoint = f'{url}/put_results'

    requests.put(endpoint, params=params, json=json.dumps(data))

