import sys

sys.path.append("..")

from mesacat.generate_agents import (
    generate_agents,
    get_agent_types,
    get_buildings,
    plot_agents,
)
from unittest import TestCase
import os
import geopandas as gpd
import osmnx as ox
from datetime import time

population_data = os.path.join(os.path.dirname(__file__), "population_data")
sample_data = os.path.join(os.path.dirname(__file__), "sample_data")
domain_file = os.path.join(sample_data, "newcastle-small.gpkg")


class TestGenerateAgents(TestCase):

    def test_generate_agents(self):
        domain = gpd.read_file(domain_file).geometry[0]
        domain, _ = ox.projection.project_geometry(domain, "EPSG:3857", to_latlong=True)
        agents = generate_agents(domain, 5000, population_data, time(hour=9, minute=15))
        plot_agents(domain, agents)


if __name__ == "__main__":
    TestGenerateAgents().test_generate_agents()
