#Выполнила Маслова Варвара.Группа ТРПО24-3
# Chess
Создать объектно-ориентированную реализацию программы для игры в шахматы.
Реализовать программу, которая позволяет играть в шахматы на компьютере.
Взаимодействие с программой производится через консоль (базовый вариант). Игровое
поле изображается в виде 8 текстовых строк, плюс строки с буквенным обозначением
столбцов (см. пример на Рис. 1) и перерисовывается при каждом изменении состояния
поля. При запросе данных от пользователя программа сообщает, что ожидает от
пользователя (например, позицию фигуры для следующего хода белыми; целевую
позицию выбранной фигуры) и проверяет корректность ввода (допускаются только ходы
соответствующие правилам шахмат; поддержка рокировки, сложных правил для пешек и
проверки мата вынесена в отдельные пункты). Программа должна считать количество
сделанных ходов.
Сама программа НЕ ходит: т.е. не пытается выполнить ходы за одну из сторон, а
предоставляет поочередно вводить ходы за белых и черных.
Требования к реализации:
Основные объекты и абстрактные сущности игры должны быть представлены в виде
объектов, представителей соответствующих классов, часть классов должны быть
организованы в виде иерархии. В частности: шахматные фигуры – объекты,
представители классов, организованных в виде иерархии; доска – объект; ходы фигур –
объекты. Вся основная информация должна храниться в атрибутах объектов или классов
(например, информация о положении фигур, цвете фигур, символах, используемых для
визуализации фигур и т.п.). Основная часть функционала должна программы должна быть
организована в виде методов, закрепленных за соответствующими объектами или
классами. Например, это касается методов определяющих допустимые ходы фигур.
Организация иерархий классов, атрибутов и методов должна позволять гибко расширять
возможности программы с минимальными изменениям в уже созданном коде.

#Дополнительные задания:

2. На базе игры в шахматы реализовать игру в шашки. Разработать модификацию
шахмат с минимальным вмешательством в существующий код.
Сложность 2

3. На базе игры в шахматы на классической доске реализовать игру в гексагональные
шахматы ( https://ru.wikipedia.org/wiki/Гексагональные_шахматы ). Выбрать один
из трех вариантов: шахматы Глинского; шахматы МакКуэя; шахматы Шафрана.
Разработать модификацию шахмат с минимальным вмешательством в
существующий код для обычных шахмат.
Сложность 3

5. Реализовать возможность «отката» ходов. С помощью специальной команды
можно возвращаться на ход (или заданное количество ходов) назад вплоть до
начала партии. Информация о ходах в партии должна храниться в объектно-
ориентированном виде.
Сложность 1

![image](https://github.com/user-attachments/assets/1f41d966-755e-430d-b19e-24b97d6905f6)

