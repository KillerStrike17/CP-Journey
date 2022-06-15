class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        first_salary = brackets[0][0]
        first_tax = brackets[0][1]
        if first_salary > income:
            return income*first_tax/100
        else:
            tax = first_salary*first_tax/100
            print(tax)
            for _ in range(1, len(brackets)):
                print(first_salary)

                if brackets[_][0] > income:
                    tax += (income-first_salary)*brackets[_][1]/100
                    break
                else:
                    tax += (-first_salary + brackets[_][0])*brackets[_][1]/100
                    first_salary = brackets[_][0]
                print(tax)
            return tax
