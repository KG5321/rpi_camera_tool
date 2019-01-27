from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload

class drive_api:

    def __init__(self, scopes, token, credentials):
        self.drive_service = None
        self.SCOPES = scopes
        self.creds = None
        self.token = token
        self.credentials = credentials
    
    def init_drive(self):
        self._get_creds()
        self.drive_service = build('drive', 'v3', credentials=self.creds)

    def _get_creds(self):
        if os.path.exists(self.token):
            with open(self.token, 'rb') as token:
                self.creds = pickle.load(token)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials, self.SCOPES)
                self.creds = flow.run_local_server()
            with open(self.token, 'wb') as token:
                pickle.dump(self.creds, token)

    def upload_file(self, file_name, file, folder_id, mimetype='image/jpeg'):
        file_metadata = {'name': file_name, 'parents': [folder_id]}
        media = MediaFileUpload(file, mimetype=mimetype)
        file = self.drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()