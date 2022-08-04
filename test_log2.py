from module.paiplog import paiplog, get_logger
log_file_name = 'test_log2'

@paiplog
def divide3(a=1,b=0) : 
    return a/b

class Test():
    def __init__(self) : 
        self.log_file_name = 'test_log2'
        self.log_file_dir = ''
        self.logger_obj = get_logger(log_file_name=self.log_file_name, log_sub_dir=self.log_file_dir)

    @paiplog
    def divide2(a=1,b=0) :
        temp_a, temp_b = a,b
        return temp_a/temp_b

if __name__ == '__main__':
    test = Test()
    test.divide2()
    divide3()
