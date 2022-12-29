print("Bạn đang ở trong một căn phòng tối tăm nằm trong một lâu đài bí hiểm.")
import random
exitChoice = "Không có gì"
while exitChoice != "Thoát":
    print("Có 4 cánh cửa trước mặt bạn. Hãy chọn 1 cánh cửa để thoát hiểm.")
    playerChoice = input("Hãy chọn 1,2,3 hoặc 4...")
    if playerChoice == "1":
        print("Bạn đã tìm thấy căn phòng chứa kho báu. Phát tài rồi!")
        print("Bạn đã thắng cuộc. Trò chơi kết thúc.")
    elif playerChoice == "2":
        print("Cửa bật mở. Một tiểu yêu giận dữ lao ra tấn công bạn.")
        print("Bạn có thể:")
        print("1) Tìm cách chạy thoát")
        print("2) Ở lại chiến đấu")
        monsterChoice = input("Chọn 1 hoặc 2...")
        if monsterChoice == "1":
            print("Bạn đã tìm thấy 1 lối nhỏ để thoát khỏi lâu đài. Chúc mừng bạn đã tự do")
            print("Bạn đã chiến thắng! Trò chơi kết thúc")
        elif monsterChoice == "2":
            print("Con yêu tinh tiến đến phan chùy vào đầu bạn")
            print("*ponk...ponk...")
            print("Bạn đã thua. Trò chơi kết thúc!")
        else:
            print("Xin lỗi, bạn phải chọn 1 hoặc 2.")
    elif playerChoice == "3":
        print("Bạn bước vào phòng và thấy 1 con rồng đang ngủ say.")
        print("Bạn có thể:")
        print("1) Thử trộm vàng của con rồng.")
        print("2) Thử đi vòng qua rồng để tới cửa ra.")
        dragonChoice = input("Chọn 1 hoặc 2...")
        if dragonChoice == "1":
            print("Con rồng thức giấc và nuốt chửng bạn luôn. Ái chà chà ngon quá!")
            print("Bạn đã thua! Trò chơi kết thúc.")
        elif dragonChoice == "2":
            print("Bạn rón rén đi qua con rồng và thoát khỏi tòa lâu đài. Xin chào ánh mặt trời!")
            print("Bạn đã chiến thắng! Trò chơi kết thúc!")
        else:
            print("Xin lỗi, bạn phải chọn 1 hoặc 2.")
    elif playerChoice == "4":
        print("Căn phòng bạn bước vào có 1 con nhân sư.")
        print("Nhân sư bắt bạn đoán được con số nó đang nghĩ đến, số đó nằm trong khoảng từ 1 đến 10.")
        number = int(input("Bạn chọn số nào?"))
        import random
        if number == random.randint(1,10):
            print("Nhân sư gầm lên đầy thất vọng. Bạn đã đoán đúng.")
            print("Nhân sư phải thả bạn đi.")
            print("Bạn đã chiến thắng. Trò chơi kết thúc.")
        else:
            print("Nhân sư nói đáp án của bạn không chính xác.")
            print("Bạn đã trở thành tù nhân của nó mãi mãi.")
            print("Bạn đã thua. Trò chơi kết thúc.")
    else:
        print("Xin lỗi, bạn đã không lựa chọn 1,2,3 hoặc 4")
    exitChoice = input("Ấn Enter để chơi lại, hoặc gõ THOÁT để đóng trò chơi.")
