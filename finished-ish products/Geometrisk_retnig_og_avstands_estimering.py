import numpy as np
import copy
from PySide6.QtCore import QLineF, QPointF

class angle_cord_estimation():

    #opimaliserings problema som gjenstår:
    #samma med simulator vinkel
    #retunera angle hvis intersrection føkke seg opp
    #kommentera
    #gjør koden clean(tenke hovedsaklig på dict/list kukeriet som e rundt forbi)
    #laga mer passande navn te funksjoinan og variabel navnan

    def __init__(self, dist_short_mic: float = 12, spd_sound: float = 343, boat_placment: str = '78', sim: bool = False):
        self.dist_short_mic = dist_short_mic
        self.spd_sound = spd_sound
        self.boat_placment = boat_placment
        self.sim = sim

    def angle_calc6(self, tdoas: list):
        fake_mics = []
        tdoas_temp = copy.copy(tdoas)

        spacing_little = self.dist_short_mic
        spacing_big = np.sqrt(spacing_little**2 + spacing_little**2)

        # snur koordinatsystemet
        for i in range(4):
            ref = np.argmin(tdoas_temp)
            fake_mics.append(tdoas_temp[ref])
            tdoas_temp.remove(tdoas_temp[ref])

        m2_m1 = tdoas[2] - tdoas[0]
        m2_m3 = tdoas[2] - tdoas[1]
        m2_m4 = tdoas[2] - tdoas[3]
        m1_m4 = tdoas[0] - tdoas[3]
        m1_m3 = tdoas[0] - tdoas[1]
        m4_m3 = tdoas[3] - tdoas[1]

        sound_diff_1 = ((m2_m1 >= 0) and (m2_m3 >= 0) and (m4_m3 >= 0)) and (
                    (m2_m4 < 0) and (m1_m4 < 0) and (m1_m3 < 0))
        sound_diff_2 = ((m2_m1 < 0) and (m2_m3 < 0) and (m2_m4 < 0) and (m1_m4 < 0) and (m1_m3 < 0) and (m4_m3 < 0))
        sound_diff_3 = ((m2_m1 < 0) and (m2_m3 < 0) and (m4_m3 < 0)) and (
                    (m2_m4 >= 0) and (m1_m4 >= 0) and (m1_m3 >= 0))
        sound_diff_4 = (
                    (m2_m1 >= 0) and (m2_m3 >= 0) and (m2_m4 >= 0) and (m1_m4 >= 0) and (m1_m3 >= 0) and (m4_m3 >= 0))

        if (sound_diff_1 or sound_diff_2 or sound_diff_3 or sound_diff_4):

            fma = {'m1': fake_mics[0], 'm2': fake_mics[2], 'm3': fake_mics[1], 'm4': fake_mics[3]}
        else:
            fma = {'m1': fake_mics[1], 'm2': fake_mics[3], 'm3': fake_mics[0], 'm4': fake_mics[2]}


        angle_m2_m3 = np.arccos((fma['m2'] - fma['m3']) * self.spd_sound / spacing_big) + 0
        angle_m1_m4 = np.arccos((fma['m1'] - fma['m4']) * self.spd_sound / spacing_big) - np.pi / 2
        angle_m2_m4 = np.arccos((fma['m2'] - fma['m4']) * self.spd_sound / spacing_little) - np.pi / 4
        angle_m1_m3 = np.arccos((fma['m1'] - fma['m3']) * self.spd_sound / spacing_little) - np.pi / 4
        angle_m2_m1 = np.arccos((fma['m2'] - fma['m1']) * self.spd_sound / spacing_little) + np.pi / 4
        angle_m4_m3 = np.arccos((fma['m4'] - fma['m3']) * self.spd_sound / spacing_little) + np.pi / 4

        list_angles = [angle_m2_m3, angle_m1_m4, angle_m2_m4, angle_m1_m3, angle_m2_m1, angle_m4_m3]

        if fma['m1'] > fma['m3']:
            list_angles[4] = np.pi / 2 - list_angles[4]
            list_angles[5] = np.pi / 2 - list_angles[5]

        # bestemme kvadrant

        tdoas_temp2 = copy.copy(tdoas)

        for i in range(2):
            ref = np.argmax(tdoas_temp2)
            tdoas_temp2.remove(tdoas_temp2[ref])

        # bestemme kvadrant
        if (tdoas_temp2 == [tdoas[0], tdoas[1]]):
            # print("Kvadrant 1, + 0deg")
            pass

        elif (tdoas_temp2 == [tdoas[0], tdoas[2]]):
            # print("Kvadrant 2, + 90deg")
            for i in range(len(list_angles)):
                list_angles[i] = list_angles[i] + np.pi / 2
        elif (tdoas_temp2 == [tdoas[2], tdoas[3]]):
            # print("Kvadrant 3, + 180deg")
            for i in range(len(list_angles)):
                list_angles[i] = list_angles[i] + np.pi
        elif (tdoas_temp2 == [tdoas[1], tdoas[3]]):
            # print("Kvadrant 4, + 270deg")
            for i in range(len(list_angles)):
                list_angles[i] = list_angles[i] + 3*np.pi / 2

        general_angle = sum(list_angles)/len(list_angles)

        # angle_read = {}
        # #gjør radiana øve te grade
        # for i in range(len(list_angles)):
        #     name = f'angle {i + 1}'
        #     angle_read[name] = angle[name] * 180 / np.pi
        #
        # print(angle_read)
        return list_angles, general_angle

    def simulation(self):
        toad_78 = [0, 0.019, 0.029, 0.048]
        toad_45 = [0.0, 0.0, 0.03498542274, 0.03498542274]
        toad_34 = [0., (1.37 + 0.92) / 343, (1.37 + 0.92 + 9.506) / 343, (1.37 + 0.92 + 9.506 + 1.438 + 0.809) / 343]



        if self.boat_placment == '78':
            # alt ser ut te å fungera her
            t1 = toad_78[0]
            t2 = toad_78[1]
            t3 = toad_78[2]
            t4 = toad_78[3]
            mic = {'m1': t3, 'm2': t4, 'm3': t1, 'm4': t2}

        if self.boat_placment == '45':
            t1 = toad_45[0]
            t2 = toad_45[1]
            t3 = toad_45[2]
            t4 = toad_45[3]
            mic = {'m1': t3, 'm2': t4, 'm3': t1, 'm4': t2}

        if self.boat_placment == '34':
            # må finna ein bære måte å beregna 45 gradaren på
            t1 = toad_34[0]
            t2 = toad_34[1]
            t3 = toad_34[2]
            t4 = toad_34[3]
            mic = {'m1': t4, 'm2': t3, 'm3': t2, 'm4': t1}


        toad = [mic['m1'], mic['m3'], mic['m2'], mic['m4']]

        return toad

    def cord2lines(self, r, vinkel: list):
        # vinkel += np.pi
        end_cords = {}
        for i in range(6):
            x_name = f'x_{i + 1}'
            y_name = f'y_{i + 1}'
            end_cords[x_name] = r * np.cos(vinkel[i])
            end_cords[y_name] = r * np.sin(vinkel[i])
        start_cords =  {'x_1': -6 * np.sqrt(2), 'y_1': 0, 'x_2': 0, 'y_2': 6 * np.sqrt(2),
                        'x_3': -6 * np.sqrt(2), 'y_3': 0, 'x_4': 0, 'y_4': 6 * np.sqrt(2),
                        'x_5': -6 * np.sqrt(2), 'y_5': 0, 'x_6': 0, 'y_6': -6 * np.sqrt(2)}

        return start_cords, end_cords

    def boat_cord_estimat(self, start_cord: dict, end_cord: dict):
        list_line = {}
        for i in range(6):
            name = f'l_{i + 1}'
            p1 = QPointF(start_cord[f'x_{i + 1}'], start_cord[f'y_{i + 1}'])
            p2 = QPointF(end_cord[f'x_{i + 1}'], end_cord[f'y_{i + 1}'])
            list_line[name] = QLineF(p1, p2)

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
        else:
            print('LAG ET SYSTEM DER VINKEL BLIR PASSA UT ISTEDE SÅ GUI-EN FÅR NÅE DATA!!!!!!!!')
        print(x,y)
        return x, y

    def distance (self, x:float, y:float):
        dist = np.sqrt(x**2 + y**2)
        return dist

    def timestamp2cord(self, timestamps: list ):

        if self.sim:
            angles, avreage_angle = self.angle_calc6(self.simulation())
            start_coord, end_cords =  self.cord2lines(2000, angles)
            boat_coords = self.boat_cord_estimat(start_coord, end_cords)
            dist = self.distance(boat_coords[0], boat_coords[1])


        else:
            angles, avreage_angle = self.angle_calc6(timestamps)
            start_coord, end_cords = self.cord2lines(2000, angles)
            boat_coords = self.boat_cord_estimat(start_coord, end_cords)
            dist = self.distance(boat_coords[0], boat_coords[1])


        return boat_coords, dist, avreage_angle



if __name__ == '__main__':
    boat = angle_cord_estimation( dist_short_mic= 12 , spd_sound= 343, boat_placment= '78',sim= True)
    print(boat.timestamp2cord([]))
    #list_angle, gen_angle = boat.angle_calc6(boat.simulation('78'), 343, 12*np.sqrt(2), 12)
    #print(list_angle, gen_angle, gen_angle*180/np.pi)