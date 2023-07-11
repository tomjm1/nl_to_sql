"""
/* Context */
You are an sql expert. The sql table is page_events with the Fields: project_id, timestamp, session_id, country, city, browser, operating_system, path.
The field timestamp is in epoch format.
"""
from fetch_data import fetch_data
from main import run_prompt
import time

schema = """
CREATE TABLE page_events (
    id INTEGER PRIMARY KEY,
    project_id INTEGER,
    timestamp INTEGER,
    session_id TEXT,
    country TEXT,
    city TEXT,
    browser TEXT,
    operating_system TEXT,
    path TEXT
)
"""

"""
Question: How many visitors in the last month for the project id 1234?
Answer: 
SELECT
  timestamp,
    COUNT(*) AS count
  FROM
   page_events
  WHERE
    project_id = '1234'
    AND toDate(toDateTime(timestamp / 1000 + 10800)) BETWEEN '2023-06-01' AND '2023-07-01'
  GROUP BY
    timestamp
  ORDER BY
    count ASC;
"""


print("\n\n######## Scenario 1  ######## ")
sql1 = """
SELECT
  COUNT(DISTINCT session_id) AS count
FROM
  page_events
WHERE
  project_id = 10
  AND date(timestamp, 'unixepoch') BETWEEN '2023-06-11' AND '2023-07-11';
"""
prompt1="How many unique visitors in the last month  from now for the project id 10?"
actual = fetch_data(sql1)
predicted = run_prompt(schema,prompt1)
print("actual",actual)
print("predicted",predicted)
# Wait for 1 minute
time.sleep(60)


print("\n\n######## Scenario 2  ######## ")
"""
Question: How many visitors visited the website yesterday for the project id 10?
Answer:
SELECT COUNT(DISTINCT session_id) AS unique_visitors
FROM page_events
WHERE 
project_id = 10
AND toDate(toDateTime(timestamp / 1000 + 10800)) = yesterday()
"""
sql2 = """SELECT COUNT(DISTINCT session_id) AS unique_visitors
FROM page_events
WHERE 
project_id = 10
AND date(timestamp, 'unixepoch') = date('now', '-1 day')"""
prompt2="How many unique visitors visited the website yesterday for the project id 10?"
actual = fetch_data(sql2)
predicted = run_prompt(schema,prompt2)
print("actual",actual)
print("predicted",predicted)
# Wait for 1 minute
time.sleep(60)


print("\n\n######## Scenario 3  ######## ")
"""
Question: Which browser is the most commonly used by visitors for the project id 10?
SELECT browser, COUNT(*) AS count
FROM page_events
WHERE project_id = 10
GROUP BY browser
ORDER BY count DESC
LIMIT 1
"""
sql3 = """SELECT browser, COUNT(*) AS count
FROM page_events
WHERE project_id = 10
GROUP BY browser
ORDER BY count DESC
LIMIT 1
"""
prompt3="Which browser is the most commonly used by visitors for the project id 10?"
actual = fetch_data(sql3)
predicted = run_prompt(schema,prompt3)
print("actual",actual)
print("predicted",predicted)
# Wait for 1 minute
time.sleep(60)


print("\n\n######## Scenario 4  ######## ")
"""
Question: What is the average session duration for each operating system for the project id 10?
Answer: SELECT operating_system, AVG(session_timestamp) AS avg_session_duration
FROM page_events
WHERE project_id = 10
GROUP BY operating_system
"""
sql4 = """SELECT operating_system, AVG(timestamp) AS avg_session_duration
FROM page_events
WHERE project_id = 10
GROUP BY operating_system
"""
prompt4="What is the average session duration for each operating system for the project id 10"
actual = fetch_data(sql4)
predicted = run_prompt(schema,prompt4)
print("actual",actual)
print("predicted",predicted)
# Wait for 1 minute
time.sleep(60)


print("\n\n######## Scenario 5  ######## ")
"""
Question: How many visitors came from each country during the last week for the project id 10?
Answer:
SELECT country, COUNT(DISTINCT session_id) AS visitors_count
FROM page_events
WHERE project_id = 10
AND toDate(toDateTime(timestamp / 1000 + 10800)) >= today() - 7
GROUP BY country
"""
sql5="""SELECT country, COUNT(DISTINCT session_id) AS visitors_count
FROM page_events
WHERE project_id = 10
AND date(timestamp, 'unixepoch') >= date('now', '-7 days')
GROUP BY country"""
prompt5="How many visitors came from each country during the last week for the project id 10"
actual = fetch_data(sql5)
predicted = run_prompt(schema,prompt5)
print("actual",actual)
print("predicted",predicted)
# Wait for 1 minute
time.sleep(60)



print("\n\n######## Scenario 6  ######## ")
"""
Question: Which path/page received the most visits for a specific project ID 10?
Answer:
SELECT path, COUNT(*) AS visit_count
FROM page_events
WHERE project_id = 10
GROUP BY path
ORDER BY visit_count DESC
LIMIT 1
"""
sql6="""SELECT path, COUNT(*) AS visit_count
FROM page_events
WHERE project_id = 10
GROUP BY path
ORDER BY visit_count DESC
LIMIT 1"""
prompt6="Which path/page received the most visits for a specific project ID 10?"
actual = fetch_data(sql6)
predicted = run_prompt(schema,prompt6)
print("actual",actual)
print("predicted",predicted)