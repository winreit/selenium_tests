# Описание

# Проверка аутентификации и авторизации пользователя

Автоматизированные тесты для сайта saucedemo.com с использованием Selenium WebDriver и pytest с отчетами Allure.


## Функциональность
- Этот проект содержит автоматизированные тесты для демонстрационного сайта SauceDemo. Проект демонстрирует:

- Открытие страницы логина.

- Ввод логина (standard_user) и пароля (secret_sauce).

- Нажатие кнопки Login.

- Проверка успешного входа (открытие страницы с товарами).

- Проверка успешного выхода

- Allure-отчёты

## Технологии
  - **Python 3.10**
  - **selenium 4.15.2**
  - **pytest 7.4.3**

## Установка
1. Клонируйте репозиторий:
   ```bash
   [git clone https://github.com/SergeyKurilko/alkotekaParser.git](https://github.com/winreit/scrapy](https://github.com/winreit/selenium_tests)
   ```
2. Перейдите в каталог selenium_tests
   ```bash
   cd selenium_tests
   ```
3. Создайте виртуальное окружение и активируйте его:
  
   Для macOS/Linux
   ```bash
   python3 -m venv venv
   source venv/bin/activate 
   ```
   Для Windows
   ```bash
   python -m venv myenv
   myenv\Scripts\activate
   ```
   
6. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

7. Включите автоматизацию Safari (для macOS):
   ```bash
   defaults write com.apple.Safari IncludeDevelopMenu -bool true
   ```
   Включите удаленную автоматизацию
   ```bash
   safaridriver --enable
   ```

## Использование

  Запустить все тесты с Safari (по умолчанию)
   ```bash
   pytest
   ```
  Запустить с подробным выводом
   ```bash
   pytest -v
   ```
  Запустить с Safari (по умолчанию)
   ```bash
  pytest --browser=safari
   ```
  Запустить с Chrome (требует webdriver)
   ```bash
  pytest --browser=chrome
   ```
  Запустить с Firefox (требует webdriver)
   ```bash
  pytest --browser=firefox
   ```


  
