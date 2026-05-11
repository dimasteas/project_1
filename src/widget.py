from .masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """
    Обрабатывает информацию о карте или счёте и возвращает строку
    с замаскированным номером.
    """
    # Разделяем строку на слова
    parts = info.split()

    # Последний элемент — это номер, всё остальное — тип
    number = parts[-1]
    type_name = " ".join(parts[:-1])

    # Определяем, счёт это или карта
    if type_name.lower().startswith("счет"):
        # Для счёта используем маску **XXXX
        masked_number = get_mask_account(number)
    else:
        # Для карты используем маску карты
        masked_number = get_mask_card_number(number)

    return f"{type_name} {masked_number}"


def get_date(date_str: str) -> str:
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
