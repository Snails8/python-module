import functions_framework
import logging
import google.cloud.logging
import datetime
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# デバッグ：環境変数一覧
print(dict(os.environ))

# Cloud Loggingクライアントの初期化
#client = google.cloud.logging.Client(project=project_id)
#client = google.cloud.logging.Client()
# client.setup_logging()

# setup_logging() するとログレベルが INFO になるので DEBUG に変更
logger.setLevel(logging.DEBUG)

str = "test"
logger.warning("test message in main: %s", str)

logger.warning("GOOGLE_CLOUD_PROJECT: %s", os.environ.get('GOOGLE_CLOUD_PROJECT'))

# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def get_forecast(cloud_event):
    print("get_forecast function started")
    logger.info("get_forecast function started")
    try:
        now = datetime.datetime.now()
        logger.info("now: {}".format(now))
        logger.debug("now: {}".format(now))
        logger.warning("now: {}".format(now))
        logger.error("now: {}".format(now))
        logger.critical("now: {}".format(now))
        return "OK"
    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")
        return "Error", 500