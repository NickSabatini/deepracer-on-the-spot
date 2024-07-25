import math

def reward_function(params):

    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    progress = params['progress']
    steps = params['steps']
    speed = params['speed']
    all_wheels_on_track = params['all_wheels_on_track']
    steering = abs(params['steering_angle'])

    reward = 1

    # add reward for low steering angle
    if steering < 15:
        reward += 1

    # reward for speed (0-2)
    if speed > 1.5:
        reward += 1

    # Progress (each 10% checkpoint gives 10 times ratio of progress to current steps)
    reward += 10 * progress / steps

    # distance from center line reward
    center_reward = (1 - (distance_from_center/(track_width*0.5)) ** (0.6)) * 10
    reward += center_reward

    # reward for finishing the track
    if progress >= 100:
        reward += 1000

    if (not all_wheels_on_track) or (distance_from_center/(track_width*0.5)) > 0.8:
        reward = 1e-3

    return float(reward)
