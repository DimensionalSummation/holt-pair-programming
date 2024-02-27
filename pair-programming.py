import numpy as np

def scale(arr):
    """Takes an input array and returns values scaled to lie in the range [0.0, 1.0].
    Input: ndarray
    Returns: ndarray of floats"""
    
    # ensure the input is an array
    assert (type(arr1)==np.ndarray), 'Please input int, float, or ndarray'
    
    # the scaled term corresponding to the current term in the input array is calculated by taking the difference between the
    # current term and the min and dividing it by the range of the input array
    
    scaled_array = np.array([])
    arr_range = float(np.max(arr) - np.min(arr)) # range of input array
    
    for num in arr:
        
        diff = num - np.min(arr) # difference between current and min term
        scaled_array = np.append(scaled_array, diff/arr_range)
        
    return scaled_array