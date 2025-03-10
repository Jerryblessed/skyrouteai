import os
import networkx as nx
import nx_arangodb as nxadb
import pandas as pd
import matplotlib.pyplot as plt
import io
from openai import AzureOpenAI
from langchain.chains import LLMChain
from langchain.chat_models import AzureChatOpenAI
from langchain.prompts import PromptTemplate

# Set up environment variables for ArangoDB
os.environ["DATABASE_HOST"] = "https://tutorials.arangodb.cloud:8529"
os.environ["DATABASE_USERNAME"] = "TUThqy2rf7vstghfr8wuhbc59"
os.environ["DATABASE_PASSWORD"] = "TUTpj1exghn8jutfpibxca2g"
os.environ["DATABASE_NAME"] = "TUT0pwg4agundai61ujmyjdu"

# Load credentials
DB_HOST = os.environ["DATABASE_HOST"]
DB_USERNAME = os.environ["DATABASE_USERNAME"]
DB_PASSWORD = os.environ["DATABASE_PASSWORD"]
DB_NAME = os.environ["DATABASE_NAME"]

# Azure OpenAI API details
API_BASE = "https://thisisoajo.openai.azure.com/"
MODEL = "gpt-4o"
API_KEY = "9I4UEJweVUdih04Uv8AXcAxs5H8jSQRfwaugcSQYHcI882wSpFvqJQQJ99BAACL93NaXJ3w3AAABACOGkv4f"
API_VERSION = "2023-06-01-preview"

# Load flight and airport data
def create_flight_graph():
    G = nx.DiGraph()
    
    airports_csv = """id,Name,City,Country,AirportID,CoordinatesX,CoordinatesY
    1,Goroka Airport,Goroka,Papua New Guinea,GKA,-6.081689834590001,145.391998291
    2,Madang Airport,Madang,Papua New Guinea,MAG,-5.20707988739,145.789001465
    """
    flights_csv = """airline,source_airport,source_airport_id,destination_airport,destination_airport_id
    2B,AER,2965,KZN,2990
    2B,ASF,2966,KZN,2990
    """
    
    # Read data into DataFrames
    airports_df = pd.read_csv(io.StringIO(airports_csv))
    flights_df = pd.read_csv(io.StringIO(flights_csv))
    
    # Add airport nodes
    for _, row in airports_df.iterrows():
        G.add_node(row["AirportID"], name=row["Name"], city=row["City"], 
                   country=row["Country"], coordinates=(row["CoordinatesX"], row["CoordinatesY"]))
    
    # Add flight edges
    for _, row in flights_df.iterrows():
        if row["source_airport_id"] in G and row["destination_airport_id"] in G:
            G.add_edge(row["source_airport_id"], row["destination_airport_id"], airline=row["airline"])
    
    return G, airports_df, flights_df

# Create the flight graph
G_nx, airports_df, flights_df = create_flight_graph()

# Store graph in ArangoDB
G_adb = nxadb.Graph(
    incoming_graph_data=G_nx,
    name="FlightGraph",
    arango_url=DB_HOST,
    username=DB_USERNAME,
    password=DB_PASSWORD,
    database_name=DB_NAME
)

def visualize_graph():
    print("🔍 Visualizing graph in ArangoDB...")
    for node in G_nx.nodes(data=True):
        print(f"Node: {node}")
    for edge in G_nx.edges(data=True):
        print(f"Edge: {edge}")

# Convert natural language to AQL
def nl_to_aql(nl_query):
    llm = AzureChatOpenAI(
        api_key=API_KEY,
        api_version=API_VERSION,
        base_url=f"{API_BASE}/openai/deployments/{MODEL}"
    )
    prompt = PromptTemplate.from_template("Convert this natural language query to AQL: {query}")
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(query=nl_query)

# Compute PageRank
def compute_pagerank():
    pr = nx.pagerank(G_nx, alpha=0.85)
    return sorted(pr.items(), key=lambda x: x[1], reverse=True)

# Find shortest flight route
def find_shortest_route(source, destination):
    try:
        path = nx.shortest_path(G_nx, source=source, target=destination, method="dijkstra")
        return path
    except nx.NetworkXNoPath:
        return f"No route found between {source} and {destination}."
    except nx.NodeNotFound as e:
        return f"Error: {e}"

# Plot flight network
def plot_flight_network():
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G_nx)
    nx.draw(G_nx, pos, with_labels=True, node_color="skyblue", edge_color="gray", node_size=3000, font_size=10)
    plt.title("Flight Network Visualization")
    plt.show()

if __name__ == "__main__":
    print("🚀 AI-Powered Flight Optimization System! 🚀")
    while True:
        print("\nOptions:")
        print("1️⃣ View flight network")
        print("2️⃣ Find shortest flight route")
        print("3️⃣ AI travel assistant")
        print("4️⃣ Compute PageRank")
        print("5️⃣ Convert NL to AQL query")
        print("6️⃣ Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            plot_flight_network()
        elif choice == "2":
            source = input("Enter source airport ID: ").strip()
            destination = input("Enter destination airport ID: ").strip()
            route = find_shortest_route(source, destination)
            print(f"✈️ Shortest route: {route}")
        elif choice == "3":
            user_prompt = input("Ask your AI travel assistant: ")
            response = nl_to_aql(user_prompt)
            print(f"🤖 AI Response: {response}")
        elif choice == "4":
            rankings = compute_pagerank()
            print(f"🔥 PageRank Influence Ranking: {rankings}")
        elif choice == "5":
            nl_query = input("Enter natural language query: ")
            aql_query = nl_to_aql(nl_query)
            print(f"📝 AQL Query: {aql_query}")
        elif choice == "6":
            print("Goodbye! Safe travels! ✈️")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 6.")
