##놀이공원 입장료 성인은 10,000원 어린이는 8,000원 메서드에 input값(남은 돈이랑 성인 몇명 어린이 몇명) 체크후 들어갈수 있는지 값을 반환
## def/if 조건문 /연산식 input값으로
#A=어른의 수 C=어린아이의 수 M=지불한 돈 R=(가능,불가능)


def bill(A,C,M):
   T = A * 10000 + C * 8000
   if M>=T:
      print("yes")
   else:
      print("no")

   return

bill(1,1,20000)



