from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')
import json
from scrapegraphai.graphs import SmartScraperGraph

url_req = []
@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        url_req = request.form['url_req']
        print(url_req)
        return render_template('index.html')
    else:
        return render_template('index.html')



"""
# Define the configuration for the scraping pipeline
graph_config = {
    "llm": {
        "model": "ollama/llama3.2",
	#"temperature": 0.1,
	"format": "json",
	#"model_tokens": 2000,
	#"base_url": "http://localhost:11434",
    },
    "verbose": True,
    "headless": False,
}


urlz = str(url_req)



# Create the SmartScraperGraph instance
smart_scraper_graph = SmartScraperGraph(
    prompt="get every post, get the url in html tag",
    source=urlz,
    config=graph_config
    )

# Run the pipeline
result = smart_scraper_graph.run()
print(json.dumps(result, indent=4))

"""
if __name__ == '__main__':
    app.run(debug=True)
