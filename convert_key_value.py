''' convert all keys below from camel case to snake case
read json and convert keys from camel to snake case. 
testTest = test_test
'''
import json

def camel_to_snake(key1):
    c = ''.join(['_' + c if c.isupper() else c for c in key1])
    return c.lower()

def loop_dict(data, new_data):
    for k,v in data.items():
        new_k = camel_to_snake(k)    
        if type(v) == dict:
            new_data1 = {}
            loop_dict(v,new_data1)
            #print(f'new_k inside dict {new_k} {new_data1}')
            new_data[new_k] = new_data1
        elif type(v) == list:
            new_data2_lst = []
            for i in range(len(v)):
                if type(v[i]) == dict:
                    new_data2_dict = {}
                    loop_dict(v[i], new_data2_dict)
                    new_data2_lst.append(new_data2_dict)
                else:
                    new_data2_lst.append(v[i])
            new_data[new_k] = new_data2_lst
        else:
            #print(new_k, v)
            new_data[new_k] = v
    #print(data)
    print(new_data)
                

if __name__ == "__main__":
    with open('./camelcase.json', 'r') as ipf:
        data = json.load(ipf)
    #
    new_data = {}
    loop_dict(data,new_data)
    print('finished')