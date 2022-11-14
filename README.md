<div align="center">
  <img src="https://user-images.githubusercontent.com/36193643/201700009-88ed5cc1-8bfc-408f-99b5-0b3fe36da1b5.png" />
</div>

<h1 align=center>Reddit profile crawler</h1>
<p align=center>A program that saves a user's profile comments as a JSON.</p>

## 🚀 Features

- Saves a Reddit users comments and optionally the parent comment or post to a JSON file

The output is as follows, for instance [Arnold Schwarzenegger](https://www.reddit.com/user/GovSchwarzenegger/):

```json
{
  "user": "GovSchwarzenegger",
  "comments": [
    {
      "parentText": "Your After School All Stars program really changed and shaped my childhood. I was able to play sports that my parents definitely could not afford. I had snacks for when I was hungry because I couldn\u2019t bring a lunch. I made life long friends.Thank you for being you!! Motivating in so many different ways.",
      "text": "I absolutely love hearing that!",
      "submittedAt": 1668287426.0,
      "permalink": "/r/u_GovSchwarzenegger/comments/ysrb1k/do_something_this_veterans_day_beyond_posting/iw49ri4/"
    },
    {
      "parentText": "I'm glad you're not one of those politician pretending to help without doing anything. You really go out and put your money where your mouth is. All the best, and I hope you keep doing what you're doing.",
      "text": "I appreciate that, but I don\u2019t think it\u2019s a politician issue, I think it\u2019s a people issue. Looking at social media, I see a lot of regular people who talk and talk and complain but don\u2019t do anything. We all have power if we are willing to look up from complaining on our phones and see what we can do.",
      "submittedAt": 1668287187.0,
      "permalink": "/r/u_GovSchwarzenegger/comments/ysrb1k/do_something_this_veterans_day_beyond_posting/iw497f6/"
    },
    <...>
  ]
}
```

## ⚙️ Setup

1. Install the dependencies: `python -m pip install -r requirements.txt`
2. Create a Reddit app [here](https://www.reddit.com/prefs/apps)
3. Create an `.env` file with the following properties:

```sh
client_id=
client_secret=
user_agent=
```

4. Provide the data needed in the `.env` file as prescribed in the [praw](https://praw.readthedocs.io/en/stable/getting_started/quick_start.html) documentation

## ▶️ Options

`crawler.py [OPTIONS]`

    -h,                                  Print this help text and exit
    -u, --user                           The user whose comments will be fetched
    -c, --context                        Include the parent comment text, providing further context
