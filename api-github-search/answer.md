**Q1: Role of query parameters in this request**
Query parameters (`q`, `sort`, `order`, `per_page`) are used to customize the API request.  
- `q` specifies the search keyword ("python").  
- `sort` decides the sorting criteria (stars).  
- `order` sets the direction (descending).  
- `per_page` limits the number of results (5).  
They allow us to control what data we get back from the API.

**Q2: Why use `response.json()` instead of `response.text`?**
- `response.json()` converts the API response into a Python dictionary, making it easy to access keys like `"items"`.  
- `response.text` gives raw string data, which would require manual parsing.  
Since the GitHub API returns JSON, using `.json()` is the most efficient way to handle the data.