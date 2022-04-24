from pkg_resources import safe_extra


counties_dict = {}

counties_dict['Arapahoe'] = 422829
counties_dict['Denver'] = 463353
counties_dict['Jefferson'] = 432438
print(counties_dict)

voting_data = []

voting_data.append({'county':'Arapahoe', 'registered_voters': 422829})
voting_data.append({'county':'Denver', 'registered_voters': 463353})
voting_data.append({'county':'Jefferson', 'registered_voters':432438})

print(voting_data)