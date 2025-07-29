from zxcvbn import zxcvbn

def check_password_strength(password):
    result = zxcvbn(password)
    return {
        'score': result['score'],
        'feedback': result['feedback'],
        'crack_time': result['crack_times_display']['offline_slow_hashing_1e4_per_second']
    }
