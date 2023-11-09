from django.db.models import TextChoices


class DaysChoice(TextChoices):
    PON = "Pon", "Пон"
    BT = "Vt", "Вт"
    SR = "Sr", "Ср"
    CT = "Ct", "Чт"
    PT = "Pt", "Пт"
    SB = "Sb", "Сб"
    VS = "Vs", "Вс"
    MON = "Mon", "Mon"
    TUE = "Tue", "Tue"
    WED = "Wed", "Wed"
    THU = "Thu", "Thu"
    FRI = "Fri", "Fri"
    SAT = "Sat", "Sat"
    SUN = "Sun", "Sun"
