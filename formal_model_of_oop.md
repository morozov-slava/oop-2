В Python возможно реализовать полиморфный и ковариантный вызовы метода с определёнными нюансами для ковариантности.

Пример полиморфного вызова метода:

```py
from abc import ABC, abstractmethod


class Report(ABC):
    @abstractmethod
    def export_to_parquet(self, path: str) -> None:
        pass


class FinancialReport(Report):
    def export_to_parquet(self, path: str) -> None:
        pass


class SalesReport(Report):
    def export_to_parquet(self, path: str) -> None:
        pass


def export_report_to_parquet(report: Report) -> None:
    report.export_to_parquet()


reports = [FinancialReport(), SalesReport()]
for r in reports:
    export_report_to_parquet(r)
```



Ковариантность обычно проявляется в контексте **типов возвращаемых значений**: подклассы могут переопределять методы и возвращать более конкретный тип.

Пример ковариантного вызова метода:

```py
from abc import ABC, abstractmethod
from typing import Protocol


class Report(ABC):
    @abstractmethod
    def export_to_parquet(self, path: str) -> None:
        pass
        

class FinancialReport(Report):
    def export_to_parquet(self, path: str) -> None:
        pass


class SalesReport(Report):
    def export_to_parquet(self, path: str) -> None:
        pass


# Протокол (интерфейс) с возвращаемым типом Report
class ReportFactory(Protocol):
    def create(self) -> Report:
        pass


# Конкретная реализация, которая возвращает FinancialReport (подтип Report)
class FinancialReportFactory(Protocol):
    def create(self) -> FinancialReport:
        return FinancialReport()
	

def create_report(factory: ReportFactory) -> Report:
    return factory.create()

factory = FinancialReportFactory()
report = create_report(factory) 
```

Ввиду того, что Python является языком с динамической типизацией, то проверка может осуществляться только с помощью статических анализаторов типа (по типу `mypy`), а во время выполнения не осуществляется строгий контроль над типами.



