from flask import Flask, render_template
from models import db
from flask_migrate import Migrate
def create_app():
    app= Flask(__name__)
    # app.config["SECRET_KEY"]="flask-example"
    app.config["SQLALCHEMY_DATABASE_URI"]=f"sqlite:///{app.instance_path}/my-database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app,db)

    @app.route("/")
    def index():
        return {"name":"Dư"}
    @app.route("/about")
    def about():  
        return "Trang giới thiệu"
    @app.route("/product/<id>")
    def get_product(id):  
        list_product = [{
            "id":1,
            "name":"Sp1"
        },
        {
            "id":2,
            "name":"Sp2"
        },
        {
            "id":3,
            "name":"Sp3"
        },
        {
            "id":4,
            "name":"Sp4"
        }]
        product = list(filter(lambda x: x["id"]==int(id) , list_product))
        return render_template("product-detail.html",data=product[0])
    @app.route("/products")
    def get_list_product():  
        list_product = [{
            "id":1,
            "name":"Sp1"
        },
        {
            "id":2,
            "name":"Sp2"
        },
        {
            "id":3,
            "name":"Sp3"
        },
        {
            "id":4,
            "name":"Sp4"
        }]
        return render_template("product.html",data =list_product)
    return app
