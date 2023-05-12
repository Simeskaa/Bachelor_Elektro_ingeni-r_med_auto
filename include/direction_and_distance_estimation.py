import numpy as np
import copy
from PySide6.QtCore import QLineF, QPointF

class angle_cord_estimation():
    def __init__(self, dist_short_mic: float = 0.275610, spd_sound: float = 343, max_distance: float = 100):
        # making local variables in the class
        # -------------------------------------------------
        self.dist_short_mic = dist_short_mic
        self.dist_long_mic = np.sqrt(self.dist_short_mic ** 2 + self.dist_short_mic ** 2)
        self.spd_sound = spd_sound
        self.max_dist = max_distance
        self.average_angle = None
        self.dist = None
        self.U = None

    def norm_values(self,toad):
        norm_toad = [0.0] * len(toad)
        for i in range(len(toad)):
            toad[i] *= -1
        low_val_index = np.argmin(toad)  # Lowest value
        low_val = toad[low_val_index]

        for j in range(len(toad)):
            norm_toad[j] = toad[j] + abs(low_val)

        return norm_toad
    def angle_calc(self, tdoa: list):
        # rotating the coordinate system to the first quadrant
        # -------------------------------------------------
        fake_mics = []
        tdoas_temp = copy.copy(tdoa)

        for i in range(4):
            ref = np.argmin(tdoas_temp)
            fake_mics.append(tdoas_temp[ref])
            tdoas_temp.remove(tdoas_temp[ref])

        # tdoa = time delay of arrivle
        m3_m1 = tdoa[2] - tdoa[0]
        m3_m2 = tdoa[2] - tdoa[1]
        m3_m4 = tdoa[2] - tdoa[3]
        m1_m4 = tdoa[0] - tdoa[3]
        m1_m2 = tdoa[0] - tdoa[1]
        m4_m2 = tdoa[3] - tdoa[1]

        sound_diff_1 = ((m3_m1 >= 0) and (m3_m2 >= 0) and (m4_m2 >= 0)) and \
                       ((m3_m4 < 0) and (m1_m4 < 0) and (m1_m2 < 0))
        sound_diff_2 = ((m3_m1 < 0) and (m3_m2 < 0) and (m3_m4 < 0) and (m1_m4 < 0) and (m1_m2 < 0) and (m4_m2 < 0))
        sound_diff_3 = ((m3_m1 < 0) and (m3_m2 < 0) and (m4_m2 < 0)) and \
                       ((m3_m4 >= 0) and (m1_m4 >= 0) and (m1_m2 >= 0))
        sound_diff_4 = ((m3_m1 >= 0) and (m3_m2 >= 0) and (m3_m4 >= 0) and (m1_m4 >= 0) and (m1_m2 >= 0) and (m4_m2 >= 0))

        if (sound_diff_1 or sound_diff_2 or sound_diff_3 or sound_diff_4):
            # fake microphone array
            fma = {'m1': fake_mics[0], 'm2': fake_mics[1], 'm3': fake_mics[2], 'm4': fake_mics[3]}
        else:
            fma = {'m1': fake_mics[1], 'm2': fake_mics[0], 'm3': fake_mics[3], 'm4': fake_mics[2]}

        # finding angles
        # -------------------------------------------------
        angle_m3_m2 = np.arccos((fma['m3'] - fma['m2']) * self.spd_sound / self.dist_long_mic) + 0
        angle_m1_m4 = np.arccos((fma['m1'] - fma['m4']) * self.spd_sound / self.dist_long_mic) - np.pi / 2
        angle_m3_m4 = np.arccos((fma['m3'] - fma['m4']) * self.spd_sound / self.dist_short_mic) - np.pi / 4
        angle_m1_m2 = np.arccos((fma['m1'] - fma['m2']) * self.spd_sound / self.dist_short_mic) - np.pi / 4
        angle_m3_m1 = np.arccos((fma['m3'] - fma['m1']) * self.spd_sound / self.dist_short_mic) + np.pi / 4
        angle_m4_m2 = np.arccos((fma['m4'] - fma['m2']) * self.spd_sound / self.dist_short_mic) + np.pi / 4

        x1 = 0
        x2 = self.dist_long_mic / 2
        x3 = -self.dist_long_mic / 2
        x4 = 0
        y1 = self.dist_long_mic / 2
        y2 = 0
        y3 = 0
        y4 = -self.dist_long_mic / 2
        T_1 = tdoa[0]
        T_2 = tdoa[1]
        T_3 = tdoa[2]
        T_4 = tdoa[3]
        c = self.spd_sound

        X = np.array([[x2 - x1, y2 - y1],
                      [x3 - x1, y3 - y1],
                      [x4 - x1, y4 - y1]])
        T = np.array([[c * (T_2 - T_1)],
                      [c * (T_3 - T_1)],
                      [c * (T_4 - T_1)]])
        self.U = np.linalg.pinv(X) @ T
        angle_center = np.arctan(self.U[1] / self.U[0])

        list_angles = [angle_m3_m2, angle_m1_m4, angle_m3_m4, angle_m1_m2, angle_m3_m1, angle_m4_m2, angle_center[0]]

        # removing negative angle from co
        # -------------------------------------------------
        if fma['m1'] > fma['m3']:
            list_angles[4] = np.pi / 2 - list_angles[4]
            list_angles[5] = np.pi / 2 - list_angles[5]

        # moving the angle to correct quadrant
        # -------------------------------------------------
        tdoas_temp2 = copy.copy(tdoa)

        for i in range(2):
            ref = np.argmax(tdoas_temp2)
            tdoas_temp2.remove(tdoas_temp2[ref])

        if (tdoas_temp2 == [tdoa[0], tdoa[1]]):
            pass

        elif (tdoas_temp2 == [tdoa[0], tdoa[2]]):
            for i in range(len(list_angles)):
                list_angles[i] = list_angles[i] + np.pi / 2

        elif (tdoas_temp2 == [tdoa[2], tdoa[3]]):
            for i in range(len(list_angles)):
                list_angles[i] = list_angles[i] + np.pi

        elif (tdoas_temp2 == [tdoa[1], tdoa[3]]):
            for i in range(len(list_angles)):
                list_angles[i] = list_angles[i] + 3 * np.pi / 2
        return list_angles, self.average_angle

    def angle_2_cord_calc(self, angles: list, average_angle: float):
        # finding start and end coordinates
        # -------------------------------------------------
        end_cords = {}
        for i in range(len(angles)):
            x_name = f'x_{i + 1}'
            y_name = f'y_{i + 1}'
            end_cords[x_name] = self.max_dist * np.cos(angles[i])
            end_cords[y_name] = self.max_dist * np.sin(angles[i])
        end_cords['x_7'] = self.U[0][0]*self.max_dist
        end_cords['y_7'] = self.U[1][0]*self.max_dist

        start_cords = {'x_1': -self.dist_long_mic / 2, 'y_1': 0, 'x_2': 0, 'y_2': self.dist_long_mic / 2,
                       'x_3': -self.dist_long_mic / 2, 'y_3': 0, 'x_4': 0, 'y_4': self.dist_long_mic / 2,
                       'x_5': -self.dist_long_mic / 2, 'y_5': 0, 'x_6': 0, 'y_6': -self.dist_long_mic / 2,
                       'x_7': -self.U[0][0]*self.max_dist, 'y_7': -self.U[1][0]*self.max_dist}
        # making the coords to lines to be used in intersection
        # -------------------------------------------------
        list_line = {}
        for i in range(int(len(start_cords)/2)):
            name = f'l_{i + 1}'
            p1 = QPointF(start_cords[f'x_{i + 1}'], start_cords[f'y_{i + 1}'])
            p2 = QPointF(end_cords[f'x_{i + 1}'], end_cords[f'y_{i + 1}'])
            list_line[name] = QLineF(p1, p2)

        # finding intersection
        # -------------------------------------------------
        par_12 = list_line['l_1'].intersects(list_line['l_2'])
        par_14 = list_line['l_1'].intersects(list_line['l_4'])
        par_16 = list_line['l_1'].intersects(list_line['l_6'])
        par_52 = list_line['l_5'].intersects(list_line['l_2'])
        par_54 = list_line['l_5'].intersects(list_line['l_4'])
        par_32 = list_line['l_3'].intersects(list_line['l_2'])
        par_36 = list_line['l_3'].intersects(list_line['l_6'])
        par_26 = list_line['l_2'].intersects(list_line['l_6'])
        par_46 = list_line['l_4'].intersects(list_line['l_6'])

        intersection_list_test = [par_12, par_14, par_16, par_52, par_54, par_32, par_36, par_26, par_46]
        print(f'\nintersecting test: {intersection_list_test}')

        par_17 = list_line['l_1'].intersects(list_line['l_7'])
        par_27 = list_line['l_2'].intersects(list_line['l_7'])
        par_37 = list_line['l_3'].intersects(list_line['l_7'])
        par_47 = list_line['l_4'].intersects(list_line['l_7'])
        par_57 = list_line['l_5'].intersects(list_line['l_7'])
        par_67 = list_line['l_6'].intersects(list_line['l_7'])

        intersection_list = [par_17, par_27, par_37, par_47, par_57, par_67]

        # taking the useful intersections and finding the average of them
        # -------------------------------------------------
        bound_inter_list = []
        for i in range(len(intersection_list)):
            if intersection_list[i][0] == QLineF.BoundedIntersection:
                bound_inter_list.append(intersection_list[i][1])
        x = 0
        y = 0
        if len(bound_inter_list) > 0:
            for i in range(len(bound_inter_list)):
                x = bound_inter_list[i].x() + x
                y = bound_inter_list[i].y() + y
            x = x / len(bound_inter_list)
            y = y / len(bound_inter_list)
            angle_overrule = False
        else:
            angle_overrule = True
            x = self.max_dist*np.cos(average_angle)/2
            y = self.max_dist*np.sin(average_angle)/2
        return x, y, angle_overrule

    def coord_2_distance_calc(self, x: float, y: float):
        # calculating distance from center
        # -------------------------------------------------
        self.dist = np.sqrt(x ** 2 + y ** 2)
        return self.dist

    def timestamp_2_cord(self, timestamps: list):
        # combining the different functions for easier usage
        # -------------------------------------------------
        toad = self.norm_values(timestamps)
        angles, average_angle = self.angle_calc(toad)
        boat_coords_x, boat_coords_y, angle_overrule = self.angle_2_cord_calc(angles, average_angle)
        dist = self.coord_2_distance_calc(boat_coords_x, boat_coords_y)
        return boat_coords_x, boat_coords_y, dist, average_angle, angle_overrule

    @property
    def angle2boat(self) -> float:
        return self.average_angle

    @property
    def dist2boat(self) -> float:
        return self.dist

