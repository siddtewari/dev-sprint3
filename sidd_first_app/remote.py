import flask, flask.views
import os
import utils

class Remote(flask.views.MethodView):
	@utils.login_required
	def get(self):
		return flask.render_template('remote.html')

	@utils.login_required
	def post(self):
		result = eval (flask.request.form['expression']) #"Whatever you want, OCTO thorp!!" #
		flask.flash(result)
		return flask.redirect(flask.url_for('remote')) #return self.get() # return the result of the function self.get()
