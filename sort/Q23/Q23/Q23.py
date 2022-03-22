
if __name__=="__main__":

    """
    input:학생수 n
          이름 국어점수 영어점수 수학점수

    조건:  국어점수 감소
           국어점수가 같으면 영어 점수 증가
           국어 영어점수가 같으면 수학 감소
           모두 같으면 사전순

    output: 이름
    """
    #https://wangin9.tistory.com/entry/python-list-of-class-sort-by-attribute
    #클래스를 이용해 정렬
    #input
    n=12

    class Student:
        def __init__(self, name ,korean ,english ,math):
            self.name=name
            self.korean=korean
            self.english=english
            self.math=math
        def __repr__(self):
            return repr((self.name))
            #return repr((self.name, self.korean,self.english,self.math))
        def __lt__(self, other):
            #국어 점수가 다른 경우
            if self.korean!=other.korean:
                return self.korean>other.korean
            #국어 점수는 같고, 영어 점수가 다른 경우
            elif self.english!=other.english:
                return self.english<other.english
            #국어,영어 점수는 같고 수학 점수가 다른 경우
            elif self.math!=other.math:
                return self.math>other.math
            #세 점수가 다 같은 경우
            else:
                return self.name<other.name
    student=[
        Student("Junkyu",50,60,100),
        Student("Sangkeun",80,60,50),
        Student("Sunyoung",80,70,100),
        Student("Soong",50,60,90),
        Student("Haebin",50,60,100),
        Student("Kangsoo",60,80,100),
        Student("Donghyuk",80,60,100),
        Student("Sei",70,70,70),
        Student("Wonseob",70,70,90),
        Student("Sanghyun",70,70,90),
        Student("nsj",80,80,80),
        Student("Taewhan",50,60,90),

        ]

    sorted_student=sorted(student)
    #print(sorted_student)
    for i in sorted_student:
        print(i.name)