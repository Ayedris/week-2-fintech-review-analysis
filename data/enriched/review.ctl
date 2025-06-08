OPTIONS (SKIP=1)
LOAD DATA
INFILE *
INTO TABLE review_stage
APPEND
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
TRAILING NULLCOLS
(
  review_text,
  rating,
  review_datetime DATE "YYYY-MM-DD HH24:MI:SS",
  bank_name,
  source,
  cleaned_text,
  sentiment_score,
  sentiment_label,
  keywords
)
