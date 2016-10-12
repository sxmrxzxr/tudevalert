def on_open(lst, fil):
	with open(fil, "r") as f:
		lst = [l.strip() for l in f]
	print lst
	return lst

def on_close(lst, fil):
	with open(fil, "w") as f:
		for l in lst:
			f.write(l+"\n")
	print lst
