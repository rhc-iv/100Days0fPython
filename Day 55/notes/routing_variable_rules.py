# Routing In Flask:

# Modern web applications use meaningful URLs to help users. Users are more
# likely to like a page and come back if the page uses a meaningful URL they
# can remember and use to directly visit a page.

# Use the route() decorator to bind a function to a URL.

#   @app.route('/')
#   def index():
#       return 'Index Page'

#   @app.route('/hello')
#   def hello():
#       return 'Hello, World'

# You can do more! You can make parts of the URL dynamic and attach multiple
# rules to a function.

# Variable Rules In Flask:

# You can add variable sections to a URL by marking sections with
# <variable_name>. Your function then receives the <variable_name> as a
# keyword argument. Optionally, you can use a converter to specify the type
# of the argument like <converter:variable_name>.

#   from markupsafe import escape

#   @app.route('/user/<username>')
#   def show_user_profile(username):
#       # show the user profile for that user
#       return 'User %s' % escape(username)

#   @app.route('/post/<int:post_id>')
#   def show_post(post_id):
#       # show the post with the given id, the id is an integer
#       return 'Post %d' % post_id

#   @app.route('/path/<path:subpath>')
#   def show_subpath(subpath):
#       # show the subpath after /path/
#       return 'Subpath %s' % escape(subpath)


# Converter types:

# string
# (default) accepts any text without a slash

# int
# accepts positive integers

# float
# accepts positive floating point values

# path
# like string but also accepts slashes

# uuid
# accepts UUID strings