import datetime
from flask import Flask, render_template, request
from Users import Users
from Discuss import Discuss
from Auto import Auto
from data import db_session

auto_doo = Flask(__name__)
USERNAME = 'Неизвестный'
EMAIL = ''
REGISTRATION_DATE = ''


@auto_doo.route('/registration', methods=['GET', 'POST'])
def registration_page():
    """ОБРАБОТЧИК СТРАНИЦЫ РЕГИСТРАЦИИ
    Работает с БД Users, по умолчанию рендерит страницу, при активации POST запроса отправляет на сервер данные.
    Также проверяет: Если схожий аккаунт уже есть в БД, то просто авторизует пользователя. Иначе добавляет данные
    в БД и авторизует."""
    global USERNAME, EMAIL, REGISTRATION_DATE
    db_session.global_init('db/Users.db')
    if request.method == 'GET':
        return render_template('registration_page_code.html', sh_username=USERNAME)
    elif request.method == 'POST':
        db_sess = db_session.create_session()
        username = request.form['username']
        email = request.form['email']
        about = request.form['about']
        password = request.form['password']
        userdata = db_sess.query(Users).filter(Users.Nickname == username,
                                               Users.Email == email,
                                               Users.About == about,
                                               Users.Password == password
                                               ).all()
        if userdata:
            USERNAME = userdata.Nickname
            REGISTRATION_DATE = userdata.Registration_date
            EMAIL = userdata.Email
            return render_template('profile_page_code.html',
                                   username=USERNAME,
                                   email=EMAIL,
                                   date_of_registration=REGISTRATION_DATE,
                                   )
        else:
            USERNAME = request.form['username']
            REGISTRATION_DATE = datetime.date.today()
            EMAIL = request.form['email']
            db_sess.add(Users(
                            Nickname=USERNAME,
                            Email=EMAIL,
                            About=request.form['about'],
                            Password=request.form['password'],
                            Registration_date=REGISTRATION_DATE
            ))
            db_sess.commit()
            return render_template('profile_page_code.html',
                                   username=USERNAME,
                                   email=EMAIL,
                                   date_of_registration=REGISTRATION_DATE,
                                   )


@auto_doo.route('/adding_auto', methods=['GET', 'POST'])
def adding_new_auto_page():
    """ОБРАБОТЧИК СТРАНИЦЫ ДОБАВЛЕНИЯ АВТО
    Работает с БД Auto, по умолчанию рендерит страницу, при активации POST запроса отправляет данные на сервер.
    Также проверяет: Если схожие данные уже есть в БД, то возвращает сообщение о том, что такая статья уже существует.
    Иначе добавляет её, и возвращает сообщение о том, что статья успешно добавленна"""
    global USERNAME
    db_session.global_init('db/Auto.db')
    if request.method == 'GET':
        return render_template("adding_auto_page_code.html", sh_username=USERNAME)
    elif request.method == 'POST':
        db_sess = db_session.create_session()
        name = request.form['name_auto']
        clas = request.form['class_auto']
        height = request.form['height']
        width = request.form['width']
        length = request.form['length']
        power = request.form['engines_power']
        volume = request.form['engines_volume']
        max_speed = request.form['max_speed']
        date = request.form['made_date']
        maker = request.form['country_maker']
        autodata = db_sess.query(Auto).filter(Auto.Name_auto == name,
                                              Auto.Class_auto == clas,
                                              Auto.Height == height,
                                              Auto.Width == width,
                                              Auto.Length == length,
                                              Auto.Engines_power == power,
                                              Auto.Engines_volume == volume,
                                              Auto.Max_speed == max_speed,
                                              Auto.Made_date == date,
                                              Auto.Country_maker == maker).all()
        if autodata:
            return render_template("done_page.html", sh_username=USERNAME, message='Такая статья уже существует:(')
        else:
            db_sess.add(Auto(
                Name_auto=name,
                Length=length,
                Width=width,
                Height=height,
                Engines_power=power,
                Class_auto=clas,
                Engines_volume=volume,
                Max_speed=max_speed,
                Description=request.form['description'],
                Country_maker=maker,
                Made_date=date
            ))
            db_sess.commit()
            return render_template("done_page.html", sh_username=USERNAME, message='Статья добавлена успешно!')


