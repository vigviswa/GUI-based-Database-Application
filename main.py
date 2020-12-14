# Import all required modules

from contacts import app
from contacts.views import contact, render_template

app.register_blueprint(contact)
app.url_map.strict_slashes = False

# Error Handling

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
