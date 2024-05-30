
# Request data from TrafficPeak using JSON format APIs

This is to get the TrafficPeak data using Python requests and Json modules.

Hydrolix provides a number of query interfaces that can be used to interact with the system.
You can query your Hydrolix cluster via HTTP at https://<your-hostname>/query:

Example)
```bash
$ curl -u "API_ID:API_PW" -XPOST https://${HDX_HYDROLIX_URL}/query -d 'SELECT count() FROM sample_project.sample_table'
2010
```


Note that most clusters have authentication enabled, so the above line requires user authentication. 
To query data, Hydrolix provides several options such as the ClickHouse client, JDBC driver, and Python library. 

This Python code utilizes HTTPS requests via Python's requests module, along with the json module, to format responses as JSON data. 
The original response is plain text-based. If you use an API client or monitoring tools, a JSON response would be a better fit.
This Python script executes a SQL query against an API endpoint, authenticates the request using HTTP Basic Authentication, and then formats the response data as JSON. 

Here’s a rough explanation of the code:
* The script imports necessary modules: requests for HTTP requests, json for JSON handling, argparse for command-line argument parsing, and os for environment variable access.
* API_URL is set from an environment variable which should contain the API endpoint URL.
* USERNAME and PASSWORD are also read from environment variables and are used for authentication.

* Function execute_query(query) takes a SQL query as an argument.
* The function extracts column names from the SQL query by parsing the SELECT clause.
* It sends the query to the API using an HTTP POST request with basic authentication.

If the response status is 200 (OK), it processes the response:
- The response text is split into lines.
- Each line represents a row of data, which is split into individual values.
- A dictionary is created for each row by mapping column names to values.
- The dictionaries are collected into a list, which is then converted to a JSON-formatted string.
- The JSON data is printed.
- If the response status is not 200, it prints an error message with the status code.

* The script uses argparse to parse the command-line argument which is the SQL query to execute.
* It calls the execute_query function with the parsed query.

This code is useful for querying a database or service via an API and outputting the results in a structured JSON format, 
Making it easier to integrate with other tools or scripts.




## Acknowledgements

 - [Hydrilix Query Data](https://docs.hydrolix.io/docs/python-library)
 - [via Python Library](https://docs.hydrolix.io/docs/python-library)


## Authors

- [@BrandonKang](https://github.com/BrandonKang)


## Demo
To run the script, you would use a command like..

Define API URL and your credentials<br/>
```bash
$ export API_URL="YOUR_API_URL"
$ export API_USERNAME="YOUR_API_ID"
$ export API_PASSWORD="YOUR_API_PASSWORD"

$ python3 tp_api_json.py "SQL_QUERY_OF_YOURS"
```
![Sample1](https://osaka-obj-storage.jp-osa-1.linodeobjects.com/tp_query_demo.jpg)
