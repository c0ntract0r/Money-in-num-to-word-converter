under_20 = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen'] 
tens = ['', '','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety'] 
above_100 = {100: 'Hundred',1000:'Thousand', 1000000:'Million', 1000000000:'Billion'} 

#main logic start
def NumToWord(num): 
    if num < 20: 
        return under_20[num]  
    elif num < 100: 
    	return tens[(int)(num/10)] + ('' if num%10==0 else ' ' + under_20[num%10])

    pivot = max([key for key in above_100.keys() if key <= num]) 
    return NumToWord((int)(num/pivot)) + ' ' + above_100[pivot] + ('' if num%pivot==0 else ' ' + NumToWord(num%pivot))
# Main logic end

val = float(input("Enter money value: "))
dec_point = int(val)
float_point = int(round(val - dec_point, 2) * 100)
print(NumToWord(dec_point), 'dollars,', NumToWord(float_point), 'cents.\n')

