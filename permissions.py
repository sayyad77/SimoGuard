from database import get_rank
from config import OWNER_ID


# ترتيب الرتب من الأعلى إلى الأقل
RANK_LEVELS = {
    "مميز": 1,
    "ادمن": 2,
    "مشرف": 3,
    "مدير": 4,
    "منشئ": 5,
    "مالك": 6,
    "مالك أساسي": 7,
    "مطور": 8
}


def is_owner(user_id):
    return user_id == OWNER_ID


def get_user_rank(user_id):
    if is_owner(user_id):
        return "مطور"

    return get_rank(user_id)


def rank_level(user_id):
    rank = get_user_rank(user_id)

    if rank:
        return RANK_LEVELS.get(rank, 0)

    return 0


def has_rank(user_id, rank):
    return rank_level(user_id) >= RANK_LEVELS.get(rank, 0)


    return is_owner(user_id) or has_rank(user_id, "ادمن")


def can_kick(user_id):
    return has_rank(user_id, "مشرف")


def can_change_ranks(user_id):
    return has_rank(user_id, "مالك")


def is_developer(user_id):
    return is_owner(user_id)
def can_manage(user_id):
    return is_owner(user_id) or has_rank(user_id, "ادمن")


def can_kick(user_id):
    return is_owner(user_id) or has_rank(user_id, "مشرف")


def can_change_ranks(user_id):
    return is_owner(user_id) or has_rank(user_id, "مالك")


def is_developer(user_id):
    return is_owner(user_id)
