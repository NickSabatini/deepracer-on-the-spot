def reward_function(params):
    '''
    Example of penalize steering, which helps mitigate zig-zag behaviors
    '''
    
    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']

    steering = abs(params['steering_angle']) # Only need the absolute steering angle
    speed = params['speed']

    steps = params['steps']
    progress = params['progress']

    all_wheels_on_track = params['all_wheels_on_track']

    reward = 1e-3

    step_reward = (progress / steps) * 10

    reward += step_reward

    # Steering penality threshold, change the number based on your action space setting
    STEERING_THRESHOLD = 20

    # Penalize reward if the car is steering too much
    if steering > STEERING_THRESHOLD:
        reward *= 0.8

    # Steering penality threshold, change the number based on your action space setting
    SPEED_THRESHOLD = 2.5

    # Penalize reward if the car is steering too much
    if speed < SPEED_THRESHOLD:
        reward *= 0.8

    if not all_wheels_on_track:
        reward *= 0.2

    return float(reward)
