# Traveling Salesman City-Tour Optimizer

🧭 A Python-based tool to find and visualize the shortest city tour route using the **Travelling Salesman Problem (TSP)** approach.

---

## 🚀 Features

- 📍 Reads city coordinates from a CSV
- 📐 Calculates distance matrix using the Haversine formula
- 🧠 Optimizes shortest path using Nearest Neighbour TSP algorithm
- 🌍 Plots route using `matplotlib`
- 🗺️ Outputs the route as a `.geojson` file for GIS apps

---

## 📁 File Structure

```

tsp\_city\_tour\_optimizer/
├── data/
│   └── places.csv           # Input city names with lat-long
├── output/
│   ├── route.geojson        # Output GeoJSON for map visual
│   └── route\_plot.png       # Plotted route image
├── src/
│   ├── distance.py          # Haversine formula to compute distances
│   ├── tsp\_solver.py        # Nearest Neighbour algorithm for TSP
│   └── tsp.py               # Main script to run the entire pipeline
├── requirements.txt         # Dependencies
└── README.md                # Project overview

````

---

## ⚙️ How It Works

1. **Load cities** from `places.csv`
2. **Compute distance matrix** using the Haversine formula
3. **Solve TSP** with a simple nearest neighbor approach
4. **Visualize the result** with matplotlib and export GeoJSON

---

## 📌 How to Run

```bash
# Clone this repo
git clone https://github.com/iamnaresh06/tsp_city_tour_optimizer.git
cd tsp_city_tour_optimizer

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the TSP Optimizer
python src/tsp.py
````

---

## 🧠 Algorithms & Modules Used

* `Haversine` Formula – for accurate distance between geo-coordinates
* `Nearest Neighbor TSP` – for finding an approximate shortest route
* `matplotlib` – for plotting the city route
* `csv`, `json`, `os`, `argparse` – for file handling and input/output management

---

## 📹 Project Video

In the video, I walk through:

* Project overview
* File structure & modules
* How the algorithm works
* How the final output looks visually
  🌐 [Project Video](https://youtu.be/YU9sP1mt6kE?si=lAz00jTzj7aSE_3v)

---

👤 **Author**  
**Reddy Naresh**  
🔗 [GitHub: @iamnaresh06](https://github.com/iamnaresh06)  
💼 [LinkedIn: iamnaresh06](https://www.linkedin.com/in/iamnaresh06)  
🌐 [Portfolio Website](https://reddynaresh.netlify.app/)
