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

    # reward for not oversteering
    if steering < 15:
        reward += 1

    # reward for staying in high speed range
    if speed > 1.5:
        reward += 1

    # Speedy track completion reward (reward high ratio of progress to steps)
    reward += 10 * progress / steps

    # Contiguous track completion reward (avoid crashing and reseting progress)
    reward += progress / 10

    # distance from center line reward
    center_reward = (1 - (distance_from_center/(track_width*0.5)) ** 2) * 10
    reward += center_reward

    # reward for finishing the track without crashing
    if progress >= 100:
        reward += 1000

    if (not all_wheels_on_track) or (distance_from_center/(track_width*0.5)) > 0.8:
        reward = 1e-3

    return float(reward)
