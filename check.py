class Process:
    
    def check_existance(self,file_name,query_string):
        with open(file_name) as f:
            if query_string in f.read():
                return "true"
            else:
                return "false"

    def store_exploit(self,exploit_query):
        if exploit_query not in EXPLOIT_QUERYS:
            EXPLOIT_QUERYS.append(exploit_query)

class ReadLog:
    
    def check_log(self,log_path,exploit_list):
        process = Process()
        for exploit_file in exploit_list:
            with open(exploit_file,encoding="mbcs") as f:
                exploits = [line.rstrip('\n') for line in f]
                for exploit in exploits:
                    result = process.check_existance(log_path,str(exploit))
                    if(result == "true"):
                        process.store_exploit(str(exploit))
                        
                
EXPLOIT_QUERYS = []       
read_log = ReadLog()
read_log.check_log('access.log',["xss.log"])
print(EXPLOIT_QUERYS)
