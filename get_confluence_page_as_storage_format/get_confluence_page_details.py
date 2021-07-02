#!/usr/bin/env python3

import os, sys, boto3
import datetime
from atlassian import Confluence

## Get the appropriate details of the Confluence base URL, space and page by user input (to make script universal).
confluence_url = input("What is the base URL of the Confluence page? ")
confluence_space = input("what is the Confluence Space the page is in? ")
page_title = input("what is the Confluence page title? ")


## Use the env vars to authenticate with the Confluence API.
confluence = Confluence(
    url = confluence_url,
    username = os.environ['USERNAME'], # email address for the Atlassian account used to create api-token.  Export using: export USERNAME="****"
    password = os.environ['PASSWORD'], # api-token created.  Export using: export PASSWORD="****"
    cloud = True)

## get_page_id calls get_page_by_title()
page_id = confluence.get_page_id(space=confluence_space, title=page_title)

## get the page and expand the storage to see the html used
page_c = confluence.get_page_by_id(page_id, expand='body.storage')

print(page_c['body']['storage']['value'])
