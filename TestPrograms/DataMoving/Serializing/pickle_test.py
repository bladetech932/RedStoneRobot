import pickle

# An arbitrary collection of objects supported by pickle.
data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

with open('data.topsecret', 'w+b') as i:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(data, i, pickle.HIGHEST_PROTOCOL)

with open('data.topsecret' , 'r+b') as o:
    data_in =  pickle.load(o)

print(data_in)
