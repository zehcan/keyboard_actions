#*************************************
#function for shifting q-keyboard keys
#*************************************
def shift(nShiftNumber, sShiftKey):

    #definition of keyboard, simple solution, just keep them in array. For large files processing array would not be the best solution of course
    keyboard_string_array = ["1","2","3","4","5","6","7","8","9","0","q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l",";","z","x","c","v","b","n","m",",","."]

    # used ascii codes to conttol the keyboard range
    if  (ord(sShiftKey) >= 97 and ord(sShiftKey) <= 122) or (ord(sShiftKey) >= 48 and ord(sShiftKey) <= 57) or ord(sShiftKey) == 46 or ord(sShiftKey) == 59 or ord(sShiftKey) == 47 or ord(sShiftKey) == 44:
        index_ShiftKey = keyboard_string_array.index(sShiftKey)
        if index_ShiftKey + nShiftNumber < 0 or index_ShiftKey + nShiftNumber > 39:
            return "ERROR"
        return keyboard_string_array[index_ShiftKey + nShiftNumber]
    else:
        return sShiftKey

#*************************************
#main block of the file operation
#*************************************
try:

    #Getting file inputs
    print "Type the filename of the parameter file: "
    file_parameter = raw_input("> ")

    print "Type the filename of the text file: "
    file_text = raw_input("> ")

    #Reading parameters
    txt_parameter = open(file_parameter)
    array_parameter = txt_parameter.read().split(",")

    #Assign blank to the text variable
    text = ""
    for param in array_parameter:
        txt_text = open(file_text, 'r')
        lines = txt_text.readlines()
        txt_text.close()
        for line in lines:
            for c in line:
                text = text + shift(int(param), c)
        print text

        #swaping the result text to the file, can be developed with swapping file without changing the original file.
        txt_text = open(file_text, 'w')
        txt_text.write(text)
        txt_text.close()
        text = ""

except ValueError:
    print("Error")
