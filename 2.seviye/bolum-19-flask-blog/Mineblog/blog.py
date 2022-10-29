from MySQLdb.cursors import DictCursor
from flask import Flask, render_template, flash, redirect, url_for, session, request, send_from_directory
from flask_mysqldb import MySQL, MySQLdb
from wtforms import Form, StringField, SelectField, TextAreaField, PasswordField, validators
from flask_wtf.file import FileField, FileAllowed
from passlib.hash import sha256_crypt
from functools import wraps
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# * kullanıcı giriş decorator'ı
app.secret_key = "dneme_blog"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "deneme_blog"
mysql = MySQL(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.before_first_request
def create_tables():
    cursor = mysql.connection.cursor(DictCursor)
    sorgu = """CREATE TABLE IF NOT EXISTS users(
    id INT AUTO_INCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    photo_adress TEXT NOT NULL DEFAULT "/uploads/default-profile-picture.jpg",
    PRIMARY KEY(id))"""
    cursor.execute(sorgu)
    mysql.connection.commit()
    sorgu = """CREATE TABLE IF NOT EXISTS articles(
    id INT AUTO_INCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    author TEXT NOT NULL,
    author_id TEXT NOT NULL,
    created_date Timestamp not null DEFAULT CURRENT_TIMESTAMP(),
    PRIMARY KEY(id))"""
    cursor.execute(sorgu)
    mysql.connection.commit()
    # ! cursor.commit() bu yanlış bir daha yapma bundan
    cursor.close()



def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash(message="bu sayfayı görüntülemek için giriş yapınız",
                  category="danger")
            return redirect(url_for("login"))
    return decorated_function

# * Kullanıcı kayıt formu


class RegisterForm(Form):
    name = StringField("isim soyisim", validators=[validators.Length(
        min=4, max=25, message="isim soyisim min 4 maks 25 karakter uzunlugunda olmalıdır.")])
    username = StringField("kullanıcı adı", validators=[
                           validators.Length(min=5, max=35)])
    email = StringField("email adresi", validators=[validators.Email(
        message="geçerli bir email adresi girmediniz")])
    password = PasswordField("parola : ", validators=[validators.DataRequired(
        message="parola boş bırakılamaz"), validators.EqualTo(fieldname="confirm", message="girdiğiniz parolalar uyuşmuyor.....")])
    confirm = PasswordField("parola doğrula")
    photo = FileField("profil fotorafı", validators=[
                      FileAllowed(['png', 'jpg', 'jpeg', 'gif'])])


class LoginForm(Form):
    # ? username = StringField("kullanıcı adı",validators=[validators.data_required(message="isim boş bırakılamaz")])
    username = StringField("kullanıcı adı")
    password = PasswordField("parola")

# * 404 hatası yönlendirici


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# * ansayfa yönlendirici


@app.route("/")
def index():
    return render_template("index.html")

# * hakkımda sayfası yönlendirici


@app.route("/about")
def about():
    return render_template("about.html")

# * makaleler sayfası yönlendirici


@app.route("/articles")
def articles():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    sorgu = "SELECT * FROM articles"

    result = cursor.execute(sorgu)
    if result > 0:
        articles = cursor.fetchall()
        for article in articles:
            sorgu = "SELECT photo_adress FROM users WHERE id= %s"

            cursor.execute(sorgu, (article["author_id"],))

            article["author_photo"] = author_photo = cursor.fetchone()[
                "photo_adress"]

        return render_template("articles.html", articles=articles)
    else:
        return render_template("articles.html")

# * kontrol paneli


@app.route("/dashboard")
@login_required
def dashboard():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    sorgu = "SELECT * FROM articles WHERE author= %s"

    result = cursor.execute(sorgu, (session["username"],))
    if result > 0:
        articles = cursor.fetchall()
        return render_template("dashboard.html", articles=articles)
        pass
    else:
        return render_template("dashboard.html")

# * kayıt işlemi


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.hash(form.password.data)

        cursor = mysql.connection.cursor()

        sorgu = "INSERT INTO users (name,username,email,password) VALUES(%s,%s,%s,%s)"

        cursor.execute(sorgu, (name, username, email, password))
        mysql.connection.commit()
        cursor.close()

        flash(message="başarıyla kayıt oldunuz....", category="success")

        return redirect(url_for("login"))
    else:
        return render_template("register.html", form=form)

# * giriş işlemi


@app.route("/login", methods=["GET", "POST"])
def login():
    loginform = LoginForm(request.form)
    if request.method == "POST":
        username = loginform.username.data
        password_entered = loginform.password.data

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        sorgu = "SELECT * FROM users where username = %s"

        result = cursor.execute(sorgu, (username,))
        if result > 0:
            data = cursor.fetchone()
            real_password = data["password"]
            if sha256_crypt.verify(password_entered, real_password):
                flash(message="başarıyla {} hesabına giriş yapıldı".format(
                    username), category="success")

                session["logged_in"] = True
                session["username"] = username
                session["user_id"] = data["id"]

                session["user_photo_adress"] = data["photo_adress"]

                return redirect(url_for("index"))
            else:
                flash(message="hatalı bir parola girdiniz", category="danger")
                return redirect(url_for("login"))
        else:
            flash(message="böyle bir kullanıcı bulunmuyor", category="danger")
            return redirect(url_for("login"))

        cursor.close()

        return redirect(url_for("index"))
    else:
        return render_template("login.html", form=loginform)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

# * yazar detay sayfası


@app.route("/author/<string:name>")
def author(name):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    sorgu = "SELECT * FROM articles WHERE author= %s"

    result = cursor.execute(sorgu, (name,))
    if result > 0:
        articles = cursor.fetchall()
        for article in articles:
            sorgu = "SELECT photo_adress FROM users WHERE id= %s"

            cursor.execute(sorgu, (article["author_id"],))

            article["author_photo"] = author_photo = cursor.fetchone()[
                "photo_adress"]
        return render_template("author.html", articles=articles)
    else:
        return render_template("author.html")

# * makale detay sayfası


@app.route("/article/<string:id>")
def article(id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    sorgu = "SELECT * FROM articles WHERE id = %s"

    result = cursor.execute(sorgu, (id,))
    if result > 0:
        article = cursor.fetchone()
        sorgu = "SELECT photo_adress FROM users WHERE id= %s"

        cursor.execute(sorgu, (article["author_id"],))

        article["author_photo"] = author_photo = cursor.fetchone()[
            "photo_adress"]

        return render_template("article.html", article=article)
    else:
        return render_template("article.html")

# * makale ekleme


@app.route("/addarticle", methods=["GET", "POST"])
@login_required
def addarticle():
    articleform = ArticleForm(request.form)
    if request.method == "POST" and articleform.validate():
        title = articleform.title.data
        content = articleform.content.data

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        sorgu = "INSERT INTO articles(title,author,author_id,content) VALUES(%s,%s,%s,%s)"

        cursor.execute(sorgu, (title, session["username"], session["user_id"], content))
        mysql.connection.commit()
        cursor.close()
        flash(message="makale başarıyla eklendi", category="success")
        return redirect(url_for("dashboard"))

    return render_template("addarticle.html", form=articleform)

# * makale silme


@app.route("/delete-article/<string:id>")
@login_required
def delete(id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    sorgu = "SELECT * FROM articles WHERE author_id= %s and id= %s"

    result = cursor.execute(sorgu, (session["user_id"], id))
    if result > 0:
        sorgu2 = "DELETE from articles where id = %s"
        cursor.execute(sorgu2, (id,))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for("dashboard"))
    else:
        flash(message="böyle bir makale yok veya silmeye yetkiniz yok",
              category="danger")
        return redirect(url_for("index"))

# * makale güncelleme


@app.route("/update-article/<string:id>", methods=["GET", "POST"])
@login_required
def update(id):
    if request.method == "GET":
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        sorgu = "SELECT * FROM articles where id=%s and author_id=%s"

        result = cursor.execute(sorgu, (id, session["user_id"]))

        if result == 0:
            flash(
                message="böyle bir makale yok veya bu işleme yetkiniz yok", category="danger")
            cursor.close()
            return redirect(url_for("index"))
        else:
            article = cursor.fetchone()
            form = ArticleForm()

            form.title.data = article["title"]
            form.content.data = article["content"]
            cursor.close()
            return render_template("update-article.html", form=form)
    else:
        form = ArticleForm(request.form)
        newtitle = form.title.data
        newcontent = form.content.data

        cursor = mysql.connection.cursor()

        sorgu = "UPDATE articles set title=%s ,content=%s where id=%s"

        cursor.execute(sorgu, (newtitle, newcontent, id))
        mysql.connection.commit()
        cursor.close()
        flash(message="makale başarıyla güncellendi", category="success")
        return redirect(url_for("dashboard"))

# * kullanıcı bilgisi güncelleme


@app.route("/profile-settings", methods=["GET", "POST"])
@login_required
def profile_settings():
    if request.method == "GET":
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        sorgu = "SELECT * FROM users where id=%s"

        result = cursor.execute(sorgu, (session["user_id"],))

        user_data = cursor.fetchone()
        form = RegisterForm()
        form.password.label = "kullanılan parola"
        form.confirm.label = "yeni parola"
        form.name.data = user_data["name"]
        form.email.data = user_data["email"]
        form.username.data = user_data["username"]
        form.photo = user_data["photo_adress"]
        cursor.close()
        return render_template("profile-settings.html", form=form)
    else:
        form = RegisterForm(request.form)
        name = ("name", form.name.data)
        email = ("email", form.email.data)
        username = ("username", form.username.data)

        oldpassword = form.password.data
        newpassword = sha256_crypt.hash(form.confirm.data)

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        try:
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file and allowed_file(file.filename):

                filename = secure_filename(file.filename)
                if not os.path.exists(UPLOAD_FOLDER):
                    os.makedirs(UPLOAD_FOLDER)
                file.save(os.path.join(UPLOAD_FOLDER, filename))

                photo = ("photo_adress",
                         ("/"+UPLOAD_FOLDER + "/" + str(filename)))
                session["user_photo_adress"] = photo[1]
            photo = ("photo_adress", session["user_photo_adress"])
            new_data_tuple = (name, email, username, photo)

            sorgu = "SELECT * FROM articles where author=%s"
            update_article = cursor.execute(sorgu, (session["username"],))
            if update_article > 0:
                user_articles = cursor.fetchall()
            for i in new_data_tuple:
                if type(i[1]) != type(None):
                    if len(i[1]) != 0:
                        sorgu = "UPDATE users set qwerts=%s where id=%s".replace(
                            "qwerts", i[0])
                        cursor.execute(sorgu, (i[1], session["user_id"]))
            mysql.connection.commit()

            sorgu = "SELECT * FROM users where id=%s"

            cursor.execute(sorgu, (session["user_id"],))
            user_data = cursor.fetchone()
            if sha256_crypt.verify(oldpassword, user_data["password"]):
                sorgu = "UPDATE users set password=%s where id=%s"
                newpassword = newpassword.strip()
                cursor.execute(sorgu, (newpassword, session["user_id"]))
                mysql.connection.commit()
                flash("şifreniz başarıyla güncellendi", category="success")
            else:
                flash("eski parolayı hatalı girdiniz", category="danger")

            if update_article > 0:
                sorgu = "UPDATE articles set author=%s where id=%s"
                for article in user_articles:
                    cursor.excute(sorgu, (username[1], article["id"]))
                    mysql.connection.commit()

            session["username"] = username[1]

            cursor.close()
            flash(message="profil ayarların başarıyla güncellendi",
                  category="success")
            return redirect(url_for("profile_settings"))
        except Exception as err:
            with open(f"{os.path.dirname(__file__)}\\error.log", "r+", encoding="utf-8") as f:
                f.write("profil ayarları güncelleme hatası" + str(err) + "\n")
            flash(message="bir hatadan dolayı işlem yapılamadı", category="danger")
            return redirect(url_for("profile_settings"))

# * makale formu


class ArticleForm(Form):
    title = StringField("makale başlığı", validators=[validators.Length(
        min=5, max=110, message="makale başılığı 5-110 karakter arasında bir uzunlukta olmalı")])
    content = TextAreaField("makale içeriği", validators=[validators.Length(
        min=10, message="makale içeriği minimum 10 karakter uzunluğunda olmalı")])

# * arama URL


@app.route("/search", methods=["GET", "POST"])
def searh():
    if request.method == "GET":
        return redirect(url_for("index"))
    else:
        keyword = request.form.get("keyword")

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        sorgu = ("SELECT * from articles where title like '%" + keyword + "%'")

        result = cursor.execute(sorgu)

        if result == 0:
            flash("aranan kelimeye uygun makale bulunamamadı ....", "warning")
            return redirect(url_for("articles"))
        else:
            articles = cursor.fetchall()
            flash("{} aramasına bulunan sonuçlar".format(keyword), "warning")
            return render_template("articles.html", articles=articles)

# * dosya yükleme


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory("uploads",
                               filename)

# todo profil resimleri yönetimi veritabanındaki adresten çekilecek

# ! dneme için


@app.route("/deneme")
@login_required
def deneme():
    return render_template("deneme.html")


app.debug = True
# !

if __name__ == "__main__":
    app.run()


#  todo profil fotolarnını staticten çekebilirsin
