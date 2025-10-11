class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"


# don't touch above this line
# This calculates the Vanity of each item in list
# Example:
# vanity(Influencer(10, 1))  → 15  
# vanity(Influencer(4, 3))   → 19  
# vanity(Influencer(8, 0))   → 8  
def vanity(influencer):
    return influencer.num_bio_links * 5 + influencer.num_selfies
# This sorts them after we calculate the vanity of each item in list
# [
#   (Influencer(8, 0), 8) =>   # vanity = 8
#   (Influencer(10, 1),15) => # vanity = 15
#   (Influencer(4, 3), 19) => # vanity = 19
# ]
def vanity_sort(influencers):
    return sorted(influencers, key=vanity)
