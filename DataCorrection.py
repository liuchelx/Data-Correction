# issues:

# True/true vs true/false
# null vs None
# double quotation

import json


with open('./data.json', 'r') as json_file:
    data = json.load(json_file)
    for each in data['data']:
        each['_id'] = each['_id'][1::2]





# 1. generate an list of _ids, which has inconsistent data:  0 (we want them be stored as boolean)

for jsonCount in data['data']:

	for i in jsonCount["options"]:

		if type(jsonCount['options'][i]) is not bool:
			if jsonCount['options'].get(i,'True') == 0:
				jsonCount['options'][i] = False
			elif jsonCount['options'].get(i,'True')  == 1:
				jsonCount['options'][i] = True
			

for jsCount in data['data']:

	if jsCount['options'] != {} and jsCount['options'].has_key('enable_cancel_notification'):
		if jsCount['options']['enable_cancel_notification'] ==True and jsCount['options']['enable_new_user_notification'] ==True and jsCount['options']['enable_renewal_notification'] ==True:
			jsCount['options']['enable_all_notification'] = True	
		if jsCount['options']['enable_cancel_notification'] ==False or jsCount['options']['enable_new_user_notification'] ==False or jsCount['options']['enable_renewal_notification'] ==False:
			jsCount['options']['enable_all_notification'] = False	


print(json.dumps(data, sort_keys=True, indent=4))
                                                                                                                                                                                                                                                       
# 2. correct data by rule:
# if all of "enable_cancel_notification", "enable_new_user_notification",           "enable_renewal_notification" are True  then change "enable_all" to True

# if any one of "enable_cancel_notification", "enable_new_user_notification",           "enable_renewal_notification" are False, then change "enable_all" to False
