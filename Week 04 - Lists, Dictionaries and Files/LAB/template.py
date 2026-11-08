"""
RECORD CHECK  -  my version
===========================

Name  : Mariya Midhat
Lane  :  AI    (delete two)
Date  : 17/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here

def check_record(value, limit):
    """Calculate the difference, percentage and status."""
    difference = value - limit
    percent = (value / limit) * 100

    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, difference, percent, status):
    """Print the report for one dataset."""
    print(f"Dataset: {label}")
    print(f"Difference: {difference}")
    print(f"Percentage: {percent:.2f}%")
    print(f"Status: {status}")
    print()



# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}


records = [
    {"label": "survey_2026", "value": 1187, "limit": 1200},
    {"label": "sales_2026", "value": 1500, "limit": 1400},
    {"label": "customers_2026", "value": 900, "limit": 1000}
]


#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.


print("AI & DATA SCIENCE - DATASET REPORT")
print("================================")

for record in records:
    difference, percent, status = check_record(
        record["value"], record["limit"]
    )

    print_report(
        record["label"], difference, percent, status
    )


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
