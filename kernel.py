# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:11:45 2019

@author: ZhaoQian
"""

import numpy as np

'''
C = 80
distance = [35, 40, 16, 54, 28, 28, 27]
green_rate= [55, 60, 65, 65, 60, 65, 70, 50]
'''

def find_max_gap_numbernic(phase, ab_distance):
    
    T = phase

    delta_origin = []
    
    # 最大挪移量组合的较小值
    max_move_min_value = 0

    for i in range(len(ab_distance)):
        #if ab_distance[i] % T > T/2:
        #    delta.append(T - (ab_distance[i] % T))
        #else:
            delta_origin.append(ab_distance[i] % T)

    # print(delta)

    delta = sorted(delta_origin)
    # print(delta)

    max_gap = 0

    for i in range(len(delta) - 1):
        if delta[i+1] - delta[i] > max_gap:
            max_gap = delta[i+1] - delta[i]
            max_move_min_value = delta[i]

    # print(max_gap)

    return max_gap, delta_origin, max_move_min_value

def coordination(C, distance, green_rate):
    # 交叉口距离
    dis = 0
    ab_distance = []
    for i in range(len(distance)):
        dis += distance[i]
        ab_distance.append(dis)
    # print(ab_distance)
    #车速 11m/s.
    
    bound_speed = int(11/10 * C / 2)
    gap = np.zeros(20)
    
    max_gap_index = 0
    delta = []
    delta_distance = []
    max_move_min_value_set = []
    
    for i in range(bound_speed-10, bound_speed+10):
        gap[i - (bound_speed-10)], delta, max_move_min_value = \
        find_max_gap_numbernic(i, ab_distance)
        delta_distance.append(delta)
        max_move_min_value_set.append(max_move_min_value)
    
    #最大挪移量对应的下标。
    index = np.argmax(gap)
    max_gap_index = index + (bound_speed-10) 
    #print(max_gap_index)
    
    # 挪移量
    move_distance = delta_distance[index]
    #最大挪移量对中的较小值。
    max_move_min = max_move_min_value_set[index]
    
    # 把a并入列表
    important_value = []
    important_value.append(max_gap_index)
    important_value.extend(move_distance)
    # print(important_value)
    
    # 最大挪移量
    # max_move_distance = (max_gap_index - max(gap))/2
    #print(max_move_distance)
    
    #最大挪移量对中的较小值。
    max_move_max = max_move_min + max(gap)
    # print(max_move_max)
    
    important_point = (max_gap_index + max_move_min - max_move_max)/2 + max_move_max
    # print(important_point)
    
    #转换后的最大挪移量最小列表
    exchanged_max_move_min_list = []
    for each in important_value:
        if each <= max_move_min:
            each += max_gap_index
        exchanged_max_move_min_list.append(each)
    #print(exchanged_max_move_min_list)
    
    important_distance = []
    abs_important_distance = []
    for each in exchanged_max_move_min_list:
        c = each - important_point
        important_distance.append(c)
        abs_important_distance.append(abs(c))
    #print(important_distance)
    
    important_ture_distance = []
    for i in range(len(important_distance)):
        important_ture_distance.append(50*i + important_distance[i])
    #print(important_ture_distance)
    
    # 绿灯损失
    important_loss = []
    for each in abs_important_distance:
        important_loss.append(100*each/max_gap_index)
    print(important_loss)
    
    valid_rate = []
    for i in range(len(green_rate)):
        valid_rate.append(int(green_rate[i] - important_loss[i]))
    print(valid_rate)
    
    return valid_rate

# result = coordination(C, distance, green_rate)