file = open('./test.env')
env = file.readlines()[0]
file.close()
index = len(env) - 1
token = env[:index]