from flask import render_template, Blueprint


root_bp = Blueprint("root", __name__)


@root_bp.route("/")
def index():
    return render_template(
        template_name_or_list="index.html", title="Home", username="Shadaab Karim"
    )
