В репозитории находится итоговый проект по курсу "Тестировщик-автоматизатор на Python" от SkillFactory. 
Объект тестирования: Авторизации/Регистрации/Восстановления страниц личного кабинета Росстелеком. 
Ссылка на ЛК Ростелеком: https://b2c.passport.rt.ru

По заданию тестирования необходимо:

1. Протестировать требования.
2. Разработать тест-кейсы (не менее 15). Необходимо применить несколько техник тест-дизайна.
3. Провести автоматизированное тестирование продукта (не менее 15 автотестов). По одному автотесту на каждый написанный тест-кейс.
4. Оформить описание обнаруженных дефектов. Если дефекты не обнаружены, то необходимо описать 3 потенциально возможных дефекта на данном ресурсе.

С тест-кейсами и описанными ошибками/дефектами/недостатками можно ознакомиться по ссылке: https://docs.google.com/spreadsheets/d/1T6JnWBaFkIqWItMfUW7AfXqzLwAxvfRZRWKbqxRZqV4/edit?usp=sharing

Проект выполнен с помощью библиотеки Pytest и Selenium

Тесты находятся в папке "tests" в файле "tests_auto". 
В папке "pages" хранится "base_page", "auth_page" и отдельный файл "elements", содержащий локаторы для поиска элементов на странице. 
Файл "settings" - данные для авторизации, в файле "requirments" - список необходимых для установки библиотек.
