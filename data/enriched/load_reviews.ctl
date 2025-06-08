LOAD DATA
INFILE *
INTO TABLE review_stage
APPEND
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
TRAILING NULLCOLS
(
    bank_name,
    review_text,
    rating,
    sentiment,
    review_date "TO_DATE(:review_date, 'YYYY-MM-DD')"
)

BEGINDATA
