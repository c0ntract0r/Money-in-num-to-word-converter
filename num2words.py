under_20 = ['զրո','մեկ','երկու','երեք','չորս','հինգ','վեց','յոթ','ութ','ինը','տաս'] 
tens = ['', 'տասն','քսան','երեսուն','քառասուն','հիսուն','վաթսուն','յոթանասուն','ութանասուն','իննսուն'] 
above_100 = {100: 'հարյուր',1000:'հազար', 1000000:'միլլիոն', 1000000000:'միլլիարդ'} 

#main logic start
def NumToWord(num): 
    if num <= 10: 
        return under_20[num]  
    elif num < 100: 
    	return tens[(int)(num/10)] + ('' if num%10==0 else '' + under_20[num%10])

    pivot = max([key for key in above_100.keys() if key <= num]) 
    return NumToWord((int)(num/pivot)) + ' ' + above_100[pivot] + ('' if num%pivot==0 else ' ' + NumToWord(num%pivot))
# Main logic end

val = float(input("Enter money value: "))
dec_point = int(val)
float_point = int(round(val - dec_point, 2) * 100)
print(NumToWord(dec_point), 'դրամ,', NumToWord(float_point), 'լումա.\n')

