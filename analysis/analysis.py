from Decryption.decryption import list_of_dangerous,list_of_not_dangerous







not_dangerous=list_of_not_dangerous
dangerous=list_of_dangerous


def percentage_of_danger(text):
    risk=0
    words=text.split(" ")
    count_words=len(words)
    print(type(words))
    print(words)
    for word in words:
        for wor in not_dangerous:
            if word==wor:
                risk+=1
        for wor in dangerous:
            if word==wor:
                risk+=2
    return risk/count_words





# print(dangerous)
# print(not_dangerous)
# print(percentage_of_danger(als.get_data_text('7c05613d7f4507be4a34fd1fff8947cf58817d749f52d7d11548b5c4250b5f51')))
        



