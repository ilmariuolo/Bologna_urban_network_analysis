from utils import set_road_network, connectivity_analysis, degree_histogram, vulnerability, centrality_analysis

city = 'Bologna'
city_radius = 1000

G, city_radius = set_road_network(city,city_radius)

connectivity_analysis(city,city_radius=4000,average_path_length = False)

degree_histogram(city, city_radius)

vulnerability(city)

centrality_analysis(city, city_radius)