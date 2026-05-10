def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, оставляя видимыми первые 6 и последние 4 цифры.
    """
    masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета, оставляя видимыми только последние 4 цифры.
    """
    masked = f"**{account_number[-4:]}"
    return masked
