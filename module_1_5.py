spy = "I am from Mossad"
immutable_var = tuple([1, 2.45, 'Gut', False, spy])
print ('Неизменный кортеж:',immutable_var)

#immutable_var.extend("OMG")

mutable_list = [6, 31.09, 'Prisonbreak', True, spy]
print ('Изначальный список:', mutable_list)
print ('Откуда наш шпион?')
spy = input()
mutable_list = [6, 31.09, 'Prisonbreak', True, spy]
mutable_list.remove(31.09)
print ('Измененный список:',mutable_list)