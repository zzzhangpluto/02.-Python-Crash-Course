#1. 测试函数
#1.1单元测试和测试用例
#模块unittest提供了代码测试工具

#1.2可通过的测试
import unittest
def get_formatted_name(first_name,last_name):
    full_name=first_name+' '+last_name
    return full_name.title()

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        """能够正确处理像 Janis Joplin这样的姓名吗"""
        formatted_name=get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
unittest.main()

#1.3不能通过的测试
def get_formatted_name(first,last,middle=''):
    if middle:
        full_name=first+' '+middle+' '+last
    else:
        full_name=first+' '+last
    return full_name.title()

#1.4测试未通过怎么办
#检查刚对函数所做的修改，找出导致函数行为不符合预期的修改

#1.5添加新测试
import unittest
def get_formatted_name(first,last,middle=''):
    if middle:
        full_name=first+' '+middle+' '+last
    else:
        full_name=first+' '+last
    return full_name.title()

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        """能够正确处理像 Janis Joplin这样的姓名吗"""
        formatted_name=get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
    def test_first_middle_last_name(self):
        formatted_name=get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')
unittest.main()

#2. 测试类
#2.1各种断言方法
#assertEqual(a,b)
#assertNotEqual(a,b)
#assertTrue(x)
#assertFalse(x)
#assertIn(item,list)
#assertNotIn(item,list)

#2.2一个要测试的类
class AnonymousSursey():
    """收集匿名调查问卷的答案"""
    def __init__(self,question):
        """存储一个问题，并为存储答案做准备"""
        self.question=question
        self.responses=[]
    def show_question(self):
        """显示调查问卷"""
        print(self.question)
    def store_response(self,new_response):
        """存储单份调查问卷"""
        self.responses.append(new_response)
    def show_results(self):
        """显示收集到的所有问卷"""
        print("Survey results:")
        for response in self.responses:
            print('-'+response)

question="What language did you first learn to speak?"
my_survey=AnonymousSursey(question)
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response=input("Language: ")
    if response=='q':
        break
    my_survey.store_response(response)
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

#2.3测试AnonymousSurvey类
import unittest
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def test_store_single_response(self):
        """测试单个答案会被妥善存储"""
        question="What language did you first lean to speak?"
        my_survey=AnonymousSursey(question)
        my_survey.store_response('English')
        self.assertIn('English',my_survey.responses)
    def test_store_three_response(self):
        """测试三个答案会被妥善存储"""
        question = "What language did you first lean to speak?"
        my_survey = AnonymousSursey(question)
        responses=['English','Spanish','Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)
unittest.main()

#2.4方法setUp()
import unittest
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question="What language did you first lean to speak?"
        self.my_survey=AnonymousSursey(question)
        self.responses=['English','Spanish','Mandarin']
    def test_store_single_response(self):
        """测试单个答案会被妥善存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
    def test_store_three_response(self):
        """测试三个答案会被妥善存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, my_survey.responses)
unittest.main()
