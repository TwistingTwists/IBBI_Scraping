# IBBI_Scraping

## for Status Cause List, the file :

#### filename : StatusCause_resume.py

###### commands :

1. `python StatusCause_resume.py --start-date "01 01 2019" --end-date "02 01 2019" --filename Jan_2`

> ####### explanation :

    --start-date "01 01 2019" = in `dd mm yyyy` format
    --end-date "02 01 2019" = in `dd mm yyyy` format
    --filename Jan_2 = Anycustom filename (without spaces. i.e. `fil name` is not valid. but `filname` is valid)

2.  `python StatusCause_resume.py --start-date "01 01 2019" --end-date "02 01 2019" --filename Jan_2 --bb=5378`

    > ####### explanation :

        --bb = bench name

3.  `python StatusCause_resume.py --start-date "01 01 2019" --end-date "02 01 2019" --filename Jan_2 --bb=5378 --ss=5395`

> ####### explanation :

    --ss = sub bench within bench name (must have `--bb` as option.)

---

## for IBBI, the file :

#### filename : ibbi.py

1. `python ibbi.py --query "a" --ann 2 --filename outp --lastPage 4`

> --ann 1 = "Public+Announcement+of+Corporate+Insolvency+Resolution+Process"
> --ann 2 : "Public+Announcement+of+Liquidation+Process",
> --ann 3: "Public+Announcement+of+Voluntary+Liquidation+Process",
