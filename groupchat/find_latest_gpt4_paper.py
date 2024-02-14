# filename: find_latest_gpt4_paper.py
import feedparser

# Define the base URL for the arXiv API
ARXIV_API_URL = "http://export.arxiv.org/api/query?"

# Define the search query parameters
search_query = "all:GPT-4"
start = 0
max_results = 1
sortBy = "submittedDate"
sortOrder = "descending"

# Construct the query URL
query = f"search_query={search_query}&start={start}&max_results={max_results}&sortBy={sortBy}&sortOrder={sortOrder}"
url = ARXIV_API_URL + query

# Fetch the feed data from arXiv
feed = feedparser.parse(url)

# Check if any entries were found
if feed.entries:
    paper = feed.entries[0]
    print(f"Title: {paper.title}")
    print(f"Authors: {', '.join(author.name for author in paper.authors)}")
    print(f"Published: {paper.published}")
    print(f"Summary: {paper.summary}")
    print(f"Link: {paper.link}")
else:
    print("No papers found on GPT-4.")

# Please note that this will provide the latest paper. To get potential applications, a manual review of the paper is required.