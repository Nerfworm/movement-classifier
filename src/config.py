CONNECTED_DEVICES = {
    'hmd': {
        'serial': '1PASH5D1P17365',
        'index': 0,
        'device_class': 'HMD',
        'body_part': 'hmd',
    },
    'left_foot': {
        'serial': 'human://LEFT_FOOT',
        'index': 1,
        'device_class': 'Tracker',
        'body_part': 'left_foot',
    },
    'left_knee': {
        'serial': 'human://LEFT_KNEE',
        'index': 2,
        'device_class': 'Tracker',
        'body_part': 'left_knee',
    },
    'right_foot': {
        'serial': 'human://RIGHT_FOOT',
        'index': 3,
        'device_class': 'Tracker',
        'body_part': 'right_foot',
    },
    'right_knee': {
        'serial': 'human://RIGHT_KNEE',
        'index': 4,
        'device_class': 'Tracker',
        'body_part': 'right_knee',
    },
    'waist': {
        'serial': 'human://WAIST',
        'index': 5,
        'device_class': 'Tracker',
        'body_part': 'waist',
    },
    'chest': {
        'serial': 'human://CHEST',
        'index': 6,
        'device_class': 'Tracker',
        'body_part': 'chest',
    },
    'right_elbow': {
        'serial': 'human://RIGHT_ELBOW',
        'index': 7,
        'device_class': 'Tracker',
        'body_part': 'right_elbow',
    },
    'left_elbow': {
        'serial': 'human://LEFT_ELBOW',
        'index': 8,
        'device_class': 'Tracker',
        'body_part': 'left_elbow',
    },
    'controller_left': {
        'serial': '1PASH5D1P17365_Controller_Left',
        'index': 9,
        'device_class': 'Controller',
        'body_part': 'controller_left',
    },
    'controller_right': {
        'serial': '1PASH5D1P17365_Controller_Right',
        'index': 10,
        'device_class': 'Controller',
        'body_part': 'controller_right',
    }
}

LABELS = ["idle", "walking", "raised right arm"]

DATA_DIRECTORIES = {
    "logs": "./data/logs/",
    "models": "./data/models/",
    "processed": "./data/processed/",
    "raw": "./data/raw/"
}