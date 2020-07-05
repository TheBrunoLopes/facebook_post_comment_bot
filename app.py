import facebook

from _utils import get_env

post_id = get_env("FACEBOOK_POST_ID")
token = get_env("FACEBOOK_TOKEN")

print(f"Posting on {post_id}")
graph = facebook.GraphAPI(access_token=token, version="3.1")

graph.put_comment(object_id=post_id, message='Já foste Lopes....')
