# radqbank/xp.py
from radqbank.xp import level_for_xp

def xp_for_streak(streak):
    cfg = get_cfg()
    bonus = cfg["points"]["streak_bonus"]
    return 0 if streak < 3 else bonus * (streak - 2)

def level_for_xp(total_xp):
    levels = get_cfg()["level_thresholds"]
    lvl = 0
    for threshold in levels:
        if total_xp >= threshold:
            lvl += 1
    return lvl - 1  # zero-indexed
