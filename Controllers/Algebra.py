class Algebra:
    """
        Evaluate the given source in the context of globals and locals.
    """
    def __init__(self) -> None:
        self.__rest: list[float] = []
        self.__items: list[str] = []
        self.__final_result: list[str] = []
        self.__auxiliar: int = 0
        self.__status_sec: bool = False
        self.__count: int = 0
        self.__operatore: list[str] = ['*', '/', '+', '-']

    @property
    def rest(self) -> list[float]:
        return self.__rest

    @property
    def items(self) -> list[str]:
        return self.__items

    @property
    def finalResult(self) -> list[str]:
        return self.__final_result

    @property
    def auxiliar(self) -> int:
        return self.__auxiliar

    @property
    def status_sec(self) -> bool:
        return self.__status_sec

    @property
    def status_count(self) -> int:
        return self.__count

    @property
    def operatore(self) -> list[str]:
        return self.__operatore

    @rest.setter
    def rest(self, value) -> None:
        self.__rest = value

    @items.setter
    def items(self, value) -> None:
        self.__items = value

    @finalResult.setter
    def finalResult(self, value) -> None:
        self.__final_result = value

    @auxiliar.setter
    def auxiliar(self, value) -> None:
        self.__auxiliar = value

    @status_sec.setter
    def status_sec(self, value) -> None:
        self.__count = value

    @operatore.setter
    def operatore(self, value) -> None:
        self.__operatore = value

    def mainSolve(self):
        values: str = input("valores: ")
        [self.items.append(item) for item in values]
        position: list[float] = [index for index, operators in enumerate(self.items) if
                                 operators == "*" or operators == "/"]
        operators: list[str] = [operator for index, operator in enumerate(values) if index in position]
        before: list[float] = [float(values[index - 1]) for index in position]
        after: list[float] = [float(values[index + 1]) for index in position]
        intermediate_result: list[float or str] = []
        verify_condition: bool = False
        response: str
        if '+' in values or '-' in values:
            response = self.ifmultiOrDiv(operators, before, after, values, intermediate_result, verify_condition, position)
        else:
            response = self.ifNotMultiOrDiv(values)
        return response

    def ifmultiOrDiv(self, operators, before, after, values, intermediate_result, verify_condition, position) -> str:
        """
        :param operators:
        :param before:
        :param after:
        :param values:
        :param intermediate_result:
        :param verify_condition:
        :return:
        """
        for i in range(0, len(before)):
            if operators[i] == '*':
                intermediate_result.append(before[i] * after[i])
            elif operators[i] == '/':
                try:
                    intermediate_result.append(before[i] / after[i])
                except ZeroDivisionError:
                    intermediate_result.append("Indeterminate")
        for index, itens in enumerate(self.items):
            if index + 1 in position:
                continue
            elif index - 1 in position:
                continue
            else:
                if itens not in self.operatore[:2]:
                    self.rest.append(self.items[index])
                else:
                    self.rest.append(intermediate_result[self.auxiliar])
                    self.auxiliar += 1

        for index, item in enumerate(self.rest):
            if item == "+" and self.status_sec == False:
                self.finalResult.append(str(float(self.rest[index - 1]) + float(self.rest[index + 1])))
                status_sec = True
            elif item == "-" and self.status_sec:
                self.finalResult.append(str(float(self.finalResult[self.count]) - float(self.rest[index + 1])))
                self.__count += 1
                status_sec = True
            elif item == "-" and self.status_sec == False:
                self.finalResult.append(str(float(self.rest[index - 1]) - float(self.rest[index + 1])))
                status_sec = False
            elif item == "+" and self.status_sec:
                self.finalResult.append(str(float(self.finalResult[self.__count]) + float(self.rest[index + 1])))
                self.__count += 1
                status_sec = True
        return self.finalResult[len(self.finalResult) - 1]

    def ifNotMultiOrDiv(self, values) -> str:
        for index, item in enumerate(values):
            if item == "*" and self.status_sec == False:
                self.finalResult.append(str(float(values[index - 1]) * float(values[index + 1])))
                status_sec = True
            elif item == "/" and self.status_sec:
                self.finalResult.append(str(float(self.finalResult[self.__count]) / float(values[index + 1])))
                self.__count += 1
                status_sec = True
            elif item == "/" and self.status_sec == False:
                self.finalResult.append(str(float(values[index - 1]) / float(values[index + 1])))
                status_sec = False
            elif item == "*" and self.status_sec:
                self.finalResult.append(str(float(self.finalResult[self.__count]) * float(values[index + 1])))
                self.__count += 1
                status_sec = True

        return self.finalResult[len(self.finalResult) - 1]


if __name__ == '__main__':
    a = Algebra()
    result: str = a.mainSolve()
    print(result)
