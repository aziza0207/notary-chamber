from django.db.models import TextChoices


class DaysChoice(TextChoices):
    PON = "Понедельник", "Понедельник"
    BT = "Вторник", "Вторник"
    SR = "Среда", "Среда"
    CT = "Четверг", "Четверг"
    PT = "Пятница", "Пятница"
    SB = "Суббота", "Суббота"
    VS = "Воскресенье", "Воскресенье"
    MON = "Monday", "Monday"
    TUE = "Tuesday", "Tuesday"
    WED = "Wednesday", "Wednesday"
    THU = "Thursday", "Thursday"
    FRI = "Friday", "Friday"
    SAT = "Saturday", "Saturday"
    SUN = "Sunday", "Sunday"
