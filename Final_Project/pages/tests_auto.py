from pages.auth_page import AuthPage
from pages.elements import *
from settings import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver import ActionChains


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument("--start-maximized")
    return chrome_options


def test_auth_by_email_positive(selenium):
    # EXP-002 - Проверка авторизации на сайте ЛК Ростелеком через номер телефонаи пароль
    page = AuthPage(selenium)
    page.enter_username(AuthPhone.phone)
    page.enter_pass(AuthPhone.password)
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'


def test_auth_by_email_nagative(selenium):
    # EXP-003 - Проверка авторизации на сайте ЛК Ростелеком через email и пароль
    page = AuthPage(selenium)
    page.enter_username(AuthEmail.email)
    page.enter_pass(AuthEmail.password)
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'


def test_auth_by_phonenumber_positive(selenium):
    # EXP-004 - Проверка авторизации на сайте ЛК Ростелеком с невалидным номером телефона/паролем 
    page = AuthPage(selenium)
    page.enter_username(AuthPhone.phone)
    page.enter_pass(InvalidData.password)
    page.btn_click()

    assert page.get_relative_link() != '/account_b2c/page'
    assert page.find_el('xpath', '//*[@id="page-right"]/div/div/p').text == 'Неверный логин или пароль'


def test_auth_by_phonenumber_negative(selenium):
    # EXP-005 Проверка авторизации на сайте ЛК Ростелеком с невалидным email/паролем 
    page = AuthPage(selenium)
    page.enter_username(AuthEmail.email)
    page.enter_pass(InvalidData.password)
    page.btn_click()

    assert page.get_relative_link() != '/account_b2c/page'
    assert page.find_el(*wrong_log_pass_message).text == 'Неверный логин или пароль'


def test_auth_by_login_negative(selenium):
    # EXP-006 - Проверка авторизации на сайте ЛК Ростелеком с валидным логин/паролем 
    page = AuthPage(selenium)
    page.enter_username(AuthLogin.login)
    page.enter_pass(AuthLogin.password)
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'


def test_auth_by_login_symbol_negative(selenium):
    # EXP-007 - Проверка авторизации на сайте ЛК Ростелеком с невалидным логин/паролем 
    page = AuthPage(selenium)
    page.enter_username(SymbolData.login)
    page.enter_pass(SymbolData.password)
    page.btn_click()

    assert page.get_relative_link() != '/account_b2c/page'
    assert page.find_el('xpath', '//*[@id="page-right"]/div/div/p').text == 'Неверный логин или пароль'


def test_auth_by_login_kirill_negative(selenium):
    # EXP-008 Авторизация пользователя с использованием кириллицы в поле ввода логин/пароль
    page = AuthPage(selenium)
    page.enter_username(KirillData.login)
    page.enter_pass(KirillData.password)
    page.btn_click()

    assert page.get_relative_link() != '/account_b2c/page'
    assert page.find_el('xpath', '//*[@id="page-right"]/div/div/p').text == 'Неверный логин или пароль'


def test_auth_with_maxlens_negative(selenium):
    # EXP-009 - Проверка ввода в поля логина и пароля строки длиной >2500 символов
    page = AuthPage(selenium)
    page.enter_username(BIGData.login * 500)
    page.enter_pass(BIGData.password * 500)
    page.btn_click()

    assert page.find_el(*internal_error_message_text).text == 'Internal Server Error'


def test_forget_password(selenium):
    # EXP-010 - Проверка перехода по ссылке "Забыл пароль"
    page = AuthPage(selenium)
    page.forget_password_link.click()

    assert page.find_el(*res_pass_text).text == 'Восстановление пароля'


def test_registration(selenium):
    # EXP-011 - Проверка перехода по ссылке "Зарегистрироваться"
    page = AuthPage(selenium)
    page.registration_link.click()

    assert page.find_el(*reg_page_text).text == 'Регистрация'


def test_chat_viber(selenium):
    # EXP-012 - Открытие чата в Viber
    page = AuthPage(selenium)
    chat_vb = page.find_el(*widget_bar)
    original_window = page.driver.current_window_handle
    hover = ActionChains(selenium).move_to_element(chat_vb)
    hover.perform()
    page.find_el(*viber_button).click()
    WebDriverWait(page.driver, 5).until(EC.number_of_windows_to_be(2))
    for window_handle in page.driver.window_handles:
        if window_handle != original_window:
            page.driver.switch_to.window(window_handle)
            break
    assert page.get_base_url() == 'chats.viber.com'


def test_chat_telegram(selenium):
    # EXP-013 - Открытие чата в Telegram
    page = AuthPage(selenium)
    chat_tg = page.find_el(*widget_bar)
    original_window = page.driver.current_window_handle
    hover = ActionChains(selenium).move_to_element(chat_tg)
    hover.perform()
    page.find_el(*telegram_button).click()
    WebDriverWait(page.driver, 5).until(EC.number_of_windows_to_be(2))
    for window_handle in page.driver.window_handles:
        if window_handle != original_window:
            page.driver.switch_to.window(window_handle)
            break
    assert page.get_base_url() == 'telegram.me'


def test_auth_vk(selenium):
    # EXP-014 - Проверка перехода по ссылке авторизации пользователя через VK
    page = AuthPage(selenium)
    page.vk_button.click()

    assert page.get_base_url() == 'oauth.vk.com'


def test_auth_ok(selenium):
    # EXP-015 - Проверка перехода по ссылке авторизации пользователя через сайт одноклассники
    page = AuthPage(selenium)
    page.ok_button.click()

    assert page.get_base_url() == 'connect.ok.ru'


def test_auth_moymir(selenium):
    # EXP-016 - Проверка перехода по ссылке авторизации пользователя через сайт Мой мир
    page = AuthPage(selenium)
    page.mailru_button.click()

    assert page.get_base_url() == 'connect.mail.ru'


def test_auth_google(selenium):
    # EXP-017 - Проверка перехода по ссылке авторизации пользователя через Google
    page = AuthPage(selenium)
    page.google_button.click()

    assert page.get_base_url() == 'accounts.google.com'


def test_auth_yandex(selenium):
    # EXP-018 - Проверка перехода по ссылке авторизации пользователя через Yandex
    page = AuthPage(selenium)
    page.ya_button.click()

    assert page.get_base_url() == 'passport.yandex.ru'
