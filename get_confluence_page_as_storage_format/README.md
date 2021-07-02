A straightforward python script to get the storage format/details of a particular Confluence page.


Context:

As part of investigating some AWS accounts I needed to produce a Confluence page with a table:  this was hindered by the decision to not support using markup tables.
After reading through *many* documents, most official one not kept up-to-date, I discovered that this could be formatted using a form of Confluence-xhtml, (you can read the guide here for formatting Confluenec via the API: https://confluence.atlassian.com/doc/confluence-storage-format-790796544.html)

To help me see this more clearly, and frankly just to play with the Altassian/Confluence API, I created a script that prompts for details of the page title, the Space, and base URL, and uses values that must be exported for the username and API-token used for authentication (it would be best to use a call to AWS SSM if you are going to use this for anything production-based...you've been warned!)

This was about four weeks after starting to learn Python, so may be a little rough around the edges (I highly recommend this course if you are starting your Python journey: https://edube.org/study/pe1).

As always feel free to use and feedback