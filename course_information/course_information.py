dic_id = {101 : [3004, 'Haynes', '8:00 AM'],102 : [4501, 'Alvarado', '9:00 AM'],103 : [6755, 'Rich', '10:00 AM'],110 : [1244, 'Burke', '11:00 AM'],241 : [1411, 'Lee', '1:00 PM']}
id =int(input("Please enter the ID:"))
if id not in dic_id:
    print("Invalid ID")
else:
    print("Room number:" + str(dic_id[id][0]) + " Instructor:" + dic_id[id][1] + " Meeting Time:" + dic_id[id][2])