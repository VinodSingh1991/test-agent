"""
Preset birthday card patterns for common use cases
"""
from .birthdaycard_builder import BirthdayCardBuilder

# Age-based patterns
BIRTHDAY_25 = (
    BirthdayCardBuilder()
    .avatar("/user.jpg")
    .name("John Doe")
    .age(25)
    .message("Happy 25th Birthday!")
    .date("January 15")
    .build()
)

BIRTHDAY_30 = (
    BirthdayCardBuilder()
    .avatar("/jane.jpg")
    .name("Jane Smith")
    .age(30)
    .message("Happy 30th Birthday!")
    .date("March 22")
    .build()
)

BIRTHDAY_40 = (
    BirthdayCardBuilder()
    .avatar("/bob.jpg")
    .name("Bob Johnson")
    .age(40)
    .message("Happy 40th Birthday!")
    .date("July 10")
    .build()
)

# Milestone birthdays
BIRTHDAY_21 = (
    BirthdayCardBuilder()
    .avatar("/alice.jpg")
    .name("Alice Brown")
    .age(21)
    .message("Happy 21st Birthday! 🎉")
    .date("April 5")
    .build()
)

BIRTHDAY_50 = (
    BirthdayCardBuilder()
    .avatar("/carol.jpg")
    .name("Carol Wilson")
    .age(50)
    .message("Happy 50th Birthday! 🎊")
    .date("September 18")
    .build()
)

# Today's birthdays
TODAY_BIRTHDAY_1 = (
    BirthdayCardBuilder()
    .avatar("/david.jpg")
    .name("David Lee")
    .age(28)
    .message("Happy Birthday David!")
    .date("Today")
    .build()
)

TODAY_BIRTHDAY_2 = (
    BirthdayCardBuilder()
    .avatar("/emma.jpg")
    .name("Emma Davis")
    .age(32)
    .message("Happy Birthday Emma!")
    .date("Today")
    .build()
)

# Upcoming birthdays
UPCOMING_BIRTHDAY = (
    BirthdayCardBuilder()
    .avatar("/frank.jpg")
    .name("Frank Miller")
    .age(35)
    .message("Birthday coming soon!")
    .date("Tomorrow")
    .build()
)

# Team birthdays
EMPLOYEE_BIRTHDAY = (
    BirthdayCardBuilder()
    .avatar("/emp.jpg")
    .name("Sarah Connor")
    .age(29)
    .message("Happy Birthday to our amazing team member!")
    .date("December 8")
    .build()
)

MANAGER_BIRTHDAY = (
    BirthdayCardBuilder()
    .avatar("/manager.jpg")
    .name("Michael Scott")
    .age(45)
    .message("Happy Birthday to the best manager!")
    .date("March 15")
    .build()
)

# Generic patterns
GENERIC_BIRTHDAY = (
    BirthdayCardBuilder()
    .avatar("/user.jpg")
    .name("Team Member")
    .age(30)
    .message("Happy Birthday!")
    .date("Today")
    .build()
)

# All patterns
ALL_BIRTHDAYCARD_PATTERNS = {
    "age_25": BIRTHDAY_25,
    "age_30": BIRTHDAY_30,
    "age_40": BIRTHDAY_40,
    "age_21": BIRTHDAY_21,
    "age_50": BIRTHDAY_50,
    "today_1": TODAY_BIRTHDAY_1,
    "today_2": TODAY_BIRTHDAY_2,
    "upcoming": UPCOMING_BIRTHDAY,
    "employee": EMPLOYEE_BIRTHDAY,
    "manager": MANAGER_BIRTHDAY,
    "generic": GENERIC_BIRTHDAY,
}
