from task_generator.constants import Constants
import rospy
import numpy as np

class ObstacleManager:
    def __init__(self, namespace, map_manager, simulator):
        self.map_manager = map_manager
        self.namespace = namespace
        self.simulator = simulator

    def start_scenario(self, scenario):
        self.simulator.spawn_pedsim_agents(scenario["obstacles"]["dynamic"])

    def reset_scenario(self, scenario):
        self.simulator.remove_all_obstacles()

        if not scenario.get("obstacles") or not scenario.get("obstacles").get("static") or not scenario.get("obstacles").get("dynamic"):
            return

        for obstacle in scenario["obstacles"]["static"]:
            self.simulator.spawn_obstacle(
                [*obstacle["pos"], 0],
                yaml_path=obstacle["yaml_path"],
            )

        for obstacle in scenario["obstacles"]["dynamic"]:
            self.simulator.spawn_obstacle(
                [*obstacle["pos"], 0],
                yaml_path=obstacle["yaml_path"],
            )

    def reset_random(
            self, 
            dynamic_obstacles=Constants.ObstacleManager.DYNAMIC_OBSTACLES,
            static_obstacles=Constants.ObstacleManager.STATIC_OBSTACLES,
            forbidden_zones=[]
        ):
        if forbidden_zones is None:
            forbidden_zones = []

        self.simulator.remove_all_obstacles()

        obstacles = []

        # Create dynamic obstacles
        for i in range(dynamic_obstacles):
            position = self.map_manager.get_random_pos_on_map(
                safe_dist=Constants.ObstacleManager.OBSTACLE_MAX_RADIUS,
                forbidden_zones=forbidden_zones,
            )

            obstacles.append(self.simulator.create_dynamic_obstacle(position=position))

        # Create static obstacles
        for _ in range(static_obstacles):
            position = self.map_manager.get_random_pos_on_map(
                safe_dist=Constants.ObstacleManager.OBSTACLE_MAX_RADIUS,
                forbidden_zones=forbidden_zones,
            )

            obstacles.append(self.simulator.create_static_obstacle(position=position))

        # Spawn obstacles
        self.simulator.spawn_obstacles(obstacles)