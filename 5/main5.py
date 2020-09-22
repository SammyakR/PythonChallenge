
import pickle


pickle_off = open ("banner.p", "rb")
emp = pickle.load(pickle_off)

print(emp)
print(type(emp))

for element in emp:
	print("".join([(k*v) for k,v in element]))

