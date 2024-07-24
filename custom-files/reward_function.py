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
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']

    reward = 1e-3

    # Progress
    reward += (progress / 100) * 4

    # reward for speed (0-4)
    reward += speed

    # distance from center line reward
    center_reward = (1 - (distance_from_center/(track_width*0.5))**2) * 4
    reward += center_reward

    # reward for finishing the track
    if progress >= 100:
        reward += 50

    if not all_wheels_on_track:
        reward = 1e-3

    return float(reward)
