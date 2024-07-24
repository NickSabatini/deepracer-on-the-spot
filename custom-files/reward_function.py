import math

def reward_function(params):
    '''
    Example of penalize steering, which helps mitigate zig-zag behaviors
    '''
    
    # Read input parameters
    steering = abs(params['steering_angle']) # Only need the absolute steering angle
    speed = params['speed']
    steps = params['steps']
    progress = params['progress']
    all_wheels_on_track = params['all_wheels_on_track']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    reward = 1e-3

    # Progress per step reward is large, this is a proxy for quick completion of the track
    reward += progress * 4

    # reward for speed
    reward += speed

    # Reward for velocity vector alignment with direction of track
    # Calculate the direction of the center line based on two closest waypoints
    waypoint_1 = waypoints[closest_waypoints[0]]
    waypoint_2 = waypoints[closest_waypoints[1]]
    
    track_direction = math.atan2(waypoint_2[1] - waypoint_1[1], waypoint_2[0] - waypoint_1[0])
    track_direction = math.degrees(track_direction)
    
    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff
    
    # Reward function based on the direction difference
    if direction_diff < 10:
        reward += 4

    if not all_wheels_on_track:
        reward *= 0.5

    return float(reward)
