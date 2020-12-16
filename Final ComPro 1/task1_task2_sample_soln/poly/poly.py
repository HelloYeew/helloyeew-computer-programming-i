from OO_complex import *

class Polynomial:

    def __init__(self, coefficients):
        self.coefficients = coefficients

    def add(self, other):
        new_coefficients = []
        target_length = max(len(self.coefficients), len(other.coefficients))
        ext1 = (target_length - len(self.coefficients)) * [0] + self.coefficients
        ext2 = (target_length - len(other.coefficients)) * [0] + other.coefficients
        for index in range(target_length):
            new_coefficients.append(ext1[index] + ext2[index])
        return Polynomial(new_coefficients)

    def val(self, v):
        poly_value = 0
        for index, coeff in enumerate(self.coefficients):
            poly_value += self.coefficients[index] *  v**(len(self.coefficients) - 1 - index)
        return poly_value
    
    def mul(self, other):
        target_length = len(self.coefficients) - 1 + len(other.coefficients) - 1 + 1
        list_of_coefficient_list = []
        for i in range(target_length):
            list_of_coefficient_list.append([])
        for self_index, self_coeff in enumerate(self.coefficients):
            self_degree = len(self.coefficients) - 1 - self_index
            for other_index, other_coeff in enumerate(other.coefficients):
                other_degree = len(other.coefficients) - 1 - other_index
                result_index = (target_length - 1) - (self_degree + other_degree)
                list_of_coefficient_list[result_index].append(self_coeff * other_coeff)
        result = []
        for l in list_of_coefficient_list:
            result.append(sum(l))
        return Polynomial(result)
    
    def coeff(self, i):
        return self.coefficients[len(self.coefficients) - 1 - i]
    
    def roots(self):
        if len(self.coefficients) - 1 > 2:
            return 'Order too high to solve for roots.'
        else:
            if len(self.coefficients) - 1 == 1:
                return -1.0 * self.coefficients[1] / self.coefficients[0]
            else:
                a = self.coefficients[0]
                b = self.coefficients[1]
                c = self.coefficients[2]
                D = b**2 - 4*a*c
                if D > 0:
                    return [(-1.0*b + D**0.5)/(2*a), (-1.0*b - D**0.5)/(2*a)]
                else:
                    return [str(Complex(-1.0*b/2*a, abs(D)**0.5/2*a)), str(Complex(-1.0*b/2*a, -1.0*abs(D)**0.5/2*a))]

    def __call__(self, v):
        return self.val(v)

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)

    def __str__(self):
        poly_str = ''
        for index, coeff in enumerate(self.coefficients):
            if len(self.coefficients) - 1 - index > 1:
                poly_str += str(self.coefficients[index]) + '(' + 'z**' + str(len(self.coefficients) - 1 - index) + ') + '
            elif len(self.coefficients) - 1 - index == 1:
                poly_str += str(self.coefficients[index]) + '(' + 'z' + ') + '
            else:
                poly_str += str(self.coefficients[index])
        return poly_str
