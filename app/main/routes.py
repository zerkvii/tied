from flask import Blueprint,request,render_template
from app.models import Post
main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('main/home.html', posts=posts, title='主页')


@main.route("/about")
def about():
    return render_template('main/about.html', title='关于')

