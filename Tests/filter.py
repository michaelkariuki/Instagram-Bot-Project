import re

hashtags = "#motivation #fitness #inspiration #love #life #instagood #quotes #lifestyle #success #motivationalquotes #workout #instagram #gym #goals #happy #believe #follow #mindset #positivevibes #fitnessmotivation #fit #training #happiness #bhfyp #selflove #like #health #entrepreneur #bodybuilding #bhfyp"

hashtags_v2 = "#fitness #motivation #fitnessmotivation #success #fitnessmodel #fitnessaddict #motivationalquotes #fitnessgirl #gymmotivation #fitnessjourney #mondaymotivation #instafitness #fitnesslife #workoutmotivation #motivational #fitnesslifestyle #fitnessgoals #successful #successquotes #motivationmonday #fitnessfreak #igfitness #weightlossmotivation #bodybuildingmotivation #morningmotivation #fitnessfood #fitnessgear #runningmotivation #polefitness #successmindset"


#Converts a string filled with hashtags into a list of hashtags
#Can take a prefilter to clean data further into the right format
def convert_str_2_hashtag(hashtags, pre_filter=None):
    result_initial = hashtags# Global list

    #if there is a prefilter, do this
    if pre_filter:
        result_initial = pre_filter(result_initial)

    #split the string using according to white spaces
    result_list = re.split(r'\s', str(result_initial))

    #check if any item in the list has a #
    #combine the list into a string then check if # exist in 
    #the string
    if "#" in '\t'.join(result_list):
        return result_list
    else:
        #if not, add hashtags(function)
        final_result = add_hashtags(result_list)
        return final_result


def  remove_hashtag(hashtags, pre_filter=None):
    result_initial = hashtags
    result_list = []

    if pre_filter:
        result_initial = pre_filter(result_initial)
    
    hashtag_list = re.split(r'\s', str(result_initial))

    for hashtag in hashtag_list:
        x = re.sub(r'#', '',hashtag)
        result_list.append(x)

    return result_list


def add_hashtags(list):
    return ["#"+ str(hashtag) for hashtag in list]

print(convert_str_2_hashtag(hashtags_v2))

# print(remove_hashtag(hashtags_v2))