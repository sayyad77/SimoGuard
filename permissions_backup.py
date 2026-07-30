from database import get_rank
from config import OWNER_ID


def is_owner(user_id):
    return user_id == OWNER_ID


def is_admin(user_id):
    rank = get_rank(user_id)

    return rank in [
        "مالك",
        "مدير",
        "مشرف"
    ]


def can_manage(user_id):
    return is_owner(user_id) or is_admin(user_id)
