# Проект по тестированию сайта банка "ВТБ"
> <a target="_blank" href="https://vtb.ru/">VTB bank</a>

![main page screenshot](qa_guru_15-master/pictures/main_page.png)

----

### Особенности проекта

* Оповещения о прохождении тестов в Telegram
* Сборка проекта в Jenkins
* Отчеты Allure Report
* Интеграция с Allure TestOps
* Запуск автотестов в Selenoid

### Список проверок, реализованных в автотестах

- [x] Проверить, что текст "Новости"- отображается в разделе "Акционерам"
- [x] Проверить, что текст "Признаны лучшими в разных сферах"- отображается в разделе "О банке"
- [x] Проверить, что текст "Тарифы для бизнеса"- отображается в разделе "Бизнесу"
- [x] Проверить, что текст "Услуги"- отображается в разделе "Кредитным организациям"
- [x] Проверить, что текст "Предложения банка:"- отображается в разделе "Частным лицам"
- [x] Проверить, что текст "Кому подойдет самозанятость"- отображается в разделе "Самозанятым"
----

### Используемый стэк

<img title="Python" src="qa_guru_15-master/pictures/icons/python-original.svg" height="40" width="40"/> <img title="Pytest" src="qa_guru_15-master/pictures/icons/pytest-original.svg" height="40" width="40"/><img title="Allure Report" src="qa_guru_15-master/pictures/icons/Allure_Report.png" height="40" width="40"/> <img title="Allure TestOps" src="qa_guru_15-master/pictures/icons/AllureTestOps.png" height="40" width="40"/> <img title="GitHub" src="qa_guru_15-master/pictures/icons/github-original.svg" height="40" width="40"/> <img title="Selenoid" src="qa_guru_15-master/pictures/icons/selenoid.png" height="40" width="40"/> <img title="Selenium" src="qa_guru_15-master/pictures/icons/selenium-original.svg" height="40" width="40"/> <img title="Selene" src="qa_guru_15-master/pictures/icons/selene.png" height="40" width="40"/> <img title="Pycharm" src="qa_guru_15-master/pictures/icons/pycharm.png" height="40" width="40"/> <img title="Telegram" src="qa_guru_15-master/pictures/icons/tg.png" height="40" width="40"/> <img title="Jenkins" src="qa_guru_python_8_15/pictures/icons/jenkins-original.svg" height="40" width="40"/>

----

### Локальный запуск автотестов

#### Выполнить в cli:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest . --browser-version=100
```

#### Получение отчёта:
```bash
allure serve build/allure-results
```

----

### Проект в Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/qa_guru_15_bank_page_opening/">Ссылка</a>

#### Параметры сборки

```python
BROWSER_VERSION = 100 # Версия браузера
ENVIRONMENT = ['PREPROD', 'PROD'] # Окружение
COMMENT = 'some comment' # Комментарий
```
#### Запуск автотестов в Jenkins
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/qa_guru_15_bank_page_opening/">проект</a>

![jenkins project main page](qa_guru_15-master/pictures/jenkins_project_main_page.png)

2. Нажать "Build with Parameters"
3. В поле "BROWSER_VERSION" ввести: 100
4. Из списка "ENVIRONMENT" выбрать: PROD
5. В поле "COMMENT" ввести комментарий
6. Нажать "Build"

![jenkins_build](qa_guru_15-master/pictures/jenkins_build.png)

----

### Allure отчет
#### Общие результаты 
![allure_report_overview](qa_guru_15-master/pictures/allure_report_overview.png)

#### Результаты прохождения теста
![allure_reports_behaviors](qa_guru_15-master/pictures/allure_reports_behaviors.png)

#### Графики

![allure_reports_graphs](qa_guru_15-master/pictures/alluere_reports_graphs_1.png)
![allure_reports_graphs](qa_guru_15-master/pictures/alluere_reports_graphs_2.png)

----

### Интеграция с Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/3782/dashboards">Ссылка на проект</a>

#### Дашборд с общими показателями тестовых прогонов

![allure_test_ops_dashboards](qa_guru_15-master/pictures/allure_testops_dashboards.png)

#### История запуска тестовых наборов

![allure_testops_launches](qa_guru_15-master/pictures/allure_testops_launches.png)

#### Тест кейсы

![allure_testops_suites](qa_guru_15-master/pictures/allure_testops_suites.png)



----

### Оповещения в Telegram
![telegram_allert](qa_guru_15-master/pictures/telegram_allert.png)

----

### Видео прохождения автотеста
![autotest_gif](qa_guru_15-master/pictures/autotest.gif)

----

