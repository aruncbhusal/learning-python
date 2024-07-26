import requests

class Post:
    def __init__(self, post_id):
        all_posts= requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
        for post in all_posts:
            if post["id"] == post_id:
                # The post_id passed from the href had become a text because I didn't
                # specify it in the route. My bad here
                self.title = post["title"]
                self.subtitle = post["subtitle"]
                self.content = post["body"]
                break
    
    def jsonify(self):
        return {
            "title": self.title,
            "subtitle": self.subtitle,
            "content": self.content,
        }