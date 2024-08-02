import math

def reward_function(params):

    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    progress = params['progress']
    steps = params['steps']
    speed = params['speed']
    all_wheels_on_track = params['all_wheels_on_track']
    steering_angle = params['steering_angle']
    left_of_center = params['is_left_of_center']

    reward = 1

    # reward for not oversteering
    if abs(steering_angle) < 15:
        reward += 1

    # reward for staying in high speed range
    if speed > 1.5:
        reward += 1

    # distance from center line reward
    if distance_from_center/(track_width*0.5) < 0.5:
        reward += 5

    # Contiguous track completion reward (avoid crashing and reseting progress)
    reward += progress / 10

    # reward for getting across finish without crashing
    if progress >= 100:
        reward += 1000

    # reward for staying on the track
    if (not all_wheels_on_track):
        reward = 1e-3

    return float(reward)
