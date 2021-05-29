data = [] 
for row in result: 
    data.append(row) 
 
mno = set()  
for row in data: 
    if int(row['_source']['recordCount']) > 0: 
        mno.update(row['_source']['masterNo']) 


def process_file(input_file: str, username:str, passwrod: str, url: str): 
    data = json.load(open(input_file, 'r')) 
    bad = {} 
    missing = {} 
    for record in data: 
        master_no = record['_id'] 
        g_data = call_gsky(master_no) 
        missing_keys, bad_keys = compare_json(g_data, record['_source']) 
        missing[master_no] = missing_keys   
        bad[master_no] = bad_keys 
        sleep(1) 
    return bad, missing 

def load_args(): 
    parser = argparse.ArgumentParser() 
    parser.add_argument("-f", dest="file", help="input file with 1 ID per line", action="append") 
    parser.add_argument("-i", dest="index", help="name of index to query", action="append") 
    parser.add_argument("-e", dest="host", help="URL for ES host",  
    default='link') 
    parser.add_argument("-p", dest="port", help="Port for ES host", default=9200) 
    parser.add_argument("-o", dest="output", help="Output file, 1 ID per line", default="output_ids.csv") 
    return parser.parse_args()
