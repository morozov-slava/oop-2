В целом, при создании публичных связей между модулями снижается инкапсуляция и общая гибкость системы, и по сути сам принцип модульности в некотором роде нарушается.
По идее, при тестировании может быть необходимость сделать модули публичными.

Метрики для количественной оценки принципов организации модулей:
- Размер модуля.
- Связность компонентов модуля (внутренняя связность).
- Связность с другими модулями (внешняя связность).
- Цикломатическая сложность модуля.

Оценка модульности программы:

- **Размер модуля:** 
	- Чем больше методов в модуле, тем выше размер модуля.
	  (как следствие, модуль сложнее поддерживать, развивать и выше вероятность перегруженности модуля)
	- Чем больше строк кода в методе, тем выше размер модуля.
	  (можно оценивать как среднее кол-во строк кода в методе модуля)
- **Связность компонентов модуля:**
	- Чем сильнее связаны методы в рамках модуля, тем выше внутренняя связность.
	  (модуль с нулевой связанностью - это модуль, каждая функциональная единица которого не связана с другими функциональными единицами этого же модуля)
	- Возможная единица измерения: 0.5k/n
   
где:
- k - общее кол-во связей между функциональными компонентами (берём половину, т.к. две связных между собой функциональные единицы будут два раза учитываться).
- n - общее кол-во функциональных единиц в модуле.

- **Связность с другими модулями:**
	- Чем больше зависимых компонентов у некоторого модуля от других, тем выше его внешняя связность, что делает модуль менее гибким, сложным для восприятия и поддержки.
	- Измерять можно попробовать таким образом, чтоб учитывать как кол-во связей с конкретным модулем, так и кол-во модулей, с которым данный модуль связан.
	  Пример простейшего варианта: k^(m+1)
где:
- k - кол-во модулей, с которыми связан рассматриваемый модуль.
- m - среднее кол-во связей на один связанный модуль.

- **Цикломатическая сложность модуля:**
	- Цикломатическая сложность модуля характеризует кол-во возможных путей исполнения программы.
	- Рассчитывается по стандартной формуле расчёта цикломатической сложности, но берётся среднее для каждой функциональной единицы модуля.

