# Tumblr Reposter

Problem: you've created your tumblr as a "primary" account but you decided you
want to have it as a shared tumblr
Solution: Create a new tumblr, repost all the old images

# Usage

```console
$ virtualenv .
$ . bin/activate
$ pip install -r REQUIREMENTS.txt
$ vim move-tumblr.com -> create new secrets at https://api.tumblr.com/console and add them at the top
$ python move-tumblr.py myold.tumblr.com mynew.tumblr.com
```
