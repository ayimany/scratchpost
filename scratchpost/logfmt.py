import logging


class ColorFormatter(logging.Formatter):
    # ANSI Escape Codes for Colors
    GREY = "\x1b[38;20m"
    YELLOW = "\x1b[33;20m"
    RED = "\x1b[31;20m"
    BOLD_RED = "\x1b[31;1m"
    BLUE = "\x1b[34;20m"
    RESET = "\x1b[0m"

    # Define the format for the brackets and level name
    FORMAT_STYLE = "[%(levelname)s]"

    COLORS = {
        logging.DEBUG: BLUE,
        logging.INFO: GREY,
        logging.WARNING: YELLOW,
        logging.ERROR: RED,
        logging.CRITICAL: BOLD_RED,
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelno, self.GREY)

        # Create the colored bracketed level name
        colored_level = f"{log_color}[{record.levelname}]{self.RESET}"

        # Save the original levelname to restore it later
        original_levelname = record.levelname
        record.levelname = colored_level

        log_fmt = "%(levelname)s %(asctime)s - %(message)s"
        formatter = logging.Formatter(log_fmt, datefmt="%H:%M:%S")

        result = formatter.format(record)

        # Restore original levelname so other handlers aren't affected
        record.levelname = original_levelname
        return result


logger = logging.getLogger("Scratchpost")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setFormatter(ColorFormatter())
logger.addHandler(ch)
