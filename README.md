# InspiroGram

Like [InspiroCord](https://github.com/xDrixxyz/InspiroCord) but posts to Instagram instead.

## Setup Instructions

**You need to have Git installed**. [Click here](https://lmgtfy.com/?q=how+to+install+git) to learn how to install it.

Git clone, install requirements using `pip3 install -r requirements.txt`, copy the `config.example.json` file to `config.json` and fill in the blanks with your Instagram username and password and save it.

You can also add a text to post with the image (caption under the image) in `config.json` or leave it empty.

When you're done editing the config, run the `inspirogram.py` script.

(Linux users: `chmod +x ./inspirogram.py`)

```
$ python3 inspirogram.py
```

Enjoy!

## Notes

- You may get warnings from the Python library I'm using to post images to Instagram that the endpoint is untested. This is the library and not my script.

- You'll know that the posting was successful when either of the following happen:
  - You can see the post on the Instagram account you've setup with the script.
  - You see the words `Uploaded to IG!` in the console output.

- The first time you run the script, it *may* say that the `ig.json` file is missing. Just `Ctrl+C` to stop the script and re-start it. I do not know why this happens or if there is a way for me to stop it from happening programmatically, but for now just deal with it.

- The `timeout` in the config is the time to wait before generating and posting another quote. It is in SECONDS, not milliseconds! 300 seconds is 5 minutes, which is the default value.
