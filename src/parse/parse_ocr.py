import re


def parse_ocr_amount(text: str):
    """
    parse_ocr_amount: Uses regex to parse long line of text to find amount
    """
    match = re.findall(
        r"(?:Total|Amount|MYR|RM|Ringgit Malaysia|Ringgit|Jumlah|Bayar)[\s:]*(\d+\.\d{2})",
        string=text,
        flags=re.IGNORECASE,
    )

    if match:
        return match
    else:
        return False
