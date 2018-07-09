from dog import Dog
from pet import Pet

dacshound = Dog("Dacshound")

buddy = Pet("buddy", dacshound)

buddy.set_owner("Riley", "555-555-5432")

print(buddy)