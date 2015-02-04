import praw
import ngrams
import re

username='usernameanagrambot'
password=''

title_trans=''.join(chr(c) if chr(c).isupper() or chr(c).islower() else '' for c in range(256))

userAgent="The amazing anagram in a username finder. Written by /u/marksist"

r= praw.Reddit(userAgent)
r.login(username, password)

subr=r.get_subreddit('all')

for submission in subr.get_hot():
     x=ngrams.anagramfinder(re.sub('[^a-zA-Z]+', '', submission.author.name).encode('ascii','ignore'))
