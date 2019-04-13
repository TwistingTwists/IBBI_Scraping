
import datetime
# NCLT url
# field_bench_target_id = "5378"
# title = "300"
# year = "2018"


def make_nclt_url(bench, title, year):

    field_bench_target_id = bench
    title = title
    year = year

    nclt_url = "https://nclt.gov.in/order-judgements?field_bench_target_id=" + field_bench_target_id + "&field_search_date_value_1%5Bmin%5D%5Bdate%5D=&field_search_date_value_1%5Bmax%5D%5Bdate%5D=&title=" + title + \
        "&field_search_date_value%5Bvalue%5D%5Byear%5D=" + year + \
        "&field_name_of_petitioner_value=&field_name_of_respondent_value=&field_search_date_value%5Bvalue%5D%5Byear%5D=&advocate_name=&field_search_date_value%5Bvalue%5D%5Byear%5D="

    return nclt_url


nclt_url = make_nclt_url("5378", "300", "2018")


# Status Cause LIst
# yr = "2019"
# bench = "5378"
# sub_bench = "5394"
def toDateStr(x): return x.strftime('%d, %m, %Y').split(',')


dr = [
    datetime.date.fromordinal(ordinal)
    for ordinal in range(
        start_date.toordinal(),
        end_date.toordinal(),
    )
]


def make_nclt_StatusCauseurl(bench, sub_bench, year):
    yr = year
    bench = bench
    sub_bench = sub_bench
    [d, m, yr] = toDateStr(dr[0])

    nclt_StatusCauseList = "https://nclt.gov.in/status-of-cause-list?field_date_value%5Bvalue%5D%5Bday%5D=" + d + "&field_date_value%5Bvalue%5D%5Bmonth%5D=" + \
        m + "&field_date_value%5Bvalue%5D%5Byear%5D=" + yr + "&field_bench_target_id=" + \
            bench + "&field_bench_court_target_id_entityreference_filter=" + sub_bench
    return nclt_StatusCauseList


nclt_StatusCauseList = make_nclt_StatusCauseurl("5378", "5394", "2019")
