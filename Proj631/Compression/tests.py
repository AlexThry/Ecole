from Classes.Class_Node import Node



def median(liste):
	if len(liste)%2 == 0:
		median = liste[int(len(liste)/2)-1]
		_before = liste[:int(len(liste)/2)-1]
		_after = liste[int(len(liste)/2):]
	else:
		median = liste[int(len(liste)/2)]
		_before = liste[:int(len(liste)/2)]
		_after = liste[int(len(liste)/2) + 1:]
	return median, _before, _after




if __name__ == "__main__":
	liste = [1,2,3,4,5]
	create_root()