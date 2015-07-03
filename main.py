import webapp2

from google.appengine.ext import ndb

## this is just a skeleton of how your code should be.
## i think you can make changes in this code to suit your requirements


head='''
<head>
<center><h1><p style="color:#6699FF">Welcome to Login</p></h1>
<i>from </i><a href='http://mukulworld.in/'>Mukul World</a></center><br></head>
'''
LoginForm="""
<center>
<form action="/login" method="post">
      <table>
      <tr><td>username:</td><td><input type='text' name="username"></td></tr>
      <tr><td>password:</td><td><input type='password' name="password" ></td></tr>
      <tr><td></td><td><input type="reset" value="Reset"><input type="submit" value="Submit"></div>
    </form>
    </center>
"""
SignupForm="""
<br>
<center>
<form action="/signup" method="post">
      <table>
      <tr><td>desired username:</td><td><input type='text' name="username"></td></tr>
      <tr><td>password:</td><td><input type='password' name="password" ></td></tr>
      <tr><td></td><td><input type="reset" value="Reset"><input type="submit" value="Submit"></div>
    </form>
    </center>
"""


class LoginDB(ndb.Model):
    user_name=ndb.StringProperty()
    user_pwd=ndb.StringProperty()

class SignupHandler(webapp2.RequestHandler):
    def post(self):
        login_details=LoginDB(user_name=self.request.get('username'),
                              user_pwd=self.request.get('password'))
        login_details.put()
        self.response.write('database updated')
        

class LoginHandler(webapp2.RequestHandler):
    def post(self):
        global given_user_name
        given_user_name=self.request.get('username')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<html>'+head+'<body style="color:#6699FF" vlink="#6699FF">')
        given_user_pwd=self.request.get('password')
        q=LoginDB.query(LoginDB.user_name==given_user_name)
        self.response.write('<br>')
        self.response.write('<br>')
        x=q.fetch()
        if len(x)==0:
            self.response.write('please sign up')
        else:
            for i in x:
                y=i.user_pwd
                self.response.write(' ')
                self.response.write('<br>')
            if y==given_user_pwd:
                self.response.write('Welcome '+given_user_name+'<br>You have logged in!<br>')
            else:
                self.response.write('password does not match')
            
class Welcome(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<html>'+head+'<body>'+LoginForm+'<br>'+SignupForm+'</body></html>')


app = webapp2.WSGIApplication([
    ('/', Welcome),('/login',LoginHandler),('/signup',SignupHandler)], debug=True)
