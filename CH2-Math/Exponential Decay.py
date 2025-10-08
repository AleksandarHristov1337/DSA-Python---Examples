def decayed_followers(intl_followers, fraction_lost_daily, days):
    # First we calculate the retention rate (the fraction of followers kept each day)
    # If 20% are lost daily, 80% are retained: 1 - 0.2 = 0.8
    retention_rate = 1 - fraction_lost_daily

    # Here we use the geometric decay formula where we set remaining_total to
    # initial_value * (retention_rate ** time)
    # So remaining_total = intl_followers * (retention_rate ** days)
    remaining_total = intl_followers * (retention_rate ** days)

    # We return the number of remaining followers as an integer
    # Since we can't have partial followers, we round down using int()
    return int(remaining_total)
