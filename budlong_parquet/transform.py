import duckdb
duckdb.sql("""
    COPY (
        SELECT DISTINCT
            session_id,
            session_date,
            customer_id,
            store_id,
            device_type,
            TRIM(browser_os) browser_os,  
            SPLIT_PART(TRIM(browser_os), ' ', 1) AS browser,
            SPLIT_PART(TRIM(browser_os), ' ', 2) AS os,
            session_purchase_made,
            session_duration_minutes,
            session_pages_visited,
            COALESCE(session_quality_score, avg(session_quality_score) OVER()) AS session_quality_score
        FROM output.parquet
    )
    TO 'LimpyoVersion.parquet'
    (FORMAT PARQUET);
""")

 #incase lang nay extra spaces sa browser_os column sir hehe (sa line 10)