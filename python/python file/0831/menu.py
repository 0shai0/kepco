# #1번

# Q=input("메뉴를 확인하시겠습니까? : [예], [아니요]")
# yes=["예"]
# menu={"김밥":["원조김밥","소고기김밥","돈까스김밥"],"분식":["오뎅","잔치국수","라볶이"],"식사":["제육덮밥","오므라이스","된장찌개"],"국밥":["콩나물국밥","갈비탕","육개장"]}
# if Q in yes:
#     Key_list=list(menu.keys())
#     for key in Key_list:
#         print(key)
#         for List in menu[key]:
#             print(List)
#         print()

#2번
price={"원조김밥":2500,"소고기김밥":3500,"돈까스김밥":3500,"오뎅":4500,"잔치국수":6000,"라볶이":5000,"제육덮밥":6500,"오므라이스":6500,"된장찌개":6000,"콩나물국밥":6000,"갈비탕":7000,"육개장":7000}
Key_list2=list(price.keys())
payment = 0
bill_list=[]
cnt=0



while payment < 10000000:
    order=input("어떤 걸로 주문하시겠습니까? :")
    if order in Key_list2:
        Q2 = int(input("몇 개를 주문하시겠습니까? : [숫자만] "))
        found = 0
        for item in bill_list:
            if item[0] == order:
                item[1] += Q2 #item[1] = item[1] + Q2
                payment = price[order] * item[1]
                found = True
                break
        if not found:
            bill_list.append([order, Q2])
            payment = price[order] * Q2 + payment
        if payment < 9000000:
            print(bill_list, payment)
            pay=input("결제하시겠습니까? : [예], [아니요] ")
            answer=["예"]
            if pay in answer:
                pay2=input("[현금]으로 결제하시겠습니까? [카드]로 결제하시겠습니까?")
                answer2=["현금","지폐"]
                if pay2 in answer2:
                    answer3=int((input("현금은 얼마를 주시겠습니까? : [숫자만] ")))
                    print("결제")
                    print("잔액 : %d원" %(answer3-payment))
                    print("영수증")
                    print(bill_list,"%d원"%payment)
                    print("잔액 : %d원" %(answer3-payment))
                    break
                else:
                    print("결제")
                    print("결제금액 : %d원"%payment)
                    print("영수증")
                    print(bill_list,"%d원"%payment)
                    break
            else:
                print("추가 메뉴를 결정하신 후 다시 말씀해주시길 바랍니다")
        else:
            print("900만원을 초과해서 주문하실 수 없습니다")
            break
    else:
        print("메뉴판에 존재하지 않는 메뉴입니다")
        break