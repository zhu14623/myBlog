# -*- coding: UTF-8 -*-

def get_post_data(request):

    strs=''
    content_type_table =['application/json','application/x-www-form-urlencoded']
    content_type=request.headers.get("Content-Type")

    if content_type not in content_type_table:
        strs='An alternative way of submitting data'

    if content_type ==content_type_table[0]:
        return request.json,strs
    elif content_type ==content_type_table[1]:
        return request.form.to_dict(),strs   
    else:
        return request.form.to_dict(),strs