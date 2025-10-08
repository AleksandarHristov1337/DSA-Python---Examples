def get_follower_prediction(follower_count, influencer_type, num_months):

    # First we do check what type is the infulencer
    if influencer_type == "fitness":
        growth_rate = 4 
    elif influencer_type == "cosmetic":
        growth_rate = 3  
    else:
        growth_rate = 2 
    
    # Here we use the geometric progression formula where we set total_followers to a1 * r^n or follower_count * (growth_rate ** num_months)
    total_followers = follower_count * (growth_rate ** num_months)
    
    
    # Very important to use int because otherwise we will get float number and for example 10×(22.5)≈10×5.65685424=56.5685424 we need int(56.5685424)=56
    return int(total_followers)
