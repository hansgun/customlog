## 로그 설정 파일 

### 파일 구성 

**1. log.py [로그 포맷, 레벨, 디렉터리 지정]**
- 로그 포맷 class : PaipLogFormatter    
  .``` '%(asctime)s - %(levelname)-10s - %(filename)s - %(funcN    ame)s - %(message)s' ```
  * ex : ``` 2022-07-08 18:35:49,197 - ERROR      - Calculator - divide - Exception: division by zero ```  
- get_logger function  
  . 로그 저장 디렉터리 지정 : ```  linux_log_dir = './logs_dir/' ```  
  . 로그 레벨 지정 : default ```logging.ERROR``` 테스트시는 ```logging.DEBUG``` 혹은 ```logging.INFO``` 로 지정하여 진행 

**2. paiplog.py [decorator]**

### 사용법   
* paiplog.paiplog , log 를 임포트 한다  
* 적용하고자 하는 function 에 @paiplog decorator 적용  
* log.py에 지정된 레벨 이상의 로그가 지정된 디렉터리에 지정된 형태로 저장됨   

##### function 적용 시
```python
from paiplog import paiplog
import log

@paiplog
def divide3(a=1,b=0) :
    return a/b
```

#### class 적용 시
```python 
from paiplog import paiplog
import log

class Calculator():
    def __init__(self, first=0, second=0, log_file_name='', log_file_dir=''):
        self.first = first
        self.second = second
        #log file name and directory which we want to keep
        self.log_file_name = log_file_name
        self.log_sub_dir = log_file_dir

    @paiplog
    def divide(self):
        try:
            return self.first / self.second
        except:
            raise

if __name__ == '__main__':
    calculator = Calculator(5, 0, 'calculator_file', '')
    calculator.divide()

```

```

