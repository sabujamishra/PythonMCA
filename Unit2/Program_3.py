import logging

logging.basicConfig(
    filename="system_exceptions.log",   
    level=logging.ERROR,                
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def generate_exception():
    try:
        result = 10 / 0
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print("Error: Division by zero occurred.")
        logging.error("Arithmetic Exception: %s", e)
    finally:
        print("Execution complete.")

generate_exception()
