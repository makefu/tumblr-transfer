#!/usr/bin/env python
""" usage: repost-tumblr [options] [OLDBLOG] [NEWBLOG]

Options:
    --limit=NUM         Limit to fetch [Default: 50]
    --begin=NUM         Blog post to begin [Default: 0]
    --end=NUM           Blog post to end (defaults to total_posts)

"""

from docopt import docopt
from pprint import pprint
import pytumblr
import sys


consumer_key = ''
consumer_secret = ''
token = ''
token_secret = ''

def main():
    args = docopt(__doc__)
    oldblog = args.get('OLDBLOG',False) or "log.shackspace.de"
    newblog = args.get('NEWBLOG',False) or "shackspace.tumblr.com"
    client = pytumblr.TumblrRestClient(
          consumer_key
        , consumer_secret
        , token
        , token_secret
    )
    postnum = int(args['--end']) if args['--end'] else int(client.posts(oldblog)['blog']['total_posts'])
    limit = int(args['--limit'])
    begin = int(args['--begin'])
    print('from:{} to:{} begin:{} end:{} limit:{}'.format(oldblog,newblog,begin,postnum,limit))

    for offset in reversed(range(begin,postnum,limit)):
        print("current offset: {}".format(offset))
        for post in reversed(client.posts(oldblog,limit=limit,offset=offset)['posts']):

            ident = post['id']
            summary = post['summary']
            reblogkey = post['reblog_key']
            print('moving post: {} ({} {})'.format(summary,ident,reblogkey))
            ret = client.reblog(newblog, id=ident, reblog_key=reblogkey)
            print('Return code {} - {}'.format(ret['meta']['status'],ret['meta']['msg']))
            if ret['meta']['status'] == 400:
                print("got 400 error from tumblr ....")
                pprint(ret)
                sys.exit()

if __name__ == "__main__":
    main()
