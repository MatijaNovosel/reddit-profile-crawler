<h1 align=center>Reddit profile crawler</h1>
<p align=center>A program that saves a user's profile as a JSON.</p>

## 🚀 Features

- Saves a Reddit users comments and optionally the parent comment or post to a JSON file

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
