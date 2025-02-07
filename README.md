# Iliad NLP Analysis and Character Interaction Graph

## Project Overview
This project is an interactive Natural Language Processing (NLP) system designed to analyze character interactions in *The Iliad*. It extracts relationships between characters, performs sentiment analysis, and visualizes interactions using a dynamic graph. Users can interact with the system via a web interface or through an API.

## Features
- **Character Frequency Analysis**: Counts character appearances in the text.
- **Relationship Extraction**: Identifies frequently co-occurring characters.
- **Sentiment Analysis**: Evaluates the sentiment of interactions involving a selected character.
- **Graph Visualization**: Displays character networks dynamically using NetworkX.
- **Web Interface**: Users explore interactions through a Streamlit dashboard.
- **API Access**: Developers can retrieve insights via a FastAPI-powered REST API.

## Technologies & Tools
| Component             | Technology Used  |
|----------------------|----------------|
| **NLP Processing**  | spaCy, NLTK, TextBlob |
| **Backend API**     | FastAPI, pydantic |
| **Web Interface**   | Streamlit, requests |
| **Graph Visualization** | NetworkX, Matplotlib |
| **Containerization** | Docker, Docker Compose |
| **Deployment**      | AWS / GCP / Azure (Optional) |

## Installation
### Prerequisites
- Python 3.8+
- pip / uv (for dependency management)
- Docker (for containerized execution)

### Setup
1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/iliad-nlp.git
   cd iliad-nlp
   ```
2. **Create a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the API**
   ```sh
   uvicorn main:app --reload
   ```
5. **Run the Web Interface**
   ```sh
   streamlit run app.py
   ```

## Usage
### Web Interface
1. Open the Streamlit app in a browser.
2. Input a character’s name.
3. View statistics, sentiment analysis, and interaction graphs.

### API Endpoints
- `GET /character/{name}` → Returns frequency, interactions, and sentiment data.
- `GET /graph/{name}` → Returns graph data in JSON format.

## Running with Docker
### Build and Run the Container
```sh
docker build -t iliad-nlp .
docker run -p 8000:8000 iliad-nlp
```

## Future Enhancements
- Use transformer-based models (BERT, GPT) for improved sentiment analysis.
- Enable interaction filtering by book or chapter.
- Extend analysis to other ancient texts like *The Odyssey*.
- Deploy to a cloud platform for public access.

## Source
The text of *The Iliad* is sourced from: [MIT Classics - The Iliad](http://classics.mit.edu//Homer/iliad.html)

## License
MIT License

## Author
[Piero] - Electronic and Automation Engineer

## Acknowledgments
- Homer for *The Iliad*
- NLP libraries and contributors

---
This project offers a full-stack NLP solution, allowing users to explore classical literature interactively through modern AI techniques. 🚀

