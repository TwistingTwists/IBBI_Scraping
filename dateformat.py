[ 364887, 119126, 28595, 5396, 5395, 5394, 5393, 5392, 5391, 5390, 5389, 5388, 5387, 5386, 5385, 5384, 5383, 5382, 5381, 5380, 5379 ] 

nclt_b_list = [ 5365, 5366, 5367, 5368, 5369, 5370, 5371, 5372, 5373, 5374, 5375, 5376, 5377, 5378, 119125, 36488 ]

nclt_bench_list = list(map(str,nclt_b_list))

 nclt_StatusofCause_dict = { 364886 : [364886] , 119125 : [119126] , 5377 : [28595] , 5378 : [5396,5395,5394] , 5376 : [5393,5392] , 5374 : [5391,5390] , 5372 : [5389] , 5370 :[5388] , 5368 : [5387], 5366 : [5386] , 5377: [5385] , 5373 : [5384], 5371 : [5383] , 5369 : [5382] , 5367 : [5381] , 5375 : [5380] , 5365 : [5379] } 



 https://nclt.gov.in/order-judgements?field_bench_target_id=5378&field_search_date_value_1%5Bmin%5D%5Bdate%5D=&field_search_date_value_1%5Bmax%5D%5Bdate%5D=&title=300&field_search_date_value%5Bvalue%5D%5Byear%5D=2018&field_name_of_petitioner_value=&field_name_of_respondent_value=&field_search_date_value%5Bvalue%5D%5Byear%5D=&advocate_name=&field_search_date_value%5Bvalue%5D%5Byear%5D=


dr = [
    datetime.date.fromordinal(ordinal) 
    for ordinal in range(
        start_date.toordinal(),
        end_date.toordinal(),
    )
]


toDateStr = lambda x : x.strftime('%d, %m, %Y').split(',')

toDateStr(dr[0])



https://nclt.gov.in/status-of-cause-list?field_date_value%5Bvalue%5D%5Bday%5D=2&field_date_value%5Bvalue%5D%5Bmonth%5D=4&field_date_value%5Bvalue%5D%5Byear%5D=2019&field_bench_target_id=5365&field_bench_court_target_id_entityreference_filter=5379