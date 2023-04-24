import numpy as np
import copy
from PySide6.QtCore import QLineF, QPointF


class angle_cord_estimation():
    def __init__(self, dist_short_mic: float = 12, spd_sound: float = 343, max_distance: float = 2000):
        # making local variables in the class
        # -------------------------------------------------
        self.dist_short_mic = dist_short_mic
        self.dist_long_mic = np.sqrt(self.dist_short_mic ** 2 + self.dist_short_mic ** 2)
        self.spd_sound = spd_sound
        self.max_dist = max_distance
        self.average_angle = None
        self.dist = None

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
        m2_m1 = tdoa[2] - tdoa[0]
        m2_m3 = tdoa[2] - tdoa[1]
        m2_m4 = tdoa[2] - tdoa[3]
        m1_m4 = tdoa[0] - tdoa[3]
        m1_m3 = tdoa[0] - tdoa[1]
        m4_m3 = tdoa[3] - tdoa[1]

        sound_diff_1 = ((m2_m1 >= 0) and (m2_m3 >= 0) and (m4_m3 >= 0)) and \
                       ((m2_m4 < 0) and (m1_m4 < 0) and (m1_m3 < 0))
        sound_diff_2 = ((m2_m1 < 0) and (m2_m3 < 0) and (m2_m4 < 0) and (m1_m4 < 0) and (m1_m3 < 0) and (m4_m3 < 0))
        sound_diff_3 = ((m2_m1 < 0) and (m2_m3 < 0) and (m4_m3 < 0)) and \
                       ((m2_m4 >= 0) and (m1_m4 >= 0) and (m1_m3 >= 0))
        sound_diff_4 = ((m2_m1 >= 0) and (m2_m3 >= 0) and (m2_m4 >= 0) and (m1_m4 >= 0) and (m1_m3 >= 0) and (m4_m3 >= 0))

        if (sound_diff_1 or sound_diff_2 or sound_diff_3 or sound_diff_4):
            # fake microphone array
            fma = {'m1': fake_mics[0], 'm2': fake_mics[2], 'm3': fake_mics[1], 'm4': fake_mics[3]}
        else:
            fma = {'m1': fake_mics[1], 'm2': fake_mics[3], 'm3': fake_mics[0], 'm4': fake_mics[2]}

        # finding angles
        # -------------------------------------------------
        angle_m2_m3 = np.arccos((fma['m2'] - fma['m3']) * self.spd_sound / self.dist_long_mic) + 0
        angle_m1_m4 = np.arccos((fma['m1'] - fma['m4']) * self.spd_sound / self.dist_long_mic) - np.pi / 2
        angle_m2_m4 = np.arccos((fma['m2'] - fma['m4']) * self.spd_sound / self.dist_short_mic) - np.pi / 4
        angle_m1_m3 = np.arccos((fma['m1'] - fma['m3']) * self.spd_sound / self.dist_short_mic) - np.pi / 4
        angle_m2_m1 = np.arccos((fma['m2'] - fma['m1']) * self.spd_sound / self.dist_short_mic) + np.pi / 4
        angle_m4_m3 = np.arccos((fma['m4'] - fma['m3']) * self.spd_sound / self.dist_short_mic) + np.pi / 4

        list_angles = [angle_m2_m3, angle_m1_m4, angle_m2_m4, angle_m1_m3, angle_m2_m1, angle_m4_m3]

        # removing negative angle from cos
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

        self.average_angle = sum(list_angles) / len(list_angles)

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

        start_cords = {'x_1': -self.dist_long_mic / 2, 'y_1': 0, 'x_2': 0, 'y_2': self.dist_long_mic / 2,
                       'x_3': -self.dist_long_mic / 2, 'y_3': 0, 'x_4': 0, 'y_4': self.dist_long_mic / 2,
                       'x_5': -self.dist_long_mic / 2, 'y_5': 0, 'x_6': 0, 'y_6': -self.dist_long_mic / 2}

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

        intersection_list = [par_12, par_14, par_16, par_52, par_54, par_32, par_36, par_26, par_46]

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
            x = 500*np.cos(average_angle)
            y = 500*np.sin(average_angle)
        return x, y, angle_overrule

    def coord_2_distance_calc(self, x: float, y: float):
        # calculating distance from center
        # -------------------------------------------------
        self.dist = np.sqrt(x ** 2 + y ** 2)
        return self.dist

    def timestamp_2_cord(self, timestamps: list):
        # combining the different functions for easier usage
        # -------------------------------------------------
        angles, average_angle = self.angle_calc(timestamps)
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
        mic = {'m1': t3, 'm2': t4, 'm3': t1, 'm4': t2}

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

    tdoa = [mic['m1'], mic['m3'], mic['m2'], mic['m4']]

    return tdoa


if __name__ == '__main__':
    boat = angle_cord_estimation(dist_short_mic=12, spd_sound=343, max_distance=2000)
    print(boat.timestamp_2_cord(simulation('45')))

