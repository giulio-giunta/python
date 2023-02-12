'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

def compact(my_list):
	return [i for i in my_list if i]

print(compact([0,1,2,"",[], False, {}, None, "All done"]))