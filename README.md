# Vancouver Park Facilities Analysis System

A comprehensive data analysis system built with Python to analyze park facility density and distribution across Vancouver neighborhoods. This system helps users make informed decisions about neighborhood selection based on outdoor recreation needs and assists urban planners in assessing park facility development.

## 🏗️ System Overview

My project aims at managing the park and park facility data, finding parks with certain conditions on a map, and analyzing the relationship between a neighbourhood and park facilities inside it. It’s a program that mainly designed for urban planners or urban planning gamers to assess the current development of park facilities in different parks and neighbourhood areas and to decide how to maintain these facilities to meet the public’s recreation needs, while its filter function can also be helpful for the general public to decide which park they would like to go or which neighbourhood is the best to move into depending on their outdoor leisure needs.

The system processes real-time data from Vancouver's Open Data Portal to analyze:
- Park facility density across individual parks
- Facility type distribution within neighborhoods
- Interactive data management with CRUD operations
- Visual representation through maps and charts

## 🛠️ Tech Stack

- **Backend**: Python (OOP Design)
- **Data Processing**: RESTful API calls, pandas-style data manipulation
- **Visualization**: Matplotlib (charts), Folium (interactive maps)
- **Data Sources**: City of Vancouver Open Data Portal

## 🔧 Core Features

### Data Processing
- **Automated Data Fetching**: Retrieves park and facility data via RESTful API calls
- **Data Validation**: Removes invalid entries (parks with zero area)
- **Multi-level Data Structures**: Implements nested dictionaries for efficient data organization

### Analysis Capabilities
- **Density Calculations**: Computes facility density per hectare for each park
- **Distribution Analysis**: Analyzes facility type distribution across neighborhoods
- **Interactive Data Management**: Full CRUD operations for parks and facilities

### Visualization
- **Interactive Maps**: Folium-based mapping with facility location markers
- **Statistical Charts**: Matplotlib-generated histograms and pie charts
- **Customizable Views**: Sort data by density (ascending/descending order)

## 💻 Live Demo

- link: https://northeastern-my.sharepoint.com/:v:/g/personal/fan_xiy_northeastern_edu/EWYQBIGCyfpOnVb9yxasfVkBVHkg86PMIP9NwL5lyq32rA?e=LPU0rh

## 🗺️ Data Sources

- **Parks Dataset**: [Vancouver Open Data - Parks](https://opendata.vancouver.ca/explore/dataset/parks/)
- **Facilities Dataset**: [Vancouver Open Data - Park Facilities](https://opendata.vancouver.ca/explore/dataset/parks-facilities/)

## 🎯 Use Cases

**For Residents**:
- Compare neighborhood facilities before moving
- Find parks with specific facility types
- Analyze facility accessibility in different areas

**For Urban Planners**:
- Identify underserved neighborhoods
- Plan facility expansion based on density analysis
- Monitor facility distribution equity across the city

