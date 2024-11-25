# Система управления библиотекой
### Проект представляет собой легко расширяемую систему управления библиотекой
##### Проект состоит из 2х основных частей:
1. Микро фреимворк
- database .py (Микро ОРМ поддерживающая CRUD операции)
- initilize .py (Отвечает за инициализацию фреимворка)
- src .py (Отвечает за взаимодействие с пользователем)
- tools .py (Хранит готовые функции для для облегчения разработки бизнес логики)
2. Бизнес логика
- commands .py (Содержит пользовательские команды, доп информацию по ним и соответствующую view функцию)
- views .py (Содержит функции бизнес логики)
- models .py (Содержит класс таблицы бд) 

##### Схема взаимодействия

![image](https://github.com/user-attachments/assets/92e153eb-81ec-4ca7-9693-4bfcebb9ae31)

1. Запуск Manager
2. Запуск Initializer
3. Ожидание команды пользователя
4. Ожидание доп данных по команде от пользователя
5. Запуск соответствующей функции view
6. Возврат результата

##### Результат
В результате систему очень легко расширять добавляя новые команды (), а так же легко менять поля модели в базе данных 

##### TODO
1) Изменить способ хранения данных (Например на )
2) Улучшить алгоритмы CRUD операций
3) Добавить больше тестов