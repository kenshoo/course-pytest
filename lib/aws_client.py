from boto3 import client


logger = logging.getLogger(__name__)


def get_s3_client(region, key_id, access_key):
    return client('s3',
                  region_name=region,
                  aws_access_key_id=key_id,
                  aws_secret_access_key=access_key)
