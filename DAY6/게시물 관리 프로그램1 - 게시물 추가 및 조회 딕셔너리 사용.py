# 게시판 명령어 입력 : help
# add : 게시물 추가
# list : 게시물 목록 조회


# 게시판 명령어 입력 : list
# ==========  게시물 목록  ===========
# =================================== 

# 게시판 명령어 입력 : add

# 제목을 입력해주세요 : aaa
# 내용을 입력해주세요 : aaa

# 게시물이 등록되었습니다.

# 게시판 명령어 입력 : add

# 제목을 입력해주세요 : bbb
# 내용을 입력해주세요 : bbb

# 게시물이 등록되었습니다.

# 게시판 명령어 입력 : add

# 제목을 입력해주세요 : ccc
# 내용을 입력해주세요 : ccc

# 게시물이 등록되었습니다.

# 게시판 명령어 입력 : list

# ==========  게시물 목록  ===========
# 번호 : 1    제목 : aaa    내용 : aaa
# 번호 : 2    제목 : bbb    내용 : bbb
# 번호 : 3    제목 : ccc    내용 : ccc
# ====================================

num=0
list1=[]
while True:
    print("")
    command=input("게시판 명령어 입력 : ")
    print("")
    if command=="help":
        print("add : 게시물추가")
        print("list : 게시물조회")
    elif command=="add":
        title=input("제목을 입력해주세요 :")
        body=input("내용을 입력해주세요 :")
        num+=1
        dic1={"번호":num,"제목":title,"내용":body}
        list1.append(dic1)
        print("게시물이 등록되었습니다.")
    elif command=="list":
        print("========== 게시물목록 ==========")
        for a in range(num):
            print("번호 : {}  제목 : {}  내용 : {}".format(list1[a]["번호"],list1[a]["제목"],list1[a]["내용"]))
        print("=================================")
    
        
