
# **Influenza Visualization**

## **Overview**
This project focuses on understanding the relationship between **temperature changes** and **influenza dynamics** in Australia using interactive narrative visualizations. By analyzing data from 2008 to 2022, it provides insights into how temperature variations impact influenza outbreaks in different Australian states.

### **Target Audience**
- **Public Health Experts**: Develop prevention measures based on the findings.
- **Policymakers**: Formulate relevant policies.
- **General Public**: Enhance understanding of influenza and take preventive actions.

### **Data Sources**
1. **Temperature Data**: Bureau of Meteorology’s ACORN-SAT dataset (1910-2022).
2. **Influenza Case Data**: National Notifiable Diseases Surveillance System (2008-2022).

---

## **Features**
### **1. Visualization Types**
- **Heat Maps**: Display temperature variations across states and time.
- **Line Charts**: Show temperature trends over time for different states.
- **Stacked Bar Charts**: Visualize virus type and age group distribution.
- **Bubble Charts**: Explore the relationship between temperature, time, and influenza cases.

### **2. Interactive Features**
- **Sliders**: Select specific years, months, or dates.
- **Tooltips**: View detailed information by hovering over charts.
- **Checkboxes**: Filter data by states or virus types.

### **3. Design Choices**
- **Colors**:
  - Heat maps and bubble charts: Blue/green for lower temperatures, red/yellow for higher.
  - Line charts: Different colors for state-level trends.
  - Stacked bar charts: Contrasting colors for virus types.
- **Typography**: Uniform font style for consistency and readability.
- **Layout**: Clean and organized, with centrally aligned text and images.

---

## **How to Use**
### **Run Locally**
1. Clone the repository:
   ```bash
   git clone https://github.com/fangyu-sun/Influenza-Visualization.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Influenza-Visualization
   ```
3. Start a local HTTP server:
   ```bash
   python3 -m http.server 8000
   ```
4. Open your browser and access:
   ```
   http://localhost:8000
   ```

### **View Online**
Visit the GitHub Pages link: [Influenza Visualization](https://fangyu-sun.github.io/Influenza-Visualization/)

---

## **Key Findings**
1. **Temperature and Influenza Trends**:
   - Higher temperatures (~25°C+) correspond to fewer cases (e.g., Queensland in summer).
   - Lower temperatures (~10°C-) lead to outbreaks (e.g., Victoria in winter).
   
2. **Age Group and Virus Type Distribution**:
   - Vulnerable groups: Children (0-4 years) and elderly (65+ years).
   - Virus A spreads across all age groups; Virus B is more common in children and teens.

3. **Temperature-Influenced Outbreaks**:
   - Cases peak when temperatures range between 15°C and 20°C during transitional seasons (autumn/winter).

---

## **Limitations**
1. Missing data points may affect analysis accuracy.
2. Short data span (2008-2022) limits long-term trend analysis.
3. Measurement errors in temperature data from different stations.

---

## **Future Enhancements**
1. Improve data cleaning and preprocessing.
2. Enrich datasets to include longer periods and additional factors.
3. Enhance interactivity and visualization techniques for better user exploration.

---

## **References**
1. **ACORN-SAT Australia**: [Bureau of Meteorology ACORN-SAT](http://www.bom.gov.au/climate/data/acorn-sat/stations/)
2. **NNDSS Public Dataset**: [Australian Government Health](https://www.health.gov.au/resources/collections/national-notifiable-diseases-surveillance-system-nndss)
3. **Australian States GeoJSON**: [Rowan Hogan’s GitHub](https://raw.githubusercontent.com/rowanhogan/australian-states/master/states.geojson)

---

## **Screenshots**
### **Homepage**
Displays the project title and navigation buttons for accessing various visualizations.

### **Heat Map and Line Chart**
- **Heat Map**: Visualizes average temperatures for each state.
- **Line Chart**: Tracks temperature trends over time.

### **Stacked Bar Chart**
Shows the distribution of influenza cases by virus type and age group.

### **Bubble Chart**
Explores the complex relationship between temperature, time, and influenza case counts.

---

## **Contributors**
- **Fangyu Sun**: Project development, visualization design, and implementation.

For inquiries, please reach out via:
- Email: charles.fangyu.sun@gmail.com
- GitHub: [fangyu-sun](https://github.com/fangyu-sun)
