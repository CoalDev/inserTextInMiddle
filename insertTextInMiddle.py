# This function takes 2 params: an Array and a String
# The array is the string but split to an array [arr.split()]
# @author: Lior
# @date: 2.4.2020
def insertText(arr, word):
    # This is the final string that will be returned
    finalString = ''

    # because we double the size of the string
    # we loop it 2x the length of the array we are given
    for i in range((len(arr)*2)):
        # because we decide to put the word after the first word
        # we check if the word is not in a odd position
        if i%2 == 0:
            # Adding to the finalString the word from the array
            finalString += arr[int(i/2)]
        else:
            # Adding to the finalString the word that was wanted
            finalString += word
            
    # Finally returning the finalString
    return finalString