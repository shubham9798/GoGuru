import webapp2
from rivescript import RiveScript
class GoGuru(webapp2.RequestHandler):
    """def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')"""
    def main(self):
		self.response.headers['Content-Type'] = 'text/plain'
		rs = RiveScript()
		rs.load_directory("./brain")
		rs.sort_replies()
		print("----------------------------------------------------")
		print("|              WELCOME TO GOGURU                   |")
		print("----------------------------------------------------")

		while True:
			msg = raw_input("You> ")
			#msg = msg.lower()
			if msg == '/quit' or msg == 'bye':
				quit()
			reply = rs.reply("localuser", msg)
			self.response.write(reply)
app = webapp2.WSGIApplication([
    ('/', GoGuru),
], debug=True)
