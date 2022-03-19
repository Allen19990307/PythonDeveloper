# 罗马数字的转换
# author:allen
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

def intToRoman(num):
        if(1 < num and  num < 5):
            print("I" * num)
        elif 5 <= num and num < 10:
            print("V"+"I" * (num - 5))
        elif 10 <= num and num < 50:
            X_index = num // 10
            V_index = (num % 10) // 5
            if V_index != 0:
                I_index = (num % 10) - 5
            else:
                I_index =  num % 10
            # print( str(X_index) +"_"+  str(V_index) +"_"+str(I_index) )
            print("X" * X_index + "V" * V_index + "I" * I_index)
        elif 50 <= num and num < 100:
            L_index = num // 50
            X_index = (num % 50)// 10
            V_index = (num % 10) // 5
            if V_index != 0:
                I_index = (num % 10) - 5
            else:
                I_index =  num % 10
            # print( str(X_index) +"_"+  str(V_index) +"_"+str(I_index) )
            print("L" * L_index + "X" * X_index + "V" * V_index + "I" * I_index)
        elif 100 <= num and num < 500:
            C_index = num // 100
            L_index = (num % 100) // 50
            X_index = (num % 50) // 10
            V_index = (num % 10) // 5
            if V_index != 0:
                I_index = (num % 10) - 5
            else:
                I_index = num % 10
            # print( str(X_index) +"_"+  str(V_index) +"_"+str(I_index) )
            print("C" * C_index +"L" * L_index + "X" * X_index + "V" * V_index + "I" * I_index)
        elif 500 <= num and num < 1000:
            D_index = num // 500
            C_index = (num % 500) // 100
            L_index = (num % 100) // 50
            X_index = (num % 50) // 10
            V_index = (num % 10) // 5
            if V_index != 0:
                I_index = (num % 10) - 5
            else:
                I_index = num % 10
            # print( str(X_index) +"_"+  str(V_index) +"_"+str(I_index) )
            print("D" * D_index + "C" * C_index +"L" * L_index + "X" * X_index + "V" * V_index + "I" * I_index)
        elif num > 1000:
            M_index = num // 1000
            D_index = (num % 1000) // 500
            C_index = (num % 500) // 100
            L_index = (num % 100) // 50
            X_index = (num % 50) // 10
            V_index = (num % 10) // 5
            if V_index != 0:
                I_index = (num % 10) - 5
            else:
                I_index = num % 10
            # print( str(X_index) +"_"+  str(V_index) +"_"+str(I_index) )
            print("M" * M_index + "D" * D_index + "C" * C_index +"L" * L_index + "X" * X_index + "V" * V_index + "I" * I_index)

if __name__ == '__main__':
    i = 4
    intToRoman(4)
    intToRoman(8)
    intToRoman(38)
    intToRoman(78)
    intToRoman(278)
    intToRoman(578)
    intToRoman(1578)
    # 算法：递归思想