# Define the Comment class below:
class Comment:
	def __init__(self, username, text, likes):
		self.username = username
		self.text = text
		self.likes = likes

c = Comment("davey123", "lol you're so silly", 3) 
another_comment = Comment("rosa77", "soooo cute!!!", 0) 

print(c.username, c.text, c.likes)
print(another_comment.username, another_comment.text, another_comment.likes)