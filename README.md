# SkyRoute AI - Flight Optimization System

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Jerryblessed/fraudShieldgraphai/blob/main/fdetect.ipynb)

## 🚀 Inspiration

Air travel optimization is crucial for efficiency, sustainability, and cost-effectiveness. We wanted to build a system that simplifies route planning, enhances decision-making, and integrates AI for smarter travel insights. Inspired by real-world airline challenges, SkyRoute AI leverages graph-based analytics to optimize flight paths dynamically.

## ✈️ What it does

SkyRoute AI processes flight and airport data using graph-based network analysis, allowing users to:

- Visualize flight routes and airport connections in ArangoDB.
- Find the shortest and most efficient routes between airports.
- Compute PageRank to determine the most influential airports.
- Use AI-powered NLP to AQL translation for querying flight data effortlessly.
- Integrate real-time graph visualization to display network structures.

## 🏗️ Architectural Diagram

```
+--------------------+      +---------------------+
|  User Interface   | ---> |  Flask API Server   |
+--------------------+      +---------------------+
            |                      |
            v                      v
+---------------------+      +--------------------+
|    Azure OpenAI    |      |    ArangoDB       |
| (NLP to AQL Query) |      | (Graph Storage)  |
+---------------------+      +--------------------+
            |                      |
            v                      v
+--------------------+      +--------------------+
|      NetworkX     |      |      cuGraph      |
| (Graph Analysis)  |      |  (GPU Acceleration)|
+--------------------+      +--------------------+
```

## 💻 How we built it

- **NetworkX & cuGraph** for graph-based computation and shortest path analysis.
- **ArangoDB** for storing and visualizing flight network data.
- **Azure OpenAI (GPT-4o)** for NLP-based AQL query generation.
- **Flask API & Web Interface** for user interaction and query execution.
- **Matplotlib & DataFrames** for plotting and analyzing flight route data.
- **LangChain** for AI-driven query interpretations.

## 📥 Dataset

The dataset is sourced from [ArangoDB Example Datasets](https://github.com/arangodb/example-datasets/tree/master/Data%20Loader).

## 🚫 Challenges we ran into

- Optimizing large-scale graph processing efficiently with GPU acceleration.
- Converting natural language queries to accurate AQL statements.
- Ensuring real-time data visualization while handling complex computations.
- Managing ArangoDB integration with NetworkX and cuGraph.

## 🎉 Accomplishments that we're proud of

- Successfully integrated AI-powered NLP with AQL for intuitive user queries.
- Achieved high-speed graph processing using GPU acceleration with cuGraph.
- Built an interactive flight network visualization inside ArangoDB.
- Developed a fully functional Flask-based API for flight route optimization.

## 📝 What we learned

- The power of graph databases for real-world travel optimization.
- The efficiency gains from using cuGraph for GPU-accelerated graph operations.
- How NLP-driven AI can simplify complex query languages like AQL.
- The importance of data visualization in interpreting large datasets.

## 🌟 What's next for SkyRoute AI

- Real-time flight tracking integration for live travel updates.
- Machine learning-based demand forecasting for optimized flight schedules.
- Multi-modal transport integration (e.g., trains, buses) for seamless travel planning.
- User-friendly web dashboard for airline companies and travelers.
- Cloud-based API services for external applications and travel platforms.

## 🛠️ Built With

- **Python**
- **NetworkX & cuGraph**
- **ArangoDB**
- **Azure OpenAI & LangChain**
- **Flask & Matplotlib**
