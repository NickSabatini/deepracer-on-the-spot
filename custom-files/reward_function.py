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

    # reward for steering left on left side of road
    if left_of_center and steering_angle > 0:
        reward += 1

    # reward for steering right on right side of road
    if not left_of_center and steering_angle < 0:
        reward += 1

    # Speedy track completion reward (reward high ratio of progress to steps)
    reward += 10 * progress / steps

    # Contiguous track completion reward (avoid crashing and reseting progress)
    reward += progress / 10

    # distance from center line reward
    center_reward = (1 - (distance_from_center/(track_width*0.5)) ** (0.5)) * 10
    reward += center_reward

    # reward for getting to last stages of track without crashing
    if progress >= 100:
        reward += 1000

    # reward for getting past the halfway point
    if progress > 50:
        reward += 10

    if (not all_wheels_on_track) or (distance_from_center/(track_width*0.5)) > 0.8:
        reward = 1e-3

    return float(reward)
