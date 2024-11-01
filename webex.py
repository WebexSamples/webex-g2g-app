import requests

class WebexAPI:
    """
    A class representing the Webex API.

    Args:
        access_token (str): The access token for authenticating API requests.

    Attributes:
        access_token (str): The access token for authenticating API requests.
        base_url (str): The base URL of the Webex API.

    Methods:
        make_request: Sends a request to the Webex API.
        create_meeting: Creates a new meeting.

    """

    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = 'https://webexapis.com/v1'

    def make_request(self, method, endpoint, params=None, data=None):
        """
        Sends a request to the Webex API.

        Args:
            method (str): The HTTP method for the request (e.g., 'GET', 'POST', 'PUT', 'DELETE').
            endpoint (str): The API endpoint to send the request to.
            params (dict, optional): The query parameters for the request.
            data (dict, optional): The JSON data for the request.

        Returns:
            dict: The JSON response from the API.

        Raises:
            Exception: If the request fails with a non-200 status code.

        """
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

        url = f'{self.base_url}/{endpoint}'

        print(f'Making {method} request to {url}')

        response = requests.request(method, url, headers=headers, params=params, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            print(response.json())
            raise Exception(f'Request failed with status code {response.status_code}')
        
    def create_meeting(self, title, start, end):
        """
        Creates a new meeting with the specified title, start time, and end time.

        Args:
            title (str): The title of the meeting.
            start (str): The start time of the meeting in ISO 8601 format.
            end (str): The end time of the meeting in ISO 8601 format.

        Returns:
            dict: The response from the API containing information about the created meeting.

        Raises:
            Exception: If the request to create the meeting fails.

        """
        data = {
            "title": f"{title}",
            "start": start,
            "end": end,
            "enabledJoinBeforeHost": True,
            "joinBeforeHostMinutes": 15,
            "unlockedMeetingJoinSecurity": "allowJoin"
        }
        try:
            response = self.make_request('POST', 'meetings', data=data)
            return response
        except Exception as e:
            raise e
        
    def join_meeting(self, meeting_id, password, email, display_name):
        """
        Makes a Webex meeting join link API request.

        Args:
            meeting_id (str): The ID of the meeting to join.
            password (str): The password for the meeting.
            email (str): The email address of the user joining the meeting.
            display_name (str): The display name of the user joining the meeting.

        Returns:
            dict: The response from the API containing the join link.

        """
        data = {
            "meetingId": meeting_id,
            "password": password,
            "joinDirectly": False,
            "email": email,
            "displayName": display_name
        }
        try:
            response = self.make_request('POST', 'meetings/join', data=data)
            return response
        except Exception as e:
            raise e
        
# Example usage:
# access_token = 'your_access_token_here'
# api = WebexAPI(access_token)
# response = api.make_request('GET', 'rooms')
# print(response)