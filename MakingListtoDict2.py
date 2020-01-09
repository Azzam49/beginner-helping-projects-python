def make_dict(info):
    

    lst1 = info[::2]
    lst2 = info[1::2]
    
    content = {}
    #count = 0
    #while count < len(lst1) -1:

    for i in range(len(lst1)-1):
        content[lst1[i]] = lst2[i+1]
        
    print(content)



thelist = ['1', 'Aabhar', '2', 'Aabir', '3', 'Aaden', '4', 'Aadharv', '5',
           'Aadhav', '6', 'Aadhavan', '7', 'Aadhi', '8', 'Aadi', '9', 'Aadiev', '10',
           'Aadvik', '11', 'Aagm', '12', 'Aahil', '13', 'Aalam', '14', 'Aaliyan', '15', 'Aamir',
           '16', 'Aanav', '17', 'Aanay', '18', 'Aarav', '19', 'Aare', '20', 'Aari', '21', 'Aarish',
           '22', 'Aariv', '23', 'Aariz', '24', 'Aarmin', '25', 'Aarnav', '26', 'Aarohan', '27', 'Aaron','28',
           'Aarondeep', '29', 'Aaron-Grae', '30', 'Aarov', '31', 'Aarush', '32', 'Aarvin', '33', 'Aarya', '34',
           'Aaryan', '35', 'Aashay', '36', 'Aashiv', '37', 'Aasim', '38', 'Aavyan', '39', 'Aayaan', '40',
           'Aayan', '41', 'Aayansh', '42', 'Aayob', '43', 'Aayush', '44', 'Aazan', '45', 'Abanob', '46',
           'Abanoub', '47', 'Abbas', '48', 'Abbaz', '49', 'Abd', '50', 'Abdal-Kareem', '51', 'Abdallah', '52',
           'Abdalrahman', '53', 'AbdAlstar', '54', 'Abdelkader']


    
make_dict(thelist)

