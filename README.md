
## Client Testing

This repo contains a method similar to one in the client for the project 
along with a test for that function.

### To Run the Test

* Create a virtual environment
* Install the requirements
* Run `pytest`

## Discussion

The function does not return any value, so there is nothing to test in the
traditional sense.  Instead, we want to test a *side effect* of the function -
mainly that the function makes an appropriate call to the `requests.put` function.

To do this, we use the `requests-mock` library to *spy* on the function.  The 
test sets up the system to capture all calls to the `requests` library.  We
then make a call to our function, and afterward we interrogate the spy to ensure
that our function made the proper call to `requests.put`.
