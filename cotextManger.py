class Light:
    def __enter__(self):  # 들어가는 부분
        print("불을 켭니다")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("불을 끕니다.")


with Light():
    print("방에서 책을 읽습니다")
print("with 블럭 밖으로 나왔습니다.")
