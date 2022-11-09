#21900156 김예준 중간고사시험
book=[]#책리스트 저장
finish=False#끝났는지 확인
print("21900156 도서관")
while True:
    if finish:
        print("프로그램이 종료되었습니다.")
        break
    print("-"*20)
    print("#","list")
    print("#","delete")
    print("#","register")
    print("#","quit")
    print("-"*20)
    while True:
        menu= input("메뉴를 선택하시오.(정확하게 입력하시오) ")
        if menu=='list':
            print("-"*20)
            if len(book)==0:
                print("아직 아무 책도 등록되어있지 않습니다.")
            else:
                count =0
                for i in book:
                    count+=1
                    numbook='['+str(count)+']'
                    print(numbook,i)
            break
        elif menu == 'delete':
            print("-"*20)
            Dbook=input("삭제할 책번호나 책제목을 정확하게 입력해주세요. ")
            if Dbook.isdigit():
                Dbooknum=int(Dbook)
                if Dbooknum <=len(book):
                    check=input(book[Dbooknum-1]+"를 삭제하시려면 y를 입력해주세요. ")
                    if check=='y':
                        print(book[Dbooknum-1],"삭제가 성공적으로 되었습니다.")
                        book.remove(book[Dbooknum-1])
                    else:
                        print("삭제절차가 취소되었습니다. ")
                else:
                    print("잘못입력하셨습니다.")
            else:
                if Dbook in book:
                    book.remove(Dbook)
                    print(Dbook,"삭제가 성공적으로 완료되었습니다. ")
                else:
                    print("잘못입력하셨습니다.")
            break
        elif menu == 'register':
            print("-"*20)
            while True:
                Rbook=input("등록할 책 이름을 작성하시오. 만약 끝났다면, 엔터키를 눌러 메뉴로 돌아가시오. ")
                if Rbook =='':
                    break
                elif Rbook in book:
                    print("!!!이 책은 이미 리스트안에 있습니다!!!")
                    continue
                book.append(Rbook)
            break
        elif menu == 'quit':
            print("-"*20)
            finish=True
            break

        
        
