import logging

def configure_logging():
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler("app.log"), logging.StreamHandler()])
    return logging.getLogger(__name__)

logger=configure_logging()

def log_request_info(req_method, req_path, status_code, req_body, res_body):
    logging.info(f"Request Method: {req_method}")
    logging.info(f"Request Path: {req_path}")
    logging.info(f"Status Code: {status_code}")
    logging.info(f"Request Body: {req_body}")
    logging.info(f"Response Body: {res_body}")
    