import logging

def get_logger():
    try:
        logging.basicConfig(
            filename="logs/app.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        return logging.getLogger()
    except Exception as e:
        print("Logger error:", e)
        return None
