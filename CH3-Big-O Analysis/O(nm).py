def get_avg_brand_followers(all_handles, brand_name):
    # all handles containing brand_name
    total_brand_handles = 0  
    # number of influencer lists
    num_influencers = len(all_handles)  

    # Loop over each influencer's handles
    for handles in all_handles:
        # For each influencer, count handles containing brand_name
        count_for_influencer = 0
        # Here we loop try each item in all_handles in the lists
        for handle in handles:
            # this checks if the string brand_name appears anywhere inside the string handle. 
            if brand_name in handle:
                # this adds up to every string brand_name that appears anywhere inside the string handle so we can track 
                count_for_influencer += 1
                # this adds up and tell you there are for example 3 handles across all influencers that contain brand_name.
        total_brand_handles += count_for_influencer

    # check if list is empty at start of code with len and if it's 0 we return 0
    if num_influencers == 0:
        return 0 
    # Take the total number of brand-related followers and divide it evenly across all influencers — 
    # that’s the average number per influencer. 
    average = total_brand_handles / num_influencers
    return round(average, 2)  # rounding to 2 decimal places as in example
