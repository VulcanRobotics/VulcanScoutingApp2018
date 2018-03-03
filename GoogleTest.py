import requests

BaseURL = "https://www.googleapis.com/drive/v3"

auth = {"_module": "oauth2client.client", "scopes": ["https://www.googleapis.com/auth/drive.metadata.readonly"], "token_expiry": "2018-03-03T05:22:57Z", "id_token": "null", "user_agent": "Drive API Python Quickstart", "access_token": "ya29.GltzBdVrr2wyNhnTtPYFG0S2AEcXJR4Fp5r5bD7rTLbcULB3_VuHyt912csPszjKVGtYu-2Rw3y1NbtvPeHDE-VWj4uK5W53_rNsLRJMYGR9wLRmMQGaVNFk9N0f", "token_uri": "https://accounts.google.com/o/oauth2/token", "invalid": "false", "token_response": {"access_token": "ya29.GltzBdVrr2wyNhnTtPYFG0S2AEcXJR4Fp5r5bD7rTLbcULB3_VuHyt912csPszjKVGtYu-2Rw3y1NbtvPeHDE-VWj4uK5W53_rNsLRJMYGR9wLRmMQGaVNFk9N0f", "token_type": "Bearer", "expires_in": 3600, "refresh_token": "1/-59ogZe5urh-qsllt899UzDiOxdkhzR7l6PrBAohO1U"}, "client_id": "17591867147-d7ln7ro8ltqjgj5pqgckgjthe8oe6sii.apps.googleusercontent.com", "token_info_uri": "https://www.googleapis.com/oauth2/v3/tokeninfo", "client_secret": "-wohn-YIIB00fkCDUtSRU1WG", "revoke_uri": "https://accounts.google.com/o/oauth2/revoke", "_class": "OAuth2Credentials", "refresh_token": "1/-59ogZe5urh-qsllt899UzDiOxdkhzR7l6PrBAohO1U", "id_token_jwt": "null"}

r = requests.get("https://www.googleapis.com/upload/drive/v3/files")
print r


# file_metadata = {'name': 'photo.jpg'}
# media = MediaFileUpload('files/photo.jpg',
#                         mimetype='image/jpeg')
# file = drive_service.files().create(body=file_metadata,
#                                     media_body=media,
#                                     fields='id').execute()
# print 'File ID: %s' % file.get('id')
