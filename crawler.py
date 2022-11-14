import praw
import os
import sys, getopt
import json
from dotenv import load_dotenv


def main(argv):
    user = ""
    includeContext = False
    limit = None

    try:
        opts, args = getopt.getopt(argv, "hu:cl:", ["user=", "limit="])
    except getopt.GetoptError:
        print(f"crawler.py -u <username> -l <limit> -c")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print(f"crawler.py -u <username> -l <limit> -c")
            sys.exit()
        elif opt in ("-u", "--user"):
            user = arg
        elif opt in ("-c", "--context"):
            includeContext = True
        elif opt in ("-l", "--limit"):
            limit = int(arg)

    load_dotenv()

    client_secret = os.getenv('client_secret')
    client_id = os.getenv('client_id')
    user_agent = os.getenv('user_agent')

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
    )

    data = {"user": user, "comments": []}
    ctr = 0

    for comment in reddit.redditor(user).comments.new(limit=limit):
        parent = comment.parent()
        obj = {}

        if includeContext:
            parentText = ""
            if (isinstance(parent, praw.models.reddit.submission.Submission)):
                parentText = parent.selftext
            else:
                parentText = parent.body
            obj["parentText"] = parentText

        obj["text"] = comment.body
        obj["submittedAt"] = comment.created_utc
        obj["permalink"] = comment.permalink

        data["comments"].append(obj)
        ctr += 1
        print(f"Got {ctr} comments!")

    with open("result.json", "w") as f:
        f.write(json.dumps(data))


if __name__ == "__main__":
    main(sys.argv[1:])
