import math

def get_influencer_score(num_followers, average_engagement_percentage):
    # First we find out how many times must we multiply 2 to get num_followers
    log_followers = math.log(num_followers, 2)
    
    # Average_engagement_percentage is the engagement rate of the influencer, usually expressed as a decimal eg. 10% = 0.10
    # By multiplying these two values, we get the influencer score.
    influencer_score = average_engagement_percentage * log_followers
    
   
    return influencer_score
