import numpy

class Polynomial:
    def __init__(self, num_list):
        self.for_numpy = numpy.poly1d(num_list)
        self.num_list_original = num_list
        self.__num_list = num_list
        self.final_answer = ""
        self.other_object = ...

    def give_list(self):
        return self.__num_list

    def give_list_original(self):
        return self.num_list_original

    def add(self, object_for_add):
        self.other_object = object_for_add
        list_to_add = object_for_add.give_list()
        answer = self.__num_list
        i = len(self.__num_list)-1
        j = len(list_to_add)-1
        while i > 0:
            try:
                answer[i] = answer[i] + list_to_add[j]
            except:
                answer[i] = answer[i] + 0
            i -= 1
            j -= 1
        answer = self.print_formula(answer)
        return answer

    def minus(self,object_for_minus):
        list_to_minus = object_for_minus.give_list()
        answer = self.__num_list
        i = len(self.__num_list) - 1
        j = len(list_to_minus) - 1
        while i > 0:
            try:
                answer[i] = answer[i] - list_to_minus[j]
            except:
                answer[i] = answer[i] - 0
            i -= 1
            j -= 1
        answer = self.print_formula(answer)
        return answer

    def mul(self,object_for_mul):
        self.minus(self.other_object)
        list_mul1 = self.__num_list
        list_mul2 = object_for_mul.give_list()
        if len(list_mul2)>len(list_mul1):
            max_number = len(list_mul2)
        else:
            max_number = len(list_mul1)
        answer = []
        for i in range((max_number*2)-1):
            answer.append(0)
        for i in range(len(list_mul1)):
            for j in range(len(list_mul2)):
                answer[i+j] += list_mul1[i]*list_mul2[j]
        print_answer = self.print_formula(answer)
        return print_answer




    def print_formula(self,list_print):
        print_formula = ""
        print_formula += str(list_print[0]) + f"(z**{len(list_print) - 1})"
        i = len(list_print) - 2
        j = 1
        while j < len(list_print):
            if i == 0:
                print_formula += " + " + str(list_print[j])
            elif i == 1:
                print_formula += " + " + str(list_print[j]) + "(z)"
            else:
                print_formula += " + " + str(list_print[j]) + f"(z**{i})"
            j += 1
            i -= 1
        return print_formula

    def __add__(self, other):
        self.minus(other)
        return self.add(other)

    def __mul__(self, other):
        # self.minus(self.other_object)
        list_mul1 = self.__num_list
        list_mul2 = other.give_list()
        if len(list_mul2) > len(list_mul1):
            max_number = len(list_mul2)
        else:
            max_number = len(list_mul1)
        answer = []
        for i in range((max_number * 2) - 1):
            answer.append(0)
        for i in range(len(list_mul1)):
            for j in range(len(list_mul2)):
                answer[i + j] += list_mul1[i] * list_mul2[j]
        print_answer = self.print_formula(answer)
        return print_answer

    def roots(self):
        answer = self.for_numpy.roots
        return answer

    def coefficients(self):
        answer = self.for_numpy.coefficients
        return answer

    def __call__(self, v):
        self.minus(self.other_object)
        answer = 0
        for i in range(len(self.__num_list)):
            answer += self.__num_list[i]*v
        return answer


    def __str__(self):
        final_answer = self.print_formula(self.__num_list)
        return final_answer



# use numpy from
# - https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d
# - https://numpy.org/doc/stable/reference/generated/numpy.roots.html?highlight=root
