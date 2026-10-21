#find longest string

def get_longest(*name):
    if len(name)==0:
        return None

    long_name=name[0]
    for n in name:
        if len(n)>len(long_name):
            max_name=n
    return long_name

print(get_longest('Mahesh','Sahil','prasad','soham'))        