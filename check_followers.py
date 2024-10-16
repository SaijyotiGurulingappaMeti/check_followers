import instaloader

# Initialize instaloader instance
L = instaloader.Instaloader()

# Login using session file (no need to enter credentials again)
username = 'your_username'  # Replace with your Instagram username
L.load_session_from_file(username)

# Get profile information
profile = instaloader.Profile.from_username(L.context, username)

# Get the list of followers
followers = set([follower.username for follower in profile.get_followers()])

# Get the list of people you follow
following = set([followee.username for followee in profile.get_followees()])

# Find who you follow but they don't follow you back
not_following_back = following - followers

# Display the list of people who are not following back
print("People who are not following you back:")
for user in not_following_back:
    print(user)
