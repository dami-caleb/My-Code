#A set can not contain the same data twice

storage = set() #This how to create an empty set

parameters= ["INFORMATION WE COLLECT","COOKIES", "INFORMATION", "SECURITY”, THIRD-PARTY", "AFFILIATED"]

message = """purposes. These purposes include to store and/or access information on a device, like cookie management and to process personal data such as standard information sent by a device and other unique identifiers for personalised ads and content, ad and content measurement, audience insights and product development. With your consent we and our partners may use precise geolocation data and actively scan device characteristics for identification.

You may consent to the processing described above or access more"""

words_in_message = message.split()

for word in words_in_message:
    if str.upper(word) in parameters:
        storage.add(word)
print(storage)

#As you may have noticed "information" is presnt in words_in_message 3 times but it is only shown in the set once
#Set is good for a yes or non search
#
    