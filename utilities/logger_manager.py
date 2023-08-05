import logging


def setup_logger(log_file, log_level=logging.INFO):
    """
    Set up a logger that writes to a specified file with a specified logging level.

    Parameters:
    log_file (str): The name of the file where the logger will write its messages.
    log_level (int): The level of logging. This is an optional parameter that defaults to logging.INFO.
                     The possible logging levels are: 
                     -10 logging.DEBUG: Detailed information, typically of interest only when diagnosing problems.
                     - 20logging.INFO: Confirmation that things are working as expected.
                     -30 logging.WARNING: An indication that something unexpected happened, 
                                       or may happen in the near future (e.g., ‘disk space low’). 
                                       The software is still working as expected.
                     -40 logging.ERROR: Due to a more serious problem, the software has not been able to perform some function.
                     -50 logging.CRITICAL: A very serious error, indicating that the program itself may be unable to continue running.

    Returns:
    logger: A configured logger object.
    """

    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # If the logger has handlers, remove them before adding a new one
    if logger.hasHandlers():
        logger.handlers.clear()

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.setLevel(log_level)

    return logger


# def setup_logger(log_file, log_level=logging.INFO):
#     logger = logging.getLogger(__name__)
#     formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

#     # File handler
#     file_handler = logging.FileHandler(log_file)
#     file_handler.setLevel(log_level)
#     file_handler.setFormatter(formatter)

#     logger.addHandler(file_handler)
#     logger.setLevel(log_level)

#     return logger


### example of usage###
# def activate_account(request: Request, email: EmailStr):
#     logger = setup_logger('activate_account.log')

#     try:
#         targeted_user = find_account_by_email(request, email)
#         if targeted_user:
#             change_account_status(request, str(targeted_user['_id']), "active")
#     except Exception as e:
#         rais_exeption(status.HTTP_304_NOT_MODIFIED, "an error occured while activating your account, please try again later, or contact support.")
#         logger.error(f'Failed to activate account for user with email {email} due to error: {e}')
