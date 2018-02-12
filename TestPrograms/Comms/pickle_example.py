import pickle
import sys,shutil

#pickle data to file
favorite_color = {"lion":"yellow","kitty": "red"}


#open("name_of_file","mode",buffer,encoding) #make fileobj
#mode = (r)ead (w)rite (x)clusive(fail if exists) (a)ppend
#     = (b)inary (t)ext (w+)r&w

#pickle.dump(obj to pickle,fileobj,protocol)

print(pickle.HIGHEST_PROTOCOL)
pickle.dump(favorite_color, open("save.p","wb"),3)

byte_obj = pickle.dumps(favorite_color) #for sending to var instead of a file
print(byte_obj)

#unpickle from file
colors = pickle.load( open("save.p", "rb"))
print(sys.getsizeof(favorite_color))
print(sys.getsizeof(byte_obj))
