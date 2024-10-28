from google.cloud import secretmanager

def get_token(prj_id):
    secret_name = f'projects/{prj_id}/secrets/send_grid_token/versions/latest'

    client = secretmanager.SecretManagerServiceClient()
    res = client.access_secret_version(name=secret_name)
    return res.payload.data