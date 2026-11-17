"""Заготовка Ф1.1-Ф1.2: веб-форма заявки с автопроверкой (FR-1, FR-2, БП-1)."""


def validate_application(data):
    """Автопроверка полей заявки ученика перед приёмом."""
    required = ["fio", "passport", "birth_date", "category"]
    missing = [f for f in required if not data.get(f)]
    return {"valid": not missing, "missing": missing}