@auto_doo.route('/', methods=['GET', 'POST'])
def main_page():
    """ОБРАБОТЧИК  ГЛАВНОЙ СТРАНИЦЫ
    Работает с БД Auto, по умолчанию рендерит страницу, при активации POST запроса отправляет данные на сервер.
    Также ищет в БД елементы подходящие под условия из формы.
    После возвращает страницу с циклом, выводящим все найденные елементы"""
    db_session.global_init('db/Auto.db')
    global USERNAME
    if request.method == 'GET':
        return render_template("main_page_code.html", sh_username=USERNAME)
    elif request.method == 'POST':
        db_sess = db_session.create_session()
        main = request.form['main_finder']
        height = request.form['height']
        width = request.form['width']
        length = request.form['length']
        power = request.form['engines_power']
        clas = request.form['class_auto']
        volume = request.form['engines_volume']
        maker = request.form['country_maker']
        date = request.form['made_date']
        auto_list = db_sess.query(Auto).filter(Auto.Name_auto == main,
                                               Auto.Width == width,
                                               Auto.Height == height,
                                               Auto.Length == length,
                                               Auto.Engines_power == power,
                                               Auto.Class_auto == clas,
                                               Auto.Engines_volume == volume,
                                               Auto.Country_maker == maker,
                                               Auto.Made_date == date,
                                               ).all()
        return render_template("list_of_auto_page.html", sh_username=USERNAME, auto_list=auto_list)


@auto_doo.route('/profile', methods=['GET'])
def profile_page():
    """ОБРАБОТЧИК СТРАНИЦЫ ПРОФИЛЯ
    Отображает ник, електронную почту и дату регистрауии нынещнего пользователя.
    Также отображает все темы создынные этим пользователем"""
    global USERNAME, EMAIL, REGISTRATION_DATE
    if request.method == 'GET':
        return render_template("profile_page_code.html",
                               username=USERNAME, email=EMAIL,
                               date_of_registration=REGISTRATION_DATE, list_of_dis=Users.Dises
                               )


@auto_doo.route('/create_dis', methods=['GET', 'POST'])
def creating_discus():
    """ОБРАБОТЧИК СТРАНИЦЫ СОЗДАНИЯ ТЕМЫ
    Работает с БД Discuss, по умолчанию рендерит страницу, при активации POST запроса отправляет данные на сервер.
    Также проверяет: Если схожие данные уже есть в БД, то возвращает сообщение о том, что такая тема уже существует.
    Иначе добавляет её, и возвращает сообщение о том, что тема успешно добавленна"""
    global USERNAME
    db_session.global_init('db/Discuss.db')
    if request.method == 'GET':
        return render_template("creating_dis_page_code.html", sh_username=USERNAME)
    elif request.method == 'POST':
        db_sess = db_session.create_session()
        tag = request.form['tag']
        name = request.form['name_dis']
        desc = request.form['description_dis']
        disdata = db_sess.query(Discuss).filter(
            Discuss.Tag == tag,
            Discuss.Dis_name == name,
            Discuss.description == desc
        ).all()
        if disdata:
            return render_template("done_page.html", sh_username=USERNAME, message='Такая тема уже существует:(')
        else:
            dis = (Discuss(Discuss.Dis_name == name,
                           Discuss.Tag == tag,
                           Discuss.description == desc,
                           Discuss.creating_date == datetime.date.today()))
            db_sess.add(dis)
            user = db_sess.query(Users).filter(Users.Nickname == USERNAME).first()
            user.Dises.append(dis)
            db_sess.commit()
            return render_template('done_page.html', message='Тема создана успешно!', sh_username=USERNAME)


@auto_doo.route('/find_dis', methods=['GET', 'POST'])
def about_site():
    """ОБРАБОТЧИК СТРАНИЦЫ ПОИСКА ТЕМ
    Работает с БД Discuss, по умолчанию рендерит страницу, при активации POST запроса отправляет данные на сервер.
    Также ищет в БД елементы подходящие под условия из формы.
    После возвращает страницу с циклом, выводящим все найденные елементы"""
    global USERNAME
    db_session.global_init('db/Discuss.db')
    if request.method == 'GET':
        return render_template("find_dis_page_code.html", sh_username=USERNAME)
    elif request.method == 'POST':
        db_sess = db_session.create_session()
        name = request.form['find_dis']
        tag = request.form['tag']
        autor = request.form['dis_autor']
        dis_list = db_sess.query(Discuss).filter(Discuss.Dis_name == name,
                                                 Discuss.Tag == tag,
                                                 Discuss.Autor == autor).all()
        return render_template("list_of_discuss_page.html",
                               sh_username=USERNAME,
                               dis_list=dis_list)


if __name__ == '__main__':
    auto_doo.run(port=8080, host='127.0.0.1')
