# Request bot for Geometry Dash Moderator

# Operation
## For the server:
- A channel #helper-request `/define-channel helper #id`
Displays levels to be rated by the helper, with difficulty, title, video, creator and id. 
They can be accepted or rejected by the helper, with a note.
- A channel #moderator-request `/define-channel moderator #id`
Displays levels to be rated by moderators, with difficulty, title, video, creator and id.
They can be accepted or rejected by the moderator.
- A channel #request-news `/define-channel annoucement #id`
Displays news at levels accepted or rejected by helper and moderator.
- A `/define-helper #role-id` command to define a helper role.
- A `/define-moderator #role-id` command to define a moderator role.

## For a client:
- A `/request {id : Integer} {Description : String} {Video = None : Url}` *(Limit / Server : n1 / day)* command.
It adds the correct levels to a list to be noted. If the limit is exceeded, an error message is sent to the client.
- A `/vip-request {id : Integer} {Description : String} {Video = None : Url}` *(Limit / User : n2 / day)* command.
It adds the correct levels to a list to be noted, with no daily limit. If the limit is exceeded, an error message is sent to the client.

## For a helper:
- Accept or reject a level and give it a rating and a comment using an emoji system.
If accepted, it is sent to the moderator.
If rejected, a message is sent in #request-news.


## For a moderator:
- Send or decline a level, and assign a comment to it using an emoji system. 
Each interaction sends a message to #request-news.


# Data
## Level :
- `id`: Unsigned Integer (unique)
- `url`: String (valid URL)
- user`: UserId

(my code is ugly don't judge, it will be improved)