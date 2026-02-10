import logging
import re
from dataclasses import dataclass
from typing import Optional

from scratchpole.available_interests import interests, Interest


@dataclass(frozen=True)
class ExtractedInterest:
    key: str
    label: str
    value: str

def find_interest(key: str, gcode: str) -> Optional[ExtractedInterest]:
    if key not in interests.keys():
        logging.warning(f'Could not find interest {key}')
        return None

    interest = interests[key]

    match = re.search(interest.regex, gcode)
    if match:
        return ExtractedInterest(
            key,
            interest.label,
            match.group(1)
        )

    logging.warning(f'Could not find interest {key} within the parsed gcode')
    return None

