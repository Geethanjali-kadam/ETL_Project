import logging

logging.basicConfig(
    filename="etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("ETL Process Started")

print("ETL Running...")

logging.info("ETL Process Completed")