phone = "2025551212"

area = "(" + phone[:3] + ")"  
exchange = phone[3:6]          
line = phone[-4:]              

print(area + " " + exchange + "-" + line)