def simulation(boat_placment):
    tdoa_78 = [0, 0.019, 0.029, 0.048]
    tdoa_45 = [0.0, 0.0, 0.03498542274, 0.03498542274]
    tdoa_34 = [0., (1.37 + 0.92) / 343, (1.37 + 0.92 + 9.506) / 343, (1.37 + 0.92 + 9.506 + 1.438 + 0.809) / 343]

    if boat_placment == '78':
        # static simulate time delay of arrive
        # -------------------------------------------------
        t1 = tdoa_78[0]
        t2 = tdoa_78[1]
        t3 = tdoa_78[2]
        t4 = tdoa_78[3]
        mic = {'m1': t1, 'm2': t2, 'm3': t3, 'm4': t4}

    if boat_placment == '45':
        t1 = tdoa_45[0]
        t2 = tdoa_45[1]
        t3 = tdoa_45[2]
        t4 = tdoa_45[3]
        mic = {'m1': t3, 'm2': t4, 'm3': t1, 'm4': t2}

    if boat_placment == '34':
        t1 = tdoa_34[0]
        t2 = tdoa_34[1]
        t3 = tdoa_34[2]
        t4 = tdoa_34[3]
        mic = {'m1': t4, 'm2': t3, 'm3': t2, 'm4': t1}

    tdoa = [mic['m1'], mic['m2'], mic['m3'], mic['m4']]

    return tdoa


if __name__ == '__main__':
    boat = angle_cord_estimation(dist_short_mic=12, spd_sound=343, max_distance=1000)
    print(boat.timestamp_2_cord(simulation('78')))