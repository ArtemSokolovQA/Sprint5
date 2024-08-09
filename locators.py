class Locators:

    register_name_input = "(//input[@class='text input__textfield text_type_main-default' and @name='name'])[1]" # поле ввода имени в форме регистрации
    register_email_input = "(//input[@class='text input__textfield text_type_main-default' and @name='name'])[2]" # поле ввода email в форме регистрации
    register_password_input = "//input[@class='text input__textfield text_type_main-default' and @type='password']" # поле ввода пароля в форме регистрации
    register_button = "//button[text()='Зарегистрироваться']" # кнопка "зарегистрироваться" на странице регистрации
    enter_title = "//h2[text()='Вход']" # заголовок "Вход" на странице авторизации
    wrong_password_alert = "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']" # уведомление о неправильном пароле
    main_page_login_btn = "//button[text()='Войти в аккаунт']" # кнопка входа в аккаунт на главной странице
    login_email_input = "(//input[@class='text input__textfield text_type_main-default'])[1]" # поле ввода email на странице авторизации
    login_password_input = "(//input[@class='text input__textfield text_type_main-default'])[2]" # поле ввода пароля на странице авторизации
    login_btn = "//button[text()='Войти']" # кнопка войти на странице авторизации
    personal_cabinet_btn = "//p[text()='Личный Кабинет']" # кнопка личного кабинета на главной странице
    exit_btn = "//button[text()='Выход']" # кнопка выхода из аккаунта на странице личного кабинета
    make_order_btn = "//button[text()='Оформить заказ']" # кнопка оформления заказа на главной странице
    register_form_login_btn = "//a[@href='/login' and text()='Войти']" # кнопка войти на странице регистрации
    restore_password_btn = "//a[@href='/forgot-password' and text()='Восстановить пароль']" # кнопка восстановления пароля на странице авторизации
    restore_password_form_login_btn = "//a[@class='Auth_link__1fOlj' and @href='/login' and text()='Войти']" # кнопка входа на странице восстановления пароля
    constructor_btn = "//p[@class and text()='Конструктор']" # кнопка конструктора в хедере сайта
    constructor_title = "//h1[text()='Соберите бургер']" # заголовок на странице конструктора
    bun_btn = "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']" # кнопка "Булки" на странице конструктора
    sauces_btn = "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']" # кнопка "Соусы" на странице конструктора
    fillings_btn = "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'][2]" # кнопка "Начинки" на странице конструктора
    stellar_burger_logo = "//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']"