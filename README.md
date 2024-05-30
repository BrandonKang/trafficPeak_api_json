
# Request data from TrafficPeak using JSON format APIs

This is to get the TrafficPeak data using Python requests and Json modules.

Hydrolix provides a number of query interfaces that can be used to interact with the system.
You can query your Hydrolix cluster via HTTP at https://<your-hostname>/query:

$ curl -u "API_ID:API_PW" -XPOST https://${HDX_HYDROLIX_URL}/query -d 'SELECT count() FROM sample_project.sample_table'
2010

Note that most clusters have authentication enabled, so the above line requires user authentication. 
To query data, Hydrolix provides several options such as the ClickHouse client, JDBC driver, and Python library. 

This Python code utilizes HTTPS requests via Python's requests module, along with the json module, to format responses as JSON data. 
The original response is plain text-based. If you use an API client or monitoring tools, a JSON response would be a better fit.
This Python script executes a SQL query against an API endpoint, authenticates the request using HTTP Basic Authentication, and then formats the response data as JSON. 

Here’s a rough explanation of the code.
* The script imports necessary modules: requests for HTTP requests, json for JSON handling, argparse for command-line argument parsing, and os for environment variable access.
* API_URL is set from an environment variable which should contain the API endpoint URL.
* USERNAME and PASSWORD are also read from environment variables and are used for authentication.
* The script uses argparse to parse the command-line argument which is the SQL query to execute.
* It calls the execute_query function with the parsed query.

To run the script, you would use a command like..

* Define API URL and your credentials<br>
$ export API_URL="YOUR_API_URL"<br>
$ export API_USERNAME="YOUR_API_ID"<br>
$ export API_PASSWORD="YOUR_API_PASSWORD"<br>

$ python3 tp_api_json.py "SQL_QUERY_OF_YOURS"

This code is useful for querying a database or service via an API and outputting the results in a structured JSON format, 
Making it easier to integrate with other tools or scripts.


## Acknowledgements

 - [Hydrilix Query Data](https://docs.hydrolix.io/docs/python-library)
 - [via Python Library](https://docs.hydrolix.io/docs/python-library)


## Authors

- [@BrandonKang](https://github.com/BrandonKang)


## Demo

![Sample1](https://osaka-obj-storage.jp-osa-1.linodeobjects.com/tp_query_demo.jpg)



